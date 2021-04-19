"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()
DEFAULT_IMAGE = "https://www.pngitem.com/pimgs/m/80-800373_it-benefits-per-users-default-profile-picture-green.png"

def connect_db(app):
    db.app = app
    db.init_app(app)



class User(db.Model):
    __tablename__ = 'users'


    def __repr__(self):       
        return f"<User id = {self.id} first_name = {self.first_name} last_name = {self.last_name} image_url={self.image_url}>"

    id = db.Column(db.Integer, 
                    primary_key=True, 
                    autoincrement=True)

    first_name = db.Column(db.Text,
                        nullable=False) 

    last_name = db.Column(db.Text,
                        nullable=False)  

    image_url = db.Column(db.Text,
                          nullable=False,
                          default=DEFAULT_IMAGE)        


    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")                                        

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


class Post(db.Model):
    __tablename__ = 'posts'       

    
    
    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    title = db.Column(db.Text, nullable=False)

    content = db.Column(db.Text, nullable=False)      

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)          

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    
class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    
    posts = db.relationship('Post', secondary="posts_tags", backref="tags")


class PostTag(db.Model):
    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey(Post.id), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey(Tag.id), primary_key=True)

   
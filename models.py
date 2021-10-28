"""SQL models for shareb&b"""

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

import boto3
s3 = boto3.client('s3')

bcrypt = Bcrypt()
db = SQLAlchemy()

DEFAULT_IMAGE = "https://st4.depositphotos.com/14953852/24787/v/600/depositphotos_247872612-stock-illustration-no-image-available-icon-vector.jpg"

# class User(db.Model):
#     """User in the system."""

#     __tablename__ = 'users'

#     username = db.Column(
#         db.String(length=50),
#         primary_key=True,
#     )

#     password = db.Column(
#         db.Text,
#         nullable=False,
#     )

#     email = db.Column(
#         db.Text,
#         nullable=False,
#         unique=True,
#     )

#     first_name = db.Column(
#         db.Text,
#         nullable=False,
#     )

#     last_name = db.Column(
#         db.Text,
#         nullable=False
#     )

#     profile_image_url = db.Column(
#         db.Text,
#         default="/static/images/default-pic.png"
#     )

#     bio = db.Column(
#         db.Text,
#         default=""
#     )

#     location = db.Column(
#         db.Text,
#         nullable=False
#     )

#     listings_created = db.relationship(
#         "Listing",
#         foreign_keys="Listings.created",
#         backref="creator"
#     )

#     listings_rented = db.relationship(
#         "Listing",
#         foreign_keys="Listings.rented",
#         backref="renter"
#     )

#     def __repr__(self):
#         return f"<User #{self.username}, {self.first_name} {self.last_name}>"

#     @classmethod
#     def signup(cls, username, password, email, first_name, last_name, profile_image_url, bio, location):
#         """Sign up user.

#         Hashes password and adds user to system.
#         """

#         hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

#         user = User(
#             username=username,
#             password=hashed_pwd,
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#             profile_image_url=profile_image_url,
#             bio=bio,
#             location=location,
#         )

#         db.session.add(user)
#         return user

#     @classmethod
#     def authenticate(cls, username, password):
#         """Find user with `username` and `password`.

#         This is a class method (call it on the class, not an individual user.)
#         It searches for a user whose password hash matches this password
#         and, if it finds such a user, returns that user object.

#         If can't find matching user (or if password is wrong), returns False.
#         """

#         user = cls.query.filter_by(username=username).first()

#         if user:
#             is_auth = bcrypt.check_password_hash(user.password, password)
#             if is_auth:
#                 return user

#         return False



class Listing(db.Model):
    """Listing Model"""

    __tablename__ = "listings"

    id = db.Column(
        db.Integer, 
        primary_key = True,
        autoincrement = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
    )

    image = db.Column(
        db.Text, 
        nullable = False,
        default = DEFAULT_IMAGE
    )

    price = db.Column(
        db.Numeric(10, 2),
        nullable = False, 
        default = 0
    )

    description = db.Column(
        db.Text, 
        nullable = False,
        default = ""
    )

    location = db.Column(
        db.Text,
        nullable = False
    )

    # created = db.Column(
    #     db.String,
    #     db.ForeignKey('users.username', ondelete='CASCADE'),
    #     nullable=False
    # )

    # rented = db.Column(
    #     db.String,
    #     db.ForeignKey('users.username', ondelete='CASCADE'),
    # )

    @classmethod
    def findAll(cls):
        """Find all current listings"""
        listings = cls.query.all() 
        return listings


    @classmethod
    def generate_url(cls, file_name):
        """Generate url for image in database"""

        response = s3.create_presigned_url("BUCKET",file_name, expiration=None)

        print("response from")
        return response 


    def serialize(self):
        """Serialize to dictionary."""

        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": str(self.price),
            "description": self.description,
            "location": self.location
        }



def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)





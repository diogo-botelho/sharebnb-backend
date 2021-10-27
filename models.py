"""SQL models for shareb&b"""

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

import boto3
s3 = boto3.client('s3')

bcrypt = Bcrypt()
db = SQLAlchemy()

DEFAULT_IMAGE = "https://st4.depositphotos.com/14953852/24787/v/600/depositphotos_247872612-stock-illustration-no-image-available-icon-vector.jpg"

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

    @classmethod
    def findAll(cls):
        """Find all current listings"""
        listings = cls.query.all() 
        return listings


    # @classmethod
    # def findListing(cls,id):
    #     """Find all current listings"""
    #     listings = cls.query.get
    #     return listings

    # @classmethod
    # def createListing(cls,name,image,price,description,location):
    # """Create a new listing {id,name,image,price,description,location}"""
    @classmethod
    def upload_img(cls, file_name):
        """Upload img to s3 bucket"""
        result = s3.upload_file(file_name, "sharebnb-dnd")

        if result: 
            print("success")
            return "success"
        else: 
            print("error")

    @classmethod
    def generate_url(cls, file_name):
        """Generate url for image in database"""

        response = s3.create_presigned_url("sharebnb-dnd",file_name, expiration=None)

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





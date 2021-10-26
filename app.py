

from flask import Flask, jsonify
from flask_debugtoolbar import DebugToolbarExtension
# from sqlalchemy.exc import IntegrityError
# from werkzeug.exceptions import Unauthorized

from models import db, connect_db, Listing

# import dotenv
# dotenv.load_dotenv()

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sharebnb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

connect_db(app)

app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

db.create_all()

##############################################################################
# Listing Routes

@app.get("/listings")
def show_listings():
    """Show all current listings"""
    listings = Listing.findAll()
    serialized = [listing.serialize() for listing in listings]

    return jsonify(listings=serialized)

    
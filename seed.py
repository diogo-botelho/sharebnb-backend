from models import db, Listing
from app import app

# from app import app
with app.app_context():
    db.drop_all()
    db.create_all()

l1 = Listing(
    name="Millenium Park",
    price=100,
    description="",
    location="Chicago",
)

l2 = Listing(
    name="Golden Gate Park",
    description="",
    location="San Francisco",
)

db.session.add_all([l1,l2])
db.session.commit()

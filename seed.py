from models import db, Listing
# from app import app

db.drop_all()
db.create_all()

l1 = Listing(
    name="Millenium Park",
    image="",
    price=100,
    description="",
    location="Chicago",
)

l2 = Listing(
    name="Golden Gate Park",
    image="",
    description="",
    location="San Francisco",
)

db.session.add_all([l1,l2])
db.session.commit()

# Udemy: Master Python by building 100 projects in 100 days
# Mar 12-15, 2025
# Day 66 - Building RESTful API
import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        """Convert the Cafe object to a dictionary."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    """Get a random cafe from the database."""
    res = db.session.execute(db.select(Cafe))
    all_cafes = res.scalars().all()
    random_cafe = random.choice(all_cafes)
    # return jsonify(cafe={
    #     'id': random_cafe.id,
    #     'name': random_cafe.name,
    #     'map_url': random_cafe.map_url,
    #     'img_url': random_cafe.img_url,
    #     'location': random_cafe.location,
    #     'seats': random_cafe.seats,
    #     'has_toilet': random_cafe.has_toilet,
    #     'has_wifi': random_cafe.has_wifi,
    #     'has_sockets': random_cafe.has_sockets,
    #     'can_take_calls': random_cafe.can_take_calls,
    #     'coffee_price': random_cafe.coffee_price,
    # })
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def get_all_cafes():
    """Get all cafes from the database."""
    res = db.session.execute(db.select(Cafe))
    all_cafes = res.scalars().all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search')
def search_cafes_by_location():
    """Search for cafe by location."""
    location = request.args.get('loc')
    res = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    all_cafes = res.scalars().all()

    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={'Not Found': 'Sorry, we don\'t have a cafe at that location.'}), 404


# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    """Add a new cafe to the database."""
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    """Update the price of a cafe."""
    new_price = request.args.get('new_price')
    cafe_to_update = db.get_or_404(Cafe, cafe_id)

    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={'Not Found': 'Sorry, we don\'t have a cafe with that id.'}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    """Delete a cafe from the database."""
    api_key = request.args.get('api-key')

    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)

        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully delete the cafe."}), 200
        else:
            return jsonify(error={'Not Found': 'Sorry, we don\'t have a cafe with that id.'}), 404
    else:
        return jsonify(error={'Forbidden': 'Sorry, that\'s not allowed. Make sure you have the correct'}), 403


if __name__ == '__main__':
    app.run(debug=True)

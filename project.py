from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
@app.route("/restaurants/<int:restaurant_id>/")
def restaurants(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output = ''
    for i in items:
        output += i.name
        output += "</br>"
        output += i.price
        output += "</br>"
        output += i.description
        output += "</br></br>"
    return output


# Task-1: create route for new menu item here
def new_menuitem(restaurant_id):
    pass

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5002)

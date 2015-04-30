from flask import Flask, render_template, request, redirect, url_for
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
    # output = ''
    # for i in items:
    #     output += i.name
    #     output += "</br>"
    #     output += i.price
    #     output += "</br>"
    #     output += i.description
    #     output += "</br></br>"
    return render_template("menu.html", restaurant=restaurant, items=items)


# Task-1: create route for new menu item here
@app.route("/restaurant/<int:restaurant_id>/new/", methods=['GET', 'POST'])
def new_menuitem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'],
                           restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('restaurants', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)


# Task-2: create route for edit menu item function here
@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/edit/")
def edit_menuitem(restaurant_id, menu_id):
    return "Page to Edit menu item. Task-2 complete!"


# Task-3: create a route for delete menu items
@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/delete/")
def delete_menuitem(restaurant_id, menu_id):
    return "Page to delete a menu item. Task-3 complete!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5002)

from app import app
import flask
from flask import request, send_file
from models.product_model import product_model
from models.cart_item_model import cart_item_model
obj= product_model()
cart=cart_item_model()
#API ENDPOINTS ASKED

#Returns a list of all products.
@app.route("/GET/products") 
def getall():
    return obj.product_getall_model()

#Returns details of a specific product.
@app.route("/GET/products/<id>")
def get_specific_product(id):
    return obj.product_getone_model(id)

#Adds a product to the cart.
@app.route("/POST/cart",methods=["POST"])
def add_cart_item():
    return cart.add_cart_model(request.form)

#Retrieves the cart items.
@app.route("/GET/cart")
def getall_cartitems():
    return cart.cart_getall_model()

#Removes a specific item from the cart.
@app.route("/DELETE/cart/<id>", methods=["DELETE"])
def delete_cartitem(id):
    return cart.delete_cartitem_model(id)




#ADDITIONAL API END POINTS FOR CRUD OPERATIONS FOR PRODUCT TABLE
#adds a product to the table
@app.route("/products/add", methods=["POST"])
def add_product():
    return obj.add_product_model(request.form)

#update the product
@app.route("/products/update", methods=["PUT"])
def update_product():
    return obj.update_product_model(request.form)

#delete a product by id
@app.route("/products/delete/<id>", methods=["DELETE"])
def delete_product(id):
    return obj.delete_product_model(id)


#ADDTIONAL API POINTS FOR CRUD OPERATIONS FOR CART_ITEM TABLE

#get specific cart item by id
@app.route("/GET/cart/<id>")
def get_specific_cartitem(id):
    return cart.cart_getone_model(id)

#update cart item
@app.route("/cart/update", methods=["PUT"])
def update_cart():
    return cart.update_cart_model(request.form)
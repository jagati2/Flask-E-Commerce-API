# Flask-E-Commerce-API with MySQL
# Download setup
Step-1: Creating & activating venv Windows:

 python -m venv venv
  ./venv/Scripts/activate

Step-2: Installing Dependencies

  pip install -r requirements.txt

Step-3: Running application Windows:

   $env:PYTHONDONTWRITEBYTECODE=1;$env:FLASK_APP="app";$env:FLASK_ENV = "development"

   
Step-4: Connect MySQL with the code editor and create database=flask_ecommerce and tables= product and cart_item


Step-5:

   flask run

   
# Output 

# product table in mysql

![Screenshot 2024-02-23 192056](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/84199e92-27a2-4af1-8998-8050debb6702)

# cart_item table in mysql

![Screenshot 2024-02-23 192327](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/d17f11da-81b7-4c6d-9aff-d12dbfe91149)

# flask run in VS code

![Screenshot 2024-02-23 191837](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/87269919-baee-4541-8859-a019e622b43f)

# GET /products: Returns a list of all products.

![Screenshot 2024-02-23 191815](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/bf59d07b-0939-4fb3-883c-788b74cd4ddf)

# GET /products/<id>: Returns details of a specific product.

![Screenshot 2024-02-23 192125](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/2733aa4d-cb35-4cbb-b875-fd01e94e5c2d)

# POST /cart: Adds a product to the cart.

![Screenshot 2024-02-23 192417](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/be0199d2-3796-47cd-b0e7-32329bcf3a2b)
![Screenshot 2024-02-23 192619](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/a7360673-c8c5-493c-9a5d-76dcc319f5b4)


# GET /cart: Retrieves the cart items.

![Screenshot 2024-02-23 192519](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/f5b079eb-5085-4077-87e0-96148cf952b1)

# DELETE /cart/<id>: Removes a specific item from the cart.

![Screenshot 2024-02-23 192607](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/9a2a78c1-8db9-4812-8309-e46628a1cf74)

# in mysql id=2 is deleted
![Screenshot 2024-02-23 192619](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/25a81b0e-90dd-4c57-9a15-711fe6fa679d)

# Additional end points 
# get specific cart item by id
![Screenshot 2024-02-23 194742](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/a311dbe5-ebb2-4622-9c8c-892d81acda28)

# adds a product to the table
![Screenshot 2024-02-23 195227](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/77fe5429-c3a0-4b0e-bbf1-48489790d8da)
![Screenshot 2024-02-23 195240](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/546f874a-a7b6-4f8e-8265-7145fce7d6ac)


# update cart item
![Screenshot 2024-02-23 194742](https://github.com/jagati2/Flask-E-Commerce-API/assets/105737471/6ac54a76-4d28-4302-a082-43bafee4a434)



















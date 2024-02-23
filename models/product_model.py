import mysql.connector
import json
from flask import make_response , jsonify
import mysql.connector
import json

class product_model:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host='localhost',user='root',password='Purple@123',database='flask_ecommerce')
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection successful ")       
        except:
            print("error") 

    # READ OPERATION 
    def product_getall_model(self):
        self.cur.execute("select * from product")
        result=self.cur.fetchall()
        if len(result)>0:
         print(result)
         return json.dumps(result)
        else:
           return "NO DATA FOUND"


        #getting details of specific product

    def product_getone_model(self,id):
       self.cur.execute(f"SELECT * FROM product WHERE id={id}")
       product = self.cur.fetchone() 
       pass
       if product:
          print (product)
          return json.dumps( product) 
       else:
          return "NOT DATA FOUND ENTER VALID ID "  #the given ID is not found
       
          
         
    #CREATE OPERATION
    def add_product_model(self,data):
        self.cur.execute(f"INSERT INTO product(id ,name, description, price, image_url) VALUES('{data['id']}','{data['name']}', '{data['description']}', '{data['price']}', '{data['image_url']}')")
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)
    
    
    #UPDATE OPERATION
    def update_product_model(self,data):
        self.cur.execute(f"UPDATE product SET name='{data['name']}', description='{data['description']}', price='{data['price']}',image_url='{data['image_url']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)
        
    #DELETE OPERATION    
    def delete_product_model(self,id):
        self.cur.execute(f"DELETE FROM product WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"DELETED_SUCCESSFULLY"},202)
        else:
            return make_response({"message":"CONTACT_DEVELOPER"},500)
        


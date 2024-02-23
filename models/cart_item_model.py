import mysql.connector
import json
from flask import make_response , jsonify
import mysql.connector
import json

class cart_item_model:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host='localhost',user='root',password='Purple@123',database='flask_ecommerce')
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)     
        except:
            print("error") 

        

    # READ OPERATION 
    def cart_getall_model(self):
        self.cur.execute("select * from cart_item")
        result=self.cur.fetchall()
        if len(result)>0:
         print(result)
         return json.dumps(result)
        else:
           return "NO DATA FOUND"


        #getting details of specific cartitem

    def cart_getone_model(self,id):
       self.cur.execute(f"SELECT * FROM cart_item WHERE id={id}")
       product = self.cur.fetchone() 
       pass
       if product:
          print (product)
          return json.dumps( product) 
       else:
          return "NOT DATA FOUND ENTER VALID ID "  #the given ID is not found
       
          
         
    #CREATE OPERATION
    def add_cart_model(self,data):
        self.cur.execute(f"INSERT INTO cart_item(id,product_id,quantity ) VALUES('{data['id']}','{data['product_id']}', '{data['quantity']}')")
        return make_response({"message":"ADDED_TO_CART"},201)
    
    
    #UPDATE OPERATION
    def update_cart_model(self,data):
        self.cur.execute(f"UPDATE cart_item SET product_id='{data['product_id']}', quantity='{data['quantity']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({"message":"UPDATED_CART_SUCCESSFULLY"},201)
        else:
            return make_response({"message":"NOTHING_TO_UPDATE"},204)
        
    #DELETE OPERATION    
    def delete_cartitem_model(self,id):
        self.cur.execute(f"DELETE FROM cart_item WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"DELETED_FROM_CART_SUCCESSFULLY"},202)
        else:
            return make_response({"message":"CANNOT_DELETE_CONTACT_DEVELOPER"},500)
        
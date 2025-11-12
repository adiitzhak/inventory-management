from src.product import Product
from src.database.database import Database

class Inventory:
    def __init__(self):
        """init null database"""       
        self.database = Database()
        
          
    def add_product(self, product : Product):
        """ add product to database"""
        if self.database.collection.find_one({"name": product.name}):
            self.database.collection.update_one({"name" : product.name} ,{"$inc": {"quantity": 1}} )           
        else:
            self.database.collection.insert_one({"name": product.name, "price" : product.price ,"quantity": 1})
    def remove_product(self, product_name : str) -> None:
        """remove product from database"""
               
        product = self.database.collection.find_one({"name": product_name})
        if not product:
            raise ValueError("cannot found this product")
        
        if product["quantity"] > 1:
             self.database.collection.update_one({"name": product_name}, {"$inc" : {"quantity" : -1}})
        else:
             self.database.collection.delete_one({"name" : product_name})
        
        
    def get_product(self, product_name : str) ->Product:
        """return product by name"""
        product= self.database.collection.find_one({"name": product_name})
        if not product:
            raise ValueError("cannot fount this product")
        else:
            return Product(name= product["name"], price = product["price"])
          
    def total_inventory_price(self) -> float:
        """calculate total price"""
        total_price = 0.0
        for data in self.database.collection.find():
            total_price += data["price"] * data["quantity"]
        return total_price
            
           
        
        
        
                
            
        
   
        
        
        
        
        
 
        
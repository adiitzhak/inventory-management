from pymongo import MongoClient
from src.database.constants.constants import DATABASE_CONNECTION

class Database:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance =super().__new__(cls)
            cls._instance.client = MongoClient(DATABASE_CONNECTION)
            cls._instance.db = cls._instance.client["inventory"]
            cls._instance.collection = cls._instance.db["products"]
        return cls._instance
    
    def add_product(self, name, price, quantity):
        self.collection.insert_one({"name": name, "price" : price, "quantity": quantity})
        
            
            
from pymongo import MongoClient


class Database:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance =super().__new__(cls)
            cls._instance.client = MongoClient("mongodb://localhost:27017/")
            cls._instance.db = cls._instance.client["inventory"]
            cls._instance.collection = cls._instance.db["products"]
        return cls._instance
    
    def add_product(self, name, price, quantity):
        self.collection.insert_one({"name": name, "price" : price, "quantity": quantity})
        
            
            
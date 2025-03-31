from pymongo import MongoClient
import gridfs

# ✅ MongoDB Atlas Connection
client = MongoClient("mongodb+srv://madhu:madhu_1052@cluster0.krmsrrk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["Finish_db"]
fs = gridfs.GridFS(db)

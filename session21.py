
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mohit:656434@cluster0.luwabvg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    
except Exception as e:
    print(e)

db = client['mohit']

# Get Collection Names from DataBase
collections = db.list_collection_names()

for collection in collections:
    print(collection)

documents = db['users'].find()
print(documents)

for document in documents:
    print(document)
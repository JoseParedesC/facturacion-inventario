from fastapi import FastAPI
import pymongo
from Controller.ProductosController_prueba import ProductoController as PController
import Model.Productos as Productos

app = FastAPI()

#mongodb+srv://jparedesc1813:PassMongoDB@cluster0.r5exmak.mongodb.net/


client = pymongo.MongoClient("mongodb+srv://jparedesc1813:PassMongoDB@cluster0.r5exmak.mongodb.net/")

db = client['Sistema_de_Ventas']
collection = db['Productos']

try:
    if client.server_info():
        print("Conexión a MongoDB establecida correctamente.")

    var = collection.find()
    
except pymongo.errors.ConnectionFailure as e:
    print("No se pudo conectar a MongoDB: %s" % e)



@app.get("/")
def Productos_getAll():
    if client.server_info():
        print("Conexión a MongoDB establecida correctamente.")
    return {"message": "Conexión a la base de datos exitosa"}



@app.post("/producto/", response_model=Productos)
def create_producto(product: Productos):
    prod_data = product.dict()
    inserted_prod = collection.insert_one(prod_data)
    return product@app.post("/producto/", response_model=Productos)



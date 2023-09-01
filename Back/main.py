from fastapi import FastAPI
from pymongo import MongoClient
from Controller.ProductosController_prueba import ProductoController as PController

app = FastAPI()


MONGO_URI = ''

client = MongoClient(MONGO_URI)

db = client['teststore']
collection = db['productos']





@app.get("/")
def Productos_getAll():
    try:
        data = PController.Producto_buscarTodos()
        return data
    except ValueError:
        return {"error":"monda"}
    


@app.get("/productos/{code}")
def Productos_getByCode(code):
    data = PController.Productos_buscarPorCodigo(code)
    return data
import Model.Productos as Productos
import json

class ProductoController:

    def Producto_buscarTodos():
        urlJson = "C:/Users/ERDA/Documents/PersonalProyects/FacturacionPython/Back/data/data.json"   
        with open(urlJson) as contenido:
            data = json.load(contenido)

        return data
        

    def Productos_buscarPorCodigo(code):
        urlJson = "C:/Users/ERDA/Documents/PersonalProyects/FacturacionPython/Back/data/data.json"   
        with open(urlJson) as contenido:
            data = json.load(contenido)
            new_data = ""
            if data["codigo_producto"] == code:
                new_data = data

        return new_data

    def Producto_SalvarActualizar():
        pass

    def Producto_CambioEstado():
        pass
    
    def Producto_Eliminar():
        pass

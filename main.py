from fastapi import FastAPI #importa la clase fastapi de la libreria fastapi
app = FastAPI() #crea una instancia de la clase fastapi en la variable app
app.title = 'Mi primera aplicación de películas y análisis de datos' #asigna un valor a la variable title
app.version = '0.0.1'
@app.get('/',tags=['Home']) #decorador para definir una ruta
def message(): #funcion que retorna un objeto
    return 'Hello World' #devolvemos un diccionario

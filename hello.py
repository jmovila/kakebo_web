from flask import Flask#importa la clase Flask

app = Flask(__name__)#crear una instancia de Flask()--la clase que es la aplicación

@app.route('/')#estructura basica..decorador...asocia la ruta con la función
def index():
    return 'Hola, mundo!'

@app.route('/adios')
def bye():
    return 'Hasta luego, cocodrilo'


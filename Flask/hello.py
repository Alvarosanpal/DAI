# -*- coding: utf-8 -*-
from flask import Flask,request
import mandelbrot
app = Flask(__name__)

@app.route("/user/pepe")
def usuariopepe():
    return "Hola señor pepe ,¿Que tal?"

@app.route("/user/zejillo")
def usuariozejilloe():
    return "Esta es la página de Zejillo."

@app.route("/user/<name>")
def cualquiera(name):
    return "Aqui entra cualquier persona por ejemplo "+name

@app.route("/carpeta")
def carpeta():

    x1 = request.args.get('x1')
    y1 = request.args.get('y1')
    x2 = request.args.get('x2')
    y2 = request.args.get('y2')
    witdh= request.args.get('witdh')
    mandelbrot.renderizaMandelbrot(x1,y1,x2,y2,witdh,1,"foto")
    return x1+" "+y1+" "+x2+" "+y2+" "+witdh

@app.route("/")
def hello():
    return "Hola Mundo"


@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

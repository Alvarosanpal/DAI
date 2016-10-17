# -*- coding: utf-8 -*-
from flask import Flask,request, url_for
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

@app.route("/mandelbrot")
def mandelbro():

    x1 = float(request.args.get('x1'))
    y1 = float(request.args.get('y1'))
    x2 = float(request.args.get('x2'))
    y2 = float(request.args.get('y2'))
    witdh= int(request.args.get('witdh'))
    mandelbrot.renderizaMandelbrot(x1,y1,x2,y2,witdh,50,"static/foto.png")
    image='<img src=' + url_for('static',filename='foto.png') + '>'
    return image

@app.route("/")
def hello():
    return "Hola Mundo"


@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

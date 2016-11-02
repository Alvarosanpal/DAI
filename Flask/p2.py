# -*- coding: utf-8 -*-
from flask import Flask,request, url_for,render_template
import mandelbrot
import random
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
    mandelbrot.renderizaMandelbrot(x1,y1,x2,y2,witdh,20,"static/foto.png")
    image='<img src=' + url_for('static',filename='foto.png') + '>'
    return image

@app.route("/")
def hello():
    return 'static/index.html'
@app.route("/svg")
def svg():
    color=['green','blue','red','yellow','orange','black','purple','pink']
    bucle=random.randint(1,100)
    imagen='<svg height="1000" width="1000">'
    for i in range(20):
        forma={'1':'<circle cx="'+str(random.randint(1,1000))+'" cy="'+str(random.randint(1,1000))+'" r="'+str(random.randint(1,40))+'" stroke="'+color[random.randint(1,7)]+'" stroke-width="'+str(random.randint(1,8))+'" fill="'+color[random.randint(1,7)] +'" />',
        '2':'<rect x="'+str(random.randint(1,1000))+'" y="'+str(random.randint(1,1000))+'" height="'+str(random.randint(1,200))+'" width="'+str(random.randint(1,200))+'" stroke="'+color[random.randint(1,7)]+'" stroke-width="'+str(random.randint(1,8))+'" fill="'+color[random.randint(1,7)] +'" />',
        '3':'<ellipse cx="'+str(random.randint(1,1000))+'" cy="'+str(random.randint(1,1000))+'" rx="'+str(random.randint(1,200))+'" ry="'+str(random.randint(1,200))+'" stroke="'+color[random.randint(1,7)]+'" stroke-width="'+str(random.randint(1,8))+'" fill="'+color[random.randint(1,7)] +'" />'}
        imagen=imagen+forma[str(random.randint(1,3))]

    imagen=imagen+'</svg>'
    return imagen


@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

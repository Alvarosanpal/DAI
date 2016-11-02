# -*- coding: utf-8 -*-
from flask import Flask,request, url_for,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    conjunto={'logo':'logo.png','titulo':'Geoke','subtitulo':'el subtitulo','menu':[{'text':'home','link':'#home'},{'text':'info','link':'#info'},{'text':'contacto','link':'#contacto'}]}
    return render_template('index.html',contenido=conjunto)

@app.route("/fanta")
def fanta():
    conjunto={'logo':'fanta.png','titulo':'Fanta','subtitulo':'Ahora con limon','menu':[{'text':'Home','link':'#fanta'},{'text':'Proyecto Fanta','link':'http://www.fanta.com.ar/es/home/'}]}
    return render_template('index.html',contenido=conjunto)


@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

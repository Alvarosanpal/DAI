# -*- coding: utf-8 -*-
from flask import Flask,request, url_for,render_template,session,redirect

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
def ini(text,link):
    if not session:
        session['count']=0
        session['pag']=[{'text':'','link':''},{'text':'','link':''},{'text':'','link':''}]
    session['pag'][session['count']]['text']=text
    session['pag'][session['count']]['link']=link
    session['count']=(session['count']+1)%3

@app.route("/")
def hello():
    ini("Home","/")
    conjunto={'subtitulo':'Pagina Principal','paginas':session['pag']}
    return render_template('index.html',contenido=conjunto)

@app.route("/registro")
def registro():
    ini("Registrarse","/registro")
    conjunto={'subtitulo':'registrarse','paginas':session['pag']}
    return render_template('registro.html',contenido=conjunto)

@app.route("/login", methods = ['POST'])
def login():
    usu=str(request.form['username'])
    passwd=str(request.form['pass'])
    if usu=="dai" and passwd=="dai":
        session['username']=usu
    return redirect(url_for('hello'))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('hello'))

@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

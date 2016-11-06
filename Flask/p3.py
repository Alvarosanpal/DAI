# -*- coding: utf-8 -*-
from flask import Flask,request, url_for,render_template,session,redirect
import shelve
d = shelve.open('db',writeback=True)
app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
def ini(text,link):
    if not session:
        session['count']=0
        session['pag']=[{'text':'','link':''},{'text':'','link':''},{'text':'','link':''}]
    try:
        if session['username']:
            session['pag'][session['count']]['text']=text
            session['pag'][session['count']]['link']=link
            session['count']=(session['count']+1)%3
    except Exception as e:
        print ""


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

@app.route("/registrar", methods = ['POST'])
def registrar():

    d[str(request.form['alias'])]={ 'nombre': str(request.form['nombre']), 'apellidos':str(request.form['apellidos']), 'password':str(request.form['pass']), 'email':str(request.form['email']) }

    session['username']=str(request.form['alias'])
    return redirect(url_for('hello'))

@app.route("/login", methods = ['POST'])
def login():
    if d.has_key(str(request.form['username'])) and str(d[str(request.form['username'])]['password'])==str(request.form['pass']):
        session['username']=str(request.form['username'])
    return redirect(url_for('hello'))
@app.route("/profile")
def profile():
    ini("Datos personales","/profile")
    conjunto={'subtitulo':'Datos Personales','paginas':session['pag']}
    return render_template('profile.html',contenido=conjunto,usu=d[str(session['username'])],actualizar=False)

@app.route("/modifica")
def modifica():

    conjunto={'subtitulo':'Datos Personales','paginas':session['pag']}
    return render_template('profile.html',contenido=conjunto,usu=d[str(session['username'])],actualizar=True)
@app.route("/actualizar", methods = ['POST'])
def actualizar():
    d[str(session['username'])]={ 'nombre': str(request.form['nombre']), 'apellidos':str(request.form['apellidos']), 'password':str(request.form['password']), 'email':str(request.form['email']) }
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

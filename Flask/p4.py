# -*- coding: utf-8 -*-
from flask import Flask,request, url_for,render_template,session,redirect
from pymongo import MongoClient,DESCENDING
from flask_paginate import Pagination
import json
client = MongoClient()
db=client.test
db = db.restaurants
app = Flask(__name__)

@app.route("/eliminar")
def elimina():
    id=request.args.get('id')
    assert(id)
    db.remove({'restaurant_id':id})
    return str(1)
@app.route("/update", methods=['POST'])
def update():
    print request.form['restaurant_id']
    restaurant_id=request.form['restaurant_id']
    name=request.form['name']
    borough=request.form['borough']
    cuisine=request.form['cuisine']
    db.update_one({'restaurant_id': restaurant_id},{'$set':{'name':name,'cuisine':cuisine,'borough':borough}})
    return json.dumps(db.find_one({'restaurant_id': restaurant_id},{'name':1,'cuisine':1,'borough':1,'_id':0,'restaurant_id':1}))
@app.route("/add", methods=['POST'])
def add():

    name=request.form['name']
    borough=request.form['borough']
    cuisine=request.form['cuisine']
    restaurant_id=db.find({},{'_id':0,'restaurant_id':1}).sort('restaurant_id',DESCENDING)
    restaurant_id=str(int(restaurant_id[0]['restaurant_id']) +1)
    db.insert({'name':name,'cuisine':cuisine,'borough':borough,'restaurant_id':restaurant_id})

    return json.dumps(db.find_one({'restaurant_id':str(restaurant_id)},{'_id':0}))
@app.route("/actualiza")
def actu():
    restaurant=db.find({},{'name':1,'cuisine':1,'borough':1,'_id':0,'restaurant_id':1})
    data={'data':[]}
    for i in restaurant:
        data['data'].append(i)
    return json.dumps(data)
@app.route("/")
def hello():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get('page', type=int, default=1)
    restaurant=db.find({},{'name':1,'cuisine':1,'borough':1,'_id':0,'restaurant_id':1})
    pagination = Pagination(page=page, css_framework='foundation',total=restaurant.count(), search=search, record_name='restaurant',per_page=50)
    return render_template('index.html',todo=restaurant.skip(pagination.per_page*(page-1)).limit(pagination.per_page),pagination=pagination)



@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

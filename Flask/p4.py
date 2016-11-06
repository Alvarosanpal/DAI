# -*- coding: utf-8 -*-
from flask import Flask,request, url_for,render_template,session,redirect
from pymongo import MongoClient
from flask_paginate import Pagination
client = MongoClient()
db=client.test
db = db.restaurants
app = Flask(__name__)
@app.route("/")
def hello():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get('page', type=int, default=1)
    restaurant=db.find({},{'name':1,'cuisine':1,'borough':1,'_id':0})
    pagination = Pagination(page=page, total=restaurant.count(), search=search, record_name='restaurant',per_page=50)
    return render_template('index.html',todo=restaurant.skip(pagination.per_page*page).limit(pagination.per_page),pagination=pagination)



@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

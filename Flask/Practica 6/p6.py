# -*- coding: utf-8 -*-
from flask import Flask,request, url_for,render_template,session,redirect
from pymongo import MongoClient,DESCENDING
from flask_paginate import Pagination
import json
import atexit
from apscheduler.scheduler import Scheduler
import feedparser
import urllib2
import tweepy
client = MongoClient()
db=client.test
db = db.restaurants
app = Flask(__name__)
# ------------------------------------------------------------------------------
# pip install apscheduler==2.1.2
cron = Scheduler(daemon=True)
# Explicitly kick off the background thread
cron.start()

@cron.interval_schedule(minutes=10)
def job_function():
    d = feedparser.parse('http://www.htcmania.com/external.php?forumids=417')
    array=[]
    for i in range(9):
        p=d['items'][i]['content']
        array.append(p[0]['value'])
    data={}
    data['value']=array
    with open('static/data.json', 'wr') as outfile:
        json.dump(data, outfile)
    # Consumer keys and access tokens, used for OAuth
    consumer_key = 'KFcNopkjR9iXxV5nPfjPapmTI'
    consumer_secret = 'NVqfW8HP4NemUZuAM9AZOuPrc4CcS9VzX4VDNhm7xTbmVdA4XF'
    access_token = '1017044778-z2973SUROnkQIUInybyXGbKeEsD5LyswACnwSbH'
    access_token_secret = 'axUtvYsUY8JUsO2XPRx6frYX2NeTsVJV0uPeoHUDrQmB9'
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
    # https://dev.twitter.com/docs/api/1.1/get/search/tweets
    tweets = api.search(q='from:htcmania sorteo', count=15)
    data=[]
    for tweet in tweets:
        dato={'name':tweet.user.screen_name,'id':str(tweet.id)}
        data.append(dato)
    datos={}
    datos['value']=data
    with open('static/twitter.json', 'wr') as outfile:
        json.dump(datos, outfile)
    trends=api.trends_place(id=766273)
    with open('static/trends.json', 'wr') as outfile:
        json.dump(trends, outfile)
# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))
# ------------------------------------------------------------------------------
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
@app.route("/graficos")
def graficos():
    return render_template('graficas.html')
@app.route("/maps")
def maps():
    return render_template('maps.html')
@app.route("/twitter")
def twitter():

    return render_template('twitter.html')
@app.route("/")
def hello():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

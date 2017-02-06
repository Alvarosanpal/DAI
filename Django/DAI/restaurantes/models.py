from __future__ import unicode_literals

from django.db import models
import json
# Create your models here.
from django.conf import settings
TEST = settings.CLIENT.test
RESTAURANTES = settings.CLIENT.test.restaurants

class Restaurantes():
    #def add(self):

    def muestraRestaurantes(self):
        restaurant=RESTAURANTES.find({},{'name':1,'cuisine':1,'borough':1,'_id':0,'restaurant_id':1})
        data={'data':[]}
        for i in restaurant:
            data['data'].append(i)
        return json.dumps(data)
    def add(self,data):
        name=data['nombre']
        borough=data['ciudad']
        restaurant_id=RESTAURANTES.find({},{'_id':0,'restaurant_id':1}).sort('restaurant_id',-1)
        restaurant_id=str(int(restaurant_id[0]['restaurant_id']) +1)
        RESTAURANTES.insert({'name':name,'cuisine':'','borough':borough,'restaurant_id':restaurant_id})
        return RESTAURANTES.find_one({'restaurant_id':str(restaurant_id)},{'_id':0})
    def eliminar(self,id):
        RESTAURANTES.remove({'restaurant_id':id})
    def modificar(self,data):
        restaurant_id=data['id_restaurante']
        name=data['nombre']
        borough=data['ciudad']
        cuisine=''
        RESTAURANTES.update_one({'restaurant_id': restaurant_id},{'$set':{'name':name,'cuisine':cuisine,'borough':borough}})
        return RESTAURANTES.find_one({'restaurant_id': restaurant_id},{'name':1,'cuisine':1,'borough':1,'_id':0,'restaurant_id':1})

# -*- coding: utf-8 -*-
import sys
from xml.etree.ElementTree import ElementTree
import urllib
import feedparser

d = feedparser.parse("portada.xml")
if(len(sys.argv)==1):
    item=0
    enclosure=0
    for element in d['items']:
        item +=1
        for imagen in element["enclosures"]:
            enclosure+=1
            url=imagen.get('url')
            response=urllib.urlopen(url)
            out_file=open("imagenes/"+ url.split("/")[len(url.split("/"))-1] , 'wb')
            data = response.read() # a `bytes` object
            out_file.write(data)
    print "Hay " + str(item) + " noticias o contenidos "
    print "Hay " + str(enclosure) + " imagenes "
else:
    search=str(sys.argv[1])
    print d

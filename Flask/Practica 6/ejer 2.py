# -*- coding: utf-8 -*-
import sys
from xml.etree.ElementTree import ElementTree
import urllib

tree = ElementTree()
tree.parse('portada.xml')
if(len(sys.argv)==1):
    print "Hay " + str(len(tree.findall(".//item")))+ " noticias o contenidos "
    print "Hay " + str(len(tree.findall(".//enclosure")))+ " imagenes "
    for imagen in tree.iter("enclosure"):
        url=imagen.get('url')
        response=urllib.urlopen(url)
        out_file=open("imagenes/"+ url.split("/")[len(url.split("/"))-1] , 'wb')
        data = response.read() # a `bytes` object
        out_file.write(data)
else:
    search=str(sys.argv[1])
    print "Hay " + str(len(list(tree.iter(search)))) + " " + search + " en el xml"
    for element in tree.iter(search):
        print element.text

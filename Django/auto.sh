#!/bin/bash
carpeta=$1

django-admin startproject $carpeta

cd $carpeta

python manage.py startapp restaurantes
mkdir templates
mkdir static

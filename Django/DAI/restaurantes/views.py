from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from restaurantes.models import Restaurantes
import json
from django.http import JsonResponse
from restaurantes.forms import formAdd
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    form = formAdd()
    return render(request,'restaurantes.html', {'form':form})

def test(request):
    return render(request,'test.html', {})

@login_required
def cargarrestaurantes(request):
    resta=Restaurantes()
    return HttpResponse(resta.muestraRestaurantes())

def addRestaurantes(request):

    if request.method == 'GET':
        return HttpResponse("El metodo utilizado debe ser POST")

    # A POST request: Handle Form Upload
    form = formAdd(request.POST) # Bind data from request.POST into a restaurantes_form

    # If data is valid, proceeds to create a new post and redirect the user
    if form.is_valid():
        #content = form.cleaned_data['content']
        #created_at = form.cleaned_data['created_at']
        #post = m.Post.objects.create(content=content,created_at=created_at)

        return JsonResponse({'mensaje':form.save()})
    else:
        return JsonResponse(form.errors, status=500)

    return JsonResponse({'ok':"AS"})
def eliminar(request):
    if request.method == 'POST':
        return HttpResponse("El metodo utilizado debe ser GET")

    resta=Restaurantes()
    id=request.GET['id']
    assert(id)
    resta.eliminar(id)
    return JsonResponse({'mensaje':"Eliminado con exito"}, status=200)
def actualiza (request):

    if request.method == 'GET':
        return HttpResponse("El metodo utilizado debe ser POST")

    # A POST request: Handle Form Upload
    form = formAdd(request.POST) # Bind data from request.POST into a restaurantes_form

    # If data is valid, proceeds to create a new post and redirect the user
    if form.is_valid():
        #content = form.cleaned_data['content']
        #created_at = form.cleaned_data['created_at']
        #post = m.Post.objects.create(content=content,created_at=created_at)

        return JsonResponse({'mensaje':form.update()})
    else:
        return JsonResponse(form.errors, status=500)

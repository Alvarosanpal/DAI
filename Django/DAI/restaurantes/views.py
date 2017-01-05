from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'restaurantes.html', {})

def test(request):
    return render(request,'test.html', {})

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
 dict_title={"title" :"inicio"}
 return render(request,"appcoder/index.html",dict_title)

def estudiantes(request):
 return render(request,"appcoder/estudiantes.html")

def profesores(request):
 return render(request,"appcoder/profesores.html")
 
def cursos(request):
  return render(request,"appcoder/cursos.html")
 
def entregables(request):
  return render(request,"appcoder/entregables.html")

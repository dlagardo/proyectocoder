from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from appcoder.models import Curso,Estudiante
from appcoder.forms import CursoFormulario
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
  
def formulario_curso(request):
  if request.method == "POST":
     curso= CursoFormulario(request.POST)
     print(curso)
     if curso.is_valid:

        data = curso.cleaned_data
        curso_nuevo = Curso(data['nombre'], data['camada'])
        curso_nuevo.save()
        return render(request,"appcoder/index.html")

  else:
        curso_form= CursoFormulario()
        return render(request,"appcoder/cursosFormulario.html",{"formulario":curso_form})


def buscarCurso(request):

   data = request.GET.get('camada', "")
   error = ""
   print(data)
   if data:
     try:
      curso= Curso.objects.filter(camada = data)

      return render(request,'appcoder/busquedaCurso.html', {"curso": curso[0]})

     except Exception as exc:
            print(exc)
            error = "No existe esa camada"

   return render(request, 'appcoder/busquedaCurso.html', {"error": error})

   
    

       

     
      
    
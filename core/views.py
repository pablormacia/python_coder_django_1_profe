from django.shortcuts import render

# Create your views here.

def inicio(request):
    contexto = {
        "mensaje": "Mensaje modificado desde la rama feature/template"
    }

    return render(request, "template.html", contexto)
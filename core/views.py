from django.shortcuts import render

# Create your views here.

def inicio(request):
    contexto = {
        "mensaje": "Proyecto Django funcionando"
    }

    return render(request, "template.html", contexto)
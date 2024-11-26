from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import dashboard
from AppCoder.forms import CursoFormulario

def inicio(req):
    return render(req, 'appcoder/padre.html')

def dashboard(req):
    return render(req, 'appcoder/dashboard.html')

def analista(req):
    return render(req, 'appcoder/analista.html')

def proveedores(req):
    return render(req, 'appcoder/proveedores.html')


def dashboard_form(req):
    if req.method == 'POST':
      
            dashboard =  dashboard(dashboard=req.POST['dashboard'],camada=req.POST['camada'])
 
            dashboard.save()
 
            return render(req, "AppCoder/index.html")
 
    return render(req,"AppCoder/dashboard_formulario.html")

def dashboard_form_2(request):

    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)  
        print(miFormulario) 

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data  
            dashboard = dashboard(dashboard=informacion["dashboard"], camada=informacion["camada"])  
            dashboard.save()  
            return render(request, "AppCoder/index.html")  
    else:
        miFormulario = CursoFormulario()  

    return render(request, "AppCoder/dashboard_formulario_2.html", {"miFormulario": miFormulario})


def busquedaCamada(request):
     return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

    if request.GET["camada"]:

        camada = request.GET['camada']

        dashboard = dashboard.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/resultadosBusqueda.html", {"dashboard": dashboard, "camada": camada})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)
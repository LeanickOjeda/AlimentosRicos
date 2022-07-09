from django.shortcuts import render, redirect
from .forms import MenuForm
from .models import MenuSemana


# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def menusemanal(request):
    menusemana= MenuSemana.objects.all()

    datos = {
        'menusemana': menusemana,
        'form': MenuForm
    }
    if request.method== 'POST':
        formulario = MenuForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"

    return render(request, 'core/menusemanal.html', datos)

def form_del_menu(request, id):
    menudel = MenuSemana.objects.get(nrocatalogo=id)
    menudel.delete()

    return redirect(to="menusemanal")
    

def modificar_menu(request, id):
    modmenu = MenuSemana.objects.get(nrocatalogo=id)

    datos = {
        'form': MenuForm(instance=modmenu)
    }
    if request.method=='POST':
        formulario = MenuForm(data=request.POST,instance=modmenu)
        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Modeficacion Exitosa"

    return render(request, 'core/modificar_menu.html', datos)

def pagoapropiado(request):
    return render(request, 'core/pagoapropiado.html')

def registrarusuario(request):
    
    return render(request, 'core/registrarusuario.html')
def login(request):
    
    return render(request, 'core/login.html')

def repartidores(request):
    return render(request, 'core/repartidores.html')

#Fichas

def FichaEnsalada(request):
    return render(request, 'core/Fichas/FichaEnsaladas.html')

def FichaInternacional(request):
    return render(request, 'core/Fichas/FichaInternacional')

def FichaMariscos(request):
    return render(request, 'core/Fichas/FichaMariscos.html')

def FichaPlatilloDia(request):
    return render(request, 'core/Fichas/FichaPlatilloDia.html')

def FichaPlatillosPrincipales(request):
    return render(request, 'core/Fichas/FichaPlatillosPrincipales.html')

def FichaPostres(request):
    return render(request, 'core/Fichas/FichaPostres.html')

def FichaSopas(request):
    return render(request, 'core/Fichas/FichaSopas.html')

def FichaVeganos(request):
    return render(request, 'core/Fichas/FichaVeganos.html')

#Catalogos

def Ensalada(request):
    return render(request, 'core/Catalogos/Ensaladas.html')

def Internacional(request):
    return render(request, 'core/Catalogos/Internacional')

def Mariscos(request):
    return render(request, 'core/Catalogos/Mariscos.html')

def PlatilloDia(request):
    return render(request, 'core/Catalogos/PlatilloDia.html')

def PlatillosPrincipales(request):
    return render(request, 'core/Catalogos/PlatillosPrincipales.html')

def Postres(request):
    return render(request, 'core/Catalogos/Postres.html')

def Sopas(request):
    return render(request, 'core/Catalogos/Sopas.html')

def Veganos(request):
    return render(request, 'core/Catalogos/Veganos.html')


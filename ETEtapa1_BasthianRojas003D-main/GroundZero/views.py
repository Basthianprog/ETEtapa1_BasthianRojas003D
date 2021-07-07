from django.shortcuts import render, redirect
from .models import Registro
from .models import Telefono
from .models import Moneda
from .forms import RegistroForm
# Create your views here.
def Paginaprincipal(request):

    return render(request, 'Paginaprincipal.html'

      

    )

def Productos(request):

    return render(request, 'Productos.html'

      

    )

def QuienesSomos(request):

    return render(request, 'QuienesSomos.html'

      

    )

def Registro(request):

    return render(request, 'Registro.html'

      

    )

def Despacho(request):

    return render(request, 'Despacho.html'

      

    )

def Comentarios(request):

    registros = Registro.objects.all

    
    
    return render(request, 'Registros.html', context ={ 'datos':registros},
    
    
    
    )
def Registros(request):
    registros = Registro.objects.all

    return render(request, 'Registros.html', context ={ 'datos':registros},
    
    
    
    )

def Telefonos(request):
    telefonos = Telefono.objects.all

    return render(request, 'Registros.html', context ={ 'datos':telefonos},
    
    
    
    )

def Monedas(request):
    monedas = Moneda.objects.all

    return render(request, 'Registros.html', context ={ 'datos':monedas},
    
    
    
    )
def crearRegistro(request):
    if request.method=='POST':
        registro_form = RegistroForm(request.POST)
        if registro_form.is_valid():
            registro_form.save()
            return redirect('Registros')
    else:
        registro_form= RegistroForm()
    return render(request, 'GroundZero/crearRegistro.html', {'registro_form': registro_form}

      

    )

def modRegistro(request,id):
    registro = Registro.objects.get(numeroid=id)

    com ={
        'form': RegistroForm(instance=registro)
    }
    if request.method=='POST':
        formulario = RegistroForm(data=request.POST, instance = registro)
        if formulario.is_valid:
            formulario.save()
            return redirect('Registros')
    
    
    return render(request, 'GreenPanda/modRegistro.html', com
    
    
    
    )

def eliminar(request,id):
    comentario = Registro.objects.get(NombreC=id)
    comentario.delete()
    return redirect('Registros')

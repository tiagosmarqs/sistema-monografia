from django.shortcuts import get_object_or_404, redirect, render

from orientador.forms import OrientadorForm
from orientador.models import Orientador

# Create your views here.
def index(request):

    orientador = Orientador.objects.all()
    context = {
        'lista': orientador,
        'page': 'orientador'
    }

    return render(request, 'listar_orientador.html', context=context)

def cadastrar(request):

    if request.method == 'GET':

        form = OrientadorForm()
        context = {
            'form': form,
            'page': '/',
            'titulo': 'Orientador'
        }
        return render(request, 'cadastrar.html', context=context)
    else:

        form = OrientadorForm(request.POST)
        
        if form.is_valid():
            orientador = form.save()
            form = OrientadorForm()

        context = {
            'form': form,
            'page': '/',
            'titulo': 'Orientador'
        }
        return render(request, 'cadastrar.html', context=context)


def editar(request, id):

    orientador = get_object_or_404(Orientador, pk=id)
    form = OrientadorForm(instance=orientador)

    if request.method == 'POST':

        form = OrientadorForm(request.POST, instance=orientador)

        if form.is_valid():

            orientador.save()

            return redirect('/orientador/')
        else:

            context = {
                'form': form, 
                'identificador': orientador,
                'page': '/orientador/'
            }

            return render(request, 'editar.html', context=context)        
    else:

        context = {
            'form': form, 
            'identificador': orientador,
            'page': '/orientador/'
        }

        return render(request, 'editar.html', context=context)  


def deletar(request, id):

    orientador = get_object_or_404(Orientador, pk=id)
    orientador.delete()

    return redirect('/orientador/')
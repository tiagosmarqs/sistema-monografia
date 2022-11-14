from django.shortcuts import get_object_or_404, redirect, render

from coorientador.forms import CoorientadorForm
from coorientador.models import Coorientador

# Create your views here.
def index(request):

    coorientador = Coorientador.objects.all()
    context = {
        'lista': coorientador,
        'page': 'coorientador'
    }

    return render(request, 'listar_coorientador.html', context=context)

def cadastrar(request):

    if request.method == 'GET':

        form = CoorientadorForm()
        context = {
            'form': form,
            'page': '/'
        }
        return render(request, 'cadastrar_coorientador.html', context=context)
    else:

        form = CoorientadorForm(request.POST)
        
        if form.is_valid():
            coorientador = form.save()
            form = CoorientadorForm()

        context = {
            'form': form,
            'page': '/'
        }
        return render(request, 'cadastrar_coorientador.html', context=context)


def editar(request, id):

    coorientador = get_object_or_404(Coorientador, pk=id)
    form = CoorientadorForm(instance=coorientador)

    if request.method == 'POST':

        form = CoorientadorForm(request.POST, instance=coorientador)

        if form.is_valid():

            coorientador.save()

            return redirect('/coorientador/')
        else:

            context = {
                'form': form, 
                'coorientador': coorientador,
                'page': '/coorientador/'
            }

            return render(request, 'editar_coorientador.html', context=context)        
    else:

        context = {
            'form': form, 
            'coorientador': coorientador,
            'page': '/coorientador/'
        }

        return render(request, 'editar_coorientador.html', context=context)  


def deletar(request, id):

    coorientador = get_object_or_404(Coorientador, pk=id)
    coorientador.delete()

    return redirect('/coorientador/')
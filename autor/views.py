from django.shortcuts import get_object_or_404, redirect, render

from autor.forms import AutorForm
from autor.models import Autor

# Create your views here.

def index(request):

    autor = Autor.objects.all()
    context = {
        'lista': autor,
        'page': 'autor'
    }

    return render(request, 'listar_autor.html', context=context)

def cadastrar(request):

    if request.method == 'GET':

        form = AutorForm()
        context = {
            'form': form,
            'page': '/'
        }
        return render(request, 'cadastrar_autor.html', context=context)
    else:

        form = AutorForm(request.POST)
        
        if form.is_valid():
            autor = form.save()
            form = AutorForm()

        context = {
            'form': form,
            'page': '/'
        }
        return render(request, 'cadastrar_autor.html', context=context)


def editar(request, id):

    autor = get_object_or_404(Autor, pk=id)
    form = AutorForm(instance=autor)

    if request.method == 'POST':

        form = AutorForm(request.POST, instance=autor)

        if form.is_valid():

            autor.save()

            return redirect('/autor/')
        else:

            context = {
                'form': form, 
                'autor': autor,
                'page': '/autor/'
            }

            return render(request, 'editar_autor.html', context=context)        
    else:

        context = {
            'form': form, 
            'autor': autor,
            'page': '/autor/'
        }

        return render(request, 'editar_autor.html', context=context)  
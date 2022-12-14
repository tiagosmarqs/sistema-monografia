from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import monografia

from monografia.forms import MonografiaForm
from monografia.models import Monografia

# Create your views here.
def index(request):

    monografia = Monografia.objects.all()
    context = {
        'lista': monografia,
        'page': 'monografia',
        'titulo': 'Monografias'
    }

    return render(request, 'listar.html', context=context)

def cadastrar(request):

    if request.method == 'GET':

        form = MonografiaForm()
        context = {
            'form': form,
            'page': 'monografia',
            'titulo': 'Monografia'
        }
        return render(request, 'cadastrar.html', context=context)
    else:

        form = MonografiaForm(request.POST)
        
        if form.is_valid():
            monografia = form.save()
            form = MonografiaForm()
            return redirect('/monografia/')

        context = {
            'form': form,
            'page': 'monografia',
            'titulo': 'Monografia'
        }
        return render(request, 'cadastrar.html', context=context)


def buscar(request):

    if request.GET.get('options') == 'titulo' and request.GET.get('search'):

        busca = request.GET.get('search')
        resultado = Monografia.objects.filter(titulo__icontains=busca)
        context = {
            'lista': resultado
        }

        return render(request, 'buscar_monografia.html', context=context)
    
    
    if request.GET.get('options') == 'autor' and request.GET.get('search'):

        busca = request.GET.get('search')
        resultado = Monografia.objects.filter(autor__nome__icontains=busca)
        context = {
            'lista': resultado
        }

        return render(request, 'buscar_monografia.html', context=context)
        
    if request.GET.get('options') == 'orientador' and request.GET.get('search'):

        busca = request.GET.get('search')
        resultado = Monografia.objects.filter(orientador__nome__icontains=busca)
        context = {
            'lista': resultado
        }

        return render(request, 'buscar_monografia.html', context=context)

    if request.GET.get('options') == 'coorientador' and request.GET.get('search'):

        busca = request.GET.get('search')
        resultado = Monografia.objects.filter(coorientador__nome__icontains=busca)
        context = {
            'lista': resultado
        }

        return render(request, 'buscar_monografia.html', context=context)

    if request.GET.get('options') == 'resumo' and request.GET.get('search'):

        busca = request.GET.get('search')
        resultado = Monografia.objects.filter(resumo__icontains=busca)
        context = {
            'lista': resultado
        }

        return render(request, 'buscar_monografia.html', context=context)

    if request.GET.get('options') == 'palavraschave' and request.GET.get('search'):

        busca = request.GET.get('search')
        resultado = Monografia.objects.filter(palavras_chave__icontains=busca)
        context = {
            'lista': resultado
        }

        return render(request, 'buscar_monografia.html', context=context)

    if request.GET.get('options') == 'universidade' and request.GET.get('search'):

        busca = request.GET.get('search')
        resultado = Monografia.objects.filter(universidade__icontains=busca)
        context = {
            'lista': resultado
        }

        return render(request, 'buscar_monografia.html', context=context)

    if request.GET.get('options') == 'curso' and request.GET.get('search'):

        busca = request.GET.get('search')
        resultado = Monografia.objects.filter(curso__icontains=busca)
        context = {
            'lista': resultado
        }

        return render(request, 'buscar_monografia.html', context=context)
        
    return render(request, 'buscar_monografia.html')


def editar(request, id):

    monografia = get_object_or_404(Monografia, pk=id)
    form = MonografiaForm(instance=monografia)

    if request.method == 'POST':

        form = MonografiaForm(request.POST, instance=monografia)

        if form.is_valid():

            monografia.save()

            return redirect('/monografia/')
        else:

            context = {
                'form': form, 
                'identificador': monografia,
                'page': 'monografia'
            }

            return render(request, 'editar.html', context=context)        
    else:

        context = {
            'form': form, 
            'identificador': monografia,
            'page': 'monografia'
        }

        return render(request, 'editar.html', context=context)  


def deletar(request, id):

    monografia = get_object_or_404(Monografia, pk=id)
    monografia.delete()

    return redirect('/monografia/')
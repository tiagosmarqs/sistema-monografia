from django.shortcuts import render

from coorientador.forms import CoorientadorForm

# Create your views here.
def cadastrar(request):

    if request.method == 'GET':

        form = CoorientadorForm()
        context = {
            'form': form
        }
        return render(request, 'coorientador.html', context=context)
    else:

        form = CoorientadorForm(request.POST)
        
        if form.is_valid():
            coorientador = form.save()
            form = CoorientadorForm()

        context = {
            'form': form
        }
        return render(request, 'coorientador.html', context=context)
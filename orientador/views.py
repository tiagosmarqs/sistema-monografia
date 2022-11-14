from django.shortcuts import render

from orientador.forms import OrientadorForm

# Create your views here.
def cadastrar(request):

    if request.method == 'GET':

        form = OrientadorForm()
        context = {
            'form': form,
            'page': '/'
        }
        return render(request, 'cadastrar_orientador.html', context=context)
    else:

        form = OrientadorForm(request.POST)
        
        if form.is_valid():
            orientador = form.save()
            form = OrientadorForm()

        context = {
            'form': form,
            'page': '/'
        }
        return render(request, 'cadastrar_orientador.html', context=context)
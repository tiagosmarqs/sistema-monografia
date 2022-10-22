from django.shortcuts import render

from autor.forms import AutorForm

# Create your views here.
def index(request):

    if request.method == 'GET':

        form = AutorForm()
        context = {
            'form': form
        }
        return render(request, 'autor.html', context=context)
    else:

        form = AutorForm(request.POST)
        
        if form.is_valid():
            autor = form.save()
            form = AutorForm()

        context = {
            'form': form
        }
        return render(request, 'autor.html', context=context)
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm


# Create your views here.
def home(request):

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            print('form is valid')
            print('name : ', form.cleaned_data['name'])
            print('desc : ', form.cleaned_data['desc'])
            print('price : ', form.cleaned_data['price'])
        return HttpResponse("<h3>Data printed in terminal</h3>")
    else:
        form = ProductForm()
    return render(request, 'products/home.html', {'form': form})

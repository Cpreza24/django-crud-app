from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Candy

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('about page')

def candies_index(request):
    candies = Candy.objects.all()
    return render(request, 'my_app/candies_index.html', {'candies': candies})

def candies_detail(request, candy_id):
    candy = get_object_or_404(Candy, id=candy_id)
    return render(request, 'my_app/candies/detail.html', {'candy': candy})

def candies_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        Candy.objects.create(name=name, type=type)
        return redirect('candies_index')
    return render(request, 'my_app/candies/create.html')


from django.shortcuts import render
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
    candy = Candy.objects.get(id=candy_id)
    return render(request, 'my_app/candies_detail.html', {'candy': candy})


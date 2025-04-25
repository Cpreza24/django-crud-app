from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Candy, User
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('about page')

@login_required
def candies_index(request):
    candies = Candy.objects.all()
    return render(request, 'my_app/candies_index.html', {'candies': candies})

@login_required
def candies_detail(request, candy_id):
    candy = get_object_or_404(Candy, id=candy_id)
    return render(request, 'my_app/candies/detail.html', {'candy': candy})

@login_required
def candies_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        Candy.objects.create(name=name, type=type, created_by=request.user)
        return redirect('candies_index')
    return render(request, 'my_app/candies/create.html', {'user': request.user})

@login_required
def candies_edit(request, candy_id):
    candy = get_object_or_404(Candy, id=candy_id)
    if candy.created_by != request.user:
        return HttpResponse('You are not authorized to edit this candy.', status=403)
    if request.method == 'POST':
        candy.name = request.POST.get('name')
        candy.type = request.POST.get('type')
        candy.save()
        return redirect('candies_detail', candy_id=candy.id)
    return render(request, 'my_app/candies/edit.html', {'candy': candy})

@login_required
def candies_delete(request, candy_id):
    candy = get_object_or_404(Candy, id=candy_id)
    if candy.created_by != request.user:
        return HttpResponse('You are not authorized to delete this candy.', status=403)
    if request.method == 'POST':
        candy.delete()
        return redirect('candies_index')
    return render(request, 'my_app/candies/delete.html', {'candy': candy})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('home')


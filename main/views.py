from .models import Food
from .models import Section
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

'''
def Food_list(request):
    foods = Food.objects.all()
    context = {
        "foods":foods
    }
    return render(request,"foods.html",context)
'''

def Food_list(request):
    foods = Food.objects.all()
    return render(request, 'foods/foods.html', {'foods': foods})

def detail(request, food_id):
    detail = Food.objects.get(id=food_id)
    return render(request, 'foods/detail.html', {'detail':detail})
    
def TemplateView(request):
    return render(request, 'home.html')


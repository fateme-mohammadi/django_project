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

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'foods.html', {'foods': foods})

def detail(request, food_id):
    food = Food.objects.get(id=food_id)
    return render(request, 'detail.html', {'food':food})
    
class FoodListView(ListView):
    model = Food
    template_name = "home.html"
    

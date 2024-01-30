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
class MenuListView(ListView):
    model = Section
    template_name = 'main/home.html'
    context_object_name = 'menu_items'

class FoodDetailView(DetailView):
    model = Food
    template_name = "foods/detail.html"
    
class FoodListView(ListView):
    model = Food
    template_name = "foods/foods.html"
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'home.html', {'foods': Food.objects.all()})
def logout_view(request):
    logout(request)
    return redirect('login')
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

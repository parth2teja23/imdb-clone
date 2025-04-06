from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.
def home(request):
    movies = [
        {
            "id": 1,
            "title": "Inception",
            "rating": 8.8,
            "year": 2010,
            "image": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?auto=format&fit=crop&q=80&w=600",
            "description": "A thief who steals corporate secrets..."
        },
        {
            "id": 2,
            "title": "The Dark Knight",
            "rating": 9.0,
            "year": 2008,
            "image": "https://images.unsplash.com/photo-1478720568477-152d9b164e26?auto=format&fit=crop&q=80&w=600",
            "description": "When the menace known as the Joker..."
        },
        {
            "id": 3,
            "title": "Interstellar",
            "rating": 8.6,
            "year": 2014,
            "image": "https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?auto=format&fit=crop&q=80&w=600",
            "description": "A team of explorers travel through a wormhole..."
        },
    ]
    return render(request, 'home.html', {'movies': movies})




def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # change this to your homepage url name
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


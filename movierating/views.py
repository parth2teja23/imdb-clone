from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Avg, Count

from django.contrib import messages
from .models import Rating
from .models import Movie, Rating

# Create your views here.
from django.shortcuts import render
from .models import Movie

def home(request):
    movies = Movie.objects.annotate(
        average_rating=Avg('ratings__rating'),
        rating_count=Count('ratings')
    )
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


from django.shortcuts import get_object_or_404
from .models import Movie
from .forms import RatingForm
from django.contrib.auth.decorators import login_required

@login_required
def rate_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = RatingForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        rating_obj, created = Rating.objects.update_or_create(
            user=request.user,
            movie=movie,
            defaults={'rating': form.cleaned_data['rating']}
        )
        return redirect('home')  # or 'movie_detail' if you have that

    return render(request, "rate_movie.html", {
        "movie": movie,
        "form": form,
    })

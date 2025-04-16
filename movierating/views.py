from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count

from .models import Movie, Rating
from .forms import RatingForm


# --------------------
# Home Page View
# --------------------
from django.db.models import Avg, Count, Q
from .models import Movie

from django.db.models import Avg, Count, Q

def home(request):
    movies = Movie.objects.annotate(
        average_rating=Avg('ratings__rating'),
        rating_count=Count('ratings')
    )

    query = request.GET.get('q')
    if query:
        movies = movies.filter(Q(title__icontains=query))

    sort = request.GET.get('sort')
    if sort == 'top':
        movies = movies.order_by('-average_rating')
    elif sort == 'new':
        movies = movies.order_by('-year')  # ✅ Sort by year here

    return render(request, 'home.html', {'movies': movies})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def privacy(request):
    return render(request, 'privacy.html')



# --------------------
# Auth Views
# --------------------
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
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


# --------------------
# Rating a Movie
# --------------------
@login_required
def rate_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = RatingForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        Rating.objects.update_or_create(
            user=request.user,
            movie=movie,
            defaults={'rating': form.cleaned_data['rating']}
        )
        return redirect('home')

    return render(request, "rate_movie.html", {
        "movie": movie,
        "form": form,
    })


# --------------------
# Toggle Watchlist
# --------------------
@login_required
def toggle_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user

    if movie.watchlisted_by.filter(id=user.id).exists():
        movie.watchlisted_by.remove(user)
    else:
        movie.watchlisted_by.add(user)

    return redirect('home')


# --------------------
# Watchlist View
# --------------------
@login_required
def watchlist_view(request):
    movies = request.user.watchlisted_movies.all()
    return render(request, 'watchlist.html', {'movies': movies})


from .models import Movie
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    comments = movie.comments.order_by('-timestamp')

    form = CommentForm(request.POST or None)
    if request.method == 'POST' and request.user.is_authenticated and form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.movie = movie
        new_comment.user = request.user
        new_comment.save()
        return redirect('movie_detail', movie_id=movie.id)

    return render(request, 'movie_detail.html', {
        'movie': movie,
        'comments': comments,
        'form': form
    })

from django.shortcuts import render

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

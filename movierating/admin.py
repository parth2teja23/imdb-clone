from django.contrib import admin
from .models import Movie, Rating, Comment, Watchlist

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Watchlist)

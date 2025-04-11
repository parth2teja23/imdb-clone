from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("__reload__/", include("django_browser_reload.urls")),
    
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    
    path('movie/<int:movie_id>/rate/', views.rate_movie, name='rate_movie'),
    path('movie/<int:movie_id>/toggle_watchlist/', views.toggle_watchlist, name='toggle_watchlist'),

    # ✅ Watchlist page
    path('watchlist/', views.watchlist_view, name='user_watchlist'),  # This is the important one!
]

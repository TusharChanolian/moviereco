from django.urls import path
from .views import MovieListView, MovieDetailView, MovieNewView, MovieUpdate, MovieDelete
from .models import Movies
urlpatterns = [
    path('movies',MovieListView.as_view()),
    path('movie/<int:pk>',MovieDetailView.as_view()),
    path('movie/new',MovieNewView.as_view(),name='New Movie'),
    path('movie/edit/<int:pk>',MovieUpdate.as_view()),
    path('movie/delete/<int:pk>',MovieDelete.as_view()),
]
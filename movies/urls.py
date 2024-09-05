from django.urls import path
from .views import MovieListView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
]
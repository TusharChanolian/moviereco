from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from movies.models import Movies

from .serializer import MovieSerializer

class MovieListView(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    

class MovieDetailView(RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    
class MovieNewView(CreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class MovieUpdate(UpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class MovieDelete(DestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

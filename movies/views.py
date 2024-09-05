from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Movie
from .serializers import MovieSerializer
import json

def is_admin(user):
    print(user.is_authenticated, user.is_staff, user.is_superuser)
    return user.is_authenticated and (user.is_staff or user.is_superuser)

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@method_decorator(csrf_exempt, name='dispatch')
class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        genre_query = self.request.GET.get('genre', '')

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        if genre_query:
            queryset = queryset.filter(genres__name__icontains=genre_query)

        return queryset

    @method_decorator(user_passes_test(is_admin))
    def post(self, request):
        data = json.loads(request.body)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            movie = serializer.save()
            return Response({'message': 'Movie added successfully', 'movie_id': movie.id}, status=201)
        return Response(serializer.errors, status=400)



class MovieRetrieveUpdateDestroyView(APIView):
    @permission_classes([AllowAny])
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    @method_decorator(user_passes_test(is_admin))
    def put(self, request, pk):
        print("movieee update")
        movie = get_object_or_404(Movie, pk=pk)
        data = json.loads(request.body)
        serializer = MovieSerializer(movie, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Movie updated successfully'})
        print(serializer.errors)
        return Response(serializer.errors, status=400)
    
    @permission_classes([IsAuthenticated])
    @method_decorator(user_passes_test(is_admin))
    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response({'message': 'Movie deleted successfully'})
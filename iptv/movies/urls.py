from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movies.views import MovieViewSet, api_root


movie_list = MovieViewSet.as_view({
    'get': 'list',
    'post': 'create'
}, template_name='movie_list.html')

movie_detail = MovieViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}, template_name='movie_detail.html')


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('movies/', movie_list, name='movie-list'),
    path('movies/<int:pk>/', movie_detail, name='movie-detail'),
])
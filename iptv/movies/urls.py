from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movies.views import MovieViewSet, api_root
from rest_framework import renderers


movie_list = MovieViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

movie_detail = MovieViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

movie_highlight = MovieViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('movies/', movie_list, name='movie-list'),
    path('movies/<int:pk>/', movie_detail, name='movie-detail'),
    path('movies/<int:pk>/highlight/', movie_highlight, name='movie-highlight'),
])
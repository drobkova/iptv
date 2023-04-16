from rest_framework.decorators import api_view, action, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, HTMLFormRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #renderer_classes = [TemplateHTMLRenderer, HTMLFormRenderer]
    template_name = 'movie_list.html'
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'shortName', 'iconUri', 'manifestUri', 'source']
    filterset_fields = ['id', 'name', 'shortName', 'iconUri', 'manifestUri', 'source', 'focus',
                        'disabled']


@api_view(['GET'])
def api_root(request, api_format=None):
    return Response({
        'movies': reverse('movie-list', request=request, format=api_format)
    })
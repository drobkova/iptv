from rest_framework.decorators import api_view, action, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, renderers
from django_filters import rest_framework as filters
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, `destroy`, and `highlight` actions.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'movie_list.html'
    filter_backends = [filters.DjangoFilterBackend]
    search_fields = ['name']

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        movie = self.get_object()
        return Response(movie.highlighted)



@api_view(['GET'])
def api_root(request, api_format=None):
    return Response({
        'movies': reverse('movie-list', request=request, format=api_format)
    })
from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['url', 'id', 'name', 'shortName', 'iconUri', 'manifestUri', 'source', 'focus',
                  'disabled', 'extraText', 'certificateUri', 'description',
                  'isFeatured', 'drm', 'features', 'licenseServers',
                  'licenseRequestHeaders', 'requestFilter', 'responseFilter',
                  'clearKeys', 'extraConfig', 'adTagUri', 'imaVideoId', 'imaAssetKey',
                  'imaContentSrcId', 'mimeType', 'mediaPlaylistFullMimeType',
                  'storedProgress', 'storedContent']
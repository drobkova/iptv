from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.JSONField(null=True, blank=True)  # {<class 'str'>}
    shortName = models.JSONField(null=True, blank=True)  # {<class 'str'>}
    iconUri = models.JSONField(null=True, blank=True)  # {<class 'str'>}
    manifestUri = models.JSONField(null=True, blank=True)  # {<class 'str'>}
    source = models.JSONField(null=True, blank=True)  # {<class 'str'>}
    focus = models.JSONField(null=True, blank=True)  # {<class 'bool'>}
    disabled = models.JSONField(null=True, blank=True)  # {<class 'bool'>}
    extraText = models.JSONField(null=True, blank=True)  # {<class 'list'>}
    certificateUri = models.JSONField(null=True, blank=True)  # {<class 'NoneType'>}
    description = models.JSONField(null=True, blank=True)  # {<class 'str'>, <class 'NoneType'>}
    isFeatured = models.JSONField(null=True, blank=True)  # {<class 'bool'>}
    drm = models.JSONField(null=True, blank=True)  # {<class 'list'>}
    features = models.JSONField(null=True, blank=True)  # {<class 'list'>}
    licenseServers = models.JSONField(null=True, blank=True)  # {<class 'dict'>}
    licenseRequestHeaders = models.JSONField(null=True, blank=True)  # {<class 'dict'>}
    requestFilter = models.JSONField(null=True, blank=True)  # {<class 'NoneType'>}
    responseFilter = models.JSONField(null=True, blank=True)  # {<class 'NoneType'>}
    clearKeys = models.JSONField(null=True, blank=True)  # {<class 'dict'>}
    extraConfig = models.JSONField(null=True, blank=True)  # {<class 'dict'>, <class 'NoneType'>}
    adTagUri = models.JSONField(null=True, blank=True)  # {<class 'str'>, <class 'NoneType'>}
    imaVideoId = models.JSONField(null=True, blank=True)  # {<class 'str'>, <class 'NoneType'>}
    imaAssetKey = models.JSONField(null=True, blank=True)  # {<class 'str'>, <class 'NoneType'>}
    imaContentSrcId = models.JSONField(null=True, blank=True)  # {<class 'int'>, <class 'NoneType'>}
    mimeType = models.JSONField(null=True, blank=True)  # {<class 'NoneType'>}
    mediaPlaylistFullMimeType = models.JSONField(null=True, blank=True)  # {<class 'str'>, <class 'NoneType'>}
    storedProgress = models.JSONField(null=True, blank=True)  # {<class 'int'>}
    storedContent = models.JSONField(null=True, blank=True)  # {<class 'dict'>, <class 'NoneType'>}

    class Meta:
        ordering = ['name']

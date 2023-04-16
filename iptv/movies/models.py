from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    shortName = models.CharField(max_length=100, null=True, blank=True)
    iconUri = models.CharField(max_length=100, null=True, blank=True)
    manifestUri = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    focus = models.BooleanField(null=True, blank=True)
    disabled = models.BooleanField(null=True, blank=True)
    extraText = models.JSONField(null=True, blank=True)
    certificateUri = models.JSONField(null=True, blank=True)
    description = models.JSONField(null=True, blank=True)
    isFeatured = models.BooleanField(null=True, blank=True)
    drm = models.JSONField(null=True, blank=True)
    features = models.JSONField(null=True, blank=True)
    licenseServers = models.JSONField(null=True, blank=True)
    licenseRequestHeaders = models.JSONField(null=True, blank=True)
    requestFilter = models.JSONField(null=True, blank=True)
    responseFilter = models.JSONField(null=True, blank=True)
    clearKeys = models.JSONField(null=True, blank=True)
    extraConfig = models.JSONField(null=True, blank=True)
    adTagUri = models.JSONField(null=True, blank=True)
    imaVideoId = models.JSONField(null=True, blank=True)
    imaAssetKey = models.JSONField(null=True, blank=True)
    imaContentSrcId = models.JSONField(null=True, blank=True)
    mimeType = models.JSONField(null=True, blank=True)
    mediaPlaylistFullMimeType = models.JSONField(null=True, blank=True)
    storedProgress = models.IntegerField(null=True, blank=True)
    storedContent = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['name']

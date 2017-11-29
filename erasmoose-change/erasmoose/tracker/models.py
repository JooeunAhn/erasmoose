from django.db import models

from django.conf import settings

class Moose(models.Model):
    latlng = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="uploads/moose/", blank=True)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    @property
    def lat(self):
        if self.latlng:
            return self.latlng.split(',')[0]
        return None

    @property
    def lng(self):
        if self.latlng:
            return self.latlng.split(',')[1]
        return None
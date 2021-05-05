from django.db import models
from django.utils.translation import gettext_lazy  as _

# Create your models here.
class FreeFlowStores(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    img = models.ImageField()
    url = models.URLField()

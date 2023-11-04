from django.db import models
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global
from easy_thumbnails.fields import ThumbnailerImageField

saved_file.connect(generate_aliases_global)


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    profile_picture = models.ImageField()
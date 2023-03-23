from django.db import models

class BannerWeb(models.Model):
    gambar = models.ImageField(blank=True, null=True, upload_to='header')

class Icons(models.Model):
    judul = models.CharField(max_length=50)
    icons = models.ImageField(blank=True, null=True, upload_to='icons')
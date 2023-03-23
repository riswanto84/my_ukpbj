from django.contrib import admin

from .models import BannerWeb, Icons

@admin.register(BannerWeb)
class BannerWeb(admin.ModelAdmin):
    list_display = ['gambar',]

    class Meta:
        model = BannerWeb

@admin.register(Icons)
class Icons(admin.ModelAdmin):
    list_display = ['judul',]

    class Meta:
        model = Icons
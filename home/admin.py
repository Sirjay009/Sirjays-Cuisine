from django.contrib import admin
from .models import Home, Menu
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Home)
class HomeAdmin(SummernoteModelAdmin):

    summernote_fields = ('slogan',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('dish', 'description', 'price', 'featured_image',)

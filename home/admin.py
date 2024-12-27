from django.contrib import admin
from .models import Home
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class HomeAdmin(SummernoteModelAdmin):

    summernote_fields = ('body',)

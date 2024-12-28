from django.contrib import admin
from .models import Home
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Home)
class HomeAdmin(SummernoteModelAdmin):

    summernote_fields = ('slogan',)
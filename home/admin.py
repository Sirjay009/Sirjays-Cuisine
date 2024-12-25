from django.contrib import admin
from .models import Customer
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'phone')
    summernote_fields = ('content',)

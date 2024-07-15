from django.contrib import admin
from .models import Resources
from django_summernote.admin import SummernoteModelAdmin


# Register your models here
@admin.register(Resources)
class ResourcesAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

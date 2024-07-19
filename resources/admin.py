from django.contrib import admin
from .models import Resources, Suggestion
from django_summernote.admin import SummernoteModelAdmin


# Register Resource model
@admin.register(Resources)
class ResourcesAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


# Register Suggestion model
admin.site.register(Suggestion)

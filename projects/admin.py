from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Project

class ProjectModelAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', )
    summernote_fields = '__all__'#('description', 'additionalright','bottomdetails',)

admin.site.register(Project, ProjectModelAdmin)

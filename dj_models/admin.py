from django.contrib import admin
from .models import Dj_Model, Dj_ModelField, Dj_ModelLine
# Register your models here.


admin.site.register(Dj_ModelField)
admin.site.register(Dj_ModelLine)


class Dj_ModelLineInline(admin.TabularInline):
    model = Dj_ModelLine

@admin.register(Dj_Model)
class Dj_ModelAdmin(admin.ModelAdmin):
    '''Admin View for Dj_Model'''

    list_display = (
        'name',
        'verbose_name'
        )
    list_filter = ('name',)
    inlines = [
        Dj_ModelLineInline,
    ]
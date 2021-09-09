from django.contrib import admin
from .models import Anken,Shuho

class ShuhoInline(admin.StackedInline):
    model = Shuho
    extra = 1 

class AnkenAdmin(admin.ModelAdmin):
    inlines = [ShuhoInline]
    list_display = ('ankenmei', 'tantousha', 'koumoku','joutai')

admin.site.register(Anken, AnkenAdmin)
#admin.site.register(Anken)
#admin.site.register(Shuho)
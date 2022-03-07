from re import search
from django.contrib import admin
from .models import Category, Projeto
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'owner']
    search_fields = ['name', 'description']
    list_filter = ['owner']

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['name','description',]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Projeto, ProjetoAdmin)
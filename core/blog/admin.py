
from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.BlogPost)
class AuthorAdmin(admin.ModelAdmin):
    list_display=( 'title','id',  'author', 'content', 'status','slug')
    prepopulated_fields= { 'slug' :('title',), }


admin.site.register(models.Category)

from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'urlAbreviada', 'author', 'publicar', 'estado')
    list_filter = ('estado', 'creado', 'publicar', 'author')
    search_fields = ('titulo', 'body')
    prepopulated_fields = {'urlAbreviada': ('titulo',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publicar'
    ordering = ('estado', 'publicar')
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    elegir_estado = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }
    
    titulo = models.CharField(max_length=250)
    urlAbreviada = models.SlugField(max_length=250, unique_for_date='publicar')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    body = models.TextField()
    publicar = models.DateTimeField(default=timezone.now)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10, choices=elegir_estado, default='draft')
    
    class Meta:
        ordering = ('-publicar',)
        
    def __str__(self):
        return self.titulo
    

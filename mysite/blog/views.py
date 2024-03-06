from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
# creacion de vista de detalle y listado
#prueba de git rama ocualta

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


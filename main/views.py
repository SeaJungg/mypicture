from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def index(request):
    all_data = Post.objects.all()
    return render(request, 'index.html', {'all_data':all_data})


def create(request):
    return redirect('index')
    

def detail(request, id):
    row_data = get_object_or_404(Post, pk = id)
    return render(request, 'detail.html', {'row_data':row_data})
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'crud/usuario_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'crud/usuario_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('usuario_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'crud/usuario_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('usuario_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'crud/usuario_edit.html', {'form': form})

def delete(request, pk):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Post.objects.get(pk=pk)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('usuario_list')
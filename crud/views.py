from django.shortcuts import render
from django.utils import timezone
from .models import Usuario
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import UsuarioForm
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'crud/usuario_list.html', {'usuarios': usuarios})

def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'crud/usuario_detail.html', {'usuario': usuario})

def usuario_new(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.published_date = timezone.now()
            usuario.save()
            return redirect('usuario_detail', pk=usuario.pk)
    else:
        form = UsuarioForm()
    return render(request, 'crud/usuario_edit.html', {'form': form})

def usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.published_date = timezone.now()
            usuario.save()
            return redirect('usuario_detail', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'crud/usuario_edit.html', {'form': form})

def delete(request, pk):
    instancia = Usuario.objects.get(pk=pk)
    instancia.delete()
    return redirect('usuario_list')
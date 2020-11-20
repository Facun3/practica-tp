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
    if request.method == "POST": #Confirma si el request es del tipo POST que es el metodo utilizado.
        form = UsuarioForm(request.POST) #Guarda los datos del formulario como un tipo UsuarioForm, que es algo que crea el usuario a sus necesidades.
        if form.is_valid(): # Confirma que los valores sean correctos
            usuario = form.save(commit=False) #Guarda los datos pero no definitivamente
            usuario.save() #Guarda los datos del formulario
            return redirect('usuario_detail', pk=usuario.pk) #Redirecciono al nuevo template con su key correspondiente.
    else:
        form = UsuarioForm() #Si el formulario no es valido no guardo los campos
    return render(request, 'crud/usuario_edit.html', {'form': form}) #Retorno el request con el template usuario_edit y le paso el form con los campos.

def usuario_edit(request, pk): 
    usuario = get_object_or_404(Usuario, pk=pk) #Confirmo que el usuario existe y obtengo sus valores por su key.
    if request.method == "POST": #Confirma si el request es del tipo POST que es el metodo utilizado.
        form = UsuarioForm(request.POST, instance=usuario) #Guarda los datos del formulario como un tipo UsuarioForm
        if form.is_valid(): # Confirma que los valores sean correctos
            usuario = form.save(commit=False) #Guarda los datos pero no definitivamente
            usuario.save() #Guarda los datos del formulario
            return redirect('usuario_detail', pk=usuario.pk) #Redirecciono al nuevo template con su key correspondiente.
    else:
        form = UsuarioForm(instance=usuario) #Si el formulario no es valido no guardo los campos
    return render(request, 'crud/usuario_edit.html', {'form': form}) #Retorno el request con el template usuario_edit y le paso el form con los campos.


def delete(request, pk):
    instancia = Usuario.objects.get(pk=pk) #Obtengo la instancia del objeto a borrar por key.
    instancia.delete() #Borro el usuario.
    return redirect('usuario_list') #redirecciono a la lista de usuarios.
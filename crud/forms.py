from django import forms

from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario #Selecciono el modelo que cree previamente
        fields = ('apellido', 'nombre', 'dni', 'domicilio', 'nacimiento') # Selecciono los campos que tendra el formulario.
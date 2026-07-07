from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
            "paternal_name",
            "maternal_name",
            "age",
            "email",
            "gender",
            "phone",
        ]
        labels = {
            "name":"Agrega tu Nombre(s)",
            "paternal_name":"Apellido Paterno",
            "maternal_name":"Apellido Matero",
            "age":"Asigna tu edad",
            "gender":"Selecciona tu género",
            "email":"Correo electrónico",
            "phone":"Agrega tu número movil",
        }
        exclude = []

    def clean_age(self, *args, **kwargs):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise forms.ValidationError("Debes ser mayor de 18 años para registrarte.")
        return age
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if "@gmail.com" not in email:
            raise forms.ValidationError("El correo necesita ser de dominio @gmail.com")
        return email
    
    def clean_phone(self, *args, **kwargs):
        phone = self.cleaned_data.get("phone")
        if not str(phone).isdigit():
            raise forms.ValidationError("Asigna un número válido.")
        return phone
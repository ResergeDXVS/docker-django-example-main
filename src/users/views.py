from django.shortcuts import render
from .forms import UserForm
# Create your views here.
def userCreate(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        print("Usuario registrado")
    return render(request, "users/user_form.html",context={"form":form})
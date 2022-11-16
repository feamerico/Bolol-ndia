from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from core.forms import CustomUserForm


def registro(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Registrado com sucesso! Logue para continuar')
            return redirect('loginpage')
    context = {'form': form}
    return render(request, "loja/auth/registro.html", context)


def loginpage(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        passwd = request.POST.get('password')

        user = authenticate(request, username=name, password=passwd)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
            return redirect('loginpage')

    return render(request, 'loja/auth/login.html')

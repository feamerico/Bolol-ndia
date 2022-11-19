from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
    if request.user.is_authenticated:
        messages.warning(request, "Você já está logado!")
        return redirect('home')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logado com sucesso!')
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
                return redirect('loginpage')

        return render(request, 'loja/auth/login.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Deslogado com sucesso!')
    return redirect('home')

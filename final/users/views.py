from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth')
    else:
        form = UserRegisterForm()

    return render(request,
                  'users/registration.html',
                  {
                    'title': 'Страница регистрации',
                    'form': form
                  })

@login_required
def profile(request):
    if request.method == 'POST':
        updateUserForm = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if updateUserForm.is_valid(): #если обе формы валидные - обновляем
            updateUserForm.save()
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
            'updateUserForm': updateUserForm
        }
    return render(request, 'users/profile.html', data)

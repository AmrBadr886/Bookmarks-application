from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def main_page(request):
    return render(request, 'bookmarks/main_page.html')


def user_page(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'bookmarks/user_page.html', {'user': user})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('main_page'))
            else:
                error = 'invalid username or password'
        else:
            error = None
    else:
        form = LoginForm()
        error = None
    return render(request, 'bookmarks/user_login.html', {'form': form, 'error':error})

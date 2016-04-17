from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User


def main_page(request):
    return render(request, 'bookmarks/main_page.html')


def user_page(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'bookmarks/user_page.html', {'user': user})

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', main_page, name='main_page'),
    url(r'^users/(?P<username>\w+)$', user_page, name='user_page'),
    url(r'^login$', user_login, name='user_login'),
    url(r'^logout$', user_logout, name='user_logout'),
    url(r'^register$', user_register, name='user_register')
]

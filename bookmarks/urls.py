from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', main_page, name='main_page'),
    url(r'^users/(?P<username>\w+)$', user_page, name='user_page')
]

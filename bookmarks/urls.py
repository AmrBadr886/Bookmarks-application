from django.conf.urls import url
from .views import *

urlpatterns = [
    # Browsing
    url(r'^$', main_page, name='main_page'),
    url(r'^users/(?P<username>\w+)$', user_page, name='user_page'),
    url(r'^tags$', tag_cloud_page, name='tag_cloud_page'),
    url(r'^tags/(?P<tag_name>[^\s]+)', tag_page, name='tag_page'),
    url(r'^search/$', search_page ,name='search_page'),

    # Session management
    url(r'^login$', user_login, name='user_login'),
    url(r'^logout$', user_logout, name='user_logout'),
    url(r'^register$', user_register, name='user_register'),


    # Account management
    url(r'^save/$', bookmark_save, name='bookmark_save')
]

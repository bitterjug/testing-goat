from django.conf.urls import patterns, url
from lists.views import (
    view_list,
    home_page,
)

urlpatterns = patterns('',
    url(r'^$', home_page, name='home'),
    url(r'^lists/unique-list/$', view_list, name='view_list')
)

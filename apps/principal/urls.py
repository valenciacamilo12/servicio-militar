from django.conf.urls import url
#from django.contrib.auth import login
from apps.principal.views import index, login, registro

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/', login, name='login'),
    url(r'^registro/', registro, name='registro')
]

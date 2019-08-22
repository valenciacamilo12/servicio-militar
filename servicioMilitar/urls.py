"""servicioMilitar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import logout_then_login,PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('apps.principal.urls')),
    url(r'^soldado/', include('apps.soldado.urls', namespace='soldado')),
    url(r'^cuartel/', include('apps.cuartel.urls', namespace='cuartel')),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^registro/', include('apps.usuarios.urls')),

    url(r'^password_reset/', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_ \-]+)/(?P<token>.+)/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
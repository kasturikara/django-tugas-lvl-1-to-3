from django.contrib import admin
from django.urls import path, include
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mynewextension/', include('first_app.urls')),
    path('admin/', admin.site.urls),
]

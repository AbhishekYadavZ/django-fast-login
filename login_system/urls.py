from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontend, name="frontend"),
    path('backend/', views.backend, name="backend"),
    path('login/', include('django.contrib.auth.urls')),
]

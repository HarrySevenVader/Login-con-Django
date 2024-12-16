from django.contrib import admin
from django.urls import path
from accounts.views import user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_login, name='home'),  # Ruta para la raíz del sitio
    path('login/', user_login, name='login'),
]

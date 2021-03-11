from django.contrib import admin
from django.urls import path
from controle_gastos_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gastos/', gastos)
]

from django.contrib import admin
from django.urls import path
from agende.views import home, cadastro, agendamento, listagem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro/', cadastro, name="cadastro"),
    path('agendamento/', agendamento, name="agendamento"),
    path('listagem/', listagem, name="listagem")
]

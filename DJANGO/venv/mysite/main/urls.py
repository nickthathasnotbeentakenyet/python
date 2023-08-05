from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about', views.about, name='about'), # давая имена ссылкам можно менять адреса ссылок ->
    # -> (вместо) path("about", ... можно path("about123", ...  и ссылка будет везде корректно меняться 
    # path('login', login, name='login'),
]
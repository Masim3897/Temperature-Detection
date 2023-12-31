
from django.contrib import admin
from django.urls import path
from temprature import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('temprature/',views.temp),
    path('temprature/<int:tempid>',views.tempdetail),
   ]

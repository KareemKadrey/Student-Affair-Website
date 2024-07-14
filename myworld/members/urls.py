from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('Home page',views.new,name="home"),
    path('index', views.index, name='index'),
    path('Active', views.active, name='Active'),
]
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('month/', views.month, name='month'),
    path('week/', views.week, name='week'),
    path('add/', views.add, name='add'),
    path('addmonth/', views.addmonth, name='addmonth'),
    path('addweek/', views.addweek, name='addweek'),
    path('delete/<int:todo_id>/', views.deleteItem, name='delete'),
    path('deleteweek/<int:todoweek_id>/', views.deleteweek, name='deleteweek'),
    path('deletemonth/<int:todomonth_id>/', views.deletemonth, name='deletemonth'),

]
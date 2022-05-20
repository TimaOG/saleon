from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.openMain, name='home'),
    path('mate/', views.openMates, name='mate'),
    path('about/', views.openAbout, name='about'),
    path('cafes/<int:page>', views.openCafes, name='cafe'),
    path('shops/<int:page>', views.openShops, name='shops'),
    path('travels/<int:page>', views.openTrevel, name='travels'),
    path('fun/<int:page>', views.openFun, name='fun'),
    path('med/<int:page>', views.openMed, name='med'),
    path('car/<int:page>', views.openCar, name='car'),
    path('oneshop/<int:page>', views.openOneShop, name='oneshop'),
    path('study/<int:page>', views.openStudy, name='study'),
    path('other/<int:page>', views.openOther, name='other'),
    path('<int:pk>', views.openPageAboutMate, name='matepage')
]
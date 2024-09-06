from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('classes/', views.classes, name='classes'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfolio_details, name='portfolio_details'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),

]

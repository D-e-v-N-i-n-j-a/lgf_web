from django.urls import path
from .views import home,aboutUs,donate,blogs




app_name = 'home'
urlpatterns = [
    path('',home,name='home'),
    path('about',aboutUs,name='about'),
    path('donate',donate,name='donate'),
    path('blog',blogs,name='blog')
]







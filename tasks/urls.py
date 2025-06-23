
from django.urls import path
from .views import home ,home2 ,about,contact

urlpatterns = [
    path('', home, name='home'),
    path('home2', home2, name='home'),             # http://127.0.0.1:8000/
    path('about/', about, name='about'),     # http://127.0.0.1:8000/about/
    path('contact/', contact, name='contact'),
]
from django.urls import path
from .views import homepage, homepage_rus


urlpatterns = [
    path('', homepage, name='home'),

    path('rus_page/', homepage_rus, name='home_rus'),

]

from django.urls import path
from .views import index, create, update, delete, popular, popular_posts, lastpost, registr, vhod

urlpatterns = [
    path('', index, name='home'),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name="delete"),
    path('popular_posts', popular_posts, name='popular_posts'),
    path('popular/<int:id>', popular, name='popular'),
    path('lastpost/', lastpost, name='lastpost'),

    path('vhod/', vhod, name='vhod'),
    path('registr/', registr, name='registr'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('<int:game_id/', views.get_game_data, name='game_data'),
]
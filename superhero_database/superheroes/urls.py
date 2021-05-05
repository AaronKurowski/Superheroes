from django.urls import path
from . import views


app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('update/<int:superhero_id>/', views.update, name='update_superhero'),
    path('delete/<int:superhero_id>/', views.delete, name='delete_superhero')
]

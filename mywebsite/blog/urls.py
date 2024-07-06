from django.urls import path
from . import views


urlpatterns = [
    path('update/<int:id_update>/', views.update, name='update'),
    path('delete/<int:id_delete>/', views.delete, name='delete'),
    path('create/',views.create,name='create'),
    path('',views.index,name='index')
]
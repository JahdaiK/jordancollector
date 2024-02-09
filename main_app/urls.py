from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jordans/', views.jordans_index, name='index'),
    path('jordans/<int:jordan_id>/', views.jordans_detail, name='detail'),
    path('jordans/create/', views.JordanCreate.as_view(), name = 'jordans_create'),
    path('jordans/<int:pk>/update/', views.JordanUpdate.as_view(), name = 'jordans_update'),
    path('jordans/<int:pk>/delete/', views.JordanDelete.as_view(), name = 'jordans_delete'),
    path('jordans/<int:jordan_id>/add_task/', views.add_task, name = 'add_task'),
]

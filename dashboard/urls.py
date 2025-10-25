from django.urls import path
from dashboard import views


urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('add/', views.add_log, name='add_log'),
    path('edit/<int:pk>/', views.edit_log, name='edit_log'),
    path('delete/<int:pk>/', views.delete_log, name='delete_log'),
]

from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.EventUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.EventDeleteView.as_view(), name='delete'),
]
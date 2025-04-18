from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('update/<int:pk>/', views.update_status, name='update_status'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

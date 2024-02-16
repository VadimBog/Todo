from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('create-task/', views.TaskCreate.as_view(), name='create_task'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='update_task'),
    path('task-delete/<int:pk>/', views.DeleteTask.as_view(), name='delete_task'),
]
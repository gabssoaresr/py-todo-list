from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, toggle_task_status,
    TagListView, TagCreateView, TagUpdateView, TagDeleteView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),  # Lista de tarefas
    path('task/add/', TaskCreateView.as_view(), name='add_task'),  # Adicionar tarefa
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='edit_task'),  # Editar tarefa
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),  # Deletar tarefa
    path('task/<int:pk>/toggle/', toggle_task_status, name='toggle_task_status'),  # Alternar status da tarefa
    path('tags/', TagListView.as_view(), name='tag_list'),  # Lista de tags
    path('tag/add/', TagCreateView.as_view(), name='add_tag'),  # Adicionar tag
    path('tag/<int:pk>/edit/', TagUpdateView.as_view(), name='edit_tag'),  # Editar tag
    path('tag/<int:pk>/delete/', TagDeleteView.as_view(), name='delete_tag'),  # Deletar tag
]

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.utils.timezone import now
from .models import Task, Tag
from .forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    queryset = Task.objects.prefetch_related('tags').order_by('is_done', '-created_at')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('home')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('home')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('home')


def toggle_task_status(request, pk):
    """Custom view for toggling task status."""
    task = Task.objects.get(pk=pk)
    task.is_done = not task.is_done
    task.deadline = now() if task.is_done else None
    task.save()
    return redirect('home')


class TagListView(ListView):
    model = Tag
    template_name = 'tasks/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/tag_form.html'
    success_url = reverse_lazy('tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/tag_form.html'
    success_url = reverse_lazy('tag_list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tasks/tag_confirm_delete.html'
    success_url = reverse_lazy('tag_list')

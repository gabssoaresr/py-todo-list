# Todo list

In this task, you have to implement a todo list site.

## Steps for implementation

1. Create pull request;
2. Switch to your branch;
3. Implement Todo List using Django;
4. Create Pull Request from your_branch to main branch;

## Task

You should have such models:
1. Task - todo list is consist of tasks. Each task should have fields for:
    - content - describes what you should do.
    - datetime, when a task was created
    - optional deadline datetime if a task should be done until some
datetime
    - the boolean field that marks if the task is done or not
    - tags that are relevant for this task
2. Tag - a tag symbolizes the theme of the task and consists only of a name.

A task can have multiple tags and a tag can be in multiple tasks.

Create the home page. The home page is accessed by `127.0.0.1:8000/`, where you
should have:
1. Sidebar with the links to:
   - Home page
   - Tag list page
    the sidebar should be on all pages.
2. Todo list which is a list of tasks.
   - Tasks should be ordered from `not done` to `done` and from newest to oldest
   - All task information should be displayed.
   - There should be a button to add a new task.
   - For each task add links for updating and deletion.
   - Also, add a button `Complete` if a task is not done and `Undo` if a task is
done, this button changes the status of the task to the opposite and redirects
to this page.

The home page should look like this:
![](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_exam_first_scr_6e2c7167de.png)

Create a tag list page. A tag list page is accessed by `127.0.0.1:8000/tags/`,
there you should have:
1. Table with tags names, links for updating,  and deletion.
2. Button to add a new tag.

Of course, pages for adding tags and tasks must be also implemented.

A tag list page should look like this:
![](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_exam_second_scr_1c4563cb17.png)

**Everybody should be able to easily clone and run your project!**




###############################################


Views
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Tag
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.order_by('is_done', '-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tasks/tag_list.html', {'tags': tags})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('home')


Eu já tenho pronto a estrutura do back preciso criar os templates 
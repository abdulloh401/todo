from django.shortcuts import render, get_object_or_404, redirect
from app.models import Tasks
from app.forms import TaskForm
from django.views.decorators.csrf import csrf_exempt
import json



def index(request):
    tasks = Tasks.objects.all()
    complete = Tasks.objects.filter(status=True)
    not_complete = Tasks.objects.filter(status=False)

    context = {
        "tasks": tasks,
        "complete": complete,
        "not_complete": not_complete,
    }
    return render(request, 'index.html', context)


def detail(request, pk):
    task = get_object_or_404(Tasks.objects.all(), id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "task": task,
        "form": form,
    }
    return render(request, 'update.html', context)


def delete(request, pk):
    task = get_object_or_404(Tasks.objects.all(), id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("index")
    return render(request, 'delete.html')


def add(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    context = {
        "form": form,
    }
    return render(request, 'add.html', context)


@csrf_exempt  # Use this only if you're not using CSRF protection in your AJAX requests
def toggle_task_status(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Tasks, id=pk)
        data = json.loads(request.body)
        task.status = data.get('status', False)
        task.save()








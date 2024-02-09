from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Jordan
from .forms import TaskForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def jordans_index(request):
    jordans= Jordan.objects.all()
    return render(request, 'jordans/index.html', {'jordans': jordans})

def jordans_detail(request, jordan_id):
    jordan = Jordan.objects.get(id=jordan_id)

    task_form = TaskForm()
    return render(request, 'jordans/detail.html', { 
        'jordan': jordan, 'task_form': task_form
    })

def add_task(request, jordan_id):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.jordan_id = jordan_id
        new_task.save()
    return redirect('detail', jordan_id=jordan_id)

class JordanCreate(CreateView):
    model = Jordan
    fields = '__all__'
    success_url = '/jordans/{jordan_id}'

class JordanUpdate(UpdateView):
    model = Jordan
    fields = ['colorway', 'materials']

class JordanDelete(DeleteView):
    model = Jordan
    success_url = '/jordans'

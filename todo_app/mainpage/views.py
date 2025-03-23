from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Tasks
from .forms import TasksForm,UpdateTaskForm
# Create your views here.

def ListTaskView(request):

    if request.method == 'POST':
        form = TasksForm(request.POST)
        tasks = Tasks.objects.all()
        if form.is_valid() and tasks.count()<6:
            task = form.cleaned_data['task']
            Tasks.objects.create(task=task)
            messages.success(request,message='Successfully Added')
            return redirect('create_retrieve')
        else:
            messages.error(request,message='Invalid task or Task full')
            return render(request,'create_retrieve.html',{'form':form,'tasks':tasks})

    form = TasksForm()
    tasks = Tasks.objects.all()
    return render(request,'create_retrieve.html',{'form':form,'tasks':tasks})

def DeleteTaskView(request,pk,delete):
    task_obj = get_object_or_404(Tasks,pk=pk)
    if delete == 'Yes':
        task_obj.delete()
        return redirect('create_retrieve')
        
    elif delete == 'No':
        return redirect('create_retrieve')

    else:
        form = TasksForm()
        tasks = Tasks.objects.all()
        return render(request,'delete.html',{'form':form,'tasks':tasks,'pk':pk})

def UpdateTaskView(request,pk):
    if request.method == 'POST':
        task_obj = get_object_or_404(Tasks,pk=pk)
        update_form = UpdateTaskForm(request.POST,instance=task_obj)
        if update_form.is_valid():
            update_form.save()
            return redirect('create_retrieve')
        
    form = TasksForm()
    update_form = UpdateTaskForm()
    tasks = Tasks.objects.all()
    return render(request,'update.html',{'form':form,'update_form':update_form,'tasks':tasks,'pk':pk})

    
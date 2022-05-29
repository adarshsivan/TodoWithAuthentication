from django.shortcuts import render, redirect
from home.models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):
    if request.method == "POST":
        task = request.POST['task']
        desc = request.POST['desc']
        obj = Todo(task_name=task, description=desc, added_by= request.user)
        obj.save()
        return render(request, 'home.html', {"activeHome": "active"})
    else:
        return render(request, 'home.html', {"activeHome": "active"})

@login_required(login_url='/accounts/login')
def task(request):
    data = Todo.objects.filter(added_by=request.user)
    return render(request, 'task.html', {"data": data, "activeTask": "active"})


def delete(request):
    ID = request.GET['id']
    Todo.objects.filter(id=ID).delete()
    return redirect('task')


def update(request):
    ID = request.GET['id']
    if request.method == "POST":
        taskName = request.POST['task']
        desc = request.POST['desc']
        Todo.objects.filter(id=ID).update(task_name=taskName, description=desc)
        return redirect('task')
    data_task = "None"
    data_desc = "None"
    obj = Todo.objects.filter(id=ID)
    if(obj != None):
        for i in obj:
            data_task = i.task_name
            data_desc = i.description
    return render(request, 'update.html', {"taskValue": data_task, "descValue": data_desc, "id": ID})


from django.shortcuts import render,HttpResponse
from .models import ToDoList
def home(request):
    context={'success':False}
    if request.method=='POST':
        title=request.POST['title']
        start_date=request.POST['start_date']
        deadline=request.POST['Deadline_time']
        ins=ToDoList(Task_Name=title,deadline=deadline)
        ins.save()
        context={'success':True,
                 'msg':'Added'   
        }
    return render(request,'home.html',context)


def tasks(request):
    task=ToDoList.objects.all()
    context={
        'task':task,
    }
    return render(request,'task.html',context)


def taskdelete(request,id):
    task=ToDoList.objects.get(id=id)
    task.delete()
    context={'success':True,
              'msg':'deleted'   
        }
    return render(request,'home.html',context)

def taskupdate(request,id):
    task=ToDoList.objects.get(id=id)
    context={
        'task':task,
    }
    return render(request,'update.html',context)

def edit(request,id):
    task=ToDoList.objects.get(id=id)
    context={'success':False}
    if request.method=='POST':
        title=request.POST['title']
        start_date=request.POST['start_date']
        deadline=request.POST['Deadline_time']
        task.Task_Name=title
        task.start_date=start_date
        task.deadline=deadline
        task.save()
        context={'success':True,
                 'msg':'Updated'   
        }
        return render(request,'home.html',context)

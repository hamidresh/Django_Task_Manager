from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from .form import UserForm ,ComentForm , TaskForm


def home(request):
    user = User.objects.all()
    task = Task.objects.all()
    comments=Comment.objects.all()
    
    context = {'user' : user , 'task' : task  ,"comments": comments}
    return render(request, 'home.html',context)

def create_user(request):
    form = UserForm()
    if request.method == 'POST' :
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    print(context)
    return render(request, 'create_user.html',context)

def update_user(request,pk):
    user_id = User.objects.get(id=pk)
    form = UserForm(instance=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST , instance=user_id)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'update_user.html',context)

def delete_user(request,pk):   
    user_id = User.objects.get(id=pk) 
    if request.method == "POST" :
        user_id.delete()
        return redirect('/')
    context = {'item':user_id}
    return render(request , 'delete_user.html',context)

def add_comment(request):
    users = User.objects.all()
    tasks = Task.objects.all()

    if request.method == 'POST':
        user_id = request.POST.get('user')
        task_id = request.POST.get('task')
        comment_type = request.POST.get('comment_type')

        user = User.objects.get(id=user_id)
        task = Task.objects.get(id=task_id)

        Comment.objects.create(user=user, task=task, comment_type=comment_type)

        return redirect('/') 

    return render(request, 'add_comment.html', {'users': users, 'tasks': tasks})

def delete_comment(request,pk):
    comment_id = Comment.objects.get(id=pk)

    if request.method == "POST" :
            comment_id.delete()
            return redirect('/')
    context = {'item':comment_id}
    return render(request , 'delete_comment.html',context)

def create_task(request):
    form = TaskForm()
    user = User.objects.all()
    if request.method == 'POST' :
        form = TaskForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form,'user':user}
    print(context)
    return render(request, 'create_task.html',context)

def delete_task(request,pk):   
    task_id = Task.objects.get(id=pk) 
    if request.method == "POST" :
        task_id.delete()
        return redirect('/')
    context = {'item':task_id}
    return render(request , 'delete_task.html',context)

def update_task(request,pk):
    user_id = Task.objects.get(id=pk)
    form = TaskForm(instance=user_id)
    if request.method == 'POST':
        form = TaskForm(request.POST , request.FILES ,instance=user_id)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'update_task.html',context)


from django.shortcuts import render, redirect
from .models import todo, todomonth, todoweek

def home(request):
    data = todo.objects.all()
    return render(request, 'tasks/home.html', {'data': data})

def add(request):
    tododata = request.POST['todo'] # Adds todo item
    todo_items = todo(content=tododata)
    todo_items.save()
    return redirect(home)


def deleteItem(request, todo_id):
    item = todo.objects.get(id=todo_id)
    item.delete()
    return redirect(home)


def week(request):
    dataweek = todoweek.objects.all()
    return render(request, 'tasks/week.html', {'dataweek': dataweek})

def addweek(request):
    tododata = request.POST['todoweek']
    todo_items = todoweek(content_week=tododata)
    todo_items.save()
    return redirect(week)

def deleteweek(request, todoweek_id):
    item = todoweek.objects.get(id=todoweek_id)
    item.delete()
    return redirect(week)


def month(request):
    datamonth = todomonth.objects.all()
    return render(request, 'tasks/month.html', {'datamonth': datamonth})

def addmonth(request):
    tododata = request.POST['todomonth']
    todo_items = todomonth(content_month=tododata)
    todo_items.save()
    return redirect(month)

def deletemonth(request, todomonth_id):
    item = todomonth.objects.get(id=todomonth_id)
    item.delete()
    return redirect(month)
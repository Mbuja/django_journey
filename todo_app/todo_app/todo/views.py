from django.shortcuts import render,redirect
from todo.forms import ToDoForm
from .models import Todo
# Create your views here.

def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == 'POST':
        form  = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = ToDoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title":"TODO_LIST",
    }

    return render(request,'index.html',page)
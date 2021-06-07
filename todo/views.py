from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem


# Create your views here.
def todoView(request):
    all_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_items})


def AddTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    # print(item_to_delete)
    return HttpResponseRedirect('/todo/')

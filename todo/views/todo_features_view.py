from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Todo
from ..forms import TodoForm


def todo_list(request):
    """Displays the to-do list, handles new to-do creation, and updates status via drag-and-drop."""
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        if 'todo_id' in request.POST and 'new_status' in request.POST:
            todo = get_object_or_404(Todo, pk=request.POST['todo_id'], user=request.user)
            todo.status = request.POST['new_status']
            todo.save()

            return JsonResponse({'status': 'success'})

        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    todos = Todo.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'todo/todo_list.html', {
        'todos': todos,
        'form': form,
        'status_groups': [
            ('TODO', 'To Do'),
            ('IN_PROGRESS', 'In Progress'),
            ('DONE', 'Done'),
        ]
    })


@login_required
def update_status(request, pk):
    """Updates the status of a to-do item to the next stage."""
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if todo.status == 'TODO':
        todo.status = 'IN_PROGRESS'
    elif todo.status == 'IN_PROGRESS':
        todo.status = 'DONE'
    else:
        todo.status = 'TODO'
    todo.save()
    return redirect('todo_list')


@login_required
def delete_todo(request, pk):
    """Deletes a specific to-do item owned by the authenticated user."""
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return redirect('todo_list')

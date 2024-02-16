from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Task


# Create your views here.
                                              #For learning purposes. View.py Classes
class TaskList(ListView):                    # django searching todo_app/task_list.html to connect
    model = Task                             # class require model OR queryset
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'              #getting object throught 'task'
    template_name = 'todo_app/task.html'      #changing default rout

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'                        #all fields of model
    success_url = reverse_lazy('tasks')       #after succesfull creating object redirect to name='tasks'

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

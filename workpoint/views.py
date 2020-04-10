from django.shortcuts import render
from .models import MainTask, Point

# Create your views here.
def index(request):
    points = Point.objects.all()
    maintasks = MainTask.objects.all()
    context = {'points': points, 'maintasks': maintasks}
    return render(request, "workpoint/index.html", context)


def by_maintask(request, maintask_id):
    points = Point.objects.filter(maintask=maintask_id)
    maintasks = MainTask.objects.all()
    current_maintask = MainTask.objects.get(pk=maintask_id)
    context = {
        "points": points,
        "maintasks": maintasks,
        "current_maintask": current_maintask,
    }
    return render(request, "workpoint/by_maintask.html", context)


from django.views.generic.edit import CreateView
from .forms import PointForm, MainTaskForm
from django.urls import reverse_lazy


class PointCreateView(CreateView):
    template_name = 'workpoint/create.html'
    form_class = PointForm
    succes_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maintasks'] = MainTask.objects.all()
        return context

class MainTaskCreateView(CreateView):
    template_name = 'workpoint/createmaintask.html'
    form_class = MainTaskForm
    succes_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maintasks'] = MainTask.objects.all()
        return context

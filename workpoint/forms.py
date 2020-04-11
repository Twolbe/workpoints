from django.forms import ModelForm
from .models import Point, MainTask


class PointForm(ModelForm):
    class Meta:
        model = Point
        fields = ("tag", "description", "resolution", "status", "maintask")


class MainTaskForm(ModelForm):
    class Meta:
        model = MainTask
        fields = ("title", "description", "status")

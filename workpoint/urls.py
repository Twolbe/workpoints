from django.urls import path

from .views import index, by_maintask, PointCreateView, MainTaskCreateView

urlpatterns = [
    path("workpoint/<int:maintask_id>/", by_maintask, name="by_maintask"),
    path("workpoint/", index, name="index"),
    path("workpoint/add/", PointCreateView.as_view(), name="add"),
    path("workpoint/add/maintask/", MainTaskCreateView.as_view(), name="addmaintask"),
]

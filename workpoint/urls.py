from django.urls import path

from .views import index, by_maintask, PointCreateView, MainTaskCreateView

urlpatterns = [
    path('<int:maintask_id>/', by_maintask, name='by_maintask'),
    path('', index, name='index'),
    path('add/', PointCreateView.as_view(), name='add'),
    path('add/maintask/', MainTaskCreateView.as_view(), name='addmaintask')
]

from django.contrib import admin
from .models import Point, MainTask
from django.utils.translation import gettext_lazy as _


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    pass


@admin.register(MainTask)
class MainTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "status", "date_init")
    list_display_links = ("title", "status")
    search_fields = ("title",)
    list_filter = ("status",)
    radio_fields = {"status": admin.HORIZONTAL}

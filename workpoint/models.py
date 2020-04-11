from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date, datetime


class Point(models.Model):
    tag = models.CharField("tag", max_length=50)
    description = models.TextField("Description", null=True, blank=True)
    resolution = models.TextField("Resolution", null=True, blank=True)

    class Status(models.TextChoices):
        NEW = "n", _("New")
        PROCESSING = "p", _("Processing")
        DONE = "d", _("Done")

    status = models.CharField(
        "Status", max_length=1, choices=Status.choices, default=Status.NEW
    )
    date_init = models.DateTimeField("Beggining date", db_index=True)
    maintask = models.ForeignKey(
        "MainTask", on_delete=models.CASCADE, verbose_name="MainTasks"
    )

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Point"
        verbose_name_plural = "Points"


class MainTask(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.TextField("Description", null=True, blank=True)
    date_init = models.DateTimeField("Beggining date", db_index=True)

    class Status(models.TextChoices):
        NEW = "n", _("New")
        PROCESSING = "p", _("Processing")
        DONE = "d", _("Done")

    status = models.CharField(
        "Status", max_length=1, choices=Status.choices, default=Status.NEW
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Main Task"
        verbose_name_plural = "Main Tasks"
        ordering = ["-date_init"]

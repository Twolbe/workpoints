from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date, datetime

# Create your models here.
class Point(models.Model):
    class Meta:
        verbose_name = 'Point'
        verbose_name_plural = "Points"

    tag = models.CharField('tag', max_length=50)
    description = models.TextField('Description', null=True, blank=True)
    resolution = models.TextField('Resolution', null=True, blank=True)

    class Status(models.TextChoices):
        NEW = 'n', _('New')
        PROCESSING = 'p', _('Processing')
        DONE = 'd', _('Done')

    status = models.CharField('Status', max_length=1, choices=Status.choices, default=Status.NEW)
    date_init = models.DateTimeField('Beggining date', db_index=True)
    maintask = models.ForeignKey('MainTask', on_delete=models.CASCADE, null=True, verbose_name='MainTasks')

    def __str__(self):
        return self.tag


class MainTask(models.Model):
    class Meta:
        verbose_name = 'Main Task'
        verbose_name_plural = 'Main Tasks'
        ordering = ['-date_init']

    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description', null=True, blank=True)
    date_init = models.DateTimeField('Beggining date', db_index=True)

    # NEW = 'n'
    # PROCESSING = 'p'
    # DONE = 'd'

    # STATUS = [
    #     (NEW, 'New'),
    #     (PROCESSING, 'Processing'),
    #     (DONE, 'Done'),
    # ]
    # status = models.CharField('Status', max_length=1, choices=STATUS, default=NEW)

    class Status(models.TextChoices):
        NEW = 'n', _('New')
        PROCESSING = 'p', _('Processing')
        DONE = 'd', _('Done')

    status = models.CharField('Status', max_length=1, choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return self.title

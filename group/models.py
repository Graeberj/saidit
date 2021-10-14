from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from saidituser.models import SaidItUser


class SubGroup(models.Model):
    group_name = models.CharField(max_length=30)
    group_description = models.TextField(null=True, blank=False)
    time_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(SaidItUser, on_delete=CASCADE)
    # member = models.ManyToManyField('self', blank=True, related_name='group_member')
    # apply to group/ subscribe to group manytomany field?

    def __str__(self):
        return self.group_name

from django.db import models
from saidituser.models import SaidItUser
from django.utils import timezone
from group.models import SubGroup
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(SaidItUser, on_delete=models.CASCADE)
    posted_in = models.ForeignKey(SubGroup, on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    time_created = models.DateTimeField(default=timezone.now)
    like_dislike = models.BooleanField(default=False, choices=(
        (True, 'like'), (False, 'dislike')))
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    # rate = models.ManyToManyField('', symmetrical=False, blank=True, related_name='+')

    # notification
    class Meta:
        ordering = ["-time_created"]
    def __str__(self):
        return self.body




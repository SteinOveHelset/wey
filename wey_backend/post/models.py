import uuid

from django.db import models
from django.utils.timesince import timesince

from account.models import User


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
    
    def created_at_formatted(self):
       return timesince(self.created_at)


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(User, related_name='post_attachments', on_delete=models.CASCADE)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        else:
            return ''


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)

    attachments = models.ManyToManyField(PostAttachment, blank=True)

    likes = models.ManyToManyField(Like, blank=True)
    likes_count = models.IntegerField(default=0)

    comments = models.ManyToManyField(Comment, blank=True)
    comments_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
    
    def created_at_formatted(self):
       return timesince(self.created_at)
    

class Trend(models.Model):
    hashtag = models.CharField(max_length=255)
    occurences = models.IntegerField()
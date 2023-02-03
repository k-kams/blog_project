from django.contrib.auth.models import AbstractUser
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Users(AbstractUser):
    phone_number = models.CharField(max_length=20)


class Post(TimeStampedModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=50)
    content = models.TextField('CONTENT')
    image = models.ImageField('IMAGE', upload_to='blog/image/', blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    like = models.ManyToManyField(Users, related_name='likes', blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField('CONTENT')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    @property
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content

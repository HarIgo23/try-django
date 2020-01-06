from django.db import models
from django.conf import settings
# if anywhere else you need user model
# from django.contrib.auth import get_user_model


User = settings.AUTH_USER_MODEL  # if use user model in Foreign Key


class BlogPost(models.Model):  # user.blogpost_set -> queryset related with user
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

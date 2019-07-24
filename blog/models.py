from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# import reverse
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # redirect will actually redirect you to a specific route
    # reverse will return the full url to that route as a string
    def get_absolute_url(self):
        # return the full url of our post-detail route with the primary key
        # self.pk means the primary key of the instance of a Post
        return reverse('post-detail', kwargs={'pk': self.pk})
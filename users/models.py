from django.db import models
# import User model
from django.contrib.auth.models import User

class Profile(models.Model):
    # creates a 1:1 relationship with the existing User model
    # on_delete=models.CASCADE argument tells django what will happen to the Profile when a user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image field
    # default picture = default.jpg default image for any user
    # upload_to='profile_pics' refers to the directory where images will be stored when uploaded
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

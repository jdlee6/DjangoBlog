from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # this save method will get run after our model is saved
    # the save method already exists that's why we need to OVERRIDE it with the same name and added functionality
    def save(self):
        # run the save method of our parent class
        super().save()
        
        # opens image of the current instance
        img = Image.open(self.image.path)
        # if image height/width is greater than 300 pixels
        if img.height > 300 or img.width > 300:
            # image dimensions into 300 x 300
            output_size = (300, 300)
            # resizes the image
            img.thumbnail(output_size)
            img.save(self.image.path)
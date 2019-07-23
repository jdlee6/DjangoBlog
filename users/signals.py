# signal that gets fired after an object is saved
# we want to get a post_save signal when a user is created
from django.db.models.signals import post_save
# the User model will be referred to as the sender in this case
from django.contrib.auth.models import User
# need to create a receiver (import it): a function that receives the signal and then performs a task
from django.dispatch import receiver
# import Profile because we will creating the Profile within our function
from .models import Profile


# when a User is saved (in decorator), create a profile (the function)

# 1st arg is the signal in this case the post_save 
# 2nd arg is the sender in this case is the User
@receiver(post_save, sender=User)
# this function will be ran everytime a user is created
# instance means instance of user
def create_profile(sender, instance, created, **kwargs):
    # if that instance of user was created
    if created:
        # create profile object with the user equal to the instance of the User that was created
        Profile.objects.create(user=instance)

# save profile function that saves our profile everytime the User object gets saved 
@receiver(post_save, sender=User)
# **kwargs parameter accepts any additional keywords
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
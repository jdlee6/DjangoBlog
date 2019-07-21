from django.contrib import admin
# import Post from cwd's models module
from .models import Post

# register our Post model to the admin site
admin.site.register(Post)
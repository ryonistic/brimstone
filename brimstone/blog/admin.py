"""A simple Post model registered for the admin panel with the default command."""
from django.contrib import admin
from .models import Post


admin.site.register(Post)

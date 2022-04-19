from PIL import Image
from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Post(models.Model):
    """slugs are unique, author sets to null on on_delete"""
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL)
    date_posted = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=300, unique=True)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media')

    def save(self, *args, **kwargs):
        """creating a SlugField for each instance
        by overriding the save method"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # each image file must be sized down to save space
        image = Image.open(self.image.path)
        if image.height > 700 or image.width > 700:
            output_size = (700, 700)
            image.thumbnail(output_size)
            image.save(self.image.path)

    def get_absolute_url(self):
        return f"/postdetail/{self.slug}/"

    def __str__(self):
        return str(f'{self.title} by {self.author}')

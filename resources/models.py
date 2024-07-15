from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Resources(models.Model):
    """
    Stores fields for Resources
    """
    title = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

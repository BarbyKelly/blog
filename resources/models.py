from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Resources(models.Model):
    """
    Stores fields for Resources
    """
    title = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


# Create Suggestion form
class Suggestion(models.Model):
    """
    Model for Site Users to suggest a Resource
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="suggestion"
    )
    content = models.TextField(max_length=500)
    created_on = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"Suggestion from {self.name}"

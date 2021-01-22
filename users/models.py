# Django
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  # Profile Model
    # Proxy model that extends the base data with other information

    # OneToOneField is a relationship of one to one that extends of the User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True) # URLField is the similar to CharField but with URL
    biography = models.TextField(blank=True) # Insert big quantities of text
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True) # Validate object loading to image

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Return Username
        return self.user.username
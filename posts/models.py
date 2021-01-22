## Posts Models

# Django














# # Posts Modles

# # Django
# from django.db import models

# class User(models.Model):

#     email = models.EmailField(unique=True) # Validate email address, the optional argument max_length,min_length and empty_value... unique --- email unico
#     password = models.CharField(max_length=100) # Insert Character and is obligatory inset argument as min_length or max_length

#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     is_admin = models.BooleanField(default=False)

#     bio = models.TextField(blank=True) # Insert Text

#     biryhdate = models.DateField(blank=True, null=True) # Set date as  input date()

#     created = models.DateTimeField(auto_now_add=True)  # Set dateTime with auto_now_add we set the date and time when it was created
#     modified = models.DateTimeField(auto_now=True) # Set dateTime with auto_now we set the date and time when it was update

#     def __str__(self):
#         # Return email.
#         return self.email
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    pwd_hash = models.CharField(max_length=255)
    signup_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'
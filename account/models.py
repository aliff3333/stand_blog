from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=50)
    melicode = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/profiles', null=True, blank=True)

    def __str__(self):
        return self.user.username

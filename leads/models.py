from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#   pass

class Lead(models.Model):
  ismi = models.CharField(max_length=20)
  familiasi = models.CharField(max_length=20)
  yoshi = models.IntegerField(default=0)
  # pochtasi = models.EmailField(max_length=50)

  def __str__(self):
      return self.familiasi + " " + self.ismi 


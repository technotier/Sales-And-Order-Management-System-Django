from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    profile_pic = models.ImageField(default='profile_pic_default.png', upload_to='', null=True, blank=True)

    class Meta:
        ordering = ('-salary',)

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.designation)


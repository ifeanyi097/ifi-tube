from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=10)
    file = models.FileField(upload_to='videos')
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
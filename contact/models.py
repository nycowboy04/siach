from django.db import models

class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField
    subject=models.CharField(max_length=200)
    message=models.TextField

    def __str__(self):
        return self.id

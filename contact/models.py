from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField('subject', max_length=100)
    message = models.TextField('Write your message here', max_length=3000)

    def __str__(self):
        return self.name

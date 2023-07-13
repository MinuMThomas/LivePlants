from django.db import models
from items.models import Item
from django.contrib.auth.models import User


class Review(models.Model):
    """ Review model """

    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=True, blank=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True, blank=False, null=False)

    class Meta:
        """ Meta class for Review model """
        ordering = ['-date']

    def __str__(self):
        return f"{self.title}"

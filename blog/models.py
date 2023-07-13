from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=60, unique=True, null=False,
                             blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

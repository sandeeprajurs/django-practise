from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        # return f"/product/{self.id}"
        return reverse("articles_detail_view", kwargs={ "id": self.id})
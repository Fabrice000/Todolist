from django.db import models
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    elements = 'generic'
class Taches(models.Model):
    categories = models.CharField(max_length=50)
    finish = models.BooleanField(default=False)
    name = models.TextField()
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=50,default="low")
    duration = models.DateTimeField( auto_now=True)
    finish_duration = models.DateField(auto_now=False,null=True)
    image = models.ImageField(blank=True)
    class Meta:
        verbose_name  = ("Tache")
        verbose_name_plural  = ("Taches")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("modify", kwargs={"id": self.pk})


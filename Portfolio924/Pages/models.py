from django.db import models

# Create your models here.


class Ceres_Report(models.Model):
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=False)
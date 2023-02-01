from django.db import models

class Text(models.Model):
    text = models.CharField(max_length=60)
    

    def __str__(self):
        return self.text

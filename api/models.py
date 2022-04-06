from django.db import models

# Create your models here.
class NewsLetter(models.Model):
    email = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'NewsLetter'

    def __str__(self):
        return self.email
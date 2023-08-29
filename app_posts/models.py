from django.db import models


# Create your models here.
CATEGORY_CHOICES = (
    ('Dj', 'Django'),
    ('R', 'Ruby')
)
class Post(models.Model):
    title = models.CharField(max_length=128)
    custom_id = models.IntegerField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

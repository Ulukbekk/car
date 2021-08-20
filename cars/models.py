from PIL import Image
from django.db import models
import datetime
from user.models import User

class Car(models.Model):
    BODY_CHOICES = (
        ('sedan', 'sedan'),
        ('suv', 'suv'),
        ('wagon', 'wagon'),
        ('coup', 'coup'),
        ('hatchback', 'hatchbak'),
        ('pickup', 'pickup'),
        ('compact', 'compact'),
        ('sport coupe', 'sport coupe'),
        ('van', 'van'),
        ('crossover', 'crossover'),
    )
    COLOR_CHOICES = (
        ('red', 'red'),
        ('yellow', 'yellow'),
        ('orange', 'orange'),
        ('green', 'green'),
        ('blue', 'blue'),
        ('violet', 'violet'),
        ('gray', 'gray'),
        ('white', 'white'),
        ('black', 'black'),
    )
    TRANSMISSION_CHOICES = (
        ('manual', 'manual'),
        ('auto', 'auto'),
        ('robot', 'robot'),
    )
    RUL_CHOICES = (
        ('left', 'left'),
        ('right', 'right'),
    )


    YEAR_CHOICES = []
    for r in range(1940, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))


    category = models.CharField(choices=BODY_CHOICES, blank=True, null=False, max_length=15)
    color = models.CharField(choices=COLOR_CHOICES, blank=True, null=False, max_length=10)
    transmission = models.CharField(choices=TRANSMISSION_CHOICES, blank=True, null=False, max_length=10)
    rul = models.CharField(choices=RUL_CHOICES, blank=True, null=False, max_length=10)

    image = models.ImageField()
    title = models.CharField(max_length=30)
    volume = models.DecimalField(decimal_places=2, max_digits=9)
    price = models.FloatField()
    release_date = models.IntegerField(('release date'), choices=YEAR_CHOICES,
                               default=datetime.datetime.now().year)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               blank=True, null=True, related_name='author_post')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
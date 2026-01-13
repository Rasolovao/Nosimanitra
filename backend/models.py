from django.db import models

# Create your models here.
class AdminUIConfig(models.Model):
    NAVBAR_CHOICES = [
        ('defaut', 'Default'),
        ('golden', 'Golden'),
        ('green', 'Green'),
        ('dark', 'Dark'),
    ]
    navbar_style = models.CharField(max_length=20, choices=NAVBAR_CHOICES, default='defaut')

    def __str__(self):

        return f"Admin UI Config({self.navbar_style})"
    

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_config(cls):
        config, created = cls.objects.get_or_create(pk=1)
        return config
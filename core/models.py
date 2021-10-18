from django.db import models

class Skills(models.Model):

    name = models.CharField(
        max_length=100,
        null = False,
        blank = False,
    )
    percentage = models.PositiveIntegerField(
        default = 100, 
    )

    def __str__(self):
        return f'{self.name} - {self.percentage}%'

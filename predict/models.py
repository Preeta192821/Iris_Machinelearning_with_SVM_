from django.db import models

# Create your models here.


class Predictresult(models.Model):

    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    variety = models.CharField(max_length=30)

    def __str__(self):
        return self.variety





























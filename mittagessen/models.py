from django.db import models


class Esser(models.Model):
    name = models.CharField(max_length=400)
    alias = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    bill = models.FloatField(default=0)

    def __str__(self):
        return self.alias


class Essen(models.Model):
    name = models.CharField(max_length=400)
    category_name = models.CharField(max_length=300)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Mittagessen(models.Model):
    person = models.ForeignKey(Esser)
    type = models.ForeignKey(Essen)
    price = models.FloatField(default=0)
    date = models.DateField()

    def __str__(self):
        return '%s for %s: %f' % (str(self.type), str(self.person), self.price)

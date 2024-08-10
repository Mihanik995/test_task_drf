from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

class DistributionNod(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.PositiveIntegerField()

    products = models.ManyToManyField(to=Product)

    provider = models.ForeignKey(to='distribution_network.DistributionNod',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    dept = models.FloatField()

    creation_datetime = models.DateTimeField(auto_now=True)


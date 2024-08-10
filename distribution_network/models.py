from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f'{self.title} {self.model}'


class DistributionNod(models.Model):
    role = models.CharField(max_length=15, choices=[
        ('manufacture', 'Manufacture'),
        ('entrepreneur', 'Individual entrepreneur'),
        ('retail', 'Retail network')])

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
    dept = models.FloatField(default=0)

    creation_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.role}. {self.city}, {self.country})'

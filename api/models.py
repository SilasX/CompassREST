from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    owner = models.ForeignKey(Group, default=None, blank=True,
        null=True)

    def ownerName(self):
        if self.owner:
            return self.owner.name
        return None

    def __unicode__(self):
        return "{0} -- {1}".format(self.id, self.name)


class SellListing(models.Model):
    product = models.ForeignKey(Product)
    dateListed = models.CharField(max_length=32, blank=True)
    volumeAvailable = models.IntegerField()
    seller = models.ForeignKey(User)

    # looked-up values, flat
    def productName(self):
        return self.product.name

    def productDescription(self):
        return self.product.description

    def productPrice(self):
        return self.product.price

    def productOwnerName(self):
        if self.product.owner:
            return self.product.owner.name
        return None

    def sellerName(self):
        return self.seller.username

    def __unicode__(self):

        return "{0} -- {1} -- {2}".format(self.seller.username,
            self.product.name, self.volumeAvailable)

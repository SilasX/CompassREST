from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    producer = models.ForeignKey(Group, default=None, blank=True,
        null=True)

    def ownerName(self):
        if self.producer:
            return self.producer.name
        return None

    def __unicode__(self):
        return "{0} -- {1}".format(self.id, self.name)


#class SellListing(models.Model):
#    product = models.ForeignKey(

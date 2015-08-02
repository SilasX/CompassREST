from datetime import datetime

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import Product, SellListing


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'producer', 'ownerName')


# Stupid, roundabout way of doing primary keys since nothing else worked
class ProductField(serializers.Field):
    """
    Product objects serialized into their primary keys
    """
    def to_representation(self, obj):
            return obj.id

    def to_internal_value(self, data):
        try:
            return Product.objects.get(id=data)
        except:
            raise serializers.ValidationError("Not a valid Product ID")


def now_string():
    return datetime.now().isoformat()


class SellListingSerializer(serializers.HyperlinkedModelSerializer):
    #product_id = serializers.PrimaryKeyRelatedField(
    #    queryset=Product.objects.all())
    product = ProductField()
    dateListed = serializers.CharField(max_length=32, allow_blank=True,
        initial=now_string(), required=False, allow_null=True)
    seller = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True)
    class Meta:
        model = SellListing
        #fields = ('product_id', 'dateListed', 'volumeAvailable',
        fields = ('url', 'product', 'dateListed', 'volumeAvailable',
            "seller")

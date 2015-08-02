from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from api.serializers import (UserSerializer, GroupSerializer,
    ProductSerializer, SellListingSerializer)

# Models we add
from api.models import Product, SellListing


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Permissions
class ProductPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        else:
            user = request.user
            groups = user.groups.all()
            producer = obj.producer
            if user.is_authenticated() and producer in groups:
                return True
            return False


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (ProductPermission, )


# Permissions
class SellListingPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Anyone can view
        if request.method == "GET":
            return True
        # Only logged in users can create
        elif request.method == "POST":
            return user.is_authenticated()
        # Only the seller can modify
        elif request.method in ("PATCH", "PUT", "DELETE"):
            user = request.user
            seller = obj.seller
            if user.is_authenticated() and user == seller:
                return True
            return False
        return False


class SellListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sell listings to be viewed or edited.
    """
    queryset = SellListing.objects.all()
    serializer_class = SellListingSerializer
    permission_classes = (SellListingPermission, )

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    def perform_update(self, serializer):
        serializer.save(seller=self.request.user)

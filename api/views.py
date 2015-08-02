from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from api.serializers import (UserSerializer, GroupSerializer,
    ProductSerializer)

# Models we add
from api.models import Product


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
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (ProductPermission, )



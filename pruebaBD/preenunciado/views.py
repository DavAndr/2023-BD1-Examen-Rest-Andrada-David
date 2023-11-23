from rest_framework import viewsets
from preenunciado.models import *
from preenunciado.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import renderers
# Create your views here.

class CategoriesViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    #@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)



class CustomercustomerdemoViewset(viewsets.ModelViewSet):
    queryset = Customercustomerdemo.objects.all()
    serializer_class = CustomercustomerdemoSerializer

class CustomerdemographicsViewset(viewsets.ModelViewSet):
    queryset = Customerdemographics.objects.all()
    serializer_class = CustomerdemographicsSerializer

class CustomersViewset(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class EmployeeterritoriesViewset(viewsets.ModelViewSet):
    queryset = Employeeterritories.objects.all()
    serializer_class = EmployeeterritoriesSerializer

class EmployeesViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class OrderdetailsViewset(viewsets.ModelViewSet):
    queryset = Orderdetails.objects.all()
    serializer_class = OrderdetailsSerializer

class OrdersViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class ProductsViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class RegionViewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ShippersViewset(viewsets.ModelViewSet):
    queryset = Shippers.objects.all()
    serializer_class = ShippersSerializer

class SuppliersViewset(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer

class TerritoriesViewset(viewsets.ModelViewSet):
    queryset = Territories.objects.all()
    serializer_class = TerritoriesSerializer

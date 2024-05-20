from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from apps.Equipment.models import Equipment
from apps.Equipment.serializers import EquipmentSerializer
from rest_framework.pagination import PageNumberPagination
from apps.User.permissions import IsAdmin
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils.decorators import method_decorator


class EquipmentViewAPI(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdmin,]
    
    @method_decorator(cache_page(60*10))
    @method_decorator(vary_on_headers('Authorization'))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EquipmentDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = 'id'
    permission_classes = [IsAdmin,]
    
    @method_decorator(cache_page(60*10))
    @method_decorator(vary_on_headers('Authorization'))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
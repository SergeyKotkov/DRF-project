from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ('payment_date', 'cost',)
    search_fields = ('payment_method',)
    filterset_fields = ('payment_date', 'payment_course', 'payment_lesson', 'payment_method',)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ('payment_date', 'cost',)
    search_fields = ('payment_method',)
    filterset_fields = ('payment_date', 'payment_course', 'payment_lesson', 'payment_method',)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

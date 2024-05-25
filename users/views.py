from rest_framework import filters
from rest_framework.generics import ListAPIView

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ('date_payment',)

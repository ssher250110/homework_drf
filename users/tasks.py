from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def check_last_login_user():
    deadline_date = timezone.now().today() - timedelta(days=30)
    for user in User.objects.filter(last_login__lt=deadline_date, is_active=True):
        user.is_active = False
        user.save()

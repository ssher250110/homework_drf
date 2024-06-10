from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


@shared_task
def send_info_update_course(email, course_name):
    send_mail(
        'Update course',
        f'We have updated the course material {course_name}',
        EMAIL_HOST_USER,
        [email]
    )

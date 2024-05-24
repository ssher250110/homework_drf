from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_list = [
            {"email": "user1@user.com", "is_active": True},
            {"email": "user2@user.com", "is_active": True},
            {"email": "user3@user.com", "is_active": True},
        ]
        user_create = []
        for user_item in user_list:
            user_create.append(User(**user_item))
        User.objects.bulk_create(user_create)

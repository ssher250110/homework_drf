from rest_framework.serializers import ValidationError


def validate_link(link: str):
    if not link.startswith('https://www.youtube.com/') or link.startswith('https://m.youtube.com/'):
        raise ValidationError('Links are allowed only on youtube')


class SubscribeValidators:
    pass

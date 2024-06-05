# Generated by Django 5.0.6 on 2024-06-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_payment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='link',
            field=models.URLField(blank=True, help_text='Укажите ссылку на оплату', max_length=400, null=True, verbose_name='Ссылка на оплату'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.CharField(blank=True, help_text='Укажите id сессии', max_length=255, null=True, verbose_name='id сессии'),
        ),
    ]

from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Введите почту')
    phone = models.CharField(max_length=14, **NULLABLE, verbose_name='Телефон', help_text='Введите номер телефона')
    country = models.CharField(max_length=85, **NULLABLE, verbose_name='Страна', help_text='Введите название страны')
    avatar = models.ImageField(upload_to='users/avatars/', **NULLABLE, verbose_name='Аватар',
                               help_text='Загрузите аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)


class Payment(models.Model):
    class MethodPayment(models.TextChoices):
        TRANSFER = 'TF', 'Transfer'
        CASH = 'CH', 'Cash'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Адрес электронной почты пользователя',
                             help_text='Выберите адрес электронной почты пользователя')
    date_payment = models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа')
    paid_course = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, verbose_name='Оплаченный курс',
                                    help_text='Выберите название оплаченного курса')
    paid_lesson = models.ForeignKey(Lesson, **NULLABLE, on_delete=models.CASCADE, verbose_name='Оплаченный урок',
                                    help_text='Выберите название оплаченного урока')
    amount_payment = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Сумма оплаты',
                                         help_text='Введите сумму оплаты')
    method_payment = models.CharField(max_length=2, choices=MethodPayment.choices, default=MethodPayment.TRANSFER,
                                      verbose_name='Способ оплаты', help_text='Выберите способ оплаты')

    def __str__(self):
        return (f'{self.user} - {self.date_payment}\n{self.paid_course if self.paid_course else self.paid_lesson}\n'
                f'{self.method_payment} - {self.amount_payment}')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('-date_payment', 'user',)

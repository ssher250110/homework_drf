from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название курса', help_text='Введите название курса')
    description = models.TextField(**NULLABLE, verbose_name='Описание курса', help_text='Введите описание курса')
    preview = models.ImageField(upload_to='materials/course', **NULLABLE, verbose_name='Картинка курса',
                                help_text='Загрузите картинку курса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название урока', help_text='Введите название урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Курс',
                               help_text='Выберите название курса')
    description = models.TextField(**NULLABLE, verbose_name='Описание урока', help_text='Введите описание урока')
    preview = models.ImageField(upload_to='materials/lesson', **NULLABLE, verbose_name='Картинка урока',
                                help_text='Загрузите картинку урока')
    link = models.CharField(max_length=150, **NULLABLE, verbose_name='Ссылка', help_text='Добавьте ссылку на видео')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

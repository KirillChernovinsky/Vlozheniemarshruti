from django.db import models


class News(models.Model):
    post_name = models.CharField(max_length=20, verbose_name='Имя_поста')
    post_description = models.CharField(max_length=20, verbose_name='Описание_поста')
    post_img = models.URLField()

    def __str__(self):
        return f'{self.post_name} {self.post_description} {self.post_img}'

    # class Meta:
    #     verbose_name = 'Человека'
    #     verbose_name_plural = 'Люди'


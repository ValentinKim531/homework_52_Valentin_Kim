from django.db import models

# Create your models here.


class Article(models.Model):
    description = models.TextField(max_length=200, null=False, blank=False, verbose_name="Описание")
    status = models.TextField(max_length=20, null=False, blank=False, verbose_name="Статус")
    execution_date = models.TextField(max_length=10, null=True, blank=False, verbose_name="Дата исполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    def __str__(self):
        return f"{self.description} - {self.status} - {self.execution_date}"
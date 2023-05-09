from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Links(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    full_url = models.TextField("Длинная ссылка", unique=False, max_length=1000) #250 как то мало, решил побольше сделать
    short_url = models.SlugField("Короткая ссылка")

    def __str__(self):
        return self.short_url

    class Meta:
        ordering = ('-created_date',) # чтобы ссылки выводились по дате создания
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
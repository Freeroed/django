from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField("Имя человека", max_length=100)
    surmane = models.CharField("Фамилия человека", max_length=100)
    birthdate = models.DateField("Дата рождения")
    image_url = models.CharField("Ссылка на фото", max_length=300)

    def __str__(self):
        return self.name + ' ' + self.surmane
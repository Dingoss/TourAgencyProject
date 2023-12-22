from django.db import models

# Create your models here.
class Travel(models.Model):
    travel_name = models.CharField('Назва туру', max_length=50)
    country = models.CharField('Країна', max_length=50, null=True, blank=True)
    time_go = models.CharField('Час вильоту', max_length=50, null=True, blank=True)
    description = models.TextField('Опис туру')
    travel_time = models.CharField('Тривалість туру', max_length=50)
    price = models.IntegerField('Ціна')


    def __str__(self):
        return self.travel_name
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Тури'

class Order(models.Model):
    user_name = models.CharField('Ім`я', max_length=100)
    user_lname = models.CharField('Фамілія',max_length=100)
    user_phone = models.CharField('Номер телефону',max_length=20)
    user_email = models.EmailField('Електронна пошта')
    user_travel_name = models.CharField('Назва туру', max_length=50)

    def __str__(self):
        return f"{self.user_name} {self.user_lname}"

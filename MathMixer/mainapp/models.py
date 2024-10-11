from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Явное указание id как первичного ключа
    name = models.CharField(max_length=255)  # Название товара
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена товара
    image = models.ImageField(upload_to='products/')  # Поле для загрузки изображения товара
    characteristic1 = models.CharField(max_length=255, blank=True, null=True)  # Характеристика 1
    characteristic2 = models.CharField(max_length=255, blank=True, null=True)  # Характеристика 2
    characteristic3 = models.CharField(max_length=255, blank=True, null=True)  # Характеристика 3
    characteristic4 = models.CharField(max_length=255, blank=True, null=True)  # Характеристика 4
    characteristic5 = models.CharField(max_length=255, blank=True, null=True)  # Характеристика 5
    rating1 = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг для характеристики 1
    rating2 = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг для характеристики 2
    rating3 = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг для характеристики 3
    rating4 = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг для характеристики 4
    rating5 = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг для характеристики 5
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания товара

    def str(self):
        return self.name


class Service(models.Model):
    id = models.AutoField(primary_key=True)  # Явное указание id как первичного ключа
    name = models.CharField(max_length=255)  # Название услуги
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена услуги
    image = models.ImageField(upload_to='services/')  # Поле для загрузки изображения услуги
    characteristic1 = models.CharField(max_length=255, blank=True, null=True)  # Характеристика 1
    characteristic2 = models.CharField(max_length=255, blank=True, null=True)  # Характеристика 2
    characteristic3 = models.CharField(max_length=255, blank=True, null=True)  # Характеристика 3
    characteristic4 = models.CharField(max_length=255, blank=True, null=True)  # Характеристика 4
    characteristic5 = models.CharField(max_length=255, blank=True, null=True)  # Характеристика 5
    rating1 = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг для характеристики 1
    rating2 = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг для характеристики 2
    rating3 = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг для характеристики 3
    rating4 = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг для характеристики 4
    rating5 = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Рейтинг для характеристики 5
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания услуги

    def str(self):
        return self.name

from django.db import models

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    textdes = models.CharField(max_length=400, default='Описание отсутствует')
    rating1 = models.IntegerField(default=0)
    rating2 = models.IntegerField(default=0)
    rating3 = models.IntegerField(default=0)
    rating4 = models.IntegerField(default=0)
    rating5 = models.IntegerField(default=0)
    ratingall = models.IntegerField(default=0)
    ratingbef1 = models.IntegerField(default=0)
    ratingbef2 = models.IntegerField(default=0)
    ratingbef3 = models.IntegerField(default=0)
    ratingbef4 = models.IntegerField(default=0)
    ratingbef5 = models.IntegerField(default=0)
    counter = models.IntegerField(default=0)
    def str(self):
        return self.name

class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    charackterstick = models.OneToOneField('Charackterstick', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def str(self):
        return self.name

class Charackterstick(models.Model):
    id_charackterstick = models.AutoField(primary_key=True)
    charackterstick1 = models.CharField(max_length=255)
    charackterstick2 = models.CharField(max_length=255)
    charackterstick3 = models.CharField(max_length=255)
    charackterstick4 = models.CharField(max_length=255)
    charackterstick5 = models.CharField(max_length=255)

    def str(self):
        return f"Characteristics {self.id_charackterstick}"

class Service(models.Model):
    id_product = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    textdes = models.CharField(max_length=400, default='Описание отсутствует')
    image = models.ImageField(upload_to='products/')
    rating1 = models.IntegerField(default=0)
    rating2 = models.IntegerField(default=0)
    rating3 = models.IntegerField(default=0)
    rating4 = models.IntegerField(default=0)
    rating5 = models.IntegerField(default=0)
    ratingall = models.IntegerField(default=0)
    ratingbef1 = models.IntegerField(default=0)
    ratingbef2 = models.IntegerField(default=0)
    ratingbef3 = models.IntegerField(default=0)
    ratingbef4 = models.IntegerField(default=0)
    ratingbef5 = models.IntegerField(default=0)
    counter = models.IntegerField(default=0)

    def str(self):
        return self.name

class CategoryService(models.Model):
    id_category = models.AutoField(primary_key=True)
    charackterstick = models.OneToOneField('Charackterstick', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def str(self):
        return self.name

class CharackterstickService(models.Model):
    id_charackterstick = models.AutoField(primary_key=True)
    charackterstick1 = models.CharField(max_length=255)
    charackterstick2 = models.CharField(max_length=255)
    charackterstick3 = models.CharField(max_length=255)
    charackterstick4 = models.CharField(max_length=255)
    charackterstick5 = models.CharField(max_length=255)

    def str(self):
        return f"Characteristics {self.id_charackterstick}"


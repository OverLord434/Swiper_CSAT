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
    def __str__(self):
        return self.name

class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    charackterstick = models.OneToOneField('Charackterstick', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Charackterstick(models.Model):
    id_charackterstick = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='Отсутствует название групп характеристик')
    charackterstick1 = models.CharField(max_length=255)
    charackterstick2 = models.CharField(max_length=255)
    charackterstick3 = models.CharField(max_length=255)
    charackterstick4 = models.CharField(max_length=255)
    charackterstick5 = models.CharField(max_length=255)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

class CategoryService(models.Model):
    id_category = models.AutoField(primary_key=True)
    charackterstick = models.OneToOneField('Charackterstick', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CharackterstickService(models.Model):
    id_charackterstick = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='Отсутствует название групп характеристик')
    charackterstick1 = models.CharField(max_length=255)
    charackterstick2 = models.CharField(max_length=255)
    charackterstick3 = models.CharField(max_length=255)
    charackterstick4 = models.CharField(max_length=255)
    charackterstick5 = models.CharField(max_length=255)

    def __str__(self):
        return self.name


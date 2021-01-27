from django.db import models


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)


class Performer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    masterpiece = models.CharField(max_length=20)


# 一对一
class PerformerInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    performer = models.OneToOneField(Performer, on_delete=models.CASCADE)
    birth = models.CharField(max_length=20)
    elapse = models.CharField(max_length=20)


# 一对多
class ProgramTmp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)


# 多对多
class Program(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    performer = models.ManyToManyField(Performer)

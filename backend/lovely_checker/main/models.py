from django.db import models


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class PotentialCity(models.Model):
    name = models.CharField(max_length=255)


class IpAddressCity(models.Model):
    city = models.CharField(unique=True, max_length=255)
    ip = models.CharField(unique=True, max_length=255)

from django.db import models

class Rules(models.Model):
    name = models.CharField(max_length=50)

class Trades(models.Model):
    name = models.CharField(max_length=50)

class Users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    rule = models.ForeignKey(Rules, on_delete=models.CASCADE)
    id_deleted = models.BooleanField(default=False)

class Companies(models.Model):
    name = models.CharField(max_length=50)
    nip = models.IntegerField()
    trade = models.ForeignKey(Trades, on_delete=models.CASCADE)
    adres = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    id_deleted = models.BooleanField(default=False)

class Notes(models.Model):
    content = models.CharField(max_length=500)
    id_deleted = models.BooleanField(default=False)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()
    mail = models.CharField(max_length=20)
    job = models.CharField(max_length=50)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    id_deleted = models.BooleanField(default=False)


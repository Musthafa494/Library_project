from django.db import models

#Table Book
class book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    price=models.IntegerField()
    pdf=models.FileField(upload_to='book/pdf')
    cover=models.ImageField(upload_to='book/cover',null=True,blank=True)

class student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)


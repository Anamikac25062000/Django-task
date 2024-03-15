from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    year = models.IntegerField()
    book_doc = models.FileField(upload_to='uploads/')

class UploadFile(models.Model):
    title = models.CharField(max_length=255)
    doc = models.FileField(upload_to='uploads/')



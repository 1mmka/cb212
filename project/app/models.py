from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=64)
    isbn = models.IntegerField()
    publication = models.DateTimeField(db_index=False,auto_now_add=False)

    book_owner = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.name
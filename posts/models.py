from django.db import models


# Create your models here.

class Author(models.Model):
    full_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.full_name} - {self.phone}'


class Post(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.author}'


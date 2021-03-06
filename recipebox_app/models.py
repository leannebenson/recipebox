from django.db import models
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    time_required = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.author.name}"
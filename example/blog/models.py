from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, null=True, blank=True,
                               on_delete=models.PROTECT)

    def __str__(self):
        return self.title

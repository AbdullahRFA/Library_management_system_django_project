from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30)
    Msc = models.CharField(max_length=50)
    Bsc = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    category = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='books/',null=True,blank=True)
    descriptions = models.TextField(null=True,blank=True)
    Source = models.TextField(help_text="Enter the book online link for more deatils and buy link",null=True, blank=True)
    
    def __str__(self):
        return self.title
    
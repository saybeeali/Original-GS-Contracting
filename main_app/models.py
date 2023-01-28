from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Work(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="work")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    subject=models.TextField(max_length=100)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.name  

     
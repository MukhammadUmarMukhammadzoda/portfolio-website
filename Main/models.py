from django.db import models

# Create your models here.


class Skills(models.Model):
    title = models.CharField(max_length=30,null=True,blank=True)
    definition = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    
    
    
class DoneProjects(models.Model):
    url = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    
    
class Chronology(models.Model):
    date = models.CharField(max_length=30,null=True,blank=True)
    link = models.CharField(max_length=200,null=True,blank=True)
    defi = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.date + self.defi
# 

    
class Contact(models.Model):
    contact_link = models.CharField(max_length=200,null=True,blank=True)
    contact_name = models.CharField(max_length=500,null=True,blank=True)
    social = models.CharField(max_length=300,null=True,blank=True)
    
    def __str__(self):
        return self.contact_name

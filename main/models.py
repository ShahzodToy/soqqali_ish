from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(upload_to='portfolio')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class ClientFeedback(models.Model):
    name = models.CharField(max_length=120)
    company_name = models.CharField(max_length=120)
    comment = models.TextField()
    image = models.ImageField(upload_to='feedback')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    comment = models.TextField()
    is_checked = models.BooleanField(default=False)
    date= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='services')

    def __str__(self):
        return self.title
    

class Team(models.Model):
    full_name = models.CharField(max_length=120)
    bio = models.TextField()
    position = models.CharField(max_length=120)
    profile_image = models.ImageField(upload_to='profile_image')

    def __str__(self):
        return self.full_name

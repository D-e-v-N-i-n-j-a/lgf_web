from django.db import models

# Create your models here.


STATUS = (
    ("Completed","Completed"),
    ("In-progress","In-progress"),
)

class Team(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(null=True,blank=True,max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    img = models.ManyToManyField('Image', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField('Image', blank=True)
    
    def __str__(self) -> str:
        return f'{self.title}'
    

class Projects(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField()
    image = models.ManyToManyField('Image',blank=True)
    date_started = models.DateField()
    date_completed = models.DateField(blank=True,null=True)
    status = models.CharField(choices=STATUS,max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'{self.title} ~ {self.status}'


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    
    def __str__(self) -> str:
        return str(self.image)
    


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
     
    def __str__(self) -> str:
        return str(self.full_name)













from django.db import models
from django.contrib.auth.models import User


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
    summary = models.TextField(max_length=200)
    description = models.TextField()
    images = models.ManyToManyField('Image')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.title}'


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.full_name} on {self.blog.title}'

    

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ManyToManyField('Image',blank=True)
    date_started = models.DateField()
    date_completed = models.DateField(blank=True,null=True)
    status = models.CharField(choices=STATUS,max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'{self.title} ~ {self.status}'

    


class Metrics(models.Model):
    fund_raised = models.PositiveIntegerField(default=0)
    completed_projects = models.PositiveIntegerField(default=0)
    donations = models.PositiveIntegerField(default=0)
    volunteers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Metrics"

    class Meta:
        verbose_name_plural = "Metrics"


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    
    def __str__(self) -> str:
        return str(self.image)



class ContactFormSubmission(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class Donation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)














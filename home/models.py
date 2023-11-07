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
    img = models.ImageField(upload_to='team_images')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(f'{self.first_name}  {self.last_name}')


class BoardMembers(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(null=True,blank=True,max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(unique=True)
    img = models.ImageField(upload_to='team_images')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.first_name + " " + self.last_name)
    
    

class OurWork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='our_work_images')

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    person_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    testimonial_image = models.ImageField(upload_to='testimonial_images')  # Add this field

    def __str__(self):
        return self.person_name


class Cause(models.Model):
    image = models.ImageField(upload_to='causes_images')
    progress_percentage = models.PositiveIntegerField()
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=200)
    description = models.TextField()
    images = models.ImageField(upload_to='blog_image')
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




class PartnershipForm(models.Model):
    email = models.EmailField(max_length=255, verbose_name='Email')
    firstname = models.CharField(max_length=255, verbose_name='First Name')
    lastname = models.CharField(max_length=255, verbose_name='Last Name')
    organizations = models.CharField(max_length=255, verbose_name='Organizations')
    contact_number = models.CharField(max_length=20, verbose_name='Contact Number')
    country = models.CharField(max_length=255, verbose_name='Country')
    area_of_interest = models.CharField(max_length=255, verbose_name='Area of Interest')
    summary_of_proposed_partnership = models.TextField(verbose_name='Summary of Proposed Partnership', max_length=800)
    start_date = models.DateField(verbose_name='Start Date')
    finish_date = models.DateField(verbose_name='Finish Date')
    partnership_duration = models.CharField(max_length=255, verbose_name='Partnership Duration')
    sponsorship_amount = models.CharField(max_length=255, verbose_name='Sponsorship Amount')




class Fundraiser(models.Model):
    email = models.EmailField(max_length=255)
    firstname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255)
    area_of_interest = models.CharField(max_length=255, choices=[
        ('Charity of the Year partnership', 'Charity of the Year partnership'),
        ('Support a Project', 'Support a Project'),
        ('In-kind donations', 'In-kind donations'),
        ('Raise funds in memory of a loved one', 'Raise funds in memory of a loved one'),
        ('Cause-related marketing', 'Cause-related marketing'),
        ('Raise funds to celebrate a special occasion', 'Raise funds to celebrate a special occasion'),
    ])
    summary_of_proposed_partnership = models.TextField(max_length=800)
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    fundraising_amount = models.CharField(max_length=255, choices=[
        ('100', '100'),
        ('100-500', '100-500'),
        ('500-1000', '500-1000'),
        ('1000-3000', '1000-3000'),
    ])
    submission_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email  # You can change this to represent the model as you prefer






class Volunteers(models.Model):
    email = models.EmailField(max_length=255, verbose_name='Email')
    firstname = models.CharField(max_length=255, verbose_name='First Name')
    lastname = models.CharField(max_length=255, verbose_name='Last Name')
    contact_number = models.CharField(max_length=20, verbose_name='Contact Number')
    country = models.CharField(max_length=100, verbose_name='Country')
    summary_of_proposed_partnership = models.TextField(max_length=800, verbose_name='Summary of Proposed Partnership')

    def __str__(self):
        return f'{self.firstname} {self.lastname} ({self.email})'

    class Meta:
        verbose_name = 'Partnership Inquiry'
        verbose_name_plural = 'Partnership Inquiries'



class LibraryPictures(models.Model):
    picture = models.ImageField(upload_to='library_pictures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.picture)




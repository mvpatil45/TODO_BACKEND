from django.db import models

# Create your models here.
class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    STATUS_CHOICES=[
        ("INCOMPLETE","Incomplete"),
        ("COMPLETE","Complete")
    ]
    Task = models.CharField(max_length=100,blank=False,unique=True)
    Date= models.DateField(blank=False)
    Completed= models.CharField(max_length=10, choices=STATUS_CHOICES, default='INCOMPLETE')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    
    
    def __str__(self):
        return self.Task

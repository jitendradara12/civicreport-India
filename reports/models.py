from django.db import models
from django.contrib.auth.models import User

class InfrastructureReport(models.Model):
    ISSUE_TYPES = [
        ('POT', 'Pothole'),
        ('LIT', 'Street Light'),
        ('GRB', 'Garbage'),
        ('RD', 'Road Damage'),
        ('OTH', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('VER', 'Verified'),
        ('INP', 'In Progress'),
        ('RES', 'Resolved'),
        ('REJ', 'Rejected'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    issue_type = models.CharField(max_length=3, choices=ISSUE_TYPES)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_lng = models.DecimalField(max_digits=9, decimal_places=6)
    location_description = models.CharField(max_length=200)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='NEW')
    upvotes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.title} - {self.get_issue_type_display()}"

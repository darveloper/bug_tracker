from django.db import models
from accounts.models import User

class Ticket(models.Model):
    new = 'New'
    in_progress = 'In Progress'
    done = 'Done'
    invalid = 'Invalid'
    status_choices = [
        (new, 'New'),
        (in_progress, 'In Progress'),
        (done, 'Done'),
        (invalid, 'Invalid')
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=status_choices, default=new)
    filed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='filed_by', null=True, blank=True,)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_to', null=True, blank=True, default=None)
    completed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='completed_by', null=True, blank=True, default=None)

    def __str__(self):
        return self.title
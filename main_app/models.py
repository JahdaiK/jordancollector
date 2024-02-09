from django.db import models
from django.urls import reverse

ACTIONS =(
    ('c', 'Clean'),
    ('w', 'Wear')
)

# Create your models here.
class Jordan(models.Model):
    model = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    release_year = models.IntegerField()
    designer = models.CharField(max_length=100)
    materials = models.CharField(max_length=150)

#Changing this instance method does not impact the database therefore no make migrations is necessary
    def __str__(self) -> str:
        return f'{self.model} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'jordan_id': self.id})
    
class Task(models.Model):
    date = models.DateField('task date')
    action = models.CharField(
        max_length=1,
            choices=ACTIONS,
            default=ACTIONS[0][0]
        )
    
    jordan = models.ForeignKey(Jordan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_action_display()} on {self.date}"
    
    class Meta:
        ordering =['-date']
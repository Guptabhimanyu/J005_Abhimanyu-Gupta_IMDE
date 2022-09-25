from django.db import models   

class Task(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    start_date= models.DateField(null=True)
    end_date= models.DateField(null=True)
        
    def __str__(self):
        return self.name
    
    class Meta:
       verbose_name_plural = "Daily Task" 
       

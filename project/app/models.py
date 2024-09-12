from django.db import models

# declare a new model with a name "GeeksModel"
class AppModel(models.Model):
    token = models.CharField(max_length=65)
    public_key = models.CharField(max_length=100)
 
   
    def __str__(self):
        return self.title

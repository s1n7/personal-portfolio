from django.db import models

class Project(models.Model):    #inherit from model class
    title = models.CharField(max_length=100)        #information in documentation
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')    #all images uploaded to this folder
    url = models.URLField(blank=True)   #blank by default False

    def __str__(self):
        return self.title

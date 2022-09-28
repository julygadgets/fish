from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=50)  
    redirect_url = models.URLField(max_length=200)
    thumbnail = models.ImageField(upload_to="images")
    title = models.CharField(max_length=500)  
    description = models.CharField(max_length=500)  

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Info")

    def __str__(self):
        return self.name


 
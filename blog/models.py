from django.db import models


class Blog(models.Model):
    text= models.CharField(max_length=255)
    pub_date= models.DateTimeField()
    body= models.TextField()
    image=models.ImageField(upload_to="image/")



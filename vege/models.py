from django.db import models

class Receipe(models.Model):
  ReceipeName=models.CharField(max_length=100)
  Receipe_Descp=models.TextField()
  Receipe_Image=models.ImageField(upload_to="receipe")
from django.db import models

class Dam(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FishCount(models.Model):
    date = models.DateField()
    count = models.IntegerField(default=0)
    dam = models.ForeignKey(Dam, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.dam}"
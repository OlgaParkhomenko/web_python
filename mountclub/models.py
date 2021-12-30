from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class Country(models.Model):
    country = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)

    def __str__(self):
        return self.country


class Mountain(models.Model):
    title = models.CharField(max_length = 100)
    height = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class ClimbingEvent(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField()
    participants = models.ForeignKey(Participant, on_delete=models.CASCADE)
    mountain = models.OneToOneField(Mountain, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mountain} Climbing'





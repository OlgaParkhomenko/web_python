from django.db import models


class Patient(models.Model):
    sex_type = (('M', 'Male'),
                ('F', 'Female'))

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=sex_type)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    way_to_take = models.CharField(max_length=100)
    side_effects = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Examine(models.Model):
    places = (('P', 'At patient\'s place'),
              ('H', 'At hospital'))

    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    date = models.DateField()
    examination_place = models.CharField(max_length=100, choices=places, null=True, blank=False)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    prescription = models.ForeignKey(Medicine, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Examination of {self.patient} on {self.start_date}'

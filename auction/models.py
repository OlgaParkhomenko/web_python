from django.db import models


class Counterparty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Consignment(models.Model):
    date = models.DateField()
    seller = models.ForeignKey(Counterparty, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.counterparty} on {self.date}'


class Auction(models.Model):
    date_time = models.DateTimeField()
    place = models.CharField(max_length=100)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.date_time


class Lot(models.Model):
    lot_number = models.IntegerField()
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return self.lot_number


class Good(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    consignment = models.ForeignKey(Consignment, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Counterparty, on_delete=models.CASCADE, null=True)
    starting_price = models.IntegerField(null=True)
    final_price = models.IntegerField(null=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, null=True)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

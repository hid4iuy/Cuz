from django.db import models

class Politic(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    area = models.CharField(max_length=100)
    manifest = models.CharField(max_length=200)
    icon = models.ImageField(blank=True, null=True)

    def __str__(self):
        return '<Politics:id=' + str(self.id) +',' + self.name + '(' + self.party + ')>'

class Vote(models.Model):
    politicID = models.OneToOneField(Politic, on_delete=models.CASCADE)
    voteSum = models.IntegerField(default=0)

    # def __str__(self):
    #     return '<Vote:id=' + str(self.id) +',<Politic:id=' + str(self.politicID) + '(' + self.voteSum + ')>'
from django.db import models
class Sports(models.Model):
    name=models.CharField(max_length=150)
    category=models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Players(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField()
    sport=models.ForeignKey(Sports, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Matches(models.Model):
    sport=models.ForeignKey(Sports, on_delete=models.CASCADE)
    date=models.DateField()
    venue=models.CharField(max_length=150)
    teama=models.CharField(max_length=80)
    teamb=models.CharField(max_length=80)
    score=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.teama} vs {self.teamb}"
    
class Bookings(models.Model):
    username=models.CharField(max_length=150)
    match=models.ForeignKey(Matches, on_delete=models.CASCADE)
    bookingdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username 

from django.db import models
class Tip(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"${self.amount} - {self.date}"
# Create your models here.

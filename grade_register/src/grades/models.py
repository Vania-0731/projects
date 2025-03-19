from django.db import models

class Grade(models.Model):
    course = models.CharField(max_length=100)
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.course} - {self.grade}"

    @property
    def status(self):
        return "Approved" if self.grade >= 13 else "Failed"

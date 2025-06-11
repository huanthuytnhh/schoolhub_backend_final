# menu/models.py

from django.db import models

class Menu(models.Model):
    date = models.DateField(unique=True) # Each date should have only one menu
    imageUrl = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Menu for {self.date.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['-date'] # Order by most recent menu first

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.amount})"

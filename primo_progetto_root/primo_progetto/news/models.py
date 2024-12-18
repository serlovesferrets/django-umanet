from django.db import models

class Journalist(models.Model):
    """Modello di un giornalista"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Article(models.Model):
    """Modello di un articolo"""
    title = models.CharField(max_length=100)
    contents = models.TextField()
    journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return f"{self.title}"


from typing import TYPE_CHECKING
from django.db import models
if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager


class Journalist(models.Model):
    """Modello di un giornalista"""

    id: int
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    if TYPE_CHECKING:
        articles: RelatedManager["Article"]


class Article(models.Model):
    """Modello di un articolo"""

    id: int
    title = models.CharField(max_length=100)
    contents = models.TextField()
    journalist = models.ForeignKey[Journalist](
        Journalist, on_delete=models.CASCADE, related_name="articles"
    )

    def __str__(self):
        return f"{self.title}"

from django.db import models

class Section(models.Model):  # Bo'lim
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):  # Bob
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.section.title} - {self.title}"


class Article(models.Model):  # Modda
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="articles")
    number = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"Article {self.number} in {self.chapter.title}"

from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="projects")
    name = models.CharField(max_length=200, blank=True, null=True)
    video = models.FileField(upload_to="portfolio/media")
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category.name} - {self.video.url}"
    
    
    class Meta:
        verbose_name_plural = "Projects"
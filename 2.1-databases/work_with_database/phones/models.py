from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=40)
    price = models.FloatField(max_length=30)
    image = models.URLField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

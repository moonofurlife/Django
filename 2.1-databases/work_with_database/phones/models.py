from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='phones/')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
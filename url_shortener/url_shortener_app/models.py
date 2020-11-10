from django.db import models


class ShortUrl(models.Model):
    generated_value = models.CharField(primary_key=True, db_index=True, max_length=6, blank=False)
    actual_url = models.URLField(db_index=True, blank=False)

from django.db import models


class ParsingResult(models.Model):
    base_currency = models.TextField()
    currency_value = models.TextField(null=True)
    to_currency = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

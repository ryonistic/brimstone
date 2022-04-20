import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CaseInsensitiveFieldMixin:
    """
    Field mixin that uses case-insensitive lookup alternatives if they exist.
    """
    LOOKUP_CONVERSIONS = {
        'exact': 'iexact',
        'contains': 'icontains',
        'startswith': 'istartswith',
        'endswith': 'iendswith',
        'regex': 'iregex',
    }
    def get_lookup(self, lookup_name):
        converted = self.LOOKUP_CONVERSIONS.get(lookup_name, lookup_name)
        return super().get_lookup(converted)


class CICharField(CaseInsensitiveFieldMixin, models.CharField):
    pass

class CIEmailField(CaseInsensitiveFieldMixin, models.EmailField):
    pass


class User(AbstractUser):
    username = CICharField(unique=True, max_length=20)
    email = CIEmailField(unique=True,max_length=30)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_student = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

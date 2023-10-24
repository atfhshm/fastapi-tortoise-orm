from tortoise import models
from tortoise import fields

from enum import StrEnum

from .base import TimestampMixin

__all__ = ["User"]


class Role(StrEnum):
    USER = "USER"
    MEMBER = "MEMBER"
    ADMIN = "ADMIN"


class User(TimestampMixin):
    first_name = fields.CharField(max_length=32)
    last_name = fields.CharField(max_length=32)
    email = fields.CharField(max_length=132, unique=True)
    username = fields.CharField(max_length=64, unique=True)
    is_active = fields.BooleanField(default=True)
    role = fields.CharEnumField(Role, max_length=10)

    class Meta:
        table = "users"

    def __str__(self) -> str:
        return f"{self.email}"

# @Time : 10/7/23 1:56 PM
# @Author : HanyuLiu/Rainman
# @Email : rainman@ref.finance
# @File : models.py
from enum import Enum, IntEnum
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.postgres.fields import ArrayField
from tortoise.fields.base import CASCADE
from core.base.base_models import BaseDBModel, BaseCreatedUpdatedAtModel, BaseCreatedAtModel


class TestTable(BaseDBModel, BaseCreatedUpdatedAtModel):
    name =fields.CharField(max_length=10)
    age = fields.IntField()

    def __str__(self):
        return self.name

    class Meta:
        table = 'test_table'
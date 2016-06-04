# -*- coding: utf-8 -*-
from peewee import *

from app import db


class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = db

class Shop(BaseModel):
    description = TextField(db_column='описание', null=True)
    foto = IntegerField(db_column='фото_номер', index=True)
    level = CharField(db_column='раздел', null=True)
    name = CharField(db_column='Наименование', null=True, primary_key=True)
    price = FloatField(db_column='цена_на_сайте_с_ндс', null=True)
    sublevel = CharField(db_column='Подраздел', null=True)

    class Meta:
        db_table = 'shop'
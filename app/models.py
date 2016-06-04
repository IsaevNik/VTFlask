from peewee import *

from app import db


class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = db

class Shop(BaseModel):
    description = TextField(db_column='Description', null=True)
    foto = IntegerField(db_column='Foto', index=True)
    level = CharField(db_column='Level', null=True)
    name = CharField(db_column='Name', null=True, primary_key=True)
    price = FloatField(db_column='Price', null=True)
    sublevel = CharField(db_column='Sublevel', null=True)

    class Meta:
        db_table = 'shop'
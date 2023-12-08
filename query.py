from peewee import SqliteDatabase, Model, CharField, ForeignKeyField

db = SqliteDatabase('shopping-list.db')
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Category(BaseModel):
    name = CharField()

class Item(BaseModel):
    description = CharField()
    category = ForeignKeyField(Category, backref='items')

rows = Item.select()
for row in rows:
    print(row.description, row.category.name)

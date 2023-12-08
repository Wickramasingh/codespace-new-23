from peewee import SqliteDatabase
import database

# Connect to the database
db = SqliteDatabase('shopping-list.db')

# Drop and recreate tables using Peewee models
with db:
    db.drop_tables([database.Item, database.Category], safe=True)
    db.create_tables([database.Item, database.Category])

# Populate categories
categories_data = ['Fruits', 'Vegetables', 'Dairy', 'Meat']
for category_name in categories_data:
    database.Category.create(name=category_name)

# Populate items
items_data = [
    ('Apples', 'Fruits'),
    ('Broccoli', 'Vegetables'),
    ('Milk', 'Dairy'),
    ('Chicken', 'Meat'),
    ('Cheese', 'Dairy')
]
for item_description, category_name in items_data:
    category = database.Category.get(database.Category.name == category_name)
    database.Item.create(description=item_description, category=category)

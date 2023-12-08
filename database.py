from peewee import *

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

def setup_database():
    db.create_tables([Category, Item], safe=True)

    # Populate categories
    categories_data = ['Fruits', 'Vegetables', 'Dairy', 'Meat']
    for category_name in categories_data:
        Category.create(name=category_name)

    # Populate items
    items_data = [
        ('Apples', 'Fruits'),
        ('Broccoli', 'Vegetables'),
        ('Milk', 'Dairy'),
        ('Chicken', 'Meat'),
        ('Cheese', 'Dairy')
    ]
    for item_description, category_name in items_data:
        category = Category.get(Category.name == category_name)
        Item.create(description=item_description, category=category)

def get_items():
    items = Item.select()
    items = [
        {
            "id": item.id,
            "description": item.description,
            "category": item.category.name
        }
        for item in items
    ]
    return items

def get_item_by_id(id):
    try:
        item = Item.get(Item.id == id)
        return {"id": item.id, "description": item.description, "category": item.category.name}
    except DoesNotExist:
        return None

def add_item(description, category):
    category_obj = Category.get(Category.name == category)
    item = Item.create(description=description, category=category_obj)

def update_item(id, description, category):
    item = Item.get(Item.id == id)
    category_obj = Category.get(Category.name == category)
    item.description = description
    item.category = category_obj
    item.save()

def delete_item(id):
    item = Item.get(Item.id == id)
    item.delete_instance()

def get_categories():
    categories = Category.select()
    return [category.name for category in categories]

def search_items(query):
    # Search for items containing the query in the description or category
    query = query.lower()  # Convert the query to lowercase
    items = Item.select().where(
        (fn.Lower(Item.description).contains(query)) | (fn.Lower(Item.category.name).contains(query))
    )
    items = [
        {
            "id": item.id,
            "description": item.description,
            "category": item.category.name,
        }
        for item in items
    ]
    return items

# Additional testing functions (if needed)
def test_setup_database():
    setup_database()
    items = get_items()
    assert len(items) == 5
    print("Database setup and populated successfully.")

if __name__ == "__main__":
    test_setup_database()

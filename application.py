from bottle import route, run, template, request, redirect, post
import database

@route("/")
def get_index():
    search_query = request.query.get('query', '').strip()
    items = database.get_items()
    return template("views/list.tpl", shopping_list=items, search_query=search_query)


@route("/list")
def get_list():
    query = request.query.get('query', '').strip()
    if query:
        # If a search query is provided, redirect to the search route
        redirect(f"/search?query={query}")
    else:
        # Otherwise, display the regular list
        rows = database.get_items()
        return template("views/list.tpl", shopping_list=rows, search_query=query)

@route("/add")
def get_add():
    categories = database.get_categories()
    return template("views/add_item.tpl", categories=categories)

@route("/edit/<id>")
def get_edit(id):
    item = database.get_item_by_id(id)
    if item:
        categories = database.get_categories()
        return template("views/update_item.tpl", item=item, categories=categories)
    else:
        redirect("/")

@post("/add")
def post_add():
    description = request.forms.get("description")
    category = request.forms.get("category")
    database.add_item(description, category)
    redirect("/")

@post("/update")
def post_update():
    id = request.forms.get("id")
    description = request.forms.get("description")
    category = request.forms.get("category")
    database.update_item(id, description, category)
    redirect("/")

@route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect("/")

@route("/search")
def get_search():
    query = request.query.get('query', '').strip()
    if query:
        # Modify the query to search for items containing the search term
        rows = database.search_items(query)
    else:
        # If no search term provided, show all items
        rows = database.get_items()

    return template("views/list.tpl", shopping_list=rows, search_query=query)

def setup():
    database.setup_database()

if __name__ == "__main__":
    setup()
    run(host='localhost', port=8080)

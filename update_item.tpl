<html>
<body>
  <h2>Update Item</h2>
  <hr/>
  <form action="/update" method="post">
    <input type="hidden" name="id" value="{{ item['id'] }}"/>
    <p>Description: <input name="description" value="{{ item['description'] }}"/></p>
    <p>Category:
      <select name="category">
        % for category in categories:
          <option value="{{ category }}" % if category == item['category']: selected % end>{{ category }}</option>
        % end
      </select>
    </p>
    <p><button type="submit">Submit</button></p>
  </form>
  <hr/>
</body>
</html>

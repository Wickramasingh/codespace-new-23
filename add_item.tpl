<html>
<body>
  <h2>Add Item</h2>
  <hr/>
  <form action="/add" method="post">
    <p>Description: <input name="description"/></p>
    <p>Category:
      <select name="category">
        % for category in categories:
          <option value="{{ category }}">{{ category }}</option>
        % end
      </select>
    </p>
    <p><button type="submit">Submit</button></p>
  </form>
  <hr/>
</body>
</html>

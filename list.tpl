<html>
<body>
  <h2>Shopping List</h2>
  <hr/>
  <form action="/list" method="get">
    <p>Search: <input name="query" type="text" value="{{ search_query }}"/></p>
    <p><button type="submit">Search</button></p>
  </form>
  <table>
    <tr>
      <th>Description</th>
      <th>Category</th>
      <th>Action</th>
    </tr>
    % for item in shopping_list:
      <tr>
        <td>{{ item['description'] }}</td>
        <td>{{ item['category'] }}</td>
        <td>
          <a href="/edit/{{ item['id'] }}">Edit</a> |
          <a href="/delete/{{ item['id'] }}">Delete</a>
        </td>
      </tr>
    % end
  </table>
  <hr/>
  <a href="/add">Add new item</a>
</body>
</html>

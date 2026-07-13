## Tipos de datos admitidos {#supported-data-types}

Se admiten los siguientes tipos de datos:

<table aria-label="Tipos de datos admitidos">
  <thead>
    <tr>
      <th>Tipo de datos</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Número</td>
      <td>Un valor numérico, como <code>1</code> o <code>5.5</code>.</td>
    </tr>
    <tr>
      <td>Cadena</td>
      <td>Un valor de texto, como <code>"Hello"</code> o <code>"The Hobbit"</code>.</td>
    </tr>
    <tr>
      <td>Booleano</td>
      <td>Un valor que se evalúa como <code>true</code> o <code>false</code>.</td>
    </tr>
    <tr>
      <td>Matriz</td>
      <td>Una lista de valores, como <code>["red", "blue", "green"]</code>.</td>
    </tr>
    <tr>
      <td>Tiempo</td>
      <td>
        Un valor de marca de tiempo utilizado para comparaciones de fecha y hora. Al filtrar un atributo personalizado anidado de tiempo, puedes elegir:<br><br>
        <ul>
          <li><strong>Day of Year</strong>: comprueba solo el mes y el día para comparar, por ejemplo <code>03-15</code>.</li>
          <li><strong>Time</strong>: compara la marca de tiempo completa, incluido el año, por ejemplo <code>2023-03-15T12:00:00Z</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Objeto</td>
      <td>Un valor estructurado con pares clave-valor, como <code>{"author": "Tolkien"}</code>.</td>
    </tr>
    <tr>
      <td>Matriz de objetos</td>
      <td>
        Una lista de objetos, como <code>[{"title": "The Hobbit"}, {"title": "Dune"}]</code>.
        Para más información, consulta
        <a href="{{site.baseurl}}/array_of_objects/">Matrices de objetos</a>.
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de datos admitidos" }
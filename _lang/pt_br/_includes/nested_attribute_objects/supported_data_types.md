## Tipos de dados suportados {#supported-data-types}

Os seguintes tipos de dados são suportados:

<table aria-label="Tipos de dados suportados">
  <thead>
    <tr>
      <th>Tipo de dados</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Número</td>
      <td>Um valor numérico, como <code>1</code> ou <code>5.5</code>.</td>
    </tr>
    <tr>
      <td>String</td>
      <td>Um valor de texto, como <code>"Hello"</code> ou <code>"The Hobbit"</code>.</td>
    </tr>
    <tr>
      <td>booleano</td>
      <td>Um valor que é avaliado como <code>true</code> ou <code>false</code>.</td>
    </tr>
    <tr>
      <td>Array</td>
      <td>Uma lista de valores, como <code>["red", "blue", "green"]</code>.</td>
    </tr>
    <tr>
      <td>Horário</td>
      <td>
        Um valor de timestamp usado para comparações de data e hora. Ao filtrar um atributo personalizado de tempo aninhado, você pode escolher:<br><br>
        <ul>
          <li><strong>Day of Year</strong>: Verifica apenas o mês e o dia para comparação, como <code>03-15</code>.</li>
          <li><strong>Time</strong>: Compara o timestamp completo, incluindo o ano, como <code>2023-03-15T12:00:00Z</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Objeto</td>
      <td>Um valor estruturado com pares de chave-valor, como <code>{"author": "Tolkien"}</code>.</td>
    </tr>
    <tr>
      <td>Array de objetos</td>
      <td>
        Uma lista de objetos, como <code>[{"title": "The Hobbit"}, {"title": "Dune"}]</code>.
        Para saber mais, consulte
        <a href="{{site.baseurl}}/array_of_objects/">Arrays de objetos</a>.
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de dados suportados" }
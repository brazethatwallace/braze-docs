## Types de données pris en charge {#supported-data-types}

Les types de données suivants sont pris en charge :

<table aria-label="Types de données pris en charge">
  <thead>
    <tr>
      <th>Type de données</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Nombre</td>
      <td>Une valeur numérique, telle que <code>1</code> ou <code>5.5</code>.</td>
    </tr>
    <tr>
      <td>Chaîne de caractères</td>
      <td>Une valeur textuelle, telle que <code>"Hello"</code> ou <code>"The Hobbit"</code>.</td>
    </tr>
    <tr>
      <td>Valeur booléenne</td>
      <td>Une valeur qui s'évalue à <code>true</code> ou <code>false</code>.</td>
    </tr>
    <tr>
      <td>Tableau</td>
      <td>Une liste de valeurs, telle que <code>["red", "blue", "green"]</code>.</td>
    </tr>
    <tr>
      <td>Horodatage</td>
      <td>
        Une valeur d'horodatage utilisée pour les comparaisons de date et d'heure. Lors du filtrage d'un attribut personnalisé de type temps imbriqué, vous pouvez choisir :<br><br>
        <ul>
          <li><strong>Day of Year</strong> : ne vérifie que le mois et le jour à des fins de comparaison, par exemple <code>03-15</code>.</li>
          <li><strong>Time</strong> : compare l'horodatage complet, y compris l'année, par exemple <code>2023-03-15T12:00:00Z</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Objet</td>
      <td>Une valeur structurée avec des paires clé–valeur, telle que <code>{"author": "Tolkien"}</code>.</td>
    </tr>
    <tr>
      <td>Tableau d'objets</td>
      <td>
        Une liste d'objets, telle que <code>[{"title": "The Hobbit"}, {"title": "Dune"}]</code>.
        Pour plus d'informations, consultez la section
        <a href="{{site.baseurl}}/array_of_objects/">Tableaux d'objets</a>.
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="Types de données pris en charge" }
## Unterstützte Datentypen {#supported-data-types}

Die folgenden Datentypen werden unterstützt:

<table aria-label="Unterstützte Datentypen">
  <thead>
    <tr>
      <th>Datentyp</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Zahl</td>
      <td>Ein numerischer Wert, wie z. B. <code>1</code> oder <code>5.5</code>.</td>
    </tr>
    <tr>
      <td>String</td>
      <td>Ein Textwert, wie z. B. <code>"Hello"</code> oder <code>"The Hobbit"</code>.</td>
    </tr>
    <tr>
      <td>Boolescher Wert</td>
      <td>Ein Wert, der entweder zu <code>true</code> oder <code>false</code> ausgewertet wird.</td>
    </tr>
    <tr>
      <td>Array</td>
      <td>Eine Liste von Werten, wie z. B. <code>["red", "blue", "green"]</code>.</td>
    </tr>
    <tr>
      <td>Zeit</td>
      <td>
        Ein Zeitstempelwert, der für Datums- und Zeitvergleiche verwendet wird. Beim Filtern eines verschachtelten angepassten Zeitattributs können Sie wählen:<br><br>
        <ul>
          <li><strong>Day of Year</strong>: Prüft nur den Monat und den Tag zum Vergleich, z. B. <code>03-15</code>.</li>
          <li><strong>Time</strong>: Vergleicht den vollständigen Zeitstempel einschließlich des Jahres, z. B. <code>2023-03-15T12:00:00Z</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Objekt</td>
      <td>Ein strukturierter Wert mit Schlüssel-Wert-Paaren, wie z. B. <code>{"author": "Tolkien"}</code>.</td>
    </tr>
    <tr>
      <td>Array von Objekten</td>
      <td>
        Eine Liste von Objekten, wie z. B. <code>[{"title": "The Hobbit"}, {"title": "Dune"}]</code>.
        Weitere Informationen finden Sie unter
        <a href="{{site.baseurl}}/array_of_objects/">Arrays von Objekten</a>.
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unterstützte Datentypen" }
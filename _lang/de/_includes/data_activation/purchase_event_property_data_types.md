Die `properties`-Werte müssen ein Objekt von bis zu 50&nbsp;KB sein, wobei die Schlüssel die Eigenschaftsnamen und die Werte die Eigenschaftswerte sind. Eigenschaftsnamen müssen Strings mit maximal 255 Zeichen sein und dürfen kein vorangestelltes Dollarzeichen (`$`) enthalten.

Eigenschaftswerte können einen der folgenden Datentypen haben:

| Datentyp | Beschreibung |
| --- | --- |
| Zahl | Integer oder Gleitkommazahl |
| Boolescher Wert | Wert `true` oder `false` |
| Datetime | String im [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)- oder `yyyy-MM-dd'T'HH:mm:ss:SSSZ`-Format. Innerhalb von Arrays nicht unterstützt. |
| String | Maximal 255 Zeichen |
| Array | Unterstützt; Datetimes werden innerhalb von Arrays nicht unterstützt. |
| Objekt | Werden als Strings aufgenommen (keine verschachtelten Objekte). Verwenden Sie für verschachtelte Daten einen String-Wert (z.&nbsp;B. JSON-serialisiert). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

Die folgenden Schlüssel sind reserviert und können nicht als Eigenschaftsnamen verwendet werden: `time`, `product_id`, `quantity`, `event_name`, `price` und `currency`. Die Verwendung eines reservierten Schlüssels im `properties`-Objekt gibt den Fehler „Ungültiges ‚properties'-Feld“ zurück.
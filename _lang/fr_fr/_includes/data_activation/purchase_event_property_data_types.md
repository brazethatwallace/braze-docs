Les valeurs de `properties` doivent être un objet de 50&nbsp;Ko maximum, où les clés sont les noms des propriétés et les valeurs sont les valeurs des propriétés. Les noms de propriétés doivent être des chaînes de caractères de 255 caractères ou moins, sans signe dollar (`$`) en début de nom.

Les valeurs de propriétés peuvent être de l'un des types de données suivants :

| Type de données | Description |
| --- | --- |
| Nombre | Entier ou float |
| Valeur booléenne | Valeur `true` ou `false` |
| Date et heure | Chaîne de caractères au format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Non pris en charge dans les tableaux. |
| Chaîne de caractères | 255 caractères ou moins |
| Tableau | Pris en charge ; les dates et heures ne sont pas prises en charge dans les tableaux. |
| Objet | Ingéré en tant que chaînes de caractères (pas d'objets imbriqués). Pour les données imbriquées, utilisez une valeur de chaîne de caractères (par exemple, sérialisée en JSON). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme noms de propriétés : `time`, `product_id`, `quantity`, `event_name`, `price` et `currency`. L'utilisation d'une clé réservée dans l'objet `properties` renvoie l'erreur « Invalid 'properties' field ».
Os valores de `properties` devem ser um objeto de até 50&nbsp;KB, em que as chaves são os nomes das propriedades e os valores são os valores das propriedades. Os nomes das propriedades devem ser strings com 255 caracteres ou menos, sem cifrão (`$`) no início.

Os valores das propriedades podem ser qualquer um dos seguintes tipos de dados:

| Tipo de dado | Descrição |
| --- | --- |
| Número | Inteiro ou float |
| Booleano | Valor `true` ou `false` |
| Datetime | String no formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Não compatível com arrays. |
| String | 255 caracteres ou menos |
| Array | Compatível; datetimes não são compatíveis com arrays. |
| Objeto | Processado como strings (não como objetos aninhados). Para dados aninhados, use um valor da string (por exemplo, JSON serializado). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Table" }

As seguintes chaves são reservadas e não podem ser usadas como nomes de propriedades: `time`, `product_id`, `quantity`, `event_name`, `price` e `currency`. Usar uma chave reservada no objeto `properties` retorna o erro "Invalid 'properties' field".
{% alert note %}
**Entendendo os campos de data:**
- `TIME` e `TIME_MS`: Representam o momento em que a atualização do Perfil de usuário ocorreu na Braze (em segundos e milissegundos, respectivamente). Para dados preenchidos retroativamente, esses valores correspondem ao momento do preenchimento retroativo.
- `SF_UPDATED_AT`: Representa o momento em que os dados foram persistidos pela última vez no Snowflake. Esse campo é mais útil para determinar a atualidade dos dados — ou seja, quando a linha foi sincronizada mais recentemente com o seu data warehouse.
{% endalert %}
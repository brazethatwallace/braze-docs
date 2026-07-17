{% alert note %}
Para mensagens RCS, o encurtamento de links e o rastreamento de cliques no nível da URL são compatíveis com URLs no corpo da mensagem, mas não com URLs em ações sugeridas. Cliques em URLs de ações sugeridas são registrados como eventos de clique RCS, mas os campos `URL` e `SHORT_URL` serão nulos no Currents e no Snowflake.
{% endalert %}
{% alert note %}
**Descripción de los campos de fecha:**
- `TIME` y `TIME_MS`: Representan el momento en que se produjo la actualización del perfil de usuario en Braze (en segundos y milisegundos, respectivamente). Para los datos rellenados retroactivamente, estos valores corresponden al momento del relleno retroactivo.
- `SF_UPDATED_AT`: Representa el momento en que los datos se guardaron por última vez en Snowflake. Este campo es muy útil para determinar la actualidad de los datos, es decir, el momento en que la fila se sincronizó más recientemente con tu almacén de datos.
{% endalert %}
---
nav_title: Census
article_title: Census
description: "Este artículo de referencia describe la asociación entre Braze y Census, una plataforma de integración de datos que te permite crear dinámicamente segmentos de usuarios específicos con datos de tu almacén en la nube."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census](https://www.getcensus.com/) es una plataforma de activación de datos que conecta almacenes de datos en la nube como Snowflake y BigQuery con Braze. Los equipos de marketing pueden liberar la potencia de sus datos propios para crear segmentos de audiencia dinámicos, sincronizar los atributos de los clientes para personalizar campañas y mantener actualizados todos sus datos en Braze. Ahora es más fácil que nunca actuar con datos fiables y procesables, sin necesidad de cargar archivos CSV ni hacer favores de ingeniería.

La integración de Braze y Census te permite importar dinámicamente audiencias o datos de productos a Braze para enviar campañas personalizadas. Por ejemplo, puedes crear una cohorte en Braze para "Suscriptores de boletines con valor del ciclo de vida del cliente > 1000" para dirigirte a clientes de alto valor o "Usuarios activos en los últimos 30 días" para dirigirte a usuarios específicos y probar una próxima función beta.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de Census | Se requiere una [cuenta de Census](https://www.getcensus.com/) para aprovechar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con todos los permisos de datos de usuario (excepto `users.delete`) y permisos de `segments.list`. El conjunto de permisos puede cambiar a medida que Census añada compatibilidad con más objetos de Braze, por lo que es posible que desees conceder más permisos ahora o planificar la actualización de estos permisos en el futuro. <br><br> Puedes crearla en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST de Braze | La URL de tu endpoint REST. Tu endpoint dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
| Almacén de datos y modelo de datos | Antes de iniciar la integración, debes tener un almacén de datos configurado en Census y definir un modelo del subconjunto de datos que deseas sincronizar con Braze. Visita la [documentación de Census](https://docs.getcensus.com/destinations/braze) para consultar una lista de orígenes de datos disponibles y orientación sobre la creación de modelos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear una conexión de servicio Braze {#step-1-create-braze-service-connection}

Para integrar Census en la plataforma Census, ve a la pestaña **Connections** y selecciona **New Destination** para crear una nueva conexión de servicio Braze.

En la ventana que aparece, asigna un nombre a esta conexión e indica la URL de tu endpoint de Braze y la clave de API REST de Braze (y, opcionalmente, tu clave de importación de datos para sincronizar cohortes).

![Diálogo de nuevo destino de Census configurado con las credenciales de conexión de Braze.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Paso 2: Crear una sincronización de Census {#step-2-create-a-census-sync}

Para sincronizar clientes con Braze, debes crear una sincronización. Aquí definirás dónde sincronizar los datos y cómo quieres que se mapeen los campos entre las dos plataformas.

1. Ve a la pestaña **Syncs** y selecciona **New Sync**.<br><br>
2. En el creador, selecciona el modelo de datos de origen de tu almacén de datos.<br><br>
3. Configura dónde se sincronizará el modelo. Selecciona **Braze** como destino y el [tipo de objeto compatible](#supported-objects) para sincronizar.<br>![En la ventana "Select a Destination", "Braze" está seleccionado como la conexión, y se enumeran varios objetos.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Selecciona qué regla de sincronización quieres aplicar (**Update or Create** es la opción más común, pero puedes elegir reglas más avanzadas para manejar la eliminación de datos, por ejemplo).<br><br>
5. A continuación, para fines de coincidencia de registros, elige una clave de sincronización para [mapear](#supported-objects) tu objeto de Braze con un campo del modelo.<br>![En la ventana "Select a Sync Key", "External User ID" de Braze se relaciona con "user_id" en el origen.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. Por último, mapea los campos de datos de Census con los campos equivalentes de Braze.<br>![Mapeado de Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. Confirma los detalles y crea la sincronización.

Una vez ejecutada la sincronización, los datos de usuario estarán en Braze. Puedes crear y añadir un Segment de Braze a futuras Campaigns y Canvas de Braze para dirigirte a estos usuarios.

{% alert note %}
Al usar la integración de Census y Braze, Census solo envía los deltas (datos que cambian) en cada sincronización a Braze.
{% endalert %}

## Objetos compatibles {#supported-objects}

Census actualmente permite la sincronización de los siguientes objetos de Braze:

| Nombre del objeto | Comportamientos de sincronización |
| --- | --- |
| User | Update, Create, Mirror, Delete |
| Cohort | Update, Create, Mirror |
| Catalog | Update, Create, Mirror |
| Subscription Group Membership | Mirror |
| Event | Append |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objetos compatibles" }

Además, Census permite enviar [datos estructurados](https://docs.getcensus.com/destinations/braze#supported-objects) a Braze. Para enviar tokens de notificaciones push de usuario, tus datos deben estar estructurados como un arreglo de objetos con 2-3 valores: `app_id`, `token` y un `device_id` opcional.
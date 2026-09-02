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
| Cuenta Census | Se necesita una [cuenta en Census](https://www.getcensus.com/) para aprovechar esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con todos los permisos de datos de usuario (excepto `users.delete`) y permisos de `segments.list`. El conjunto de permisos puede cambiar a medida que Census añada compatibilidad con más objetos de Braze, por lo que es posible que quieras conceder más permisos ahora o planificar la actualización de estos permisos en el futuro. <br><br> Puedes crearla en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST or transferencia de estado representacional de Braze | La URL de tu endpoint REST or transferencia de estado representacional. Tu endpoint dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). |
| Almacén de datos y modelo de datos | Antes de comenzar la integración, debes tener un almacén de datos configurado en Census y definir un modelo del subconjunto de datos que deseas sincronizar con Braze. Visita la [documentación de Census](https://docs.getcensus.com/destinations/braze) para obtener una lista de los orígenes de datos disponibles y orientación sobre la creación de modelos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear conexión de servicio Braze {#step-1-create-braze-service-connection}

Para integrar Census en la plataforma Census, ve a la pestaña **Conexiones** y selecciona **Nuevo destino** para crear una nueva conexión de servicio Braze.

En la ventana que aparece, asigna un nombre a esta conexión e indica la URL de tu endpoint de Braze y la clave de API REST or transferencia de estado representacional de Braze (y, opcionalmente, tu clave de importación de datos para sincronizar cohortes).

![Diálogo de nuevo destino de Census configurado para las credenciales de conexión de Braze.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Paso 2: Crear una sincronización de Census {#step-2-create-a-census-sync}

Para sincronizar clientes con Braze, debes crear una sincronización. Aquí definirás dónde sincronizar los datos y cómo deseas que se mapeen los campos entre las dos plataformas.

1. Ve a la pestaña **Sincronizaciones** y selecciona **Nueva sincronización**.<br><br>
2. En el creador, selecciona el modelo de datos fuente de tu almacén de datos.<br><br>
3. Configura dónde se sincronizará el modelo. Selecciona **Braze** como destino y el [tipo de objeto compatible](#supported-objects) que deseas sincronizar.<br>![En la ventana "Selecciona un destino", se selecciona "Braze" como conexión y se enumeran varios objetos.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Selecciona qué regla de sincronización deseas aplicar (**Actualizar o Crear** es la opción más común, pero puedes elegir reglas más avanzadas para gestionar la eliminación de datos, por ejemplo).<br><br>
5. A continuación, para la coincidencia de registros, elige una clave de sincronización para [mapear](#supported-objects) tu objeto de Braze a un campo del modelo.<br>![En la ventana "Selecciona una clave de sincronización", el "ID de usuario externo" de Braze coincide con "user_id" en la fuente.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. Por último, mapea los campos de datos de Census a los campos equivalentes de Braze.<br>![Mapeado de Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. Confirma los detalles y crea la sincronización.

Una vez ejecutada la sincronización, encontrarás los datos del usuario en Braze. Ahora puedes crear y añadir un segmento de Braze a futuras Campaigns y Canvas de Braze para dirigirte a estos usuarios.

{% alert note %}
Al utilizar la integración de Census y Braze, Census solo enviará los deltas (datos que cambian) en cada sincronización a Braze.
{% endalert %}

## Objetos compatibles {#supported-objects}

Census admite actualmente la sincronización de los siguientes objetos de Braze:

| Nombre del objeto | Comportamientos de sincronización |
| --- | --- |
| Usuario | Actualizar, Crear, Reflejar, Eliminar |
| Cohorte | Actualizar, Crear, Reflejar |
| Catálogo | Actualizar, Crear, Reflejar |
| Pertenencia a un grupo de suscripción | Reflejar |
| Evento | Añadir |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objetos compatibles" }

Además, Census admite el envío de [datos estructurados](https://docs.getcensus.com/destinations/braze#supported-objects) a Braze:
- Tokens de notificaciones push de usuario: para enviar tokens de notificaciones push, tus datos deben estructurarse como un arreglo de objetos con 2-3 valores: `app_id`, `token` y un `device_id` opcional.
- Atributos personalizados anidados: se admiten tanto objetos como arreglos. A partir de abril de 2022, esta característica todavía está en acceso anticipado. Es posible que tengas que ponerte en contacto con tu director de cuentas de Braze para obtener acceso.
---
nav_title: Treasure Data
article_title: Treasure Data
description: "Este artículo de referencia describe la asociación entre Braze y Treasure Data, una plataforma de datos de clientes empresariales que te permite escribir resultados de trabajos directamente en Braze."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# Treasure Data

> [Treasure Data](https://www.treasuredata.com/) es una plataforma de datos de clientes (CDP or plataforma de datos de los clientes) que recopila y encamina información de múltiples fuentes a una variedad de otras ubicaciones en tu stack de marketing.

La integración de Braze y Treasure Data te permite escribir los resultados de los trabajos de Treasure Data directamente en Braze, lo que te permite:
* **Asignar ID externos**: Asigna ID a la cuenta de usuario de Braze desde tu sistema CRM or administración de las relaciones con el cliente.
* **Gestionar la exclusión voluntaria**: Cuando un usuario final actualiza su consentimiento eligiendo no participar.
* **Cargar tu seguimiento de eventos, compras o atributos de perfil personalizados**. Esta información puede ayudarte a crear segmentos de clientes precisos que mejoren la experiencia del usuario en tus campañas.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta de Treasure Data | Se necesita una [cuenta de Treasure Data](https://www.treasuredata.com/custom-demo/) para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`, `users.delete`, `users.alias.new`, `users.identify`.<br><br>Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST or transferencia de estado representacional de Braze | La URL de tu endpoint REST or transferencia de estado representacional. Tu endpoint dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

Puedes sincronizar tus perfiles de cliente consolidados de Treasure Data en Braze para crear segmentos objetivo. Treasure Data admite datos de cookies propios, ID de móviles, sistemas de terceros como tu CRM or administración de las relaciones con el cliente, y muchos más.

## Integración {#integration}

### Paso 1: Crear una nueva conexión {#step-1-create-a-new-connection}

En Treasure Data, ve al **Catalog** en el **Integrations Hub** y busca y selecciona **Braze**.

En el mensaje **New Authentication** que aparece, asigna un nombre a la conexión e indica tu clave de API REST or transferencia de estado representacional de Braze y el endpoint REST or transferencia de estado representacional. Selecciona **Done** cuando hayas terminado.

![Formulario de autenticación de Braze en Treasure Data con campos de clave de API REST y endpoint.]({% image_buster /assets/img/treasure_data/braze_authentication.png %}){: style="max-width:80%;"}

### Paso 2: Definir tu consulta {#step-2-define-your-query}

En Treasure Data, ve a **Queries** en tu **Data Workbench** y selecciona una consulta cuyos datos quieras exportar. Ejecuta esta consulta para validar el conjunto de resultados.

{% alert note %}
Para los usuarios que utilicen HIVE para crear consultas, HIVE requiere que cualquier columna o tabla que comience con un guion bajo vaya entre comillas invertidas. Por ejemplo, `_merge_objects`.
{% endalert %}

A continuación, selecciona **Export Results** y selecciona una autenticación de integración existente.

![Página de resultados de consulta de Treasure Data con Export Results y la integración de Braze seleccionada.]({% image_buster /assets/img/treasure_data/query_2.png %}){: style="max-width:80%;"}

Define parámetros adicionales de exportación de resultados como se indica en la siguiente [sección de personalización](#customization). En el contenido de tu integración de exportación, revisa los parámetros de integración.

![La página "Export Results". En esta página hay campos para "mode", "track record type" y "pre-formatted fields". Para este ejemplo, "User-Track" y "Custom Events" se establecen en estos campos, respectivamente.]({% image_buster /assets/img/treasure_data/braze_export_configuration.png %}){: style="max-width:80%;"}

Por último, selecciona **Done**, ejecuta tu consulta y comprueba que los datos se han transferido a Braze.

### Personalización {#customization}

Los parámetros de los resultados de exportación se incluyen en la siguiente tabla:

| Parámetro | Valores | Descripción |
|---------------------------|---|---|
| `mode` | User - New Alias<br>User - Identifying<br>User - Track<br>User - Delete | Modo del conector |
| `pre_formatted_fields` | Cadena | Usar para columnas de tipo array o JSON para mantener el formato. |
| `track_record_type` | Custom Events<br>Purchases<br>User Profile Attributes | Tipo de registro para el modo **User - Track** |
| `skip_on_invalid_records` | Booleano | Si está habilitado, continúa e ignora cualquier registro no válido para la columna JSON. <br> De lo contrario, el trabajo se detiene. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Personalización" }

{% alert note %}
Visita [Treasure Data](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration) para obtener más información sobre campos preformateados, consultas de ejemplo, detalles de parámetros y programación de trabajos de exportación de consultas.
{% endalert %}

## Webhooks

Los usuarios de Treasure Data pueden ingerir datos a través de la REST or transferencia de estado representacional API pública. Puedes utilizar Treasure Data para crear webhooks personalizados en tus datos. Para más información, visita [Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API)
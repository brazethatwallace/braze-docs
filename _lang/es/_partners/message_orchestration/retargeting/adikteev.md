---
nav_title: Adikteev
article_title: Predicción de abandono Adikteev
description: "Este artículo de referencia describe la asociación entre Braze y Adikteev, un motor de retención de usuarios que combina la predicción del abandono con servicios integrales de reorientación de aplicaciones."
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Predicción de abandono Adikteev {#adikteev-churn-prediction}

> [Adikteev](https://www.adikteev.com/churn-prediction) es un motor de retención de usuarios que combina la predicción del abandono con servicios integrales de reorientación de aplicaciones.

_Esta integración está mantenida por Adikteev._

## Sobre la integración {#about-the-integration}

La integración de Braze y Adikteev te permite impulsar la retención de usuarios aprovechando la tecnología de predicción del abandono de Adikteev dentro de las Campaigns de CRM or administración de las relaciones con el cliente de Braze para dirigirte prioritariamente a los segmentos de usuarios de alto riesgo.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta Adikteev | Se necesita una cuenta Adikteev para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con el permiso `users.track`. <br><br> Se puede crear en el panel de Braze desde **Settings** > **APIs and Identifiers**. |
| Punto de conexión REST or transferencia de estado representacional de Braze | [La URL de tu punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

{% tabs %}
{% tab Audience filtering %}
Refinamiento de tus segmentos de audiencia en función del riesgo de abandono.<br> Los nombres y valores de los atributos personalizados enviados por Adikteev son configurables.

![Captura de pantalla que muestra un ejemplo de cómo utilizar un atributo personalizado enviado por Adikteev como filtro de segmento de audiencia.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab Message targeting %}
Personalización de tus Campaigns de mensajería de Braze en función del riesgo de abandono de los destinatarios.

![Captura de pantalla que muestra un ejemplo de cómo utilizar un atributo personalizado enviado por Adikteev como filtro de segmentación de campaña.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## Integración {#integration}

### Paso 1: Comparte el flujo de eventos de tu aplicación {#step-1-share-the-event-stream-of-your-app}

Para empezar a ejecutar la predicción de abandono en la audiencia de tu aplicación, Adikteev necesitará que actives los postbacks de eventos desde tu plataforma de medición móvil. Sigue las instrucciones del [sitio web de soporte de Adikteev](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation) para configurarlo.

### Paso 2: Crea tu clave de API REST or transferencia de estado representacional de Braze {#step-2-create-your-braze-rest-api-key}

En Braze, ve a **Settings** > **APIs and Identifiers**. Selecciona **Create New API Key**, introduce el nombre de la clave de API que prefieras y asegúrate de que se añade el siguiente permiso:

- `users.track`

### Paso 3: Proporciona información al equipo de Adikteev {#step-3-provide-information-to-the-adikteev-team}

Para completar la integración, debes proporcionar tu clave de API REST or transferencia de estado representacional y la URL del punto de conexión REST or transferencia de estado representacional a tu director de cuentas de Adikteev. Adikteev establecerá la conexión y se pondrá en contacto contigo una vez finalizada la configuración para validar la integración.

## Agrupación por lotes y límites de velocidad {#batching-and-rate-limits}

El punto de conexión `user.track` se utiliza para actualizar los datos de tus usuarios. Consulta la [documentación de la API]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para obtener todos los detalles sobre los límites de velocidad del punto de conexión, las solicitudes por lotes y los detalles de las solicitudes.

{% alert tip %}
Recuerda que las llamadas a la API solo deben realizarse para actualizar datos que hayan cambiado, con el fin de reducir el número total de llamadas a la API. En otras palabras, actualiza solo a los usuarios cuyo segmento de abandono haya cambiado.
{% endalert %}

## Identificadores de usuario y dispositivo {#user-and-device-identifiers}

Los perfiles de usuario en Braze pueden asociarse a cualquier tipo de identificador de usuario o dispositivo; la lista de opciones disponibles depende de cómo hayas integrado la recopilación de datos con Braze. En el caso de Adikteev, tendrás que encontrar un identificador común entre tu MMP y tus perfiles de usuario en Braze para poder enviar correctamente la información del segmento de abandono.

## Retención y eliminación de datos {#data-retention-and-deletion}

Si no se realiza ninguna actualización, el atributo y su valor se conservan indefinidamente en los perfiles de usuario de Braze.

Para eliminar un atributo de perfil, establécelo como `null`.

## Cargas útiles de solicitud {#request-payloads}

La carga útil enviada desde Adikteev a Braze es personalizable y puede configurarse según las necesidades del cliente. Esto incluye configurar los identificadores utilizados, el nombre del atributo personalizado y si Adikteev puede crear nuevos usuarios en Braze o solo actualizar los usuarios existentes.


## Soporte y solución de problemas {#support-and-troubleshooting}

Ponte en contacto con tu director de cuentas de Adikteev para cualquier pregunta relacionada con la integración o para obtener ayuda con tus casos de uso.
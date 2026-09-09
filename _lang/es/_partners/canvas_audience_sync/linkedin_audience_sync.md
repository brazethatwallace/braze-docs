---
nav_title: LinkedIn
article_title: Sincronización de la audiencia de Canvas con LinkedIn
alias: /linkedin_audience_sync/
description: "Este artículo de referencia explica cómo utilizar Braze Audience Sync con LinkedIn para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
tool:
  - Canvas
page_order: 4

---

# Sincronización de audiencia con LinkedIn {#audience-sync-to-linkedin}

Mediante la Sincronización de audiencia de Braze con LinkedIn, las marcas pueden añadir datos de usuarios de su integración con Braze a las listas de clientes de LinkedIn para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Canvas de Braze basado en tus datos de usuario puede ahora desencadenar un anuncio para ese usuario en tus listas de clientes de LinkedIn.

**Entre los casos de uso habituales de la sincronización de audiencias se incluyen**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con LinkedIn. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

## Requisitos previos {#prerequisites}

Debes asegurarte de tener los siguientes elementos creados, completados o aceptados antes de configurar tu paso de sincronización de audiencia de LinkedIn en Canvas.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Audience Sync Pro | Braze | LinkedIn es un partner de [Audience Sync Pro]({{site.baseurl}}/partners/canvas_audience_sync/overview#audience-sync-pro). Selecciona LinkedIn en tus asignaciones de Audience Sync Pro en la página **Technology Partners** antes de conectar una cuenta publicitaria. Contacta a tu director de cuentas de Braze para obtener detalles de compra. |
| Cuenta publicitaria de LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Una cuenta publicitaria activa de LinkedIn vinculada a tu marca.<br><br>Asegúrate de haber aceptado todos los términos y condiciones relevantes de LinkedIn para acceder y utilizar esa cuenta. Tu administrador de LinkedIn debe otorgarte uno de estos roles de cuenta publicitaria: Account Billing Admin, Account Manager, Campaign Manager o Creative Manager. |
| Términos y políticas de LinkedIn | LinkedIn | Acepta cumplir con todos los términos, políticas, directrices y documentación requeridos por LinkedIn relacionados con tu uso de LinkedIn Audience Sync, incluidos todos los términos, políticas, directrices y documentación incorporados por referencia en ellos, que pueden incluir los siguientes documentos de LinkedIn: Services Terms, Ads Agreement, Data Processing Agreement y Professional Community Guidelines. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectar con LinkedIn {#step-1-connect-to-linkedin}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar LinkedIn a tu cuenta de Braze.
{% endalert %}

En el panel de Braze, ve a **Technology Partners** y selecciona **LinkedIn**. En la sección **LinkedIn Audience Sync**, selecciona **Connect LinkedIn**.

Serás redirigido a la página OAuth de LinkedIn para autorizar a Braze con los permisos relacionados con tu integración de Audience Sync. Después de seleccionar **Confirm**, serás redirigido de vuelta a Braze para seleccionar con qué cuentas de anuncios de LinkedIn deseas sincronizar.

![Se selecciona "Braze Self Service" como la cuenta de anuncios a conectar.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Cuando te conectes correctamente, volverás a la página del partner, donde puedes ver qué cuentas están conectadas y desconectar cuentas existentes.

![Una cuenta de LinkedIn conectada correctamente.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Tu conexión con LinkedIn se aplica a nivel de espacio de trabajo de Braze. Si tu administrador de LinkedIn te elimina de tu cuenta de anuncios de LinkedIn, Braze detecta un token no válido. Como resultado, tus Canvas activos que usan LinkedIn mostrarán errores y Braze no podrá sincronizar usuarios.

### Paso 2: Configurar los criterios de entrada a tu Canvas {#step-2-configure-your-canvas-entry-criteria}

Al crear audiencias para el seguimiento de anuncios, es posible que desees incluir o excluir a ciertos usuarios en función de sus preferencias y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" bajo la [CCPA](https://oag.ca.gov/privacy/ccpa). Los especialistas en marketing deben implementar los filtros relevantes para la elegibilidad de los usuarios dentro de los criterios de entrada a su Canvas. Las siguientes opciones pueden ayudar.

Si recopilaste el [IDFA de iOS a través de Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), puedes utilizar el filtro **Ads Tracking Enabled**. Selecciona el valor como `true` para enviar usuarios solo a los destinos de Audience Sync donde hayan dado su adhesión voluntaria. Los identificadores de publicidad de iOS no son compatibles como campos de coincidencia para LinkedIn Audience Sync.

![Un público de entrada con el filtro "Ad Tracking Enabled is true".]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Si estás recopilando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` o cualquier otro atributo personalizado relevante, debes incluirlos dentro de los criterios de entrada a tu Canvas como filtro:

![Un Canvas con un público de entrada de "opted_in_marketing" igual a "true".]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Para obtener más información sobre cómo cumplir con estas leyes de protección de datos dentro de la plataforma Braze, consulta [Asistencia técnica de protección de datos]({{site.baseurl}}/dp-technical-assistance).

### Paso 3: Añadir un paso de Audience Sync con LinkedIn {#step-3-add-an-audience-sync-step-with-linkedin}

Añade un componente en tu Canvas y selecciona Audience Sync. Haz clic en el botón **Custom Audience** para abrir el editor de componentes.

### Paso 4: Configuración de la sincronización {#step-4-sync-setup}

1. Selecciona **LinkedIn** como el partner de Audience Sync deseado.
2. Selecciona la cuenta de anuncios de LinkedIn deseada.
3. En el menú desplegable **Choose a New or Existing Audience**, escribe el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una nueva audiencia %}

#### Crear una nueva audiencia {#create-a-new-audience}

Introduce un nombre para la nueva audiencia, selecciona **Add Users to Audience** y selecciona qué campos deseas sincronizar con LinkedIn. Para esta integración, Braze actualmente admite los siguientes:
- Correo electrónico
- Nombre y apellido (ambos son obligatorios cuando usas coincidencia por nombre)
- Android GAID

Los identificadores de publicidad de iOS no son compatibles como campos de coincidencia para LinkedIn.

A continuación, guarda tu audiencia haciendo clic en el botón **Create Audience** en la parte inferior del editor de pasos.

![Un ejemplo de audiencia "leads" con la cuenta de anuncios de Braze seleccionada, la audiencia "leads", la acción de agregar usuarios a la audiencia y correo electrónico, Android GAID, y nombre y apellido como campos de coincidencia.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Braze muestra una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores. Puedes hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido del Canvas después de guardarla en el editor de pasos.

![Confirmación de que se creó la audiencia "leads".]({% image_buster /assets/img/linkedin/linkedin9.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios a medida que entran en el paso de Audience Sync, sujeto al [procesamiento por lotes y la latencia]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency).

{% endtab %}
{% tab Sincronizar con una audiencia existente %}

#### Sincronizar con una audiencia existente {#sync-with-an-existing-audience}

Braze también ofrece la posibilidad de agregar o eliminar usuarios de audiencias de LinkedIn existentes para confirmar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el menú desplegable y luego elige **Add to the Audience** o **Remove from the Audience**. Braze sincroniza a los usuarios a medida que entran en el paso de Audience Sync, sujeto al [procesamiento por lotes y la latencia]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency).

![Vista expandida del paso de Custom Audience del Canvas. Aquí se seleccionan la cuenta de anuncios deseada y la audiencia existente.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar el Canvas {#step-5-launch-canvas}

Después de configurar tu Audience Sync con LinkedIn, ¡lanza el Canvas! Se crea la nueva audiencia y los usuarios que pasen por el paso de Audience Sync se incluirán en esta audiencia en LinkedIn. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su recorrido de usuario.

Puedes ver la audiencia en LinkedIn accediendo a tu cuenta de anuncios y seleccionando **Audiences** en la sección **Assets** de la navegación. Desde la página **Audiences**, puedes ver el tamaño de cada audiencia una vez que alcance más de 300 miembros.

![Página de LinkedIn que muestra las siguientes métricas para la audiencia indicada.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Sincronización de usuarios y consideraciones sobre límites de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios alcanzan el paso de Audience Sync, Braze los pone en cola para agruparlos en lotes antes de enviarlos a LinkedIn. Consulta [Agrupación en lotes y latencia]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency) para saber cómo Braze despacha los lotes.

Braze envía hasta 2000 usuarios por solicitud a LinkedIn. Si los límites de velocidad de la API de LinkedIn restringen tu cuenta, Braze reintenta la sincronización durante aproximadamente 13 horas. Si la sincronización sigue sin ser posible, Braze registra a estos usuarios en la métrica Users Errored.

## Información sobre análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones para ayudarte a comprender mejor los análisis de tu componente de Audience Sync.

| MÉTRICA | DESCRIPCIÓN |
| ------ | ----------- |
| Ingresaron | Número de usuarios que ingresaron a este componente para sincronizarse con LinkedIn. |
| Avanzaron al paso siguiente | ¿Cuántos usuarios avanzaron al siguiente componente, si lo hay? Todos los usuarios avanzan automáticamente si este es el último paso en la rama del Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con LinkedIn. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a campos faltantes para la coincidencia. |
| Usuarios pendientes | Número de usuarios que Braze está procesando actualmente para sincronizar con LinkedIn. |
| Usuarios con error | Número de usuarios que no se sincronizaron con LinkedIn debido a un error de API tras aproximadamente 13 horas de reintentos. Las posibles causas de errores pueden incluir un token de LinkedIn no válido o que la audiencia haya sido eliminada en LinkedIn. |
| Salieron del Canvas | Número de usuarios que salieron del Canvas. Esto ocurre cuando el último paso en un Canvas es un componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Información sobre análisis" }

{% alert important %}
Recuerda que hay un retraso en los informes de las métricas de usuarios sincronizados y usuarios con error debido al procesamiento por lotes y al reintento de 13 horas, respectivamente.
{% endalert %}

{% alert important %}
LinkedIn proporciona métricas adicionales sobre las tasas de coincidencia dentro de su plataforma. Para revisar la coincidencia de tu Audience Sync específico, selecciona las métricas del paso Audience Sync para ir a la página **Detalles del paso en Canvas**.
<br><br>
Selecciona el partner como **LinkedIn**, tu cuenta de anuncios y la audiencia para ver el tamaño de la audiencia y la tasa de coincidencia de LinkedIn.

![Ejemplo de métricas del paso Audience Sync con 10.000 usuarios ingresados.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuánto tiempo tardará en completarse el tamaño de las audiencias en LinkedIn? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

Hay un retraso de hasta 48 horas para ver las audiencias dentro de tu cuenta de LinkedIn.

### ¿Cuál es el tamaño mínimo de audiencia para que LinkedIn la complete dentro de tu cuenta de anuncios? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

La audiencia debe incluir al menos 300 miembros para que el tamaño de la audiencia se complete dentro de tu cuenta de LinkedIn.

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Puedes desconectar y volver a conectar tu cuenta de LinkedIn en la página del partner de LinkedIn. Confirma con tu administrador de LinkedIn que tienes los permisos adecuados para la cuenta de anuncios con la que deseas sincronizar.

### ¿Por qué no se permite lanzar mi Canvas? {#why-is-my-canvas-not-allowed-to-launch}

Confirma que tu cuenta de anuncios de LinkedIn se ha conectado correctamente a Braze en la página del partner de LinkedIn. A continuación, asegúrate de haber seleccionado una cuenta de anuncios, ingresado un nombre para la nueva audiencia y seleccionado los campos para la coincidencia.

### ¿Cómo sé si los usuarios han coincidido después de enviarlos a LinkedIn? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn proporciona información sobre las tasas de coincidencia en su panel. Puedes revisarla en LinkedIn en la sección **Audiences**. Puedes revisar la tasa de coincidencia de tu audiencia de LinkedIn en los detalles del paso en Canvas de tu paso de Audience Sync.

### ¿Cuántas audiencias puede admitir LinkedIn? {#how-many-audiences-can-linkedin-support}

Actualmente, no hay límite en el número de audiencias en tu cuenta de anuncios de LinkedIn.

### ¿Por qué un segmento está atascado en estado BUILDING y no se actualiza? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Un segmento se considera sin uso y se establece como ARCHIVED después de no utilizarse continuamente durante 30 días en una campaña en borrador o activa. Debido a esto, un segmento puede parecer "atascado" en BUILDING cuando se transmiten actualizaciones a un segmento ARCHIVED, empujándolo así al estado BUILDING, y justo antes de que se archive de nuevo, se transmiten nuevas actualizaciones al segmento sin uso.
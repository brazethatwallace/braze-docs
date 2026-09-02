---
nav_title: LinkedIn
article_title: Sincronización de la audiencia de Canvas con LinkedIn
alias: /linkedin_audience_sync/
description: "Este artículo de referencia explicará cómo utilizar Braze Audience Sync con LinkedIn para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
tool:
  - Canvas
page_order: 4

---

# Sincronización de audiencia con LinkedIn {#audience-sync-to-linkedin}

Mediante la Sincronización de audiencia de Braze con LinkedIn, las marcas pueden añadir datos de usuarios de su integración con Braze a las listas de clientes de LinkedIn para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Canvas de Braze basado en tus datos de usuario puede ahora desencadenar un anuncio para ese usuario en tus listas de clientes de LinkedIn.

**Entre los casos de uso habituales de la sincronización de audiencias se incluyen**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con LinkedIn. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

{% multi_lang_include alerts/early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## Requisitos previos {#prerequisites}

Debes asegurarte de tener los siguientes elementos creados, completados o aceptados antes de configurar tu paso de sincronización de audiencias de LinkedIn en Canvas.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Cuenta publicitaria de LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Una cuenta publicitaria de LinkedIn activa vinculada a tu marca.<br><br>Asegúrate de haber aceptado todos los términos y condiciones relevantes de LinkedIn para acceder y utilizar esa cuenta, y de que tu administrador de LinkedIn te haya otorgado los permisos adecuados para gestionar audiencias. |
| Términos y políticas de LinkedIn | LinkedIn | Acepta cumplir con todos los términos, políticas, directrices y documentación requeridos por LinkedIn relacionados con tu uso de la sincronización de audiencias de LinkedIn, incluidos los términos, políticas, directrices y documentación incorporados por referencia en ellos, que pueden incluir los de LinkedIn: Términos de servicio, Acuerdo de anuncios, Acuerdo de procesamiento de datos y Directrices de la comunidad profesional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectar con LinkedIn {#step-1-connect-to-linkedin}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar LinkedIn a tu cuenta de Braze.
{% endalert %}

En el panel de Braze, ve a **Partners tecnológicos** y selecciona **LinkedIn**. En la sección **LinkedIn Audience Sync**, selecciona **Connect LinkedIn**.

![La página de tecnología de LinkedIn en Braze incluye una sección de resumen y una sección de LinkedIn Audience Sync con el botón Connected LinkedIn.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

Serás redirigido a la página de OAuth de LinkedIn para autorizar a Braze con los permisos relacionados con tu integración de Audience Sync. Después de seleccionar **Confirm**, serás redirigido de vuelta a Braze para seleccionar con qué cuentas de anuncios de LinkedIn deseas sincronizar.

![Se selecciona "Braze Self Service" como la cuenta de anuncios a conectar.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Una vez que te hayas conectado correctamente, volverás a la página del partner, donde podrás ver qué cuentas están conectadas y desconectar cuentas existentes.

![Una cuenta de LinkedIn conectada correctamente.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Tu conexión con LinkedIn se aplicará a nivel del espacio de trabajo de Braze. Si tu administrador de LinkedIn te elimina de tu cuenta de anuncios de LinkedIn, Braze detectará un token no válido. Como resultado, tus Canvas activos que usen LinkedIn mostrarán errores y Braze no podrá sincronizar usuarios.

### Paso 2: Configurar los criterios de entrada de tu Canvas {#step-2-configure-your-canvas-entry-criteria}

Al crear audiencias para el seguimiento de anuncios, es posible que desees incluir o excluir a ciertos usuarios en función de sus preferencias y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" bajo la [CCPA](https://oag.ca.gov/privacy/ccpa). Los especialistas en marketing deben implementar los filtros relevantes para la elegibilidad de los usuarios dentro de los criterios de entrada de su Canvas. Las siguientes opciones pueden ayudar.

Si has recopilado el [IDFA de iOS a través de Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), podrás usar el filtro **Ads Tracking Enabled**. Selecciona el valor como `true` para enviar usuarios solo a destinos de Audience Sync donde hayan dado su adhesión voluntaria.

![Un público de entrada con el filtro "Ad Tracking Enabled is true".]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Si estás recopilando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` u otros atributos personalizados relevantes, debes incluirlos dentro de los criterios de entrada de tu Canvas como filtro:

![Un Canvas con un público de entrada de "opted_in_marketing" igual a "true".]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Para obtener más información sobre cómo cumplir con estas leyes de protección de datos dentro de la plataforma Braze, consulta [Asistencia técnica de protección de datos]({{site.baseurl}}/dp-technical-assistance).

### Paso 3: Añadir un paso de Audience Sync con LinkedIn {#step-3-add-an-audience-sync-step-with-linkedin}

Añade un componente en tu Canvas y selecciona Audience Sync. Haz clic en el botón **Custom Audience** para abrir el editor de componentes.

![El editor de Canvas con la lista de componentes disponibles.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![El componente de Audience Sync seleccionado.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Paso 4: Configuración de la sincronización {#step-4-sync-setup}

Selecciona **LinkedIn** como el partner de Audience Sync deseado.

![Los detalles de "Set up Audience Sync" con los múltiples partners entre los que elegir.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

Luego selecciona la cuenta de anuncios de LinkedIn deseada. En el menú desplegable **Choose a New or Existing Audience**, escribe el nombre de una audiencia nueva o existente.

![Audience Sync a LinkedIn con Braze seleccionado como la cuenta de anuncios.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Add Users to Audience** y selecciona qué campos deseas sincronizar con LinkedIn. Para esta integración, actualmente admitimos los siguientes:
- Correo electrónico
- Nombre y apellido
- Android GAID

A continuación, guarda tu audiencia haciendo clic en el botón **Create Audience** en la parte inferior del editor de pasos.

![Un ejemplo de audiencia "leads" con la cuenta de anuncios de Braze seleccionada, la audiencia "leads", la acción de añadir usuarios a la audiencia y correo electrónico, Android GAID y nombre y apellido como campos de coincidencia.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Braze muestra una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores. Los usuarios pueden hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido del Canvas, ya que la audiencia se creó en modo borrador.

![Confirmación de que la audiencia "leads" fue creada.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real a medida que entran en el componente de Audience Sync.

{% endtab %}
{% tab Sincronizar con una audiencia existente %}

**Sincronizar con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a audiencias de LinkedIn existentes para confirmar que estas audiencias están actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el menú desplegable y selecciona **Add to the Audience**. Braze añadirá usuarios casi en tiempo real a medida que entren en el componente de Audience Sync.

![Vista expandida del paso de Canvas de Custom Audience. Aquí se seleccionan la cuenta de anuncios deseada y la audiencia existente.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar el Canvas {#step-5-launch-canvas}

Después de configurar tu Audience Sync con LinkedIn, ¡lanza el Canvas! La nueva audiencia se crea y los usuarios que fluyen a través del paso de Audience Sync se pasan a esta audiencia en LinkedIn. Si tu Canvas contiene componentes posteriores, tus usuarios avanzan al siguiente paso en su recorrido de usuario.

Puedes ver la audiencia en LinkedIn yendo a tu cuenta de anuncios y seleccionando **Audiences** en la sección **Assets** de la navegación. Desde la página **Audiences**, puedes ver el tamaño de cada audiencia después de alcanzar más de 300 miembros.

![Página de LinkedIn que muestra las siguientes métricas para la audiencia dada.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Sincronización de usuarios y consideraciones sobre límites de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios llegan al paso de Audience Sync, Braze los sincroniza casi en tiempo real respetando los límites de velocidad de la API de LinkedIn. Braze agrupa y procesa tantos usuarios como sea posible cada 5 segundos antes de enviarlos a LinkedIn.

El límite de velocidad de la API de LinkedIn no permite más de diez consultas por segundo ni más de 100.000 usuarios por solicitud. Si un cliente alcanza este límite, Braze reintenta la sincronización durante aproximadamente 13 horas. Si la sincronización sigue sin ser posible, Braze incluye a estos usuarios en la métrica Users Errored.

## Comprender los análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones para ayudarte a comprender mejor los análisis de tu componente Audience Sync.

| MÉTRICA | DESCRIPCIÓN |
| ------ | ----------- |
| Ingresados | Número de usuarios que ingresaron a este componente para sincronizarse con LinkedIn. |
| Avanzaron al siguiente paso | ¿Cuántos usuarios avanzaron al siguiente componente, si lo hay? Todos los usuarios avanzarán automáticamente si este es el último paso en la rama del Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con LinkedIn. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a campos faltantes para la coincidencia. |
| Usuarios pendientes | Número de usuarios que Braze está procesando actualmente para sincronizar con LinkedIn. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con LinkedIn debido a un error de API después de aproximadamente 13 horas de reintentos. Las posibles causas de errores pueden incluir un token de LinkedIn no válido o si la audiencia fue eliminada en LinkedIn. |
| Salieron del Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso en un Canvas es un componente Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

{% alert important %}
Recuerda que habrá un retraso en los informes de las métricas de usuarios sincronizados y usuarios con errores debido al vaciado masivo y al reintento de 13 horas, respectivamente.
{% endalert %}

{% alert important %}
LinkedIn proporciona métricas adicionales sobre las tasas de coincidencia dentro de su plataforma. Para revisar la coincidencia de tu Audience Sync específico, selecciona las métricas del paso Audience Sync para ir a la página **Detalles del paso en Canvas**.
<br><br>
Selecciona el partner como **LinkedIn**, tu cuenta de anuncios y la audiencia para ver el tamaño de la audiencia y la tasa de coincidencia de LinkedIn.

![Un ejemplo de métricas del paso Audience Sync con 10.000 usuarios ingresados.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuánto tiempo tardará en completarse el tamaño de las audiencias en LinkedIn? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

Hay un retraso de hasta 48 horas para ver las audiencias dentro de tu cuenta de LinkedIn.

### ¿Cuál es el tamaño mínimo de audiencia para que LinkedIn lo complete dentro de tu cuenta publicitaria? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

La audiencia debe incluir al menos 300 miembros para que el tamaño de la audiencia se complete dentro de tu cuenta de LinkedIn.

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Puedes desconectar y volver a conectar tu cuenta de LinkedIn en la página del partner de LinkedIn. Confirma con tu administrador de LinkedIn que tienes los permisos adecuados para la cuenta publicitaria con la que deseas sincronizar.

### ¿Por qué no se permite lanzar mi Canvas? {#why-is-my-canvas-not-allowed-to-launch}

Confirma que tu cuenta publicitaria de LinkedIn se haya conectado correctamente a Braze en la página del partner de LinkedIn. A continuación, asegúrate de haber seleccionado una cuenta publicitaria, ingresado un nombre para la nueva audiencia y seleccionado los campos para la coincidencia.

### ¿Cómo sé si los usuarios coincidieron después de enviarlos a LinkedIn? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn proporciona información sobre las tasas de coincidencia en su panel. Puedes revisarla en LinkedIn en la sección **Audiences**. Puedes revisar la tasa de coincidencia de tu audiencia de LinkedIn en los detalles del paso en Canvas de tu paso de Audience Sync.

### ¿Cuántas audiencias puede admitir LinkedIn? {#how-many-audiences-can-linkedin-support}

Actualmente, no hay límite en la cantidad de audiencias en tu cuenta publicitaria de LinkedIn.

### ¿Por qué un segmento está atascado en estado BUILDING y no se actualiza? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Un segmento se considera sin uso y se establece como ARCHIVED después de no utilizarse continuamente durante 30 días en una Campaign en borrador o activa. Debido a esto, un segmento puede parecer "atascado" en BUILDING cuando se transmiten actualizaciones a un segmento ARCHIVED, lo que lo empuja al estado BUILDING, y justo antes de que se archive de nuevo, se transmiten nuevas actualizaciones al segmento sin uso.
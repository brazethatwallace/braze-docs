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

- Dirigirse a usuarios de alto valor a través de múltiples canales para impulsar las compras o la interacción
- Reorientar a los usuarios menos receptivos a otros canales de marketing
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de tu marca

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con LinkedIn. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

{% multi_lang_include alerts/early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## Requisitos previos {#prerequisites}

Debes asegurarte de que tienes los siguientes elementos creados, completados o aceptados antes de configurar tu paso de sincronización con la audiencia de LinkedIn en Canvas.

| Requisito | Origen | Descripción |
| --- | --- | --- |
| Cuenta publicitaria en LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Una cuenta publicitaria activa en LinkedIn vinculada a tu marca.<br><br>Asegúrate de que has aceptado las condiciones pertinentes de LinkedIn para acceder a esa cuenta y utilizarla, y de que tu administrador de LinkedIn te ha concedido los permisos adecuados para gestionar audiencias. |
| Términos y políticas de LinkedIn | LinkedIn | Aceptas cumplir cualquiera de los términos, políticas, directrices y documentación requeridos por LinkedIn en relación con tu uso de la sincronización de audiencias de LinkedIn, incluidos los términos, políticas, directrices y documentación incorporados por referencia a los mismos, que pueden incluir los de LinkedIn: Condiciones de los servicios, Acuerdo de anuncios, Acuerdo de procesamiento de datos y Directrices de la comunidad profesional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conéctate a LinkedIn {#step-1-connect-to-linkedin}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) para conectar LinkedIn a tu cuenta de Braze.
{% endalert %}

En el dashboard de Braze, ve a **Socios tecnológicos** y selecciona **LinkedIn**. En la sección **LinkedIn Audience Sync**, selecciona **Connect LinkedIn**.

![La página de tecnología de LinkedIn en Braze incluye una sección de resumen y otra de sincronización de audiencia de LinkedIn con el botón Conectar LinkedIn.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

A continuación, se te redirigirá a la página de OAuth de LinkedIn para que autorices a Braze los permisos relacionados con tu integración de sincronización de audiencia. Cuando hayas seleccionado **Confirm**, se te redirigirá de nuevo a Braze para que selecciones las cuentas publicitarias de LinkedIn con las que deseas sincronizar.

![Se selecciona "Braze Self Service" como cuenta publicitaria a conectar.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Una vez que te hayas conectado correctamente, volverás a la página del socio, donde podrás ver qué cuentas están conectadas y desconectar las cuentas existentes.

![Una cuenta de LinkedIn conectada correctamente.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Tu conexión a LinkedIn se aplicará a nivel del espacio de trabajo de Braze. Si tu administrador de LinkedIn te elimina de tu cuenta publicitaria de LinkedIn, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilizan LinkedIn mostrarán errores, y Braze no podrá sincronizar usuarios.

### Paso 2: Configura tus criterios de entrada en Canvas {#step-2-configure-your-canvas-entry-criteria}

Al crear audiencias para el seguimiento de anuncios, es posible que desees incluir o excluir a determinados usuarios en función de sus preferencias, y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la [CCPA](https://oag.ca.gov/privacy/ccpa). Los especialistas en marketing deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada en Canvas. A continuación enumeramos algunas opciones.

Si has recopilado el [IDFA de iOS a través del SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection), podrás utilizar el filtro **Ads Tracking Enabled**. Selecciona el valor como `true` para enviar solo a los usuarios a los destinos de Audience Sync en los que hayan optado por la adhesión voluntaria.

![Una audiencia de entrada con el filtro "El seguimiento de anuncios habilitado es verdadero".]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Si estás recopilando `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, o cualquier otro atributo personalizado relevante, debes incluirlos dentro de tus criterios de entrada en Canvas como filtro:

![Un Canvas con una audiencia de entrada de "opted_in_marketing" es igual a "verdadero".]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Para saber más sobre cómo cumplir estas leyes de protección de datos dentro de la plataforma Braze, consulta la [Asistencia técnica sobre protección de datos]({{site.baseurl}}/dp-technical-assistance/).

### Paso 3: Añadir un paso de Audience Sync con LinkedIn {#step-3-add-an-audience-sync-step-with-linkedin}

Añade un componente en tu Canvas y selecciona **Audience Sync**. Haz clic en el botón **Custom Audience** para abrir el editor de componentes.

![El editor de Canvas con la lista de componentes disponibles.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![El componente de Audience Sync seleccionado.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Paso 4: Configuración de la sincronización {#step-4-sync-setup}

Selecciona **LinkedIn** como socio de Audience Sync deseado.

![Los detalles de "Configurar sincronización de audiencia" con los múltiples socios a elegir.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

A continuación, selecciona la cuenta publicitaria de LinkedIn que desees. En el desplegable **Choose a New or Existing Audience**, escribe el nombre de una audiencia nueva o existente.

![Sincronización de la audiencia con LinkedIn con Braze seleccionada como cuenta publicitaria.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Add Users to Audience** y selecciona los campos que deseas sincronizar con LinkedIn. Para esta integración, actualmente admitimos lo siguiente:
- Correo electrónico
- Nombre y apellidos
- Android GAID

A continuación, guarda tu audiencia haciendo clic en el botón **Create Audience** situado en la parte inferior del editor de pasos.

![Un ejemplo de audiencia de "clientes potenciales" con la cuenta publicitaria de Braze seleccionada, la audiencia de "clientes potenciales", la acción para añadir usuarios a la audiencia, y el correo electrónico, el GAID de Android y el nombre y apellidos como campos que deben coincidir.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Braze muestra una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si se producen errores. Los usuarios pueden hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido de Canvas, ya que la audiencia se creó en modo borrador.

![Confirmación de que se ha creado la audiencia de "clientes potenciales".]({% image_buster /assets/img/linkedin/linkedin9.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real a medida que entran en el componente Audience Sync.

{% endtab %}
{% tab Sincronizar con una audiencia existente %}

**Sincronizar con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a las audiencias existentes de LinkedIn para confirmar que dichas audiencias están actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y selecciona **Add to the Audience**. A continuación, Braze añadirá usuarios casi en tiempo real a medida que entren en el componente Audience Sync.

![Vista ampliada del paso en Canvas de audiencia personalizada. Aquí se seleccionan la cuenta publicitaria deseada y la audiencia existente.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar Canvas {#step-5-launch-canvas}

Una vez que hayas configurado tu Audience Sync con LinkedIn, ¡simplemente lanza el Canvas! Se creará la nueva audiencia, y los usuarios que pasen por el paso de Audience Sync pasarán a esta audiencia en LinkedIn. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su recorrido de usuario.

Puedes ver la audiencia en LinkedIn entrando en tu cuenta publicitaria y seleccionando **Audiences** en la sección **Assets** de la navegación. Desde la página **Audiences**, puedes ver el tamaño de cada audiencia después de alcanzar más de 300 miembros.

![Página de LinkedIn que muestra las siguientes métricas para la audiencia dada.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios alcanzan el paso de Audience Sync, Braze los sincroniza casi en tiempo real respetando los límites de velocidad de la API de LinkedIn. Braze procesa por lotes el mayor número posible de usuarios cada 5 segundos antes de enviarlos a LinkedIn.

El límite de velocidad de la API de LinkedIn no permite más de diez consultas por segundo y 100.000 usuarios por solicitud. Si un cliente alcanza este límite, Braze reintenta la sincronización durante un máximo de unas 13 horas. Si la sincronización sigue sin ser posible, Braze incluye a estos usuarios en la métrica de usuarios con errores.

## Comprender los análisis {#understanding-analytics}

La tabla siguiente incluye métricas y descripciones que te ayudarán a comprender mejor los análisis de tu componente Audience Sync.

| MÉTRICA | DESCRIPCIÓN |
| ------ | ----------- |
| Ingresados | Número de usuarios que entraron en este componente para ser sincronizados con LinkedIn. |
| Avanzaron al paso siguiente | ¿Cuántos usuarios avanzaron al siguiente componente, si lo hay? Todos los usuarios avanzarán automáticamente si este es el último paso en la rama de Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con LinkedIn. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios que Braze está procesando actualmente para sincronizarlos con LinkedIn. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con LinkedIn debido a un error de la API tras unas 13 horas de reintentos. Las causas potenciales de los errores pueden incluir un token de LinkedIn no válido o si la audiencia fue eliminada en LinkedIn. |
| Salieron de Canvas | Número de usuarios que han salido de Canvas. Esto ocurre cuando el último paso de un Canvas es un componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

{% alert important %}
Recuerda que se producirá un retraso en los informes de las métricas de usuarios sincronizados y usuarios con errores debido a la descarga masiva y al reintento de 13 horas, respectivamente.
{% endalert %}

{% alert important %}
LinkedIn proporciona métricas adicionales sobre las tasas de coincidencia dentro de su plataforma. Para revisar la coincidencia de tu Audience Sync específica, selecciona las métricas del paso de Audience Sync para ir a la página **Canvas Step Details**.
<br><br>
Selecciona el socio como **LinkedIn**, tu cuenta publicitaria y la audiencia para ver el tamaño de la audiencia y la tasa de coincidencia de LinkedIn.

![Un ejemplo de métricas del paso de Audience Sync con 10.000 usuarios ingresados.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Preguntas más frecuentes {#frequently-asked-questions}

### ¿Cuánto tardarán en poblarse los tamaños de audiencia en LinkedIn? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

Hay un retraso de hasta 48 horas para ver las audiencias dentro de tu cuenta de LinkedIn.

### ¿Cuál es el tamaño mínimo de audiencia para que LinkedIn lo incluya en tu cuenta publicitaria? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

La audiencia debe incluir al menos 300 miembros para poblar el tamaño de la audiencia dentro de tu cuenta de LinkedIn.

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Puedes desconectar y volver a conectar tu cuenta de LinkedIn en la página del socio de LinkedIn. Confirma con tu administrador de LinkedIn que tienes los permisos adecuados para la cuenta publicitaria con la que deseas sincronizar.

### ¿Por qué no se puede lanzar mi Canvas? {#why-is-my-canvas-not-allowed-to-launch}

Confirma que tu cuenta publicitaria de LinkedIn se ha conectado correctamente a Braze en la página del socio de LinkedIn. A continuación, asegúrate de haber seleccionado una cuenta publicitaria, introducido un nombre para la nueva audiencia y seleccionado los campos que coincidan.

### ¿Cómo sé si los usuarios se han emparejado después de pasar los usuarios a LinkedIn? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn proporciona información sobre las tasas de coincidencia en su dashboard. Puedes consultarlo en LinkedIn, en la sección **Audiences**. Puedes revisar la tasa de coincidencia de tu audiencia de LinkedIn en los detalles del paso en Canvas de tu paso de Audience Sync.

### ¿A cuántas audiencias puede dar soporte LinkedIn? {#how-many-audiences-can-linkedin-support}

Actualmente, no hay límite en el número de audiencias en tu cuenta publicitaria de LinkedIn.

### ¿Por qué un segmento está atascado en estado BUILDING y no se actualiza? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Un segmento se considera no utilizado y se establece en ARCHIVED después de que no se utilice de forma continuada durante 30 días en un borrador o en una Campaign activa. Por ello, un segmento puede aparecer "atascado" en BUILDING cuando se transmiten actualizaciones a un segmento ARCHIVED, empujándolo así al estado de BUILDING, y justo antes de que se archive de nuevo, se transmiten nuevas actualizaciones al segmento no utilizado.
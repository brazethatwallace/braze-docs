---
nav_title: Criteo
article_title: Sincronización del público de Canvas con Criteo
description: "Este artículo de referencia explica cómo utilizar Braze Audience Sync con Criteo para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 1
alias: /audience_sync_criteo/

tool:
  - Canvas
---

# Sincronización de audiencias con Criteo {#audience-sync-to-criteo}

Mediante la Sincronización de audiencias de Braze con Criteo, las marcas pueden optar por añadir datos de usuarios de su propia integración de Braze a las listas de clientes de Criteo para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Canvas de Braze basado en tus datos de usuario puede utilizarse ahora para desencadenar un anuncio dirigido a ese usuario en tus listas de clientes de Criteo.

**Entre los casos de uso más comunes para la sincronización de audiencias se incluyen:**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

Esta función ofrece a las marcas la opción de controlar qué datos propios específicos se comparten con Criteo. En Braze, las integraciones con las que puedes y no puedes compartir tus datos propios se tienen muy en cuenta. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
**Cláusula de exención de responsabilidad de Audience Sync Pro**<br>
Braze Audience Sync to Criteo es una integración de Audience Sync Pro. Para más información sobre esta integración, ponte en contacto con tu director de cuentas de Braze. <br>
{% endalert %}

## Requisitos previos {#prerequisites}

Debes asegurarte de que tienes los siguientes elementos creados o completados antes de configurar la sincronización de tu audiencia con Criteo.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Cuenta publicitaria de Criteo | [Criteo](https://marketing.criteo.com/) | Una cuenta de anuncios de Criteo activa vinculada a tu marca.<br><br>Asegúrate de que tu administrador de Criteo te ha concedido los permisos adecuados para acceder a audiencias. |
| [Directrices publicitarias de Criteo](https://www.criteo.com/advertising-guidelines/)<br>y<br>[Directrices de seguridad de marca de Criteo](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Como cliente activo de Criteo, debes asegurarte de que puedes cumplir las directrices de publicidad y seguridad de marca de Criteo antes de lanzar cualquier campaña de Criteo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectar con Criteo {#step-1-connect-to-criteo}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar Criteo a tu cuenta de Braze.
{% endalert %}

En el panel de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Criteo**. En Exportar audiencia de Criteo, selecciona **Connect Criteo**.

![Página de tecnología de Criteo en Braze que incluye una sección de resumen y otra de Criteo con el botón Connect Criteo.]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

Aparecerá una página de oAuth de Criteo para autorizar a Braze los permisos relacionados con tu integración de Audience Sync.

Una vez que hayas seleccionado confirmar, serás redirigido de nuevo a Braze para seleccionar las cuentas de anuncios de Criteo con las que deseas sincronizar.

![Una lista de las cuentas de anuncios disponibles que puedes conectar a Criteo.]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

Cuando te hayas conectado correctamente, volverás a la página del partner, donde podrás ver qué cuentas están conectadas y desconectar las cuentas existentes.

![Una versión actualizada de la página de socios tecnológicos de Criteo que muestra las cuentas de anuncios conectadas correctamente.]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Tu conexión con Criteo se aplicará a nivel del espacio de trabajo de Braze. Si tu administrador de Criteo te elimina de tu cuenta de anuncios de Criteo, Braze detectará un token no válido. Como resultado, tus Canvas activos que usan Criteo mostrarán errores, y Braze no podrá sincronizar usuarios.

### Paso 2: Configura tus criterios de entrada en Canvas {#step-2-configure-your-canvas-entry-criteria}

Al crear audiencias para el seguimiento de anuncios, es posible que desees incluir o excluir a determinados usuarios en función de sus preferencias, y con el fin de cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la [CCPA](https://oag.ca.gov/privacy/ccpa). Los especialistas en marketing deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada en Canvas. A continuación enumeramos algunas opciones.

Si has recopilado el [IDFA de iOS a través del SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), podrás utilizar el filtro Seguimiento de anuncios habilitado. Selecciona el valor como verdadero para enviar únicamente a los usuarios a los destinos de Audience Sync en los que hayan optado por participar.

![Filtro de entrada en Canvas que muestra el seguimiento de anuncios habilitado establecido en verdadero.]({% image_buster /assets/img/criteo/criteo11.png %})

Si estás recopilando `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, o cualquier otro atributo personalizado relevante, debes incluirlos dentro de tus criterios de entrada en Canvas como filtro:

![Filtro de entrada en Canvas que utiliza atributos personalizados de adhesión voluntaria para la elegibilidad de la audiencia.]({% image_buster /assets/img/criteo/criteo12.png %})

Para saber más sobre cómo cumplir estas leyes de protección de datos dentro de la plataforma Braze, consulta la [Asistencia técnica sobre protección de datos]({{site.baseurl}}/dp-technical-assistance).

### Paso 3: Añadir un paso de sincronización de audiencia con Criteo {#step-3-add-an-audience-sync-step-with-criteo}

Añade un componente a tu Canvas y selecciona **Audience Sync**.

![Flujo de trabajo de los pasos anteriores para añadir un componente de audiencia de Criteo en Canvas.]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![Flujo de trabajo de los pasos anteriores para añadir un componente de audiencia de Criteo en Canvas.]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### Paso 4: Configuración de la sincronización {#step-4-sync-setup}

Haz clic en el botón **Custom Audience** para abrir el editor de componentes.

Selecciona **Criteo** como partner de Audience Sync deseado.

![Editor del paso de Audience Sync con Criteo seleccionado como partner.]({% image_buster /assets/img/criteo/criteo6.png %})

A continuación, selecciona la cuenta de anuncios de Criteo que desees. En el desplegable **Choose a New or Existing Audience**, escribe el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una nueva audiencia %}
**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Add Users to Audience** y selecciona los campos que deseas sincronizar con Criteo. A continuación, guarda tu audiencia haciendo clic en el botón **Create Audience** en la parte inferior del editor de pasos.

![Vista ampliada del paso en Canvas de audiencia personalizada. Aquí se selecciona la cuenta de anuncios deseada y se crea una nueva audiencia.]({% image_buster /assets/img/criteo/criteo3.png %})

Braze muestra una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si se producen errores. Los usuarios pueden hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido del Canvas, ya que la audiencia se creó en modo borrador.

![Una alerta que aparece después de crear una nueva audiencia en el componente Canvas.]({% image_buster /assets/img/criteo/criteo1.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real a medida que entran en el componente de Audience Sync.
{% endtab %}
{% tab Sincronizar con una audiencia existente %}
**Sincronizar con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a las audiencias de Criteo existentes para garantizar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y selecciona **Add to the Audience**. A continuación, Braze añadirá usuarios casi en tiempo real a medida que entren en el componente de Audience Sync.

![Vista ampliada del paso en Canvas de audiencia personalizada. Aquí se seleccionan la cuenta publicitaria deseada y la audiencia existente.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar Canvas {#step-5-launch-canvas}

Una vez que hayas configurado la sincronización de tu audiencia con Criteo, ¡simplemente lanza el Canvas! Se creará la nueva audiencia, y los usuarios que pasen por el paso de Audience Sync pasarán a esta audiencia en Criteo. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su recorrido de usuario.

Puedes ver la audiencia en Criteo accediendo a tu cuenta de administrador de anuncios y seleccionando Segments en la **Audience Library** de la navegación. En la página **Segments**, puedes ver el tamaño de cada audiencia cuando alcance ~1.000.

![La biblioteca de audiencias muestra el segmento, el ID, la fuente, el tipo, el tamaño, el uso actual y la última actualización.]({% image_buster /assets/img/criteo/criteo.png %})

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios alcanzan el paso de Audience Sync, Braze los sincroniza casi en tiempo real respetando los límites de velocidad de la API de Criteo. Braze agrupa y procesa el mayor número posible de usuarios cada cinco segundos antes de enviarlos a Criteo.

El límite de velocidad de la API de Criteo no permite más de 250 solicitudes por minuto. Si un cliente alcanza este límite, Braze reintenta la sincronización durante un máximo de ~13 horas. Si la sincronización sigue sin ser posible, Braze incluye a estos usuarios en la métrica Usuarios con errores.

## Comprender los análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones que te ayudarán a comprender mejor los análisis de tu componente de Audience Sync.

| Métrica | Descripción |
| --- | --- |
| Ingresados | Número de usuarios que entraron en este componente para ser sincronizados con Criteo. |
| Avanzaron al paso siguiente | Cuántos usuarios avanzaron al siguiente componente, si lo hay. Todos los usuarios avanzarán automáticamente si este es el último paso en la rama del Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Criteo. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios procesados actualmente por Braze para sincronizar en Criteo. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Criteo debido a un error de la API tras unas 13 horas de reintentos. Las causas potenciales de los errores pueden incluir un token de Criteo no válido o si la audiencia fue eliminada en Criteo. |
| Salieron del Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso de un Canvas es un componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

{% alert important %}
Recuerda que se producirá un retraso en los informes de las métricas de usuarios sincronizados y usuarios con errores debido a la descarga masiva y al reintento de 13 horas, respectivamente.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}
Solo tienes que desconectar y volver a conectar tu cuenta de Criteo en la página del partner de Criteo. Asegúrate con tu administrador de Criteo de que dispones de los permisos adecuados para la cuenta publicitaria con la que deseas sincronizar.

### ¿Por qué no se puede lanzar mi Canvas? {#why-is-my-canvas-not-allowed-to-launch}

Confirma que tu cuenta de anuncios de Criteo se ha conectado correctamente a Braze en la página del partner de Criteo. A continuación, comprueba que has seleccionado una cuenta publicitaria, introducido un nombre para la nueva audiencia y seleccionado los campos que coinciden.

### ¿Cómo sé si los usuarios se han emparejado después de pasar los usuarios a Criteo? {#how-do-i-know-if-users-have-matched-after-passing-users-to-criteo}

Criteo no proporciona esta información debido a sus propias políticas de privacidad de datos.

### ¿Cuántas audiencias puede admitir Criteo? {#how-many-audiences-can-criteo-support}

En este momento, solo puedes tener 1.000 audiencias en tu cuenta de Criteo. Si superas este límite, Braze te notificará que no podemos crear nuevas audiencias. Tendrás que eliminar las audiencias que ya no utilices en tu cuenta de anuncios de Criteo.
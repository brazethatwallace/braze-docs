---
nav_title: TikTok
article_title: Sincronización de la audiencia de Canvas con TikTok
alias: /tiktok_audience_sync/
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con TikTok para ofrecer anuncios basados en activadores de comportamiento, segmentación y más."
tool:
  - Canvas
page_order: 8

---

# Sincronización de audiencia con TikTok {#audience-sync-to-tiktok}

Con Braze Audience Sync to TikTok, las marcas pueden optar por añadir los datos de usuario de su propia integración de Braze a TikTok Audiences para ofrecer anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Braze Canvas.

**Entre los casos de uso más comunes para la sincronización de audiencias se incluyen**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

Esta función permite a las marcas controlar qué datos propios específicos se comparten con TikTok. En Braze, las integraciones con las que puedes y no puedes compartir tus datos propios se tienen muy en cuenta. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
**Cláusula de exención de responsabilidad de Audience Sync Pro**<br>
Braze Audience Sync to TikTok es una integración de Audience Sync Pro. Para más información sobre esta integración, ponte en contacto con tu director de cuentas de Braze.
{% endalert %}

## Requisitos previos {#prerequisites}

Debes asegurarte de que los siguientes elementos están creados, completados o aceptados antes de configurar tu paso de audiencia de TikTok en Canvas.

| Requisito | Origen | Descripción |
| ----------- | ------ | ----------- |
| Cuenta de TikTok for Business Center | [TikTok](https://business.tiktok.com/) | Una herramienta centralizada para gestionar los activos de TikTok de tu marca (como cuentas de anuncios, páginas, aplicaciones). |
| Cuenta publicitaria de TikTok | [TikTok](https://ads.tiktok.com/) | Una cuenta de anuncios de TikTok activa vinculada a la cuenta Business Center de tu marca.<br><br>Asegúrate de que el administrador de tu TikTok Business Center te ha concedido permisos de administrador para las cuentas de anuncios de TikTok que planeas utilizar con Braze. |
| Condiciones y políticas de TikTok | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Aceptas cumplir cualquiera de los términos, políticas, directrices y documentación requeridos por TikTok relacionados con tu uso de la sincronización de audiencia de Pinterest, incluidos los términos, políticas, directrices y documentación incorporados por referencia a los mismos, que pueden incluir: las condiciones comerciales del servicio, las condiciones de publicidad, la política de privacidad, las condiciones de audiencia personalizada, las condiciones de servicio del desarrollador, el acuerdo de intercambio de datos del desarrollador, las políticas de publicidad, las directrices de marca y las directrices de la comunidad. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conéctate a TikTok {#step-1-connect-to-tiktok}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin) para conectar TikTok a tu cuenta de Braze.
{% endalert %}

En el panel de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **TikTok**. En Sincronización de audiencia de TikTok, selecciona **Connect TikTok**.

![La página de la tecnología TikTok en Braze incluye una sección de resumen y otra de sincronización de la audiencia de TikTok con el botón Connected TikTok.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

A continuación, serás redirigido a la página de TikTok OAuth para autorizar a Braze para la gestión de cuentas de anuncios y la gestión de audiencias. Una vez que hayas seleccionado **Confirm**, serás redirigido de nuevo a Braze para que selecciones las cuentas de anuncios de TikTok con las que deseas sincronizar.

![Página de autorización OAuth de TikTok que solicita acceso para la gestión de audiencias de Braze.]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Una vez conectado correctamente, volverás a la página del partner. Aquí puedes ver qué cuentas están conectadas y desconectar cuentas existentes.

![Página del partner TikTok en Braze que muestra las cuentas de anuncios de TikTok conectadas.]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Tu conexión de TikTok se aplicará a nivel del espacio de trabajo de Braze. Si tu administrador de TikTok te elimina de tu TikTok Business Center o del acceso a las cuentas de TikTok conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen componentes de TikTok Audience mostrarán errores, y Braze no podrá sincronizar usuarios.

### Paso 2: Añade un componente de audiencia de TikTok en Canvas {#step-2-add-a-tiktok-audience-component-in-canvas}

Añade un componente a tu Canvas y selecciona **Audience Sync**.

![Selector de pasos en Canvas con la opción del componente Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Tarjeta del componente Audience Sync añadida a una ruta de Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 3: Configuración de la sincronización {#step-3-sync-setup}

Haz clic en el botón **Custom Audience** para abrir el editor de componentes.

Selecciona **TikTok** como partner de Audience Sync deseado.

![Editor del componente Audience Sync con TikTok seleccionado como partner de sincronización.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

A continuación, selecciona la cuenta de anuncios de TikTok deseada. En el desplegable **Choose a New or Existing Audience**, escribe el nombre de una audiencia nueva o existente.

![Editor de Audience Sync de TikTok que muestra la selección de cuenta de anuncios y el desplegable de audiencia.]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Add Users to Audience** y selecciona los campos que deseas sincronizar con TikTok. A continuación, guarda tu audiencia haciendo clic en el botón **Create Audience** en la parte inferior del editor de pasos.

![Formulario de creación de nueva audiencia en el paso de Audience Sync de TikTok con los campos de coincidencia seleccionados.]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Braze muestra una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si se producen errores. Los usuarios pueden hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido de Canvas, ya que la audiencia se creó en modo borrador.

![Notificación de éxito en el paso de Audience Sync tras crear una nueva audiencia de TikTok.]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real a medida que entran en el paso de audiencia.

{% endtab %}
{% tab Sincronizar con una audiencia existente %}

**Sincronizar con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a las audiencias de TikTok existentes para garantizar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y selecciona **Add to the Audience**. A continuación, Braze añadirá usuarios casi en tiempo real a medida que entren en el paso de TikTok Audience.

![Vista ampliada del paso en Canvas de audiencia personalizada. Aquí se seleccionan la cuenta publicitaria deseada y la audiencia existente.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar Canvas {#step-4-launch-canvas}

Una vez que hayas configurado tu componente de TikTok Audience, ¡simplemente lanza el Canvas! Se creará una nueva audiencia, y los usuarios que fluyan a través del componente de TikTok Audience pasarán a esta audiencia en TikTok. Si tu Canvas contiene componentes subsiguientes, tus usuarios avanzarán al siguiente paso en su recorrido de usuario.

Puedes ver la audiencia en TikTok entrando en tu cuenta de **Ads Manager** y seleccionando **Audiences** en el desplegable de **Assets**. En la página **Audience**, puedes ver el tamaño de cada audiencia cuando alcance aproximadamente &#126;1000.

![Página de TikTok que muestra las siguientes métricas para la audiencia dada.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios alcanzan el paso de Audience Sync, Braze los sincroniza casi en tiempo real respetando los límites de velocidad de la API de marketing de TikTok. Braze agrupa y procesa el mayor número posible de usuarios cada 5 segundos antes de enviarlos a TikTok.

El límite de velocidad de la API de Segment de TikTok no permite más de 50 consultas por segundo y 10 000 usuarios por solicitud. Si un cliente alcanza este límite, Braze reintenta la sincronización durante un máximo de &#126;13 horas. Si la sincronización sigue sin ser posible, Braze lista a estos usuarios en la métrica de usuarios con errores.

## Comprender los análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones que te ayudarán a comprender mejor los análisis de tu componente de Audience Sync.

| Métrica | Descripción |
| ------ | ----------- |
| Ingresados | Número de usuarios que entraron en este componente para ser sincronizados con TikTok. |
| Avanzaron al paso siguiente | Número de usuarios que avanzaron al siguiente componente, si existe. Todos los usuarios avanzarán automáticamente si este es el último paso en la rama de Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con TikTok. Ten en cuenta que esto no equivale a usuarios emparejados en TikTok. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios que actualmente están siendo procesados por Braze para sincronizar en TikTok. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con TikTok debido a un error de la API tras unas 13 horas de reintentos. Las causas potenciales de errores pueden incluir un token de TikTok no válido o que la audiencia haya sido eliminada en TikTok. |
| Salieron de Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso de un Canvas es un componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

{% alert important %}
Recuerda que se producirá un retraso en los informes de las métricas de usuarios sincronizados y usuarios con errores debido a la descarga masiva y al reintento de 13 horas, respectivamente.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Puedes desconectar y volver a conectar tu cuenta de TikTok en la página del partner de TikTok. Asegúrate con tu administrador de TikTok Business Center de que tienes los permisos apropiados para la cuenta de anuncios que deseas sincronizar.

### ¿Por qué no se puede lanzar mi Canvas? {#why-is-my-canvas-not-allowed-to-launch}

Confirma que tu cuenta de TikTok se conecta correctamente a Braze en la página del partner de TikTok. A continuación, asegúrate de haber seleccionado una cuenta publicitaria, introducido un nombre para la nueva audiencia y seleccionado los campos de coincidencia.

### ¿Cómo sé si los usuarios han coincidido después de pasar usuarios a TikTok? {#how-do-i-know-if-users-have-matched-after-passing-users-to-tiktok}

TikTok no proporciona esta información debido a sus políticas de privacidad de datos.

### ¿Cuánto tardarán mis audiencias en llenarse en TikTok? {#how-long-will-it-take-for-my-audiences-to-populate-in-tiktok}

El tamaño de la audiencia se actualizará en 24-48 horas en la página de Audiences en el Ads Manager de TikTok.

### ¿Cuál es el número máximo de audiencias que puedo tener en mi cuenta de anuncios de TikTok? {#what-is-the-maximum-number-of-audiences-i-can-have-in-my-tiktok-ad-account}

Puedes tener hasta 400 audiencias por cuenta de anuncios de TikTok.

### ¿Por qué el tamaño de mi audiencia o la tasa de coincidencias en TikTok es mayor que la de los usuarios sincronizados en Braze con Audience Sync? {#why-is-my-audience-size-or-match-rate-in-tiktok-higher-than-the-users-synced-in-braze-with-audience-sync}

Esto se debe a que en TikTok, un ID puede estar asociado a varios usuarios de TikTok. Esto ocurre con mayor frecuencia cuando los clientes utilizan ID de anuncios para móviles (IDFA de iOS y GAID de Android) porque un dispositivo puede tener varios usuarios de TikTok conectados.

Además, TikTok también cuenta a los usuarios de Pangle como usuarios coincidentes, lo que en algunos casos puede dar lugar a una tasa de coincidencia elevada. Sin embargo, cuando utilizas la audiencia para la entrega de anuncios, es posible que el tamaño real de la audiencia entregable no sea tan alto como el tamaño del usuario emparejado, ya que depende de la ubicación y de otros factores influyentes.

### ¿Por qué recibo un correo electrónico con el asunto "La audiencia no existe para Canvas"? {#why-am-i-receiving-an-email-with-the-subject-audience-does-not-exist-for-canvas}

Esto puede ocurrir si la audiencia con la que elegiste sincronizar no es una audiencia de streaming (por ejemplo, si es una audiencia similar o una audiencia de archivo de usuario). Prueba a crear una nueva audiencia mediante el paso en Canvas de Braze Audience Sync.
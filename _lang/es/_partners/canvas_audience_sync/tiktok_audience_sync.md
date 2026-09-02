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

Con Braze Audience Sync to TikTok, las marcas pueden optar por añadir los datos de usuario de su propia integración de Braze a TikTok Audiences para ofrecer anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un BRAZE CANVAS.

**Entre los casos de uso más comunes para la sincronización de audiencias se incluyen**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Esta función permite a las marcas controlar qué datos propios específicos se comparten con TikTok. En Braze, las integraciones con las que puedes y no puedes compartir tus datos propios se tienen muy en cuenta. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
**Cláusula de exención de responsabilidad de Audience Sync Pro**<br>
Braze Audience Sync to TikTok es una integración de Audience Sync Pro. Para más información sobre esta integración, ponte en contacto con tu director de cuentas de Braze.
{% endalert %}

## Requisitos previos {#prerequisites}

Debes asegurarte de que los siguientes elementos estén creados, completados y/o aceptados antes de configurar tu paso de audiencia de TikTok en Canvas.

| Requisito | Origin | Descripción |
| ----------- | ------ | ----------- |
| Cuenta de TikTok for Business Center | [TikTok](https://business.tiktok.com/) | Una herramienta centralizada para gestionar los activos de TikTok de tu marca (como cuentas publicitarias, páginas y aplicaciones). |
| Cuenta publicitaria de TikTok | [TikTok](https://ads.tiktok.com/) | Una cuenta publicitaria activa de TikTok vinculada a la cuenta de Business Center de tu marca.<br><br>Asegúrate de que el administrador de tu TikTok Business Center te haya otorgado permisos de administrador para las cuentas publicitarias de TikTok que planeas usar con Braze. |
| Términos y políticas de TikTok | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Acepta cumplir con todos los términos, políticas, directrices y documentación requeridos por TikTok relacionados con tu uso de TikTok Audience Sync, incluidos los términos, políticas, directrices y documentación incorporados por referencia en ellos, que pueden incluir: los Términos comerciales del servicio, los Términos de publicidad, la Política de privacidad, los Términos de audiencias personalizadas, los Términos del servicio para desarrolladores, el Acuerdo de intercambio de datos para desarrolladores, las Políticas de publicidad, las Directrices de marca y las Directrices de la comunidad. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectar con TikTok {#step-1-connect-to-tiktok}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin) para conectar TikTok a tu cuenta de Braze.
{% endalert %}

En el panel de Braze, ve a **Integraciones de partners** > **Partners tecnológicos** y selecciona **TikTok**. En TikTok Audience Sync, selecciona **Conectar TikTok**.

![Página de tecnología de TikTok en Braze que incluye una sección de resumen y una sección de TikTok Audience Sync con el botón de TikTok conectado.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

Serás redirigido a la página de OAuth de TikTok para autorizar a Braze para la gestión de cuentas publicitarias y la gestión de audiencias. Después de seleccionar **Confirmar**, serás redirigido de vuelta a Braze para seleccionar con qué cuentas publicitarias de TikTok deseas sincronizar.

![Página de autorización OAuth de TikTok que solicita acceso para la gestión de audiencias de Braze.]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Una vez conectado correctamente, volverás a la página del partner. Aquí puedes ver qué cuentas están conectadas y desconectar cuentas existentes.

![Página del partner TikTok en Braze que muestra las cuentas publicitarias de TikTok conectadas.]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Tu conexión con TikTok se aplicará a nivel del espacio de trabajo de Braze. Si tu administrador de TikTok te elimina de tu TikTok Business Center o del acceso a las cuentas de TikTok conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen componentes de TikTok Audience mostrarán errores, y Braze no podrá sincronizar usuarios.

### Paso 2: Añadir un componente de TikTok Audience en Canvas {#step-2-add-a-tiktok-audience-component-in-canvas}

Añade un componente en tu Canvas y selecciona **Audience Sync**.

![Selector de pasos en Canvas con la opción del componente Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Tarjeta del componente Audience Sync añadida a una ruta de Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 3: Configuración de la sincronización {#step-3-sync-setup}

Haz clic en el botón **Custom Audience** para abrir el editor del componente.

Selecciona **TikTok** como el partner de Audience Sync deseado.

![Editor del componente Audience Sync con TikTok seleccionado como partner de sincronización.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

A continuación, selecciona la cuenta publicitaria de TikTok deseada. En el menú desplegable **Choose a New or Existing Audience**, escribe el nombre de una audiencia nueva o existente.

![Editor de TikTok Audience Sync que muestra la selección de cuenta publicitaria y el menú desplegable de audiencia.]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Add Users to Audience** y selecciona qué campos deseas sincronizar con TikTok. A continuación, guarda tu audiencia haciendo clic en el botón **Create Audience** en la parte inferior del editor de pasos.

![Formulario de creación de nueva audiencia en el paso de TikTok Audience Sync con campos de coincidencia seleccionados.]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Braze muestra una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores. Los usuarios pueden hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido del Canvas, ya que la audiencia se creó en modo borrador.

![Notificación de éxito en el paso de Audience Sync después de crear una nueva audiencia de TikTok.]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real a medida que entran en el paso de audiencia.

{% endtab %}
{% tab Sincronizar con una audiencia existente %}

**Sincronizar con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a audiencias de TikTok existentes para asegurar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el menú desplegable y selecciona **Add to the Audience**. Braze añadirá usuarios casi en tiempo real a medida que entren en el paso de TikTok Audience.

![Vista expandida del paso Custom Audience en Canvas. Aquí se seleccionan la cuenta publicitaria deseada y la audiencia existente.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar Canvas {#step-4-launch-canvas}
Después de configurar tu componente de TikTok Audience, ¡lanza el Canvas! Se crea una nueva audiencia, y los usuarios que pasen por el componente de TikTok Audience se añadirán a esta audiencia en TikTok. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su recorrido de usuario.

Puedes ver la audiencia en TikTok accediendo a tu **Ads Administrador Account** y seleccionando **Audiences** en el menú desplegable de **Assets**. Desde la página de **Audience**, puedes ver el tamaño de cada audiencia una vez que alcance &#126;1,000.

![Página de TikTok que muestra las siguientes métricas para la audiencia indicada.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Sincronización de usuarios y consideraciones sobre límites de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios llegan al paso de Audience Sync, Braze los sincroniza casi en tiempo real respetando los límites de velocidad de la API de marketing de TikTok. Braze agrupa y procesa tantos usuarios como sea posible cada 5 segundos antes de enviarlos a TikTok.

El límite de velocidad de la API de Segment de TikTok no permite más de 50 consultas por segundo ni más de 10 000 usuarios por solicitud. Si un cliente alcanza este límite, Braze reintenta la sincronización durante un máximo de &#126;13 horas. Si la sincronización sigue sin ser posible, Braze incluye a estos usuarios en la métrica Users Errored.

## Comprender los análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones para ayudarte a comprender mejor los análisis de tu componente Audience Sync.

| Métrica | Descripción |
| ------ | ----------- |
| Ingresados | Número de usuarios que ingresaron a este componente para ser sincronizados con TikTok. |
| Avanzaron al siguiente paso | Número de usuarios que avanzaron al siguiente componente, si existe uno. Todos los usuarios avanzarán automáticamente si este es el último paso en la rama del Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con TikTok. Ten en cuenta que esto no equivale a usuarios coincidentes en TikTok. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a campos faltantes para la coincidencia. |
| Usuarios pendientes | Número de usuarios que Braze está procesando actualmente para sincronizar con TikTok. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con TikTok debido a un error de API después de aproximadamente 13 horas de reintentos. Las posibles causas de errores pueden incluir un token de TikTok no válido o que la audiencia haya sido eliminada en TikTok. |
| Salieron del Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso en un Canvas es un componente Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

{% alert important %}
Recuerda que habrá un retraso en los informes de las métricas de usuarios sincronizados y usuarios con errores debido al vaciado masivo y al reintento de 13 horas, respectivamente.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Puedes desconectar y volver a conectar tu cuenta de TikTok en la página del partner de TikTok. Asegúrate con el administrador de tu TikTok Business Center de que tienes los permisos adecuados para la cuenta publicitaria que deseas sincronizar.

### ¿Por qué no se permite lanzar mi Canvas? {#why-is-my-canvas-not-allowed-to-launch}

Confirma que tu cuenta de TikTok se conecta correctamente a Braze en la página del partner de TikTok. A continuación, asegúrate de haber seleccionado una cuenta publicitaria, ingresado un nombre para la nueva audiencia y seleccionado los campos para la coincidencia.

### ¿Cómo sé si los usuarios coincidieron después de enviarlos a TikTok? {#how-do-i-know-if-users-have-matched-after-passing-users-to-tiktok}

TikTok no proporciona esta información debido a sus políticas de privacidad de datos.

### ¿Cuánto tiempo tardará en llenarse mi audiencia en TikTok? {#how-long-will-it-take-for-my-audiences-to-populate-in-tiktok}

El tamaño de la audiencia se actualizará en un plazo de 24 a 48 horas en la página de Audiences en el Ads Administrador de TikTok.

### ¿Cuál es el número máximo de audiencias que puedo tener en mi cuenta publicitaria de TikTok? {#what-is-the-maximum-number-of-audiences-i-can-have-in-my-tiktok-ad-account}

Puedes tener hasta 400 audiencias por cuenta publicitaria de TikTok.

### ¿Por qué el tamaño de mi audiencia o la tasa de coincidencia en TikTok es mayor que los usuarios sincronizados en Braze con Audience Sync? {#why-is-my-audience-size-or-match-rate-in-tiktok-higher-than-the-users-synced-in-braze-with-audience-sync}

Esto se debe a que en TikTok, un ID puede estar asociado con varios usuarios de TikTok. Esto ocurre con mayor frecuencia cuando los clientes utilizan ID de publicidad móvil (IDFA de iOS y GAID de Android), ya que un dispositivo puede tener varios usuarios de TikTok con sesión iniciada.

Además, TikTok también cuenta a los usuarios de Pangle como usuarios coincidentes, lo que en algunos casos puede resultar en una tasa de coincidencia elevada. Sin embargo, cuando utilizas la audiencia para la entrega de anuncios, el tamaño real de la audiencia entregable puede no ser tan alto como el tamaño de usuarios coincidentes, ya que depende de la ubicación y otros factores influyentes.

### ¿Por qué estoy recibiendo un correo electrónico con el asunto "Audience Does Not Exist For Canvas"? {#why-am-i-receiving-an-email-with-the-subject-audience-does-not-exist-for-canvas}

Esto puede ocurrir si la audiencia que elegiste para sincronizar no es una audiencia de streaming (por ejemplo, si es una audiencia similar o una audiencia de archivo de usuarios). Intenta crear una nueva audiencia a través del paso de Audience Sync de Canvas en Braze.
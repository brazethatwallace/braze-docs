---
nav_title: Pinterest
article_title: Sincronización de audiencia de Canvas con Pinterest
description: "Este artículo de referencia explica cómo utilizar Braze Audience Sync con Pinterest para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 5
alias: "/audience_sync_pinterest/"

tool:
  - Canvas

---

# Sincronización de audiencia con Pinterest {#audience-sync-to-pinterest}

Mediante Braze Audience Sync con Pinterest, las marcas pueden optar por añadir datos de usuarios de su propia integración con Braze a las audiencias de Pinterest para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, servicio de mensajes cortos, webhook, etc.) en un Canvas de Braze basado en tus datos de usuario puede utilizarse ahora para desencadenar un anuncio dirigido a ese usuario en tus audiencias de Pinterest.

**Entre los casos de uso habituales de la sincronización de audiencias se incluyen:**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con Pinterest. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
**Exención de responsabilidad de Audience Sync Pro**<br>
Braze Audience Sync to Pinterest es una integración de Audience Sync Pro. Para más información sobre esta integración, ponte en contacto con tu director de cuentas de Braze.
{% endalert %}

## Requisitos previos {#prerequisites}
Debes asegurarte de que los siguientes elementos estén creados, completados y/o aceptados antes de configurar tu paso de sincronización de audiencias de Pinterest en Canvas.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | Una herramienta centralizada para gestionar los activos de tu marca en Pinterest (como cuentas publicitarias, páginas, aplicaciones). |
| Cuenta publicitaria de Pinterest | [Pinterest](https://ads.pinterest.com/) | Una cuenta publicitaria activa de Pinterest vinculada al Pinterest Business Hub de tu marca.<br><br>Asegúrate de que el administrador de tu Pinterest Business Hub te haya otorgado permisos de administrador en las cuentas publicitarias de Pinterest que planeas usar con Braze. |
| Términos y políticas de Pinterest | Pinterest | Acepta cumplir con todos los términos, políticas, directrices y documentación requeridos por Pinterest relacionados con tu uso de la sincronización de audiencias de Pinterest, incluidos los términos, políticas, directrices y documentación incorporados por referencia en ellos, que pueden incluir: los Términos de servicio, los Términos de servicio para empresas, la Política de privacidad, los Términos de servicio para desarrolladores y API, los Términos de datos publicitarios, las Directrices de publicidad, el Acuerdo de servicios publicitarios, las Directrices de la comunidad y las Directrices de marca. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectar con Pinterest {#step-1-connect-to-pinterest}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar Pinterest a tu cuenta de Braze.
{% endalert %}

En el panel de Braze, ve a **Integraciones de partners** > **Partners tecnológicos** y selecciona **Pinterest**. En Pinterest Audience Sync, selecciona **Conectar Pinterest**.

![Página de tecnología de Pinterest en Braze que incluye una sección de resumen y una sección de Pinterest Audience Sync con el botón de Pinterest conectado.]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

Serás redirigido a la página de OAuth de Pinterest para autorizar a Braze para la gestión de cuentas publicitarias y la gestión de audiencias.

Después de seleccionar **Confirmar**, serás redirigido de vuelta a Braze para seleccionar qué cuentas publicitarias de Pinterest deseas sincronizar.

![Una lista de cuentas publicitarias disponibles que puedes conectar a Pinterest.]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

Cuando la conexión sea exitosa, volverás a la página del partner, donde podrás ver qué cuentas están conectadas y desconectar cuentas existentes.

![Una versión actualizada de la página de partners tecnológicos de Pinterest que muestra las cuentas publicitarias conectadas correctamente.]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Tu conexión con Pinterest se aplicará a nivel del espacio de trabajo de Braze. Si tu administrador de Pinterest te elimina de tu Pinterest Business Hub o del acceso a las cuentas de Pinterest conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen componentes de Pinterest Audience mostrarán errores, y Braze no podrá sincronizar usuarios.

### Paso 2: Añadir un paso de Audience Sync con Pinterest {#step-2-add-an-audience-sync-step-with-pinterest}

Añade un componente en tu Canvas y selecciona **Audience Sync**.

![Selector de pasos en Canvas con la opción del componente Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Tarjeta del componente Audience Sync añadida a una ruta de Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 3: Configuración de la sincronización {#step-3-sync-setup}

Haz clic en el botón **Custom Audience** para abrir el editor de componentes.

Selecciona **Pinterest** como el partner de Audience Sync deseado.

![Editor del componente Audience Sync con Pinterest seleccionado como partner de sincronización.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

A continuación, selecciona la cuenta publicitaria de Pinterest deseada. En el desplegable **Choose a New or Existing Audience**, escribe el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Add Users to Audience** y selecciona qué campos deseas sincronizar con Pinterest. A continuación, guarda tu audiencia haciendo clic en el botón **Create Audience** en la parte inferior del editor de pasos.

![Vista expandida del paso Custom Audience en Canvas. Aquí se selecciona la cuenta publicitaria deseada y se crea una nueva audiencia.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

Braze muestra una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores. Los usuarios pueden hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido del Canvas, ya que la audiencia se creó en modo borrador.

![Una alerta que aparece después de crear una nueva audiencia en el componente de Canvas.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real a medida que entran en el paso de Audience Sync.
{% endtab %}
{% tab Sincronizar con una audiencia existente %}
**Sincronizar con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a audiencias de Pinterest existentes para asegurar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y añádela a la audiencia. Braze añadirá usuarios casi en tiempo real a medida que entren en el paso de Audience Sync.

![Vista expandida del paso Custom Audience en Canvas. Aquí se seleccionan la cuenta publicitaria deseada y la audiencia existente.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar Canvas {#step-4-launch-canvas}

Después de configurar tu Audience Sync con Pinterest, ¡lanza el Canvas! Se crea la nueva audiencia, y los usuarios que pasen por el paso de Audience Sync se incorporarán a esta audiencia en Pinterest. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su recorrido de usuario.

Puedes ver la audiencia en Pinterest accediendo a tu cuenta del administrador de anuncios y seleccionando Audiences en el desplegable de Ads. Desde la página de Audience, puedes ver el tamaño de cada audiencia una vez que alcance aproximadamente ~100.

![Detalles de audiencia para una audiencia de Pinterest determinada que incluye nombre de la audiencia, ID de la audiencia, tipo de audiencia y tamaño de la audiencia.]({% image_buster /assets/img/pinterest/pinterest11.png %})

## Sincronización de usuarios y consideraciones sobre límites de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios alcanzan el paso de Audience Sync, Braze los sincroniza casi en tiempo real, respetando los límites de velocidad de la API de marketing de Pinterest. Braze agrupa y procesa tantos usuarios como sea posible cada 5 segundos antes de enviarlos a Pinterest.

El límite de velocidad de la API de Segment de Pinterest no permite más de siete consultas por segundo por usuario y 1900 usuarios por solicitud. Si un cliente alcanza este límite, Braze reintenta la sincronización durante aproximadamente 13 horas. Si la sincronización sigue sin ser posible, Braze registra a estos usuarios en la métrica Users Errored.

## Comprender los análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones para ayudarte a comprender mejor los análisis de tu componente de sincronización de audiencias.

| Métrica | Descripción |
| --- | --- |
| Ingresados | Número de usuarios que ingresaron a este componente para ser sincronizados con Pinterest. |
| Avanzaron al siguiente paso | ¿Cuántos usuarios avanzaron al siguiente componente, si lo hay? Todos los usuarios avanzarán automáticamente si este es el último paso en la rama del Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Pinterest. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a campos faltantes para la coincidencia. |
| Usuarios pendientes | Número de usuarios que Braze está procesando actualmente para sincronizar con Pinterest. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Pinterest debido a un error de API después de aproximadamente 13 horas de reintentos. Las posibles causas de errores pueden incluir un token de Pinterest no válido o que la audiencia haya sido eliminada en Pinterest. |
| Salieron del Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso en un Canvas es un componente de sincronización de audiencias. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

{% alert important %}
Recuerda que habrá un retraso en los informes de las métricas de usuarios sincronizados y de errores debido al vaciado masivo y al reintento de 13 horas, respectivamente.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuánto tiempo tardará en llenarse mi audiencia en Pinterest? {#how-long-will-it-take-for-my-audiences-to-populate-in-pinterest}

El tamaño de la audiencia se actualizará en un plazo de 24 a 48 horas en la página **Audiences** en el Ads Administrador de Pinterest.

### ¿Cómo sé si los usuarios coincidieron después de pasarlos a Pinterest? {#how-do-i-know-if-users-have-matched-after-passing-users-to-pinterest}

Pinterest no proporciona esta información debido a sus propias políticas de privacidad de datos.

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Confirma con el administrador de tu Pinterest Business Hub que tienes los permisos adecuados para la cuenta publicitaria que deseas sincronizar. También puedes desconectar y volver a conectar tu cuenta de Pinterest en la página del partner de Pinterest.

### ¿Por qué mi Canvas no puede lanzarse? {#why-is-my-canvas-not-allowed-to-launch}

Asegúrate de que tu cuenta de Pinterest se conecte correctamente a Braze en la página del partner de Pinterest. Verifica que hayas seleccionado una cuenta publicitaria, ingresado un nombre para la nueva audiencia y seleccionado los campos para la coincidencia.

### ¿Por qué no puedo seleccionar mi cuenta publicitaria para mi paso de Audience Sync? {#why-cant-i-select-my-ad-account-for-my-audience-sync-step}

Verifica que tu token se haya generado con los permisos de cuenta correctos. Ten en cuenta que si tienes demasiadas audiencias en tu cuenta publicitaria de Pinterest, el menú desplegable para seleccionar tu cuenta publicitaria puede agotar el tiempo de espera. En este caso, recomendamos reducir la cantidad de audiencias en tu cuenta publicitaria.
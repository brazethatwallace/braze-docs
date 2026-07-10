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

Mediante Braze Audience Sync con Pinterest, las marcas pueden optar por añadir datos de usuarios de su propia integración con Braze a las audiencias de Pinterest para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Canvas de Braze basado en tus datos de usuario puede utilizarse ahora para desencadenar un anuncio dirigido a ese usuario en tus audiencias de Pinterest.

**Entre los casos de uso habituales de la sincronización de audiencias se incluyen:**

- Dirigirse a usuarios de alto valor a través de múltiples canales para impulsar las compras o la participación
- Reorientar a los usuarios menos receptivos a otros canales de marketing
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de tu marca
- Crear audiencias Actalike para captar nuevos usuarios de forma más eficaz

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con Pinterest. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
**Exención de responsabilidad de Audience Sync Pro**<br>
Braze Audience Sync to Pinterest es una integración de Audience Sync Pro. Para más información sobre esta integración, ponte en contacto con tu director de cuentas de Braze.
{% endalert %}

## Requisitos previos {#prerequisites}
Debes asegurarte de que los siguientes elementos están creados, completados o aceptados antes de configurar tu paso de audiencia de Pinterest en Canvas.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | Una herramienta centralizada para administrar los activos de Pinterest de tu marca (como cuentas de anuncios, páginas, aplicaciones). |
| Cuenta publicitaria de Pinterest | [Pinterest](https://ads.pinterest.com/) | Una cuenta publicitaria de Pinterest activa vinculada al Pinterest Business Hub de tu marca.<br><br>Asegúrate de que el administrador de tu Pinterest Business Hub te ha concedido permisos de administrador para las cuentas de anuncios de Pinterest que piensas utilizar con Braze. |
| Términos y políticas de Pinterest | Pinterest | Aceptas cumplir cualquiera de los términos, políticas, directrices y documentación exigidos por Pinterest en relación con tu uso de la sincronización de audiencias de Pinterest, incluidos los términos, políticas, directrices y documentación incorporados por referencia a los mismos, que pueden incluir: las Condiciones del servicio, las Condiciones del servicio para empresas, la Política de privacidad, las Condiciones del servicio para desarrolladores y API, las Condiciones de datos de anuncios, las Directrices publicitarias, el Acuerdo de servicios publicitarios, las Directrices comunitarias y las Directrices de marca. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conéctate a Pinterest {#step-1-connect-to-pinterest}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar Pinterest a tu cuenta de Braze.
{% endalert %}

En el panel de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Pinterest**. En Pinterest Audience Sync, selecciona **Connect Pinterest**.

![Página de tecnología de Pinterest en Braze que incluye una sección de resumen y una sección de Pinterest Audience Sync con el botón Connect Pinterest.]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

A continuación, se te redirigirá a la página OAuth de Pinterest para que autorices a Braze para la gestión de cuentas publicitarias y la gestión de audiencias.

Tras seleccionar **Confirm**, se te redirigirá de nuevo a Braze para que selecciones las cuentas de anuncios de Pinterest que deseas sincronizar.

![Una lista de las cuentas de anuncios disponibles que puedes conectar a Pinterest.]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

Cuando te hayas conectado correctamente, volverás a la página del partner, donde podrás ver qué cuentas están conectadas y desconectar las cuentas existentes.

![Una versión actualizada de la página de socios tecnológicos de Pinterest que muestra las cuentas de anuncios conectadas correctamente.]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Tu conexión a Pinterest se aplicará a nivel del espacio de trabajo de Braze. Si tu administrador de Pinterest te elimina de tu Pinterest Business Hub o del acceso a las cuentas de Pinterest conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen componentes de audiencia de Pinterest mostrarán errores, y Braze no podrá sincronizar usuarios.

### Paso 2: Añadir un paso de sincronización de audiencia con Pinterest {#step-2-add-an-audience-sync-step-with-pinterest}

Añade un componente a tu Canvas y selecciona **Audience Sync**.

![Selector de pasos en Canvas con la opción del componente Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Tarjeta del componente Audience Sync añadida a una ruta de Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 3: Configuración de la sincronización {#step-3-sync-setup}

Haz clic en el botón **Custom Audience** para abrir el editor de componentes.

Selecciona **Pinterest** como partner de sincronización de audiencias deseado.

![Editor del componente Audience Sync con Pinterest seleccionado como partner de sincronización.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

A continuación, selecciona la cuenta de anuncios de Pinterest que desees. En el desplegable **Choose a New or Existing Audience**, escribe el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Add Users to Audience** y selecciona los campos que deseas sincronizar con Pinterest. A continuación, guarda tu audiencia haciendo clic en el botón **Create Audience** en la parte inferior del editor de pasos.

![Vista ampliada del paso en Canvas de audiencia personalizada. Aquí se selecciona la cuenta de anuncios deseada y se crea una nueva audiencia.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

Braze muestra una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si se producen errores. Los usuarios pueden hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido del Canvas, ya que la audiencia se creó en modo borrador.

![Una alerta que aparece después de crear una nueva audiencia en el componente Canvas.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real cuando entran en el paso de sincronización de audiencia.
{% endtab %}
{% tab Sincronizar con una audiencia existente %}
**Sincronizar con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a las audiencias de Pinterest existentes para garantizar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y añádela a la audiencia. A continuación, Braze añadirá usuarios casi en tiempo real cuando entren en el paso de sincronización de audiencia.

![Vista ampliada del paso en Canvas de audiencia personalizada. Aquí se seleccionan la cuenta publicitaria deseada y la audiencia existente.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar Canvas {#step-4-launch-canvas}

Una vez que hayas configurado la sincronización de tu audiencia con Pinterest, ¡lanza el Canvas! Se creará la nueva audiencia, y los usuarios que pasen por el paso de sincronización de audiencia se incorporarán a esta audiencia en Pinterest. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su recorrido de usuario.

Puedes ver la audiencia en Pinterest entrando en tu cuenta del administrador de anuncios y seleccionando Audiences en el desplegable Ads. En la página Audience, puedes ver el tamaño de cada audiencia cuando alcance ~100.

![Detalles de la audiencia de una determinada audiencia de Pinterest que incluye el nombre de la audiencia, el ID de la audiencia, el tipo de audiencia y el tamaño de la audiencia.]({% image_buster /assets/img/pinterest/pinterest11.png %})

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios llegan al paso de sincronización de audiencia, Braze los sincroniza casi en tiempo real respetando los límites de velocidad de la API de marketing de Pinterest. Braze agrupa y procesa tantos usuarios como sea posible cada 5 segundos antes de enviarlos a Pinterest.

El límite de velocidad de la API de Segment de Pinterest no permite más de siete consultas por segundo por usuario y 1.900 usuarios por solicitud. Si un cliente alcanza este límite, Braze reintenta la sincronización durante un máximo de ~13 horas. Si la sincronización sigue sin ser posible, Braze lista a estos usuarios en la métrica Usuarios con errores.

## Comprender los análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones que te ayudarán a comprender mejor los análisis de tu componente Audience Sync.

| Métrica | Descripción |
| --- | --- |
| Ingresados | Número de usuarios que entraron en este componente para ser sincronizados con Pinterest. |
| Avanzaron al paso siguiente | ¿Cuántos usuarios avanzaron al siguiente componente, si lo hay? Todos los usuarios avanzarán automáticamente si este es el último paso en la rama del Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Pinterest. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios que Braze está procesando actualmente para sincronizar en Pinterest. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Pinterest debido a un error de la API tras unas 13 horas de reintentos. Las causas potenciales de los errores pueden incluir un token de Pinterest no válido o que la audiencia haya sido eliminada en Pinterest. |
| Salieron del Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso de un Canvas es un componente de sincronización de audiencia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

{% alert important %}
Recuerda que habrá un retraso en los informes de los usuarios sincronizados y de las métricas con errores debido a la descarga masiva y al reintento de 13 horas, respectivamente.
{% endalert %}

## Preguntas más frecuentes {#frequently-asked-questions}

### ¿Cuánto tardarán mis audiencias en poblarse en Pinterest? {#how-long-will-it-take-for-my-audiences-to-populate-in-pinterest}

El tamaño de la audiencia se actualizará en 24-48 horas en la página **Audiences** del administrador de anuncios de Pinterest.

### ¿Cómo sé si los usuarios han coincidido después de pasar usuarios a Pinterest? {#how-do-i-know-if-users-have-matched-after-passing-users-to-pinterest}

Pinterest no proporciona esta información por sus propias políticas de privacidad de datos.

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Confirma con el administrador de tu Pinterest Business Hub que tienes los permisos adecuados para la cuenta de anuncios que deseas sincronizar. También puedes desconectar y volver a conectar tu cuenta de Pinterest en la página del partner de Pinterest.

### ¿Por qué no se puede lanzar mi Canvas? {#why-is-my-canvas-not-allowed-to-launch}

Asegúrate de que tu cuenta de Pinterest se conecta correctamente a Braze en la página del partner de Pinterest. Asegúrate de haber seleccionado una cuenta de anuncios, introducido un nombre para la nueva audiencia y seleccionado los campos que coincidan.

### ¿Por qué no puedo seleccionar mi cuenta de anuncios para mi paso de sincronización de audiencia? {#why-cant-i-select-my-ad-account-for-my-audience-sync-step}

Comprueba que tu token se generó con los permisos de cuenta correctos. Ten en cuenta que si tienes demasiadas audiencias en tu cuenta de anuncios de Pinterest, el menú desplegable para seleccionar tu cuenta de anuncios puede agotar el tiempo de espera. En este caso, te recomendamos que reduzcas la cantidad de audiencias en tu cuenta publicitaria.
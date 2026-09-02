---
nav_title: Snapchat
article_title: Sincronización de la audiencia de Canvas con Snapchat
description: "Este artículo de referencia explica cómo utilizar Braze Audience Sync to Snapchat para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 6
alias: "/audience_sync_snapchat/"

tool:
  - Canvas

---

# Sincronización de la audiencia con Snapchat {#audience-sync-to-snapchat}

Con Braze Audience Sync to Snapchat, las marcas pueden añadir datos de usuarios de su integración con Braze a las listas de clientes de Snapchat para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que normalmente utilizarías para desencadenar un mensaje (push, correo electrónico, servicio de mensajes cortos, webhook, etc.) en un Canvas de Braze basado en tus datos de usuario ahora se puede utilizar para desencadenar un anuncio dirigido a ese usuario en tus listas de clientes de Snapchat.

**Entre los casos de uso habituales de la sincronización de audiencias se incluyen:**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Esta característica permite a los usuarios controlar qué datos propios específicos se comparten con Snapchat. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
**Exención de responsabilidad de Audience Sync Pro**<br>
Braze Audience Sync to Snapchat es una integración de Audience Sync Pro. Para más información sobre esta integración, ponte en contacto con tu director de cuentas de Braze.
{% endalert %}

## Requisitos previos {#prerequisites}

Debes asegurarte de que los siguientes elementos estén creados, completados o aceptados antes de configurar tu paso de audiencia de Snapchat en Canvas.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Snapchat Business Administrador | Snapchat | Una herramienta centralizada para gestionar los activos de tu marca en Snapchat (como cuentas publicitarias, páginas y aplicaciones). |
| Cuenta publicitaria de Snapchat | Snapchat | Una cuenta publicitaria activa de Snapchat vinculada al Snapchat Business Administrador de tu marca.<br><br>Asegúrate de que el administrador de tu Snapchat Business Administrador te haya otorgado permisos de administrador en las cuentas publicitarias de Snapchat que planeas usar con Braze. |
| Términos y políticas de Snapchat | [Snapchat](https://www.snap.com/en-US/policies) | Acepta cumplir con todos los términos, políticas, directrices y documentación requeridos por Snapchat relacionados con tu uso de Snapchat Audience Sync, incluidos los términos, políticas, directrices y documentación incorporados por referencia en ellos, que pueden incluir: los Términos de servicio, los Términos de servicio comerciales, los Términos para desarrolladores, Audience Match, las Políticas de publicidad, la Política de contenido comercial, las Directrices de la comunidad y la Responsabilidad del proveedor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectar con Snapchat {#step-1-connect-to-snapchat}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar Snapchat a tu cuenta de Braze.
{% endalert %}

En el panel de Braze, ve a **Integraciones de partners** > **Partners tecnológicos** y selecciona **Snapchat**. En Snapchat Audience Sync, selecciona **Conectar Snapchat**.

![Página de tecnología de Snapchat en Braze que incluye una sección de resumen y una sección de Snapchat Audience Sync con el botón Conectar Snapchat.]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

Serás redirigido a la página OAuth de Snapchat para autorizar a Braze con los permisos relacionados con tu integración de Audience Sync.

Una vez que hayas seleccionado confirmar, serás redirigido de vuelta a Braze para seleccionar qué cuentas publicitarias de Snapchat deseas sincronizar.

![Una lista de cuentas publicitarias disponibles que puedes conectar a Snapchat.]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

Una vez conectado correctamente, volverás a la página del partner, donde podrás ver qué cuentas están conectadas y desconectar cuentas existentes.

![Una versión actualizada de la página de partners tecnológicos de Snapchat que muestra las cuentas publicitarias conectadas correctamente.]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Tu conexión con Snapchat se aplicará a nivel del espacio de trabajo de Braze. Si tu administrador de Snapchat te elimina de tu Snapchat Business Administrador o del acceso a las cuentas publicitarias de Snapchat conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que usen Snapchat mostrarán errores y Braze no podrá sincronizar usuarios.

### Paso 2: Añadir un paso de Audience Sync con Snapchat {#step-2-add-an-audience-sync-step-with-snapchat}

Añade un componente en tu Canvas y selecciona **Audience Sync**.

![Selector de pasos en Canvas con la opción del componente Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Tarjeta del componente Audience Sync añadida a una ruta de Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 3: Configuración de la sincronización {#step-3-sync-setup}

Haz clic en el botón **Custom Audience** para abrir el editor de componentes.

Selecciona **Snapchat** como el partner de Audience Sync deseado.

![Editor del componente Audience Sync con Snapchat seleccionado como partner de sincronización.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

A continuación, selecciona la cuenta publicitaria de Snapchat deseada. En el menú desplegable **Choose a New or Existing Audience**, escribe el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Add Users to Audience** y selecciona qué campos deseas sincronizar con Snapchat. A continuación, guarda tu audiencia haciendo clic en el botón **Create Audience** en la parte inferior del editor de pasos.

![Vista expandida del paso Custom Audience en Canvas. Aquí se selecciona la cuenta publicitaria deseada y se crea una nueva audiencia.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

Braze muestra una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores. Los usuarios pueden hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido del Canvas, ya que la audiencia se creó en modo borrador.

![Una alerta que aparece después de crear una nueva audiencia en el componente de Canvas.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real a medida que entran en el componente Audience Sync.

{% endtab %}
{% tab Sincronizar con una audiencia existente %}
**Sincronizar con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a audiencias de Snapchat existentes para asegurar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el menú desplegable y selecciona **Add to the Audience**. Braze añadirá usuarios casi en tiempo real a medida que entren en el componente Audience Sync.

![Vista expandida del paso Custom Audience en Canvas. Aquí se seleccionan la cuenta publicitaria deseada y una audiencia existente.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar el Canvas {#step-4-launch-canvas}

Después de configurar tu Audience Sync con Snapchat, ¡lanza el Canvas! Se creará una nueva audiencia y los usuarios que pasen por el paso de Audience Sync se añadirán a esta audiencia en Snapchat. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su recorrido de usuario.

Puedes ver la audiencia en Snapchat accediendo a tu cuenta del administrador de anuncios y seleccionando **Audiences** en la sección Assets de la navegación. Desde la página **Audiences**, puedes ver el tamaño de cada audiencia una vez que alcance aproximadamente 1000.

![Detalles de audiencia para una audiencia de Snapchat determinada que incluye nombre de la audiencia, tipo de audiencia, tamaño de la audiencia y retención de la audiencia en días.]({% image_buster /assets/img/snapchat/snapchat7.png %})

## Sincronización de usuarios y consideraciones sobre límites de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios llegan al paso de Audience Sync, Braze los sincroniza casi en tiempo real respetando los límites de velocidad de la API de Snapchat. Braze agrupa y procesa tantos usuarios como sea posible cada 5 segundos antes de enviarlos a Snapchat.

El límite de velocidad de la API de Snapchat no permite más de diez consultas por segundo ni más de 100.000 usuarios por solicitud. Si un cliente alcanza este límite, Braze reintenta la sincronización durante aproximadamente 13 horas. Si la sincronización sigue sin ser posible, Braze incluye a estos usuarios en la métrica Users Errored.

### Comprender los análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones para ayudarte a comprender mejor los análisis de tu componente Audience Sync.

| Métrica | Descripción |
| --- | --- |
| Entered | Número de usuarios que entraron en este componente para ser sincronizados con Snapchat. |
| Proceeded to Next Step | ¿Cuántos usuarios avanzaron al siguiente componente, si lo hay? Todos los usuarios avanzan automáticamente si este es el último paso en la rama del Canvas. |
| Users Synced | Número de usuarios que se han sincronizado correctamente con Snapchat. |
| Users Not Synced | Número de usuarios que no se han sincronizado debido a campos faltantes para la coincidencia. |
| Users Pending | Número de usuarios que Braze está procesando actualmente para sincronizar con Snapchat. |
| Users Errored | Número de usuarios que no se sincronizaron con Snapchat debido a un error de API después de aproximadamente 13 horas de reintentos. Las posibles causas de errores pueden incluir un token de Snapchat no válido o que la audiencia haya sido eliminada en Snapchat. |
| Exited Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso en un Canvas es un componente Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

{% alert important %}
Recuerda que habrá un retraso en los informes de las métricas de usuarios sincronizados y de errores debido al vaciado masivo y al reintento de 13 horas, respectivamente.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuántas audiencias puede admitir Snapchat? {#how-many-audiences-can-snapchat-support}

En este momento, solo puedes tener 1000 audiencias dentro de tu cuenta de Snapchat.

Si superas este límite, Braze te notificará que no podemos crear nuevas audiencias. Tendrás que eliminar las audiencias que ya no estés usando en tu cuenta de anuncios de Snapchat.

### ¿Cómo sé si los usuarios coincidieron después de pasarlos a Snapchat? {#how-do-i-know-if-users-have-matched-after-passing-users-to-snapchat}

Snapchat no proporciona esta información debido a sus políticas de privacidad de datos.

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Puedes desconectar y volver a conectar tu cuenta de Snapchat en la página del partner de Snapchat. Confirma con el administrador de tu Snapchat Business Administrador que tienes los permisos adecuados para la cuenta de anuncios con la que deseas sincronizar.

### ¿Por qué no se permite lanzar mi Canvas? {#why-is-my-canvas-not-allowed-to-launch}

Asegúrate de que tu cuenta de anuncios de Snapchat se conecte correctamente a Braze en la página del partner de Snapchat. Verifica que hayas seleccionado una cuenta de anuncios, ingresado un nombre para la nueva audiencia y seleccionado los campos para la coincidencia.
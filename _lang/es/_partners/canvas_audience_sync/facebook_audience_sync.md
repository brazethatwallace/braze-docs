---
nav_title: Facebook
article_title: Sincronización de la audiencia de Canvas con Facebook
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con Facebook para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 2
alias: /audience_sync_facebook/

tool:
  - Canvas

---

# Sincronización de audiencias con Facebook {#audience-sync-to-facebook}

> Con la Sincronización de audiencias de Braze con Facebook, puedes optar por añadir los datos de tus propios usuarios de tu integración Braze a las audiencias personalizadas de Facebook para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más.

Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, servicio de mensajes cortos o webhook) en un Canvas de Braze basado en tus datos de usuario puede utilizarse ahora para desencadenar un anuncio dirigido a ese usuario en Facebook utilizando audiencias personalizadas. Por ejemplo, cuando configuras una sincronización de audiencia con Facebook, puedes utilizar una amplia variedad de campos de datos propios, como correo electrónico, teléfono, nombre y apellidos.

**Entre los casos de uso habituales para sincronizar audiencias personalizadas se incluyen**:

- Dirigirse a usuarios de alto valor con múltiples canales para impulsar las compras o la participación.
- Reorientar a los usuarios menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de tu marca.
- Crear audiencias similares para captar nuevos usuarios de forma más eficaz.

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con Facebook. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios alcanzan el paso de Audience Sync, Braze los sincroniza casi en tiempo real, respetando los límites de velocidad de la API de marketing de Facebook. Braze agrupa y procesa tantos usuarios como sea posible cada 5 segundos antes de enviarlos a Facebook.

El límite de velocidad de la API de marketing de Facebook no permite más de &#126;190.000 solicitudes de API por cuenta publicitaria en un período de una hora. Si un cliente alcanza este límite, Braze reintenta la sincronización durante un máximo de &#126;13 horas. Si la sincronización sigue sin ser posible, Braze incluye a estos usuarios en la métrica Users Errored.

## Requisitos previos {#prerequisites}

Deberás confirmar que tienes los siguientes elementos creados y completados antes de configurar tu paso de Facebook Audience en Canvas.

| Requisito | Origin | Descripción |
| ----------- | ------ | ----------- |
| Facebook Business Administrador | [Facebook](https://www.facebook.com/business/help/113163272211510) | Una herramienta centralizada para gestionar los activos de Facebook de tu marca (por ejemplo, cuentas publicitarias, páginas y aplicaciones). |
| Cuenta publicitaria de Facebook | [Facebook](https://www.facebook.com/business/help/910137316041095) | Una cuenta publicitaria de Facebook activa vinculada al administrador de negocios de tu marca.<br><br>Asegúrate de que el administrador de tu Facebook Business Administrador te haya concedido permisos de "Manage Campaigns" o "Manage ad accounts" para las cuentas publicitarias de Facebook que planeas usar con Braze. Además, asegúrate de haber aceptado los términos y condiciones de tu cuenta publicitaria. |
| Términos de Facebook Custom Audiences | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Acepta los términos de Facebook Custom Audiences para las cuentas publicitarias de Facebook que planeas usar con Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conectar con Facebook {#step-1-connect-to-facebook}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar Facebook a tu cuenta de Braze.
{% endalert %}

En el panel de Braze, ve a **Integraciones de partners** > **Partners tecnológicos** y selecciona **Facebook**. En Exportación de Facebook Audience, selecciona **Conectar Facebook**.

![Página de tecnología de Facebook en Braze que incluye una sección de resumen y una sección de exportación de Facebook Audience con el botón Conectar Facebook.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Aparecerá una ventana de diálogo oAuth de Facebook para autorizar a Braze a crear audiencias personalizadas en tus cuentas publicitarias de Facebook.

![El primer cuadro de diálogo de Facebook que solicita "Conectar como X", donde X es tu nombre de usuario de Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![El segundo cuadro de diálogo de Facebook que solicita permiso para administrar anuncios de tus cuentas publicitarias.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Después de vincular Braze a tu cuenta de Facebook, selecciona las cuentas publicitarias que deseas sincronizar dentro de tu espacio de trabajo de Braze. Cuando estés conectado, volverás a la página del partner, donde podrás ver qué cuentas están conectadas y desconectar cuentas existentes.

![Una versión actualizada de la página de partners tecnológicos de Facebook que muestra las cuentas publicitarias conectadas correctamente.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Tu conexión con Facebook se aplica a nivel del espacio de trabajo de Braze. Si tu administrador de Facebook te elimina de tu Facebook Business Administrador o del acceso a las cuentas de Facebook conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen componentes de Facebook Audience mostrarán errores, y Braze no podrá sincronizar usuarios.

{% alert important %}
Para los clientes que anteriormente pasaron por el proceso de revisión de la aplicación de Facebook para [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) y [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), tu token de usuario del sistema seguirá siendo válido para el componente de Facebook Audience. No podrás editar ni revocar el token de usuario del sistema de Facebook a través de la página del partner de Facebook. En su lugar, puedes conectar tu cuenta de Facebook para reemplazar tu token de usuario del sistema de Facebook dentro de tu espacio de trabajo de Braze.

<br><br>La configuración oAuth de Facebook también se aplicará a las [exportaciones de Facebook usando Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Paso 2: Aceptar los términos de servicio de audiencias personalizadas {#step-2-accept-custom-audiences-terms-of-service}

Antes de crear tu Canvas, debes aceptar los siguientes términos de servicio de Facebook en los siguientes enlaces:

- **Términos de audiencias personalizadas de lista de clientes para tu cuenta personal:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Términos de herramientas empresariales de Facebook para tu cuenta empresarial:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Un ejemplo de los términos a aceptar para audiencias personalizadas de lista de clientes.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Un ejemplo de los términos a aceptar para las herramientas empresariales de Facebook.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

Consulta la [sección de preguntas frecuentes](#terms) para obtener más detalles sobre la auditoría de tu cuenta de Facebook durante la integración.

### Paso 3: Añadir un componente de Facebook Audience en Canvas {#step-3-add-a-facebook-audience-component-in-canvas}

Añade un componente en tu Canvas y selecciona **Facebook Audience**.

![Una lista de componentes para añadir al Canvas.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![El componente de sincronización de audiencia.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 4: Configuración de la sincronización {#step-4-sync-setup}

Selecciona el botón **Custom Audience** para abrir el editor del componente. Luego, selecciona **Facebook** como partner de sincronización de audiencia.

![Configuración de sincronización de audiencia con opciones para elegir un partner.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Selecciona la cuenta publicitaria de Facebook deseada. En el menú desplegable **Elegir una audiencia nueva o existente**, escribe el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una audiencia nueva %}

1. Introduce un nombre para la nueva audiencia personalizada.
2. Selecciona **Añadir usuarios a la audiencia** y elige los campos que deseas sincronizar con Facebook.
3. A continuación, selecciona **Crear audiencia** para guardar tu audiencia.

![Configuración de sincronización de audiencia para una audiencia con la información de correo electrónico, teléfono, nombre y apellido para hacer coincidir.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Recibirás una notificación en la parte superior del editor del paso si la audiencia se crea correctamente o si se produce un error durante este proceso. También puedes hacer referencia a esta audiencia para la eliminación de usuarios más adelante en el recorrido del Canvas, ya que la audiencia se creó en modo borrador.

Cuando lanzas un Canvas con una audiencia nueva, Braze crea la nueva audiencia personalizada al lanzar el Canvas y posteriormente sincroniza a los usuarios en tiempo casi real a medida que entran en el paso de sincronización de audiencia.

Cada paso de sincronización de audiencia se asigna a la audiencia de Facebook configurada en ese paso. Cuando el Canvas se ejecuta de nuevo (por ejemplo, en un horario recurrente), Braze sincroniza a los usuarios elegibles con esa misma audiencia; no crea una nueva audiencia de Facebook para cada ejecución del Canvas.

{% endtab %}
{% tab Sincronizar con una audiencia existente %}

Braze ofrece la posibilidad de añadir o eliminar usuarios de audiencias personalizadas de Facebook existentes para confirmar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente, haz lo siguiente:

1. Escribe el nombre de la audiencia existente en el menú desplegable.
2. Elige si deseas **Añadir a la audiencia** o **Eliminar de la audiencia**.
3. Braze añadirá o eliminará usuarios en tiempo casi real a medida que entren en el paso de Facebook Audience.

![Configuración de sincronización de audiencia para eliminar la información de correo electrónico, teléfono, nombre y apellido.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook prohíbe eliminar usuarios de audiencias personalizadas cuando el tamaño de la audiencia es demasiado bajo (normalmente menos de 1000 usuarios). Como resultado, Braze no puede sincronizar usuarios para una eliminación del paso de sincronización de audiencia hasta que la audiencia alcance el tamaño adecuado.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar Canvas {#step-5-launch-canvas}

Después de configurar tu componente de Facebook Audience, ¡es hora de lanzar el Canvas! La nueva audiencia personalizada se crea, y los usuarios que pasen por el paso de Facebook Audience se añadirán a esta audiencia personalizada en Facebook. Si tu Canvas contiene pasos posteriores, tus usuarios avanzarán al siguiente paso en su recorrido de usuario.

La pestaña **Historial** de la audiencia personalizada en el Administrador de audiencias de Facebook reflejará el número de usuarios enviados a la audiencia desde Braze. Si un usuario vuelve a entrar en el paso, se envía a Facebook de nuevo.

![Detalles de la audiencia y la pestaña Historial para una audiencia de Facebook determinada que incluye una tabla de historial de audiencia con columnas para la actividad, detalles de la actividad, elementos modificados y la fecha y hora.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Comprender los análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones para ayudarte a comprender mejor los análisis de tu componente de Audience Sync.

| Métrica | Descripción |
| --- | --- |
| Ingresados | Número de usuarios que ingresaron a este componente para sincronizarse con Facebook. |
| Avanzaron al siguiente paso | Cuántos usuarios avanzaron al siguiente componente, si lo hay. Todos los usuarios avanzarán automáticamente si este es el último paso en la rama del Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Facebook. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a campos faltantes para la coincidencia. Los campos se emparejan utilizando un operador "OR", lo que significa que mientras un usuario tenga uno de los campos en Facebook, Facebook emparejará al usuario aunque no haya coincidencia en todos los demás campos. |
| Usuarios pendientes | Número de usuarios que Braze está procesando actualmente para sincronizar con Facebook. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Facebook debido a un error de API después de aproximadamente 13 horas de reintentos. Las posibles causas de errores pueden incluir un token de Facebook no válido o que la audiencia personalizada haya sido eliminada en Facebook. |
| Salieron del Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso en un Canvas es un paso de Facebook. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

{% alert important %}
Existe un retraso en los informes de las métricas de usuarios sincronizados y usuarios con errores debido al procesamiento interno.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuánto tiempo tarda en llenarse mi audiencia en el panel del partner de Audience Sync? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

El tiempo que tarda en llenarse una audiencia depende del partner específico. Todas las redes procesarán las solicitudes de Braze e intentarán hacer coincidir a los usuarios. Las audiencias personalizadas pueden tardar hasta 24 horas en actualizarse.

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Puedes simplemente desconectar y volver a conectar tu cuenta de Facebook en la página del partner de Facebook. Confirma con el administrador de tu Facebook Business Administrador que tienes los permisos adecuados para la cuenta publicitaria con la que deseas sincronizar.

### ¿Por qué no se permite lanzar mi Canvas? {#why-is-my-canvas-not-allowed-to-launch}

- Asegúrate de que tu token de usuario del sistema esté autenticado y tenga acceso a las cuentas publicitarias deseadas en Facebook Business Administrador.
- Asegúrate de haber seleccionado una cuenta publicitaria, ingresado un nombre para la nueva audiencia personalizada y seleccionado los campos para hacer coincidir.
- Es posible que hayas alcanzado el límite de 500 audiencias personalizadas en Facebook. Ve al Administrador de audiencias de Facebook para eliminar algunas que no necesites antes de crear nuevas audiencias personalizadas con Canvas.

### ¿Cómo sé si los usuarios coincidieron después de enviarlos a Facebook? {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

Facebook no proporciona esta información por razones de privacidad.

### ¿Braze admite audiencias personalizadas basadas en valor? {#does-braze-support-value-based-custom-audiences}

En este momento, Braze no admite audiencias personalizadas basadas en valor. {% multi_lang_include product_feedback_cta.md context="gap" feature="value-based custom audience sync" %}

### ¿Braze aplica hash a los datos antes de enviarlos a los partners de Audience Sync? {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

Una vez que los datos de correo electrónico se normalizan, Braze les aplica hash con SHA256.

**IDFA/AAID/teléfono:** Braze aplica hash con SHA256. Los tipos de audiencia que sincronizamos son siempre uno de los siguientes:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256.

En cuanto a la frecuencia, Braze solo aplica hash a la información de identificación personal (PII) de los usuarios cuando estos entran en el paso de Audience Sync en el recorrido del usuario como preparación para la sincronización.

### ¿Cómo resuelvo un problema con la sincronización de una audiencia personalizada similar basada en valor? {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

En este momento, Braze no admite audiencias personalizadas similares basadas en valor. Si intentas sincronizar con esta audiencia, esto puede causar errores en tu paso de Audience Sync. Para resolver esto, sigue estos pasos:

1. Ve al panel de Facebook Ad Administrador y selecciona **Audiences**.
2. Selecciona **Create audience** > **Custom audience**.
3. Selecciona **Customer list**.
4. Sube tu CSV o lista sin la columna **Value**. Selecciona **No, continue with a customer list that doesn't include customer value**.
5. Termina de crear tu audiencia personalizada.
6. En Braze, actualiza el paso de Facebook Audience Sync con la audiencia personalizada que creaste.

### He recibido un correo electrónico relacionado con los términos de servicio de audiencias personalizadas de Facebook. ¿Qué debo hacer para resolver esto? {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

Para usar Audience Sync con Facebook, debes aceptar estos términos de servicio.

- Si tu cuenta publicitaria está directamente asociada con tu cuenta personal de Facebook, puedes aceptar los términos de servicio desde tu cuenta personal aquí: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Si tu cuenta publicitaria está vinculada a la cuenta de Business Administrador de tu empresa, debes aceptar los términos de servicio en tu cuenta de Facebook Business Administrador aquí: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Después de haber aceptado los términos de servicio de audiencias personalizadas de Facebook, haz lo siguiente:

1. Actualiza tu token de acceso de Facebook en Braze desconectando y volviendo a conectar tu cuenta de Facebook.
2. Vuelve a habilitar tu paso de Facebook Audience Sync editando y actualizando tu Canvas.

Entonces, Braze podrá sincronizar usuarios tan pronto como lleguen al paso de Facebook Audience Sync.

### ¿Qué pasó con los filtros **Connected Facebook** y **Number of Facebook Friends Using App**? {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

Los filtros de segmentación de Braze **Number of Facebook Friends Using App** y **Connected Facebook** están obsoletos. Facebook y los SDK or kit de desarrollo de software de Braze ya no recopilan los datos subyacentes en los que se basaban esos filtros.

Reemplaza los filtros obsoletos con atributos personalizados, eventos personalizados o Segments basados en la participación; por ejemplo, inicio de sesión de Facebook o vinculación social en lugar de **Connected Facebook**, o referidos, invitaciones y compartidos en lugar de **Number of Facebook Friends Using App**.

Para la reorientación con Canvas, haz coincidir a los usuarios con correo electrónico, teléfono, nombre y apellido, como se muestra en el [Paso 4: Configuración de sincronización](#step-4-sync-setup). Para ampliar el alcance, sincroniza un Segment de alto valor con Facebook y crea una audiencia similar en Meta Ads Administrador.

## Solución de problemas {#troubleshooting}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table aria-label="Solución de problemas">
  <thead>
    <tr>
      <th>Error</th>
      <th>Descripción</th>
      <th>Pasos para resolverlo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Token no válido</b></td>
      <td>Las causas típicas son que el usuario que conectó la integración cambie su contraseña, que las credenciales caduquen, entre otras.</td>
      <td>Ve a <b>Partner Integrations</b> > <b>Facebook</b> y desconecta y vuelve a conectar tu cuenta. Consulta <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-Facebook-account'>esta sección de solución de problemas</a> para conocer los pasos adicionales para auditar tu cuenta de Facebook.</td>
    </tr>
    <tr>
      <td><b>Tamaño de audiencia demasiado bajo</b></td>
      <td>Este error puede ocurrir si creaste un paso de Audience Sync que elimina usuarios de tus audiencias. Si el tamaño de tu audiencia se acerca a cero, la red puede señalar que el tamaño de la audiencia es demasiado pequeño para servir.</td>
      <td>Usa una estrategia de Audience Sync que añada y elimine usuarios de forma regular, de modo que no agote completamente el tamaño de la audiencia.</td>
    </tr>
    <tr>
      <td><b>La audiencia no existe</b></td>
      <td>El paso de Audience Sync utiliza una audiencia que no existe o fue eliminada. Esto también puede activarse si ya no tienes los permisos necesarios para acceder a la audiencia.</td>
      <td>Pide a un administrador que verifique en la plataforma del partner si la audiencia aún existe. <br><br>Si existe, confirma si el usuario que conectó la integración tiene permiso para acceder a la audiencia. Si no lo tiene, se le debe otorgar acceso a esa audiencia. <br><br>Si la audiencia fue eliminada intencionalmente, añade una audiencia activa y crea una nueva audiencia en el paso.</td>
    </tr>
    <tr>
      <td><b>Intento de acceso a cuenta publicitaria</b></td>
      <td>No tienes permisos para la cuenta publicitaria o la audiencia que seleccionaste.</td>
      <td>Trabaja con los administradores de tu cuenta publicitaria para obtener el acceso y los permisos adecuados.</td>
    </tr>
    <tr>
      <td><b>Términos de servicio no aceptados</b></td>
      <td>Para algunos destinos de Audience Sync, como Facebook, la red publicitaria requiere que aceptes términos de servicio específicos para usar la característica de Audience Sync. Este error se activará si no has aceptado los términos correspondientes. Como resultado, es posible que también hayas recibido un correo electrónico de Braze con este asunto: "Your authorization credentials for Facebook are invalid."</td>
      <td>Verifica que hayas aceptado los términos requeridos de Facebook.</td>
    </tr>
    <tr>
      <td><b>Todos los usuarios están generando errores</b></td>
      <td>Si todos los usuarios están generando errores en un paso a pesar de confirmar que estos usuarios tienen valores para los campos seleccionados en el paso, esto podría indicar un problema con tu cuenta de Facebook.</td>
      <td>Sigue los pasos en <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-Facebook-account'>esta sección de solución de problemas</a> para verificar si tu cuenta tiene algún problema.
      </td>
    </tr>
    <tr>
      <td><b>Error al crear audiencia</b></td>
      <td>En la página de partners tecnológicos de Facebook, ves "Connected", pero hay un error en el paso de Facebook Audience Sync al sincronizar una audiencia: "Failed to create audience 'audience name'". La autorización de tu cuenta de Facebook falló. Visita la página de partners tecnológicos para volver a conectar tu cuenta.</td>
      <td>Sigue los pasos en <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-Facebook-account'>esta sección de solución de problemas</a> para verificar si tu cuenta tiene algún problema.
      </td>
    </tr>
    <tr>
      <td><b>Cuenta publicitaria no aparece en el menú desplegable</b></td>
      <td>Cuando configuras el paso de Facebook Audience, una cuenta publicitaria que esperas no aparece en el SELECTOR de cuentas publicitarias.</td>
      <td>Confirma que tu aplicación de Facebook completó la <a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">revisión de la aplicación</a> para <code>ads_management</code> con el nivel de acceso que Facebook requiere para el uso de la API de Marketing. En <a href="https://business.facebook.com/">Facebook Business Administrador</a>, confirma que el token del usuario del sistema tiene los permisos correctos y está asociado con las cuentas publicitarias que usas en Braze, y que los términos de la cuenta publicitaria están aceptados. <br><br>Si el menú desplegable funciona en un Canvas nuevo pero no en un Canvas que ya editaste, intenta una actualización forzada de tu navegador (o borra tu caché) y confirma que has iniciado sesión como un usuario que aún tiene acceso a esas cuentas publicitarias.</td>
    </tr>
    <tr>
      <td><b>Error al validar el token de acceso</b></td>
      <td>Ves un error sobre la validación del token de acceso de Facebook al conectar Braze con Facebook o al sincronizar audiencias.</td>
      <td>Cierra sesión en Facebook en tu navegador. En Braze, ve a <b>Partner Integrations</b> &gt; <b>Facebook</b>, elimina las credenciales guardadas de Facebook y luego vuelve a conectar Facebook. En la página de partners tecnológicos de Facebook para Braze, desconecta y vuelve a conectar la integración si la opción está disponible. <br><br>Si los problemas continúan, sigue <a href="#audit-your-Facebook-account">Auditar tu cuenta de Facebook</a>.</td>
    </tr>
    <tr>
      <td><b>Errores de permisos de exportación o sincronización de audiencia</b></td>
      <td>La exportación o sincronización de una audiencia de Facebook falla con errores de autorización, administrador o cuenta publicitaria.</td>
      <td>En <a href="https://developers.facebook.com/">Meta for Developers</a>, abre tu aplicación y confirma que tu usuario tiene un rol de <b>Admin</b> en <b>App roles</b>. En <b>App settings</b> &gt; <b>Advanced</b>, confirma que <b>Advertising accounts</b> incluye las cuentas que usas con Braze. En <a href="https://business.facebook.com/latest/settings">Business settings</a>, confirma que el usuario que conecta o el usuario del sistema tiene acceso a la cuenta publicitaria correcta.</td>
    </tr>
  </tbody>
</table>

### Auditar tu cuenta de Facebook {#audit-your-facebook-account}

Si experimentas problemas adicionales con tu integración, consulta las siguientes secciones y pasos para auditar tu cuenta de Facebook.

#### Revisar permisos de la cuenta {#review-account-permissions}

1. Revisa [la documentación de Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) sobre cómo gestionar estos permisos en su plataforma. Para Facebook Business Administrador, necesitas al menos un rol de **Admin** o **Employee** en Business Administrador con acceso a las cuentas publicitarias necesarias.
2. Como **Employee**, confirma que el Admin te otorgue permisos completos de **Manage Ad Account** para cada cuenta publicitaria para crear una audiencia o sincronizar usuarios con la audiencia.
3. Después de que se hayan otorgado, debes desconectar y volver a conectar tu cuenta.

#### Aceptar los términos de servicio {#terms}

Acepta cualquier término de servicio (TOS) pendiente de Facebook. Facebook periódicamente requerirá que tú (el usuario) y el administrador del negocio vuelvan a aprobar sus términos de servicio.

1. El usuario conectado necesita aceptar todos los términos de servicio para cada una de sus cuentas publicitarias:
- TOS de Custom Audience para tu cuenta personal de Facebook:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Una cuenta con permisos de control total para gestionar una cuenta publicitaria.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Para encontrar tu ID de cuenta e ID de negocio, sigue estos pasos:

1. Ve a tu [cuenta de Facebook Ads Administrador](https://adsmanager.facebook.com/).
2. Confirma que estás usando la cuenta publicitaria correcta verificándola en el menú desplegable.
3. En la URL, encuentra el ID de cuenta después de `act=` y el ID de negocio después de `business_id=`

![La URL con el ID de cuenta y el ID de negocio resaltados.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Lee y selecciona **Accept** para los términos de Custom Audience. Recomendamos confirmar para qué cuenta se están firmando los términos de servicio usando el menú desplegable en la parte superior de los términos.

![El menú desplegable que muestra la cuenta que está firmando los términos de servicio.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. Debes seleccionar **Accept** para los términos de servicio. Después, verás este mensaje: "You have accepted these terms of service on behalf of Braze".
6. Actualiza tu token de acceso de Facebook con Braze desconectando y volviendo a conectar tu cuenta de Facebook.
7. Vuelve a habilitar tu paso de Facebook Audience Sync editando y actualizando tu Canvas. Braze podrá entonces sincronizar usuarios tan pronto como lleguen al paso de audiencia de Facebook.
8. Si el problema persiste, intenta usar un usuario diferente con permisos de administrador para aceptar manualmente los términos a través del Ads Administrador.

#### Completar cualquier tarea pendiente {#complete-any-pending-tasks}

Verifica si tienes alguna tarea pendiente con Facebook que pueda estar impidiéndote usar los servicios de Facebook Ads:

1. [Inicia sesión en Facebook Ads Administrador](https://adsmanager.facebook.com/).
2. Selecciona la cuenta publicitaria con la que tienes problemas.
3. En la navegación, selecciona tu **Account Overview**. <br> ![La navegación con Account Overview seleccionado.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Verifica si hay alertas que necesiten ser atendidas. <br> ![Una cuenta con una tarjeta de crédito vencida.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Verifica si hay tareas de configuración que necesiten ser completadas. <br> ![Una cuenta con una configuración de cuenta parcialmente completada.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Conectar con un usuario diferente {#connect-with-a-different-user}

Como otro paso de solución de problemas, recomendamos que un usuario administrador diferente intente conectar su cuenta haciendo lo siguiente:

1. Desconecta la integración actual.
2. Un usuario diferente con permisos de administrador conecta su cuenta de usuario de Facebook.
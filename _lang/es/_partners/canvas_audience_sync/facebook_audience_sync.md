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

Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS o webhook) en un Canvas de Braze basado en tus datos de usuario puede utilizarse ahora para desencadenar un anuncio dirigido a ese usuario en Facebook utilizando audiencias personalizadas. Por ejemplo, cuando configuras una sincronización de audiencia con Facebook, puedes utilizar una amplia variedad de campos de datos propios, como correo electrónico, teléfono, nombre y apellidos.

**Entre los casos de uso habituales para sincronizar audiencias personalizadas se incluyen**:

- Dirigirse a usuarios de alto valor con múltiples canales para impulsar las compras o la participación.
- Reorientar a los usuarios menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de tu marca.
- Crear audiencias similares para captar nuevos usuarios de forma más eficaz.

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con Facebook. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad {#user-syncing-and-rate-limit-considerations}

A medida que los usuarios llegan al paso Sincronización de audiencia, Braze los sincroniza casi en tiempo real respetando los límites de velocidad de la API de marketing de Facebook. Braze procesa por lotes el mayor número posible de usuarios cada 5 segundos antes de enviarlos a Facebook.

El límite de velocidad de la API de marketing de Facebook no permite más de &#126;190.000 solicitudes API por cuenta publicitaria en un periodo de una hora. Si un cliente alcanza este límite, Braze reintenta la sincronización durante un máximo de &#126;13 horas. Si la sincronización sigue sin ser posible, Braze lista a estos usuarios en la métrica Usuarios con errores.

## Requisitos previos {#prerequisites}

Tendrás que confirmar que tienes los siguientes elementos creados y completados antes de configurar tu paso en Canvas de Facebook Audience.

| Requisito | Origen | Descripción |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook](https://www.facebook.com/business/help/113163272211510) | Una herramienta centralizada para administrar los activos de Facebook de tu marca (por ejemplo, cuentas de anuncios, páginas y aplicaciones). |
| Cuenta publicitaria de Facebook | [Facebook](https://www.facebook.com/business/help/910137316041095) | Una cuenta de anuncios de Facebook activa vinculada al administrador de empresas de tu marca.<br><br>Asegúrate de que el administrador de tu empresa en Facebook te ha concedido permisos de "Gestionar campañas" o "Gestionar cuentas de anuncios" para las cuentas de anuncios de Facebook que piensas utilizar con Braze. Asegúrate también de que has aceptado los términos y condiciones de tu cuenta publicitaria. |
| Términos de los públicos personalizados de Facebook | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Acepta las condiciones de públicos personalizados de Facebook para las cuentas de anuncios de Facebook que piensas utilizar con Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conéctate a Facebook {#step-1-connect-to-facebook}

{% alert important %}
Debes tener el [permiso "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar Facebook a tu cuenta de Braze.
{% endalert %}

En el panel de Braze, ve a **Partner Integrations** > **Technology Partners** y selecciona **Facebook**. En Facebook Audience Export, selecciona **Connect Facebook**.

![Página de tecnología de Facebook en Braze que incluye una sección de resumen y otra de exportación de la audiencia de Facebook con el botón de Facebook conectado.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Aparecerá una ventana de diálogo oAuth de Facebook para autorizar a Braze a crear audiencias personalizadas en tus cuentas de anuncios de Facebook.

![El primer cuadro de diálogo de Facebook te pide "Conectarte como X", donde X es tu nombre de usuario de Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![El segundo cuadro de diálogo de Facebook te pide permiso para administrar los anuncios de tus cuentas publicitarias.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Después de vincular Braze a tu cuenta de Facebook, selecciona las cuentas de anuncios que deseas sincronizar dentro de tu espacio de trabajo de Braze. Cuando estés conectado, volverás a la página del partner, donde podrás ver qué cuentas están conectadas y desconectar las cuentas existentes.

![Una versión actualizada de la página de partners tecnológicos de Facebook que muestra las cuentas de anuncios conectadas correctamente.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Tu conexión a Facebook se aplica a nivel del espacio de trabajo de Braze. Si tu administrador de Facebook te elimina de tu Facebook Business Manager o del acceso a las cuentas de Facebook conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen componentes de Facebook Audience mostrarán errores, y Braze no podrá sincronizar usuarios.

{% alert important %}
Para los clientes que hayan pasado previamente por el proceso de revisión de la aplicación de Facebook para la [gestión de anuncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) y [el acceso estándar a la gestión de anuncios](https://developers.facebook.com/docs/marketing-api/access#standard), tu token de usuario del sistema seguirá siendo válido para el componente Facebook Audience. No podrás editar ni revocar el token de usuario del sistema de Facebook a través de la página del partner de Facebook. En su lugar, puedes conectar tu cuenta de Facebook para sustituir tu token de usuario del sistema de Facebook dentro de tu espacio de trabajo de Braze.

<br><br>La configuración de Facebook oAuth también se aplicará a las [exportaciones de Facebook mediante Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Paso 2: Aceptar las condiciones de servicio de las audiencias personalizadas {#step-2-accept-custom-audiences-terms-of-service}

Antes de crear tu Canvas, debes aceptar las siguientes condiciones de servicio de Facebook en los siguientes enlaces:

- **Condiciones de audiencias personalizadas de lista de clientes para tu cuenta personal:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Condiciones de herramientas de Facebook para empresas para tu cuenta de empresa:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Un ejemplo de las condiciones que hay que aceptar para las audiencias personalizadas de la lista de clientes.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Un ejemplo de las condiciones que debes aceptar para las herramientas de empresa de Facebook.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

Consulta la [sección de preguntas frecuentes](#terms) para obtener más información sobre la auditoría de tu cuenta de Facebook al realizar la integración.

### Paso 3: Añade un componente de Facebook Audience en Canvas {#step-3-add-a-facebook-audience-component-in-canvas}

Añade un componente en tu Canvas y selecciona **Facebook Audience**.

![Una lista de componentes para añadir al Canvas.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![El componente Sincronización de la audiencia.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 4: Configuración de la sincronización {#step-4-sync-setup}

Selecciona el botón **Custom Audience** para abrir el editor de componentes. A continuación, selecciona **Facebook** como partner de Sincronización de audiencias.

!["Configurar Sincronización de audiencias" con opciones para elegir un partner.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Selecciona la cuenta de anuncios de Facebook deseada. En el desplegable **Choose a New or Existing Audience**, escribe el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una nueva audiencia %}

1. Introduce un nombre para la nueva audiencia personalizada.
2. Selecciona **Add Users to Audience** y elige los campos que deseas sincronizar con Facebook.
3. A continuación, selecciona **Create Audience** para guardar tu audiencia.

![Configuración de sincronización de audiencia para una audiencia con la información de correo electrónico, teléfono, nombre y apellidos para que coincida.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Se te notificará en la parte superior del editor de pasos si la audiencia se ha creado correctamente o si se produce un error durante este proceso. También puedes hacer referencia a esta audiencia para eliminar usuarios más adelante en el recorrido Canvas, porque la audiencia se creó en modo borrador.

Cuando lances un Canvas con una nueva audiencia, Braze creará la nueva audiencia personalizada al lanzar el Canvas y, posteriormente, sincronizará a los usuarios casi en tiempo real cuando entren en el paso Sincronización de audiencia.

{% endtab %}
{% tab Sincronizar con una audiencia existente %}

Braze ofrece la posibilidad de añadir o eliminar usuarios de las audiencias personalizadas de Facebook existentes para confirmar que estas audiencias están actualizadas. Para sincronizar con una audiencia existente, haz lo siguiente:

1. Escribe el nombre de la audiencia existente en el desplegable.
2. Elige si quieres **Add to the Audience** o **Remove from the Audience**.
3. Braze añadirá o eliminará usuarios casi en tiempo real cuando entren en el paso de Facebook Audience.

![Configuración de la sincronización de la audiencia para eliminar la información de correo electrónico, teléfono, nombre y apellidos.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook prohíbe eliminar usuarios de audiencias personalizadas cuando el tamaño de la audiencia es demasiado bajo (normalmente menos de 1.000 usuarios). Como resultado, Braze no puede sincronizar usuarios para una eliminación del paso Sincronización de audiencia hasta que la audiencia alcance el tamaño de audiencia adecuado.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar Canvas {#step-5-launch-canvas}

Después de configurar tu componente Facebook Audience, ¡es hora de lanzar el Canvas! Se crea la nueva audiencia personalizada, y los usuarios que pasan por el paso de Facebook Audience se incluyen en esta audiencia personalizada en Facebook. Si tu Canvas contiene pasos posteriores, tus usuarios avanzarán al siguiente paso en su recorrido de usuario.

La pestaña **History** de la audiencia personalizada en el administrador de audiencias de Facebook reflejará el número de usuarios enviados a la audiencia desde Braze. Si un usuario vuelve a entrar en el paso, se le envía de nuevo a Facebook.

![Detalles de la audiencia y la pestaña Historial de una determinada audiencia de Facebook, que incluye una tabla Historial de la audiencia con columnas para la actividad, los detalles de la actividad, los elementos modificados y la fecha y hora.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Comprender los análisis {#understanding-analytics}

La siguiente tabla incluye métricas y descripciones que te ayudarán a comprender mejor los análisis de tu componente Audience Sync.

| Métrica | Descripción |
| --- | --- |
| Ingresados | Número de usuarios que entraron en este componente para ser sincronizados con Facebook. |
| Avanzaron al paso siguiente | Cuántos usuarios avanzaron al siguiente componente, si lo hay. Todos los usuarios avanzarán automáticamente si este es el último paso en la rama Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Facebook. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. Los campos se emparejan utilizando un operador "OR", lo que significa que mientras un usuario tenga uno de los campos en Facebook, Facebook emparejará al usuario aunque no haya coincidencia en todos los demás campos. |
| Usuarios pendientes | Número de usuarios que están siendo procesados por Braze para sincronizarse con Facebook. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Facebook debido a un error de la API tras unas 13 horas de reintentos. Las posibles causas de error pueden ser un token de Facebook no válido o que se haya eliminado la audiencia personalizada en Facebook. |
| Salieron del Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso en un Canvas es un paso de Facebook. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comprender los análisis" }

{% alert important %}
Hay un retraso en los informes de métricas de usuarios sincronizados y usuarios con errores debido al procesamiento interno.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuánto tardan mis audiencias en aparecer en el panel de mi partner de Audience Sync? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

El tiempo que se tarda en poblar una audiencia depende del partner concreto. Todas las redes procesarán las solicitudes de Braze e intentarán emparejar a los usuarios. Las audiencias personalizadas pueden tardar hasta 24 horas en actualizarse.

### ¿Qué debo hacer si recibo un error de token no válido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Solo tienes que desconectar y volver a conectar tu cuenta de Facebook en la página del partner de Facebook. Confirma con el administrador de tu empresa de Facebook que tienes los permisos adecuados para la cuenta publicitaria con la que deseas sincronizar.

### ¿Por qué no se puede lanzar mi Canvas? {#why-is-my-canvas-not-allowed-to-launch}

- Asegúrate de que tu token de usuario del sistema está autenticado y tiene acceso a las cuentas de anuncios deseadas en Facebook Business Manager.
- Asegúrate de haber seleccionado una cuenta publicitaria, introducido un nombre para la nueva audiencia personalizada y seleccionado los campos que coincidan.
- Puede que hayas alcanzado el límite de 500 audiencias personalizadas en Facebook. Ve al administrador de audiencias de Facebook para eliminar algunas innecesarias antes de crear nuevas audiencias personalizadas utilizando Canvas.

### ¿Cómo sé si los usuarios se han emparejado después de pasarlos a Facebook? {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

Facebook no facilita esta información por motivos de privacidad.

### ¿Braze admite audiencias personalizadas basadas en valores? {#does-braze-support-value-based-custom-audiences}

En este momento, Braze no admite audiencias personalizadas basadas en valores. {% multi_lang_include product_feedback_cta.md context="gap" feature="value-based custom audience sync" %}

### ¿Braze hace hash de los datos antes de enviarlos a los partners de Audience Sync? {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

Una vez normalizados los datos del correo electrónico, Braze los procesa con SHA256.

**IDFA/AAID/teléfono:** Braze hace hash con SHA256. Los tipos de audiencia que sincronizamos son siempre uno de los siguientes:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256.

En cuanto a la frecuencia, Braze solo hará hash de la información de identificación personal (PII) del usuario cuando este entre en el paso de Sincronización de audiencias en el recorrido del usuario como preparación para la sincronización.

### ¿Cómo resuelvo un problema con la sincronización de una audiencia personalizada similar basada en valores? {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

En este momento, Braze no admite audiencias personalizadas similares basadas en valores. Si intentas sincronizar con esta audiencia, pueden producirse errores en el paso Sincronización de audiencia. Para solucionarlo, sigue estos pasos:

1. Ve al panel del administrador de anuncios de Facebook y selecciona **Audiences**.
2. Selecciona **Create audience** > **Custom audience**.
3. Selecciona **Customer list**.
4. Sube tu CSV o lista sin la columna **Value**. Selecciona **No, continue with a customer list that doesn't include customer value**.
5. Termina de crear tu audiencia personalizada.
6. En Braze, actualiza el paso Sincronización de audiencia de Facebook con la audiencia personalizada que has creado.

### He recibido un correo electrónico relacionado con las condiciones del servicio de audiencia personalizada de Facebook. ¿Qué debo hacer para resolverlo? {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

Para utilizar la Sincronización de audiencias con Facebook, debes aceptar estas condiciones de servicio.

- Si tu cuenta publicitaria está directamente asociada a tu cuenta personal de Facebook, puedes aceptar las condiciones del servicio desde tu cuenta personal aquí: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Si tu cuenta publicitaria está vinculada a la cuenta del administrador de empresas de tu empresa, debes aceptar las condiciones del servicio en tu cuenta del administrador de empresas de Facebook aquí: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Después de aceptar las condiciones de servicio de tu audiencia personalizada de Facebook, haz lo siguiente:

1. Actualiza tu token de acceso a Facebook con Braze desconectando y volviendo a conectar tu cuenta de Facebook.
2. Vuelve a habilitar el paso de Sincronización de audiencia de Facebook editando y actualizando tu Canvas.

A continuación, Braze puede sincronizar a los usuarios en cuanto lleguen al paso Sincronización de audiencia de Facebook.

### ¿Qué pasó con los filtros **Connected Facebook** y **Number of Facebook Friends Using App**? {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

Los filtros de segmentación de Braze **Number of Facebook Friends Using App** y **Connected Facebook** están obsoletos. Facebook y los SDK de Braze ya no recopilan los datos subyacentes en los que se basaban esos filtros.

Sustituye los filtros obsoletos por atributos personalizados, eventos personalizados o segmentos basados en la participación; por ejemplo, inicio de sesión en Facebook o vinculación social en lugar de **Connected Facebook**, o referidos, invitaciones y compartidos en lugar de **Number of Facebook Friends Using App**.

Para la reorientación con Canvas, empareja a los usuarios con correo electrónico, teléfono, nombre y apellidos, como se muestra en el [Paso 4: Configuración de la sincronización](#step-4-sync-setup). Para ampliar el alcance, sincroniza un segmento de alto valor con Facebook y crea una audiencia similar en Meta Ads Manager.

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
      <th>Pasos para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Token no válido</b></td>
      <td>Las causas típicas son que el usuario que conectó la integración cambie su contraseña, que caduquen las credenciales, etc.</td>
      <td>Ve a <b>Partner Integrations</b> > <b>Facebook</b> y desconecta y vuelve a conectar tu cuenta. Consulta <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta sección de solución de problemas</a> para conocer los pasos adicionales para auditar tu cuenta de Facebook.</td>
    </tr>
    <tr>
      <td><b>Tamaño de la audiencia demasiado bajo</b></td>
      <td>Este error puede producirse si has creado un paso de Sincronización de audiencia que elimina usuarios de tus audiencias. Si el tamaño de tu audiencia se aproxima a cero, la red puede señalar que el tamaño de la audiencia es demasiado pequeño para servir.</td>
      <td>Utiliza una estrategia de Sincronización de audiencia que añada y elimine usuarios con regularidad, de modo que no agote por completo el tamaño de la audiencia.</td>
    </tr>
    <tr>
      <td><b>La audiencia no existe</b></td>
      <td>El paso Sincronización de audiencia utiliza una audiencia que no existe o que se ha eliminado. Esto también puede desencadenarse si ya no tienes el permiso necesario para acceder a la audiencia.</td>
      <td>Haz que un administrador compruebe en la plataforma del partner si la audiencia sigue existiendo. <br><br>Si existe, confirma si el usuario que conectó la integración tiene permiso para la audiencia. Si no es así, se le debe conceder acceso a esa audiencia. <br><br>Si la audiencia se eliminó intencionadamente, añade una audiencia activa y crea una nueva audiencia en el paso.</td>
    </tr>
    <tr>
      <td><b>Intento de acceso a la cuenta publicitaria</b></td>
      <td>No tienes permisos para la cuenta publicitaria o la audiencia que has seleccionado.</td>
      <td>Trabaja con los administradores de tu cuenta publicitaria para obtener el acceso y los permisos adecuados.</td>
    </tr>
    <tr>
      <td><b>Condiciones del servicio no aceptadas</b></td>
      <td>Para algunos destinos de Sincronización de audiencia, como Facebook, la red publicitaria exige aceptar unas condiciones de servicio específicas para utilizar la característica de Sincronización de audiencia. Este error se desencadenará si no has aceptado las condiciones adecuadas. Como resultado, es posible que también hayas recibido un correo electrónico con este asunto de Braze: "Tus credenciales de autorización para Facebook no son válidas".</td>
      <td>Comprueba que has aceptado las condiciones exigidas por Facebook.</td>
    </tr>
    <tr>
      <td><b>Todos los usuarios presentan errores</b></td>
      <td>Si todos los usuarios presentan errores en un paso a pesar de confirmar que estos usuarios tienen valores para los campos seleccionados en el paso, esto podría indicar un problema con tu cuenta de Facebook.</td>
      <td>Sigue los pasos de <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta sección de solución de problemas</a> para comprobar si tu cuenta tiene algún problema.
      </td>
    </tr>
    <tr>
      <td><b>No se pudo crear la audiencia</b></td>
      <td>En la página de partners tecnológicos de Facebook, aparece "Conectado", pero hay un error en el paso de Sincronización de audiencia de Facebook al sincronizar una audiencia: "Error al crear la audiencia 'nombre de la audiencia'". Ha fallado la autorización de tu cuenta de Facebook. Visita la página de partners tecnológicos para volver a conectar tu cuenta.</td>
      <td>Sigue los pasos de <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta sección de solución de problemas</a> para comprobar si tu cuenta tiene algún problema.
      </td>
    </tr>
    <tr>
      <td><b>Cuenta publicitaria no aparece en el desplegable</b></td>
      <td>Cuando configuras el paso de Facebook Audience, una cuenta publicitaria que esperas no aparece en el selector de cuentas publicitarias.</td>
      <td>Confirma que tu aplicación de Facebook completó la <a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">revisión de la aplicación</a> para <code>ads_management</code> con el nivel de acceso que Facebook requiere para el uso de la API de marketing. En <a href="https://business.facebook.com/">Facebook Business Manager</a>, confirma que el token de usuario del sistema tiene los permisos correctos y está asociado a las cuentas publicitarias que utilizas en Braze, y que se han aceptado las condiciones de la cuenta publicitaria. <br><br>Si el desplegable funciona en un Canvas nuevo pero no en un Canvas que ya editaste, intenta una actualización forzada de tu navegador (o borra la caché) y confirma que has iniciado sesión como un usuario que aún tiene acceso a esas cuentas publicitarias.</td>
    </tr>
    <tr>
      <td><b>Error al validar el token de acceso</b></td>
      <td>Ves un error sobre la validación del token de acceso de Facebook al conectar Braze con Facebook o al sincronizar audiencias.</td>
      <td>Cierra sesión en Facebook en tu navegador. En Braze, ve a <b>Partner Integrations</b> &gt; <b>Facebook</b>, elimina las credenciales de Facebook guardadas y luego vuelve a conectar Facebook. En la página de partners tecnológicos de Facebook para Braze, desconecta y vuelve a conectar la integración si la opción está disponible. <br><br>Si los problemas continúan, sigue los pasos de <a href="#audit-your-facebook-account">Audita tu cuenta de Facebook</a>.</td>
    </tr>
    <tr>
      <td><b>Errores de permisos de exportación o sincronización de audiencia</b></td>
      <td>La exportación o sincronización de una audiencia de Facebook falla con errores de autorización, administrador o cuenta publicitaria.</td>
      <td>En <a href="https://developers.facebook.com/">Meta for Developers</a>, abre tu aplicación y confirma que tu usuario tiene un rol de <b>Admin</b> en <b>App roles</b>. En <b>App settings</b> &gt; <b>Advanced</b>, confirma que <b>Advertising accounts</b> incluye las cuentas que utilizas con Braze. En <a href="https://business.facebook.com/latest/settings">Business settings</a>, confirma que el usuario que conecta o el usuario del sistema tiene acceso a la cuenta publicitaria correcta.</td>
    </tr>
  </tbody>
</table>

### Audita tu cuenta de Facebook {#audit-your-facebook-account}

Si experimentas problemas adicionales con tu integración, consulta las siguientes secciones y pasos para auditar tu cuenta de Facebook.

#### Revisar los permisos de la cuenta {#review-account-permissions}

1. Revisa [la documentación de Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) sobre cómo gestionar estos permisos en su plataforma. Para Facebook Business Manager, necesitas al menos un rol de **Admin** o de **Employee** del Business Manager con acceso a las cuentas de anuncios necesarias.
2. Como **Employee**, confirma que el administrador te concede todos los permisos de **Manage Ad Account** para cada cuenta de anuncios para crear una audiencia o sincronizar usuarios con la audiencia.
3. Una vez concedido, deberás desconectar y volver a conectar tu cuenta.

#### Acepta las condiciones del servicio {#terms}

Acepta las condiciones de servicio (CDS) pendientes de Facebook. Facebook requerirá periódicamente que tú (el usuario) y el administrador de la empresa aprueben de nuevo sus condiciones de servicio.

1. El usuario conectado debe aceptar todas las condiciones de servicio de cada una de sus cuentas publicitarias:
- Condiciones de audiencia personalizada para tu cuenta personal de Facebook:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Una cuenta con todos los permisos de control para administrar una cuenta publicitaria.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Para encontrar tu cuenta y tu ID de empresa, sigue estos pasos:

1. Ve a tu [cuenta de administrador de anuncios de Facebook](https://adsmanager.facebook.com/).
2. Confirma que estás utilizando la cuenta publicitaria correcta verificándola en el menú desplegable.
3. En la URL, busca el ID de cuenta después de `act=` y el ID de empresa después de `business_id=`

![La URL con el ID de cuenta y el ID de empresa resaltados.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Lee y selecciona **Accept** para las condiciones de la audiencia personalizada. Te recomendamos que confirmes para qué cuenta se están firmando las condiciones de servicio utilizando el desplegable de la parte superior de las condiciones.

![El desplegable que muestra la cuenta que está firmando las condiciones de servicio.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. Debes seleccionar **Accept** para las condiciones del servicio. Después, verás este mensaje: "You have accepted these terms of service on behalf of Braze".
6. Actualiza tu token de acceso a Facebook con Braze desconectando y volviendo a conectar tu cuenta de Facebook.
7. Vuelve a habilitar el paso de Sincronización de audiencia de Facebook editando y actualizando tu Canvas. Braze podrá sincronizar a los usuarios en cuanto lleguen al paso de Facebook Audience.
8. Si el problema persiste, prueba a utilizar otro usuario con permisos de administrador para aceptar manualmente las condiciones a través del administrador de anuncios.

#### Completa las tareas pendientes {#complete-any-pending-tasks}

Comprueba si tienes alguna tarea pendiente con Facebook que pudiera estar bloqueándote el uso de los servicios de Facebook Ads:

1. [Inicia sesión en el administrador de anuncios de Facebook](https://adsmanager.facebook.com/).
2. Selecciona la cuenta publicitaria con la que tienes problemas.
3. En la navegación, selecciona tu **Account Overview**. <br> ![La navegación con el resumen de cuenta seleccionado.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Comprueba si hay alguna alerta que deba ser atendida. <br> ![Una cuenta con una tarjeta de crédito caducada.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Comprueba si hay alguna tarea de configuración que deba completarse. <br> ![Una cuenta con una configuración de cuenta parcialmente completada.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Conectar con otro usuario {#connect-with-a-different-user}

Como otro paso de solución de problemas, recomendamos que otro usuario administrador intente conectar su cuenta haciendo lo siguiente:

1. Desconecta la integración actual.
2. Otro usuario con permisos de administrador conecta su cuenta de usuario de Facebook.
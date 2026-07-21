---
nav_title: Editor tradicional
article_title: Crear un mensaje dentro de la aplicación en el editor tradicional
page_order: 2
description: "Este artículo de referencia explica cómo crear un mensaje dentro de la aplicación usando la plataforma Braze mediante Campaigns o Canvas."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Crear un mensaje dentro de la aplicación con el editor tradicional {#create-an-in-app-message-with-the-traditional-editor}

> Puedes crear un mensaje dentro de la aplicación o un mensaje en el explorador usando la plataforma Braze mediante Campaigns, Canvas o como una Campaign de API. Te recomendamos encarecidamente que planifiques tus mensajes y prepares todos los materiales con antelación utilizando nuestra práctica [guía de preparación de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices).

## Paso 1: Elige dónde crear tu mensaje {#create-new-campaign-in-app}

¿No tienes claro si tu mensaje debe enviarse mediante una Campaign o un Canvas? Las Campaigns son mejores para campañas de mensajería únicas y dirigidas, mientras que los Canvas son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear Campaign**.
2. Selecciona **In-App Message**. Ten en cuenta que los mensajes dentro de la aplicación no están disponibles en Campaigns multicanal.
3. Ponle a tu Campaign un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.
   * Las etiquetas facilitan encontrar tus Campaigns y generar informes a partir de ellas. Por ejemplo, al usar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder), puedes filtrar por etiquetas específicas.
5. Añade y nombra tantas variantes como necesites para tu Campaign. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si todos los mensajes de tu Campaign van a ser similares o tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando el creador de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Ponle a tu paso un nombre claro y significativo.
3. Elige una [planificación de paso]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) y especifica un retraso según sea necesario. Ten en cuenta que los pasos que contienen mensajes dentro de la aplicación no pueden estar basados en acciones.
4. Filtra tu audiencia para este paso, según sea necesario. Puedes refinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso, en el momento en que se envíen los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
6. Elige cualquier otro canal de mensajería que desees combinar con tu mensaje.

{% alert important %}
No puedes tener múltiples variantes de mensajes dentro de la aplicación en un solo paso.
{% endalert %}

Puedes encontrar más información específica de Canvas en [Mensajes dentro de la aplicación en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Paso 2: Especifica las plataformas de entrega {#step-2-specify-delivery-platforms}

Comienza eligiendo qué plataformas deben recibir el mensaje. Usa esta selección para limitar la entrega de una Campaign a un conjunto específico de aplicaciones. Por ejemplo, podrías elegir **Web Browsers** para un mensaje en el explorador que anime a los usuarios a descargar tu aplicación móvil, para asegurarte de que no reciban el mensaje después de haber obtenido tu aplicación. Dado que las selecciones de plataforma son específicas de cada variante, podrías probar la participación con el mensaje por plataforma.

| Plataforma                        | Entrega del mensaje             |
|---------------------------------|------------------------------|
| Mobile Apps                     | SDK de iOS, Android y Vega |
| Web Browsers                    | SDK web                      |
| Both Mobile Apps & Web Browsers | SDK de iOS, Android, Vega y web |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Especifica las plataformas de entrega" }

## Paso 3: Especifica tus tipos de mensaje {#step-3-specify-your-message-types}

Una vez que hayas seleccionado una plataforma de envío, explora los tipos de mensaje, diseños y otras opciones asociadas. Obtén más información sobre el comportamiento esperado y la apariencia de cada uno de estos mensajes en nuestra página de [Tipos de mensaje]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types), o haciendo clic en los tipos de mensaje enlazados en las siguientes tablas.

Al decidir qué tipo de mensaje usar, considera cuánto espacio ocupará tu mensaje y cuán disruptivo puede resultar para la experiencia del usuario.

- Los mensajes de **deslizamiento hacia arriba** son los menos intrusivos, apareciendo sutilmente sin bloquear el contenido.
- Los mensajes **modales** se sitúan en un punto intermedio: lo suficientemente prominentes para captar la atención sin ocupar toda la pantalla.
- Los mensajes de **pantalla completa** son los que más llaman la atención y son ideales para anuncios o promociones importantes.

Cuanto más complejo sea tu contenido, más espacio necesitarás, y más probable será que tu mensaje interrumpa el flujo del usuario.

### Tipos de mensaje {#message-types}

Estos mensajes dentro de la aplicación son aceptados tanto por aplicaciones móviles como por aplicaciones web.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table aria-label="Tipos de mensaje" class="tg">
  <caption>Tipos de mensaje</caption>
<thead>
  <tr>
    <th>Tipo de mensaje</th>
    <th>Descripción del tipo</th>
    <th>Diseños disponibles</th>
    <th>Otras opciones</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/fullscreen'>Pantalla completa</a></td>
    <td>Mensajes que cubren toda la pantalla con un bloque de mensaje.</td>
    <td>
      <ul>
      <li>Imagen y texto</li>
      <li>Solo imagen</li>
      </ul>
    </td>
    <td>Orientación del dispositivo forzada (vertical u horizontal)</td>
    <td>¡Grande y llamativo! Úsalo cuando quieras asegurarte de que los usuarios vean tu contenido, como tus campañas más importantes, notificaciones relevantes o promociones masivas.<br><br>Ten en cuenta que en dispositivos móviles, los mensajes en vertical y horizontal no se mostrarán si la orientación del dispositivo no coincide con la orientación del mensaje.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/modal'>Modal</a></td>
    <td>Mensajes que cubren toda la pantalla con una superposición y un bloque de mensaje.</td>
    <td>
      <ul>
      <li>Texto (con imagen opcional)</li>
      <li>Solo imagen</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Un buen punto intermedio. Úsalo cuando necesites una forma evidente de captar la atención de tu usuario, como animarle a probar una nueva característica o aprovechar una promoción.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/slideup'>Deslizamiento hacia arriba</a></td>
    <td>Mensajes que se deslizan a la vista en un lugar designado sin bloquear el resto de la pantalla.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Discreto: ocupa la menor cantidad de espacio en pantalla. Úsalo para alertar a los usuarios sobre pequeños fragmentos de información, como nuevas características, anuncios, uso de cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Tipos de mensaje avanzados {#advanced-message-types}

Estos mensajes dentro de la aplicación son personalizables según tus necesidades.

<table aria-label="Tipos de mensaje avanzados" class="tg">
  <caption>Tipos de mensaje avanzados</caption>
<thead>
  <tr>
    <th>Tipo de mensaje</th>
    <th>Descripción del tipo</th>
    <th>Diseños disponibles</th>
    <th>Requisitos</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/custom_html'>Mensaje HTML personalizado</a></td>
    <td>Mensajes personalizados que funcionan según lo definido en tu código personalizado (HTML, CSS y/o JavaScript).</td>
    <td>N/A</td>
    <td>Debes establecer la opción de inicialización <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> en <code>true</code> para que tu mensaje dentro de la aplicación funcione.</td>
    <td>Esta es una buena opción si quieres todas las ventajas de los mensajes dentro de la aplicación pero necesitas funcionalidad adicional o que la apariencia se mantenga acorde a tu marca. Puedes modificar cada pequeño detalle del mensaje: fuente, color, forma, tamaño, botones, etc. <br><br>Ejemplos de casos de uso incluyen pedir a los usuarios comentarios sobre la aplicación, formularios de captura de correo electrónico o mensajes paginados</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/email_capture_form'>Formulario de captura de correo electrónico</a></td>
    <td>Normalmente se usa para capturar el correo electrónico del espectador.</td>
    <td>N/A</td>
    <td>Debes establecer la opción de inicialización <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> en <code>true</code> para que tu mensaje dentro de la aplicación funcione.</td>
    <td>Cuando solicitas a los usuarios que envíen su dirección de correo electrónico.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#web-modal-css'>Modal web con CSS</a></td>
    <td>Mensajes modales para web con CSS personalizable.</td>
    <td>
      <ul>
      <li>Texto (con imagen opcional)</li>
      <li>Solo imagen</li>
      </ul>
    </td>
    <td>El modal web con CSS es exclusivo del SDK web y solo se puede usar después de seleccionar <b>Web Browsers</b>.</td>
    <td>Cuando quieras cargar o escribir CSS personalizado para crear mensajes con un estilo completamente personalizado y atractivo.</td>
  </tr>
</tbody>
</table>

{% alert important %}
Si Braze detecta que no has incluido un botón de cierre o descarte en tu código, te solicitaremos que añadas uno. Para tu comodidad, hemos proporcionado un fragmento de código que puedes copiar y pegar en tu código: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Paso 4: Redacta tu mensaje dentro de la aplicación {#step-4-compose-your-in-app-message}

La pestaña **Compose** te permite editar todos los aspectos del contenido y comportamiento de tu mensaje.

![Un ejemplo de mensaje dentro de la aplicación de una marca para dar la bienvenida a nuevos clientes y pedirles que configuren un perfil de usuario.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

El contenido de la pestaña **Compose** varía según las opciones de mensaje elegidas en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

### Idioma {#language}

Selecciona **Add Languages** y elige los idiomas deseados de la lista proporcionada. Esto insertará [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) en tu mensaje. Te recomendamos seleccionar tus idiomas antes de escribir tu contenido para que puedas completar tu texto donde corresponda en el Liquid. Consulta nuestra [lista completa de idiomas disponibles]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

### Imagen {#image}

Dependiendo de tu tipo de mensaje, puedes **Upload Image**, **Pick a Badge** o usar **Font Awesome**. Para cargar una imagen, selecciona **Add Image** o proporciona una URL de imagen. Al seleccionar **Add Image** se abre la **Media Library**, donde puedes seleccionar una imagen cargada previamente o añadir una nueva. Cada tipo de mensaje y plataforma puede tener sus propias proporciones y requisitos sugeridos; asegúrate de verificar cuáles son antes de encargar o crear una imagen desde cero.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Encabezado y cuerpo {#header-and-body}

¡Escribe lo que quieras! Incluye texto completamente personalizado (a menudo con capacidades de HTML personalizado) con las opciones de incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) y otros tipos de personalización. Cuanto más rápido puedas transmitir tu mensaje y lograr que tu cliente haga clic, ¡mejor! Recomendamos encabezados y contenido de mensaje claros y concisos.

Algunos tipos de mensaje no necesitan y, por lo tanto, no solicitan encabezados.

#### Consejos {#tips}

##### Generar texto con IA {#generating-ai-copy}

¿Necesitas ayuda para crear un texto increíble? Prueba usar el [asistente de redacción con IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Introduce un nombre o descripción de producto y la IA generará un texto de marketing similar al humano para usar en tu mensajería.

![Botón Lanzar redactor con IA, ubicado en el campo Mensaje del creador de mensajes dentro de la aplicación.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Crear mensajes de derecha a izquierda {#creating-right-to-left-messages}

¿Necesitas ayuda para crear mensajes de derecha a izquierda para idiomas como el árabe y el hebreo? Consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) para conocer las mejores prácticas.

### Texto de botón {#buttons}

Cuando esté disponible para tu tipo de mensaje, puedes tener hasta dos botones que aparezcan debajo del cuerpo de texto. Puedes crear y editar el texto y color personalizados de los botones. También puedes añadir un enlace a los Términos de servicio dentro de los formularios de captura de correo electrónico.

Si eliges usar solo un botón, se ajustará automáticamente para ocupar el espacio disponible en la parte inferior de tu mensaje en lugar de dejar espacio para un botón adicional.

#### Elegir un botón principal {#choosing-a-primary-button}

Si decides dar formato a estos botones con tus propios colores, te recomendamos que uses el Botón 2 para tu resultado preferido.

En otras palabras, si quieres que tu usuario haga clic en un botón más que en el otro, asegúrate de que sea el botón secundario. El botón secundario a menudo ha mostrado un mejor potencial para recibir clics, especialmente si tiene un color algo contrastante o que destaque del resto del mensaje. Esto se enfatiza aún más cuando el botón principal se mezcla más visualmente con el mensaje.

![Botones principal y secundario en un mensaje dentro de la aplicación]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportamiento al hacer clic {#button-actions}

Cuando tu cliente hace clic en un botón de tu mensaje dentro de la aplicación, están disponibles las siguientes acciones.

| Acción | Descripción |
|---|---|
| Redirigir a URL web | Abre una página web no nativa. |
| [Vínculo profundo a la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Enlaza directamente a una pantalla existente en tu aplicación. |
| Cerrar mensaje | Cierra el mensaje activo actualmente. |
| Registrar evento personalizado | Elige un [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events) para desencadenar. Se puede usar para mostrar otro mensaje dentro de la aplicación o desencadenar mensajería adicional. |
| Registrar atributo personalizado | Elige un [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) para establecer para el usuario actual. |
| Solicitar permiso push | Muestra el permiso push nativo. Lee más sobre [preparación para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), así como las [mejores prácticas]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#best-practices) para preparar a los usuarios para push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamiento al hacer clic" }

Nota: las opciones __Solicitar permiso push__, __Registrar evento personalizado__ y __Registrar atributo personalizado__ requieren las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Para combinar múltiples acciones o realizar acciones adicionales del SDK no disponibles en el panel (como añadir a un grupo de suscripción o establecer un tipo de suscripción de correo electrónico), puedes usar [vínculos profundos de Braze Actions]({{site.baseurl}}/developer_guide/braze_actions).

### Opciones de dispositivos iOS {#ios-device-options}

Si lo deseas, puedes restringir tu mensaje dentro de la aplicación para que solo se envíe a dispositivos iOS. Para hacerlo, haz clic en **Change** y selecciona **Only send to iOS devices**.

### Cierre del mensaje {#message-close}

Elige entre las siguientes opciones:

- **Dismiss Automatically:** Selecciona cuántos segundos permanecerá el mensaje en pantalla.
- **Wait for User Swipe or Touch:** Requiere una opción de descarte o cierre.

### Posición del deslizamiento hacia arriba {#slide-up-position}

Esta configuración solo se aplica al tipo de mensaje de deslizamiento hacia arriba. Elige entre que tu deslizamiento aparezca **From Bottom of App Screen** o **From Top of App Screen**.

### HTML y activos {#html-and-assets}

Esta configuración solo se aplica al tipo de mensaje de código personalizado. Copia y pega HTML en el espacio disponible y carga tus activos usando un archivo ZIP.

### Marcador de posición de entrada de captura de correo electrónico {#email-capture-input-placeholder}

Esta configuración solo se aplica al tipo de mensaje de formulario de captura de correo electrónico. Introduce un texto personalizado que aparecerá como texto de marcador de posición en el campo de entrada de correo electrónico. El valor predeterminado es "Enter your email address".

## Paso 5: Dale estilo a tu mensaje dentro de la aplicación {#step-5-style-your-in-app-message}

La pestaña **Style** te permite ajustar todos los aspectos visuales de tu mensaje. Carga una imagen o insignia, o elige un icono de insignia prediseñado. Cambia los colores del texto del encabezado y cuerpo, botones y fondo seleccionando de una paleta o introduciendo un código hexadecimal, RGB o HSB.

El contenido de la pestaña **Style** varía según las opciones de mensaje elegidas en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

| Formato | Entrada | Descripción |
|---|---|---|
| [Perfil de color]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#reusable-color-profiles) | Aplicar desde la galería de plantillas de mensajes dentro de la aplicación. | Selecciona **Apply Template** y elige de la galería. Luego, selecciona **Save**. |
| Alineación de texto | Izquierda, centro o derecha. | Solo disponible para versiones más recientes del SDK de Braze. |
| Encabezado | Código de color HEX. | Se mostrará el color HEX deseado. También podrás elegir la opacidad del color. |
| Texto | Código de color HEX. | Se mostrará el color HEX deseado. También podrás elegir la opacidad del color. |
| Botones | Código de color HEX. | Se mostrarán los colores HEX deseados. También podrás elegir la opacidad de los colores. Puedes elegir colores para: el fondo del botón de cierre del mensaje, así como el fondo, texto y borde de cada botón. |
| Borde del botón | Código de color HEX. | ¡Nuevo! Esto te permitirá diferenciar tus botones principal y secundario. Sugerimos delinear los botones con colores contrastantes. |
| Color de fondo | Código de color HEX. | Se mostrará el color HEX deseado. También podrás elegir la opacidad del color. Este es el fondo de todo el mensaje y se mostrará claramente detrás del cuerpo de texto. |
| Superposición de pantalla | Código de color HEX. | Se mostrará el color HEX deseado. También podrás elegir la opacidad del color. Solo disponible para versiones más recientes del SDK de Braze. Este es el marco alrededor de todo el mensaje. |
| Chevron u otra opción de cierre de mensaje | Código de color HEX. | Se mostrará el color HEX deseado. También podrás elegir la opacidad del color. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 5: Dale estilo a tu mensaje dentro de la aplicación" }

Siempre [previsualiza y prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) tu mensaje antes de enviarlo.

{% alert important %}
Algunos tipos de mensajes dentro de la aplicación no tienen la opción de estilizar más allá de cargar HTML personalizado (o CSS o JavaScript) y activos usando un archivo ZIP. [Modal web con CSS]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#web-modal-css) te permite cargar o escribir CSS personalizado para crear mensajes con un estilo completamente personalizado y atractivo.
{% endalert %}

## Paso 6: Configura ajustes adicionales (opcional) {#step-6-configure-additional-settings-optional}

### Pares clave-valor {#key-value-pairs}

Puedes añadir [pares clave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) para enviar campos personalizados adicionales a los dispositivos de los usuarios.

## Paso 7: Construye el resto de tu Campaign o Canvas {#step-7-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construye el resto de tu Campaign; consulta las siguientes secciones para obtener más orientación sobre cómo usar mejor nuestras herramientas para crear mensajes dentro de la aplicación.

### Elige un desencadenante {#choose-a-trigger}

Selecciona la acción que deseas que desencadene tu mensaje, así como las horas de inicio y fin de tu Campaign o Canvas.

{% alert important %}
Ten en cuenta que si pretendes desencadenar tu mensaje dentro de la aplicación basándote en un evento personalizado, ese evento personalizado debe enviarse usando el SDK.
{% endalert %}

![Campaign basada en acciones con la acción desencadenante configurada como "Start Session".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

La entrega de mensajes dentro de la aplicación se basa completamente en los siguientes desencadenantes de acción:

- Realizar una compra
- Abrir la aplicación o página web
- Realizar un evento personalizado (solo funciona con eventos enviados usando el SDK)
- Abrir un mensaje push específico
- Planificar automáticamente Campaigns para enviar a una hora determinada respecto a la hora local de cada uno de tus usuarios.
- Los mensajes también se pueden configurar para repetirse de forma diaria, semanal (opcionalmente en días específicos) o mensual.

Se debe seleccionar una fecha y hora de inicio; sin embargo, una fecha de fin es opcional. Una fecha de fin impedirá que ese mensaje dentro de la aplicación específico se muestre en los dispositivos después de la fecha/hora especificada.

Consulta nuestra documentación para desarrolladores sobre [desencadenamiento de eventos del lado del servidor]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web) y [entrega local de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery#local-in-app-messages).

#### Desencadenamiento en línea versus sin conexión {#online-versus-offline-triggering}

Los mensajes dentro de la aplicación funcionan enviando el mensaje y los desencadenantes al dispositivo del usuario. Una vez que los mensajes dentro de la aplicación están en un dispositivo, esperan para mostrarse hasta que se cumpla la condición del desencadenante. Si los mensajes dentro de la aplicación ya están almacenados en caché en el dispositivo del usuario, incluso puedes desencadenar mensajes dentro de la aplicación sin conexión, sin conexión a Braze (por ejemplo, en modo avión).

{% alert important %}
Una vez que un mensaje dentro de la aplicación ha sido detenido, puede haber algunos usuarios que continúen viendo el mensaje si iniciaron una sesión antes de que el mensaje fuera detenido y posteriormente realizan el evento desencadenante. Estos usuarios se contarán como una impresión única incluso después de que la Campaign haya sido detenida.
{% endalert %}

### Elige una prioridad {#choose-a-priority}

Finalmente, después de haber seleccionado la acción que desencadenará el mensaje dentro de la aplicación, también debes establecer una prioridad. Si dos mensajes se desencadenan por la misma acción, los mensajes de alta prioridad se programarán para aparecer en los dispositivos de los usuarios antes que los mensajes con prioridades más bajas.

Puedes elegir entre las siguientes prioridades de mensaje:

- Alta prioridad (se muestra antes que otros mensajes)
- Prioridad media (predeterminada)
- Baja prioridad (se muestra después de otros mensajes)

Las opciones de alta, media y baja prioridad para mensajes desencadenados son contenedores, y como tales, múltiples mensajes podrían tener la misma prioridad seleccionada. Cuando múltiples mensajes comparten la misma prioridad, el mensaje creado o asignado más recientemente tiene precedencia y se muestra primero:

- **Contenedor de prioridad predeterminada:** Cuando dos Campaigns comparten el mismo desencadenante y usan la prioridad predeterminada (media), la Campaign creada más recientemente recibe el desencadenante.
- **Contenedor de prioridad específica:** Cuando múltiples Campaigns comparten el mismo desencadenante y se asignan a un contenedor de prioridad específico, la Campaign asignada más recientemente a ese contenedor recibe el desencadenante.

Para establecer prioridades dentro de estos contenedores, haz clic en **Set Exact Priority**, y puedes arrastrar y soltar Campaigns para ordenarlas con la prioridad correcta.

![Un ejemplo de cómo se establece la prioridad para una Campaign y un Canvas de mensajes dentro de la aplicación.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

### Elige los usuarios objetivo {#choose-users-to-target}

A continuación, debes [dirigirte a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) eligiendo segmentos o filtros para delimitar tu audiencia. Recibirás automáticamente una instantánea de cómo se ve aproximadamente la población de ese segmento. Ten en cuenta que la pertenencia exacta al segmento siempre se calcula antes de que se envíe el mensaje.

{% alert note %}
Si hay un retraso en el paso del mensaje dentro de la aplicación, la pertenencia al segmento se evaluará después del retraso. Si el usuario es elegible, el mensaje dentro de la aplicación se sincronizará en la siguiente sesión disponible.
{% endalert %}

#### Reevaluar la elegibilidad de la Campaign y Liquid {#re-evaluate-campaign-eligibility-and-liquid}

En algunos escenarios, es posible que desees reevaluar la elegibilidad de un usuario cuando desencadena un mensaje dentro de la aplicación para mostrarse. Los ejemplos incluyen Campaigns que se dirigen a un atributo personalizado que cambia con frecuencia o mensajes que deben reflejar cualquier cambio de perfil de último momento.

![Casilla de verificación para reevaluar la elegibilidad de la Campaign antes de mostrar, seleccionada.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Cuando seleccionas **Re-evaluate campaign eligibility before displaying**, se realizará una solicitud adicional a Braze para confirmar que el usuario sigue siendo elegible para este mensaje antes de enviarlo. Además, cualquier variable de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) o [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) se procesará en ese momento antes de que se muestre el mensaje.

Esto evita que se envíen mensajes dentro de la aplicación a usuarios dentro de Campaigns expiradas o archivadas. Si no reevalúas la elegibilidad de un usuario, este recibirá el mensaje dentro de la aplicación incluso después de que la Campaign haya expirado o esté archivada, porque el mensaje está en tu SDK y esperando a que los usuarios lo desencadenen.

{% alert note %}
Habilitar esta opción resultará en un ligero retraso (< 100 ms) entre el momento en que un usuario desencadena un mensaje dentro de la aplicación y el momento en que se muestra el mensaje, debido a la solicitud adicional de elegibilidad y procesamiento de plantillas.
<br><br>
No uses esta opción para mensajes que pueden desencadenarse mientras un usuario está sin conexión o cuando la reevaluación de elegibilidad y Liquid no es necesaria.
{% endalert %}

#### Usar datos añadidos por REST API en un mensaje {#use-data-added-by-rest-api-in-a-message}

Los datos de usuario que el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) añade en la misma sesión a veces se pueden usar en el mensaje dentro de la aplicación de ese usuario. Por ejemplo, si un usuario está en la audiencia de un mensaje dentro de la aplicación que está esperando un desencadenante, inicia una sesión, y en esa misma sesión la REST API actualiza su perfil, esos nuevos datos pueden aparecer en el mensaje dentro de la aplicación cuando se selecciona **Re-evaluate campaign eligibility before displaying**. Braze no procesará la plantilla del mensaje dentro de la aplicación hasta que sea el momento de renderizarlo.

Si un desencadenante envía datos a Braze y dispara el mensaje dentro de la aplicación simultáneamente, el mensaje no puede usar esos datos de perfil recién actualizados, incluso con un retraso planificado. Usa dos desencadenantes separados en su lugar: uno para enviar los datos y otro para desencadenar el mensaje dentro de la aplicación.

### Elige eventos de conversión {#choose-conversion-events}

Braze te permite rastrear con qué frecuencia los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), después de recibir una Campaign. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

{% endtab %}
{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente de Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariantes y selección inteligente, y más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) de nuestra documentación de Canvas.

Para información sobre opciones de mensajes dentro de la aplicación específicas de Canvas, consulta [Mensajes dentro de la aplicación en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Paso 8: Revisa e implementa {#step-8-review-and-deploy}

Después de haber terminado de construir la última parte de tu Campaign o Canvas, revisa sus detalles, [pruébala]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) y luego ¡envíala!

A continuación, consulta [Informes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) para aprender cómo puedes acceder a los resultados de tus campañas de mensajería.

## Cosas que debes saber {#things-to-know}

### Límites de Campaigns activas de mensajes dentro de la aplicación {#active-in-app-message-campaign-limits}

Braze valora la fiabilidad y la velocidad. Te sugerimos que envíes solo los datos que necesites a Braze y desactives cualquier Campaign que ya no aporte valor a tu marca.

Procesar Campaigns de mensajes dentro de la aplicación basadas en acciones que todavía están en estado activo pero que ya no envían mensajes o que ya no son necesarias ralentiza el rendimiento general de los servicios de Braze para ti y otros clientes. Este tiempo adicional necesario para procesar estos grandes números de Campaigns inactivas significa que cualquier mensaje dentro de la aplicación tardará más en aparecer en los dispositivos del usuario final, lo que impacta la experiencia del usuario final.

{% alert important %}
Puedes tener hasta 200 Campaigns activas de mensajes dentro de la aplicación basadas en acciones por espacio de trabajo para optimizar la velocidad de entrega de mensajes y prevenir tiempos de espera. Esto no se aplica a los Canvas.
{% endalert %}

El conteo de 200 incluye Campaigns activas de mensajes dentro de la aplicación que aún no han alcanzado su hora de fin y aquellas que no tienen hora de fin. Las Campaigns activas de mensajes dentro de la aplicación que han superado su hora de fin no se contarán. El cliente promedio de Braze tiene un total de 26 Campaigns activas a la vez, por lo que es poco probable que esta limitación te afecte.

### Evaluación de entrega según la zona horaria local {#local-time-delivery-evaluation}

Cuando una Campaign de mensajes dentro de la aplicación se planifica usando la zona horaria local del usuario, la evaluación de la hora de inicio y fin de la Campaign se gestiona en el propio dispositivo.

Las Campaigns de mensajes dentro de la aplicación normalmente se envían al dispositivo del usuario cuando se inicia o se actualiza la sesión de la aplicación. En ese momento:

1. El SDK evalúa si el usuario califica para algún mensaje dentro de la aplicación basado en desencadenantes.
2. El dispositivo comprueba si el evento desencadenante del usuario ocurrió dentro de la hora de inicio y fin de la Campaign (según la zona horaria local del usuario).
3. Si se cumplen ambas condiciones, el mensaje dentro de la aplicación es elegible para mostrarse.

#### Consideraciones {#considerations}

- Si un usuario desencadena un evento (como tocar un botón) poco después de que se entregue el mensaje dentro de la aplicación, es posible que el mensaje no aparezca hasta la siguiente actualización de sesión, siempre que se sigan cumpliendo todos los criterios de elegibilidad.
- De manera similar a otros tipos de canales, las Campaigns de mensajes dentro de la aplicación idealmente deben lanzarse con 24-48 horas de antelación. Este margen da a los usuarios tiempo suficiente para cumplir los criterios de elegibilidad e iniciar una sesión para que el mensaje sea evaluado y mostrado.
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
5. Añade y nombra tantas variantes como necesites para tu Campaign. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si todos los mensajes de tu Campaign van a ser similares o tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md in_app_message=true %}

{% alert important %}
No puedes tener múltiples variantes de mensajes dentro de la aplicación en un solo paso.
{% endalert %}

Puedes encontrar más información específica de Canvas en [Mensajes dentro de la aplicación en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Paso 2: Especificar las plataformas de entrega {#step-2-specify-delivery-platforms}

Comienza eligiendo qué plataformas deben recibir el mensaje. Usa esta selección para limitar la entrega de una campaña a un conjunto específico de aplicaciones. Por ejemplo, podrías elegir **Navegadores web** para un mensaje en el explorador que anime a los usuarios a descargar tu aplicación móvil, para asegurarte de que no reciban el mensaje después de haber obtenido ya tu aplicación. Dado que las selecciones de plataforma son específicas de cada variante, podrías probar la participación del mensaje por plataforma.

| Plataforma                                    | Entrega del mensaje             |
|------------------------------------------------|---------------------------------|
| Aplicaciones móviles                           | SDK de iOS, Android y Vega      |
| Navegadores web                                | SDK Web                         |
| Aplicaciones móviles y navegadores web         | SDK de iOS, Android, Vega y Web |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Especificar las plataformas de entrega" }

## Paso 3: Especifica los tipos de mensaje {#step-3-specify-your-message-types}

Una vez que hayas seleccionado una plataforma de envío, explora los tipos de mensaje, diseños y otras opciones asociadas. Obtén más información sobre el comportamiento esperado y la apariencia de cada uno de estos mensajes en nuestra página de [Tipos de mensaje]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types), o haciendo clic en los tipos de mensaje vinculados en las siguientes tablas.

Al decidir qué tipo de mensaje usar, considera cuánto espacio ocupará tu mensaje y cuán disruptivo puede resultar para la experiencia del usuario.

- Los mensajes de **deslizamiento hacia arriba** son los menos intrusivos, ya que aparecen de forma sutil sin bloquear el contenido.
- Los mensajes **modales** se sitúan en un punto intermedio: lo suficientemente prominentes para captar la atención sin ocupar toda la pantalla.
- Los mensajes de **pantalla completa** son los que más llaman la atención y son ideales para anuncios críticos o promociones.

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
    <td>¡Grande y llamativo! Úsalo cuando quieras asegurarte de que los usuarios vean tu contenido, como tus Campaigns más importantes, notificaciones críticas o promociones masivas.<br><br>Ten en cuenta que en dispositivos móviles, los mensajes en vertical y horizontal no se mostrarán si la orientación del dispositivo no coincide con la orientación del mensaje.</td>
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
    <td>Un buen punto intermedio. Úsalo cuando necesites una forma evidente de captar la atención del usuario, como animar a los usuarios a probar una nueva característica o aprovechar una promoción.</td>
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
    <td>Esta es una buena opción si quieres todas las ventajas de los IAM pero necesitas funcionalidad adicional o que la apariencia se mantenga acorde a tu marca. Puedes modificar cada detalle del mensaje: fuente, color, forma, tamaño, botones, etc. <br><br>Ejemplos de uso incluyen solicitar a los usuarios comentarios sobre la aplicación, formularios de captura de correo electrónico o mensajes paginados</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/email_capture_form'>Formulario de captura de correo electrónico</a></td>
    <td>Se utiliza normalmente para capturar el correo electrónico del espectador.</td>
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
    <td>Cuando quieras cargar o escribir CSS personalizado para crear mensajes con un estilo completamente personalizado y atractivo. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Si Braze detecta que no has incluido un botón de cierre o descarte en tu código, te solicitaremos que añadas uno. Para tu comodidad, hemos proporcionado un fragmento de código que puedes copiar y pegar en tu código: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Paso 4: Redacta tu mensaje dentro de la aplicación {#step-4-compose-your-in-app-message}

La pestaña **Redactar** te permite editar todos los aspectos del contenido y el comportamiento de tu mensaje.

![Ejemplo de mensaje dentro de la aplicación de una marca para dar la bienvenida a nuevos clientes e invitarlos a configurar un perfil de usuario.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

El contenido de la pestaña **Redactar** varía en función de las opciones de mensaje elegidas en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

### Idioma {#language}

Selecciona **Añadir idiomas** y elige los idiomas deseados de la lista proporcionada. Esto insertará [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) en tu mensaje. Te recomendamos seleccionar los idiomas antes de escribir el contenido para que puedas completar el texto donde corresponda en el Liquid. Consulta nuestra [lista completa de idiomas disponibles]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

### Imagen {#image}

Dependiendo del tipo de mensaje, puedes **Subir imagen**, **Elegir una señal** o usar **Font Awesome**. Para subir una imagen, selecciona **Añadir imagen** o proporciona una URL de imagen. Al seleccionar **Añadir imagen** se abre la **Biblioteca multimedia**, donde puedes seleccionar una imagen subida previamente o añadir una nueva. Cada tipo de mensaje y plataforma puede tener sus propias proporciones y requisitos sugeridos; asegúrate de verificar cuáles son antes de encargar o crear una imagen desde cero.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Encabezado y cuerpo {#header-and-body}

¡Escribe lo que quieras! Incluye texto completamente personalizado (a menudo con capacidades de HTML personalizado) con las opciones de incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) y otros tipos de personalización. Cuanto más rápido puedas transmitir tu mensaje y lograr que tu cliente haga clic, ¡mejor! Recomendamos encabezados y contenido de mensaje claros y concisos.

Algunos tipos de mensaje no necesitan y, por lo tanto, no solicitan encabezados.

#### Consejos {#tips}

##### Generar texto con IA {#generating-ai-copy}

¿Necesitas ayuda para crear un texto increíble? Prueba usar el [asistente de redacción con IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Introduce un nombre o descripción de producto y la IA generará texto de marketing similar al humano para usar en tus mensajes.

![Botón para lanzar el redactor con IA, ubicado en el campo Mensaje del creador de mensajes dentro de la aplicación.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Crear mensajes de derecha a izquierda {#creating-right-to-left-messages}

¿Necesitas ayuda para crear mensajes de derecha a izquierda para idiomas como el árabe y el hebreo? Consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) para conocer las mejores prácticas.

### Texto de los botones {#buttons}

Cuando esté disponible para tu tipo de mensaje, puedes hacer que aparezcan hasta dos botones debajo del cuerpo de texto. Puedes crear y editar el texto y el color personalizados de los botones. También puedes añadir un enlace a los Términos de servicio dentro de los formularios de captura de correo electrónico.

Si decides usar solo un botón, se ajustará automáticamente para ocupar el espacio disponible en la parte inferior de tu mensaje en lugar de dejar espacio para un botón adicional.

#### Elegir un botón principal {#choosing-a-primary-button}

Si decides dar formato a estos botones con tus propios colores, te recomendamos que uses el Botón 2 para el resultado que prefieras.

En otras palabras, si quieres que tu usuario haga clic en un botón más que en el otro, asegúrate de que sea el botón secundario. El botón secundario a menudo ha mostrado un mejor potencial para recibir clics, especialmente si tiene un color algo contrastante o que destaque del resto del mensaje. Esto se acentúa cuando el botón principal se mezcla más visualmente con el mensaje.

![Botones principal y secundario en un mensaje dentro de la aplicación]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportamiento al hacer clic {#button-actions}

Cuando tu cliente hace clic en un botón de tu mensaje dentro de la aplicación, están disponibles las siguientes acciones.

| Acción | Descripción |
|---|---|
| Redirigir a URL web | Abre una página web no nativa. |
| [Vínculo profundo a la aplicación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Vincula directamente a una pantalla existente en tu aplicación. |
| Cerrar mensaje | Cierra el mensaje activo actualmente. |
| Registrar evento personalizado | Elige un [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events) para desencadenar. Se puede usar para mostrar otro mensaje dentro de la aplicación o desencadenar mensajes adicionales. |
| Registrar atributo personalizado | Elige un [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) para establecer para el usuario actual. |
| Solicitar permiso push | Muestra el permiso push nativo. Lee más sobre [preparación para push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), así como las [mejores prácticas]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#best-practices) para preparar a los usuarios para push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamiento al hacer clic #button-actions" }

Nota: las opciones __Solicitar permiso push__, __Registrar evento personalizado__ y __Registrar atributo personalizado__ requieren las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Para combinar múltiples acciones o realizar acciones adicionales del SDK que no están disponibles en el panel (como añadir a un grupo de suscripción o establecer un tipo de suscripción de correo electrónico), puedes usar [vínculos profundos de Braze Actions]({{site.baseurl}}/developer_guide/braze_actions).

### Opciones de dispositivos iOS {#ios-device-options}

Si lo deseas, puedes restringir tu mensaje dentro de la aplicación para que solo se envíe a dispositivos iOS. Para hacerlo, haz clic en **Cambiar** y selecciona **Enviar solo a dispositivos iOS**.

### Cierre del mensaje {#message-close}

Elige entre las siguientes opciones:

- **Descartar automáticamente:** Selecciona cuántos segundos permanecerá el mensaje en la pantalla.
- **Esperar a que el usuario deslice o toque:** Requiere una opción de descarte o cierre.

Descartar un mensaje registra una impresión pero no un clic. Para saber cómo se rastrean los clics según la acción del usuario, consulta [Seguimiento de clics]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting#click-tracking).

### Posición del deslizamiento hacia arriba {#slide-up-position}

Esta configuración solo se aplica al tipo de mensaje de deslizamiento hacia arriba. Elige entre que tu deslizamiento hacia arriba aparezca **Desde la parte inferior de la pantalla de la aplicación** o **Desde la parte superior de la pantalla de la aplicación**.

### HTML y activos {#html-and-assets}

Esta configuración solo se aplica al tipo de mensaje de código personalizado. Copia y pega HTML en el espacio disponible y sube tus activos usando un [archivo ZIP]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#zip-file-uploads).

### Marcador de posición del campo de captura de correo electrónico {#email-capture-input-placeholder}

Esta configuración solo se aplica al tipo de mensaje de formulario de captura de correo electrónico. Introduce texto personalizado que aparecerá como texto de marcador de posición en el campo de entrada de correo electrónico. El valor predeterminado es "Introduce tu dirección de correo electrónico".

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

## Paso 6: Configurar ajustes adicionales (opcional) {#step-6-configure-additional-settings-optional}

### Pares clave-valor {#key-value-pairs}

Puedes añadir [pares clave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) para enviar campos personalizados adicionales a los dispositivos de los usuarios.

## Paso 7: Construye el resto de tu campaña o Canvas {#step-7-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construye el resto de tu campaña; consulta las siguientes secciones para obtener más orientación sobre cómo utilizar mejor nuestras herramientas para crear mensajes dentro de la aplicación.

### Elige un desencadenante {#choose-a-trigger}

Selecciona la acción que deseas que desencadene tu mensaje, así como las fechas y horas de inicio y fin de tu Campaign o Canvas.

{% alert important %}
Ten en cuenta que si pretendes desencadenar tu mensaje dentro de la aplicación basándote en un evento personalizado, ese evento personalizado debe enviarse mediante el SDK.
{% endalert %}

![Campaign basada en acciones con la acción desencadenante configurada como "Iniciar sesión".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

La entrega de mensajes dentro de la aplicación se basa completamente en los siguientes desencadenantes de acción:

- Realizar un pedido
- Abrir la aplicación o la página web
- Realizar un evento personalizado (solo funciona con eventos enviados mediante el SDK)
- Abrir un mensaje push específico
- Programar automáticamente Campaigns para que se envíen a una hora determinada con respecto a la zona horaria local de cada uno de tus usuarios.
- Los mensajes también pueden configurarse para que se repitan de forma diaria, semanal (opcionalmente en días específicos) o mensual.

Se debe seleccionar una fecha y hora de inicio; sin embargo, la fecha de fin es opcional. Una fecha de fin impedirá que ese mensaje dentro de la aplicación específico se muestre en los dispositivos después de la fecha/hora especificada.

Consulta nuestra documentación para desarrolladores sobre [desencadenamiento de eventos del lado del servidor]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web) y [entrega local de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery#local-in-app-messages).

#### Desencadenamiento en línea versus sin conexión {#online-versus-offline-triggering}

Los mensajes dentro de la aplicación funcionan enviando el mensaje y los desencadenantes al dispositivo del usuario. Una vez que los mensajes dentro de la aplicación están en un dispositivo, esperan a mostrarse hasta que se cumpla la condición de desencadenamiento. Si los mensajes dentro de la aplicación ya están almacenados en caché en el dispositivo del usuario, incluso puedes desencadenar mensajes dentro de la aplicación sin conexión a Braze (por ejemplo, en modo avión).

{% alert important %}
Una vez que un mensaje dentro de la aplicación se ha detenido, es posible que algunos usuarios sigan viendo el mensaje si iniciaron una sesión antes de que el mensaje se detuviera y posteriormente realizan el evento desencadenante. Estos usuarios se contarán como una impresión única incluso después de que la Campaign se haya detenido.
{% endalert %}

### Elige una prioridad {#choose-a-priority}

Finalmente, después de haber seleccionado la acción que desencadenará el mensaje dentro de la aplicación, también debes establecer una prioridad. Si dos mensajes se desencadenan a partir de la misma acción, los mensajes de alta prioridad se programarán para aparecer en los dispositivos de los usuarios antes que los mensajes con prioridades más bajas.

Puedes elegir entre las siguientes prioridades de mensaje:

- Alta prioridad (se muestra antes que otros mensajes)
- Prioridad media (predeterminada)
- Baja prioridad (se muestra después de otros mensajes)

Las opciones de alta, media y baja prioridad para los mensajes desencadenados son contenedores, y como tal, varios mensajes pueden tener la misma prioridad seleccionada. Cuando varios mensajes comparten la misma prioridad, el mensaje creado o asignado más recientemente tiene precedencia y se muestra primero:

- **Contenedor de prioridad predeterminada:** cuando dos Campaigns comparten el mismo desencadenante y usan la prioridad predeterminada (media), la Campaign que se creó en último lugar recibe el desencadenante.
- **Contenedor de prioridad específica:** cuando varias Campaigns comparten el mismo desencadenante y se asignan a un contenedor de prioridad específico, la Campaign asignada más recientemente a ese contenedor recibe el desencadenante.

Para establecer prioridades dentro de estos contenedores, haz clic en **Set exact priority** y podrás arrastrar y soltar Campaigns para ordenarlas con la prioridad correcta.

![Un ejemplo de cómo se establece la prioridad para una Campaign y un Canvas de mensajes dentro de la aplicación.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

### Elige los usuarios a los que dirigirte {#choose-users-to-target}

A continuación, debes [dirigirte a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) eligiendo Segments o filtros para acotar tu audiencia. Recibirás automáticamente una instantánea de cómo se ve aproximadamente la población de ese Segment. Ten en cuenta que la pertenencia exacta al Segment siempre se calcula antes de que se envíe el mensaje.

{% alert note %}
Si hay un retraso en el paso del mensaje dentro de la aplicación, la pertenencia al Segment se evaluará después del retraso. Si el usuario es elegible, el mensaje dentro de la aplicación se sincronizará en la siguiente sesión disponible.
{% endalert %}

#### Reevaluar la elegibilidad de la Campaign y Liquid {#re-evaluate-campaign-eligibility-and-liquid}

En algunos escenarios, es posible que desees reevaluar la elegibilidad de un usuario cuando desencadena un mensaje dentro de la aplicación para mostrarlo. Los ejemplos incluyen Campaigns que se dirigen a un atributo personalizado que cambia con frecuencia o mensajes que deben reflejar cualquier cambio de perfil de último momento.

![Casilla de verificación "Reevaluar la elegibilidad de la Campaign antes de mostrar" seleccionada.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Cuando seleccionas **Re-evaluate campaign eligibility before displaying**, se realizará una solicitud adicional a Braze para confirmar que el usuario sigue siendo elegible para este mensaje antes de enviarlo. Además, cualquier variable de [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) o [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) se procesará en ese momento antes de que se muestre el mensaje.

Esto evita que se envíen mensajes dentro de la aplicación a usuarios dentro de Campaigns expiradas o archivadas. Si no reevalúas la elegibilidad de un usuario, este recibirá el mensaje dentro de la aplicación incluso después de que la Campaign haya expirado o se haya archivado, porque el mensaje está en tu SDK y esperando a que los usuarios lo desencadenen.

{% alert note %}
Habilitar esta opción resultará en un ligero retraso (< 100 ms) entre el momento en que un usuario desencadena un mensaje dentro de la aplicación y el momento en que se muestra el mensaje, debido a la solicitud adicional de elegibilidad y procesamiento de plantillas.
<br><br>
No uses esta opción para mensajes que pueden desencadenarse mientras un usuario está sin conexión o cuando la reevaluación de elegibilidad y Liquid no es necesaria.
{% endalert %}

#### Usar datos añadidos por la REST API en un mensaje {#use-data-added-by-rest-api-in-a-message}

Los datos de usuario que el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) añade en la misma sesión a veces pueden usarse en el mensaje dentro de la aplicación de ese usuario. Por ejemplo, si un usuario está en la audiencia de un mensaje dentro de la aplicación que está esperando un desencadenante, inicia una sesión, y en esa misma sesión la REST API actualiza su perfil, esos nuevos datos pueden aparecer en el mensaje dentro de la aplicación cuando se selecciona **Re-evaluate campaign eligibility before displaying**. Braze no procesará la plantilla del mensaje dentro de la aplicación hasta que sea el momento de renderizarlo.

Si un desencadenante envía datos a Braze y activa el mensaje dentro de la aplicación al mismo tiempo, el mensaje no puede usar esos datos de perfil recién actualizados, incluso con un retraso programado. En su lugar, usa dos desencadenantes separados: uno para enviar los datos y otro para desencadenar el mensaje dentro de la aplicación.

### Elige eventos de conversión {#choose-conversion-events}

Braze te permite hacer seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), después de recibir una Campaign. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

{% endtab %}
{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente de Canvas. Para obtener más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariante y selección inteligente, y más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) de nuestra documentación de Canvas.

Para obtener información sobre las opciones de mensajes dentro de la aplicación específicas de Canvas, consulta [Mensajes dentro de la aplicación en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Paso 8: Revisar e implementar {#step-8-review-and-deploy}

Cuando hayas terminado de crear la última parte de tu Campaign o Canvas, revisa sus detalles, [pruébala]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) y ¡envíala!

A continuación, consulta [Informes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) para saber cómo puedes acceder a los resultados de tus Campaigns de mensajería.

## Cosas que debes saber {#things-to-know}

### Límites de campañas activas de mensajes dentro de la aplicación {#active-in-app-message-campaign-limits}

Braze valora la fiabilidad y la velocidad. Te sugerimos que envíes solo los datos que necesites a Braze y desactives cualquier campaña que ya no aporte valor a tu marca.

Procesar Campaigns de mensajes dentro de la aplicación basadas en acciones que siguen en estado activo pero que ya no envían mensajes o ya no son necesarias ralentiza el rendimiento general de los servicios de Braze para ti y para otros clientes. Este tiempo adicional necesario para procesar estas grandes cantidades de campañas inactivas significa que cualquier mensaje dentro de la aplicación tardará más en aparecer en los dispositivos del usuario final, lo que afecta a su experiencia.

{% alert important %}
Puedes tener hasta 200 Campaigns activas de mensajes dentro de la aplicación basadas en acciones por espacio de trabajo para optimizar la velocidad de entrega de mensajes y evitar tiempos de espera. Esto no se aplica a Canvas.
{% endalert %}

El recuento de 200 incluye Campaigns activas de mensajes dentro de la aplicación que aún no han alcanzado su hora de finalización y aquellas que no tienen hora de finalización. Las Campaigns activas de mensajes dentro de la aplicación que hayan superado su hora de finalización no se contabilizarán. El cliente promedio de Braze tiene un total de 26 campañas activas a la vez, por lo que es poco probable que esta limitación te afecte.

### Evaluación de la entrega según la zona horaria local {#local-time-delivery-evaluation}

Cuando se programa una Campaign de mensajes dentro de la aplicación utilizando la zona horaria local del usuario, la evaluación de la hora de inicio y finalización de la campaña se gestiona en el propio dispositivo.

Las Campaigns de mensajes dentro de la aplicación normalmente se envían al dispositivo del usuario cuando se inicia o se actualiza la sesión de la aplicación. En ese momento:

1. El SDK evalúa si el usuario cumple los requisitos para cualquier mensaje dentro de la aplicación basado en desencadenantes.
2. El dispositivo comprueba si el evento desencadenante del usuario ocurrió dentro de la hora de inicio y finalización de la Campaign (según la zona horaria local del usuario).
3. Si se cumplen ambas condiciones, el mensaje dentro de la aplicación es elegible para mostrarse.

#### Consideraciones {#considerations}

- Si un usuario desencadena un evento (como pulsar un botón) poco después de que se entregue el mensaje dentro de la aplicación, es posible que el mensaje no aparezca hasta la siguiente actualización de sesión, siempre que se sigan cumpliendo todos los criterios de elegibilidad.
- De forma similar a otros tipos de canal, las Campaigns de mensajes dentro de la aplicación deberían lanzarse idealmente con 24-48 horas de antelación. Este margen da a los usuarios tiempo suficiente para cumplir los requisitos de elegibilidad e iniciar una sesión para que el mensaje sea evaluado y mostrado.
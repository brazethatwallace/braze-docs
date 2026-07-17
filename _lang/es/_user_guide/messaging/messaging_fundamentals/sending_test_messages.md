---
nav_title: Enviar mensajes de prueba
article_title: Enviar mensajes de prueba
page_order: 11.5
tool:
  - Campaigns
  - Canvas
page_type: reference
description: "Este artículo de referencia cubre cómo enviar mensajes de prueba a través de los diferentes canales de Braze y cómo incorporar propiedades de eventos personalizados o atributos de usuario."
---

# Enviar mensajes de prueba {#send-test-messages}

> Antes de enviar una campaña de mensajería a tus usuarios, como práctica recomendada, te sugerimos probarla para asegurarte de que tiene el aspecto adecuado y funciona de la forma prevista. Puedes crear y enviar mensajes de prueba a dispositivos o miembros del equipo seleccionados utilizando las herramientas del panel de Braze.

{% alert important %}
Asegúrate de guardar el borrador de tu campaña después de probarla para evitar eliminar tu campaña. Puedes enviar mensajes de prueba sin guardar el mensaje como borrador.
{% endalert %}

## Paso 1: Identifica a tus usuarios de prueba {#step-1-identify-your-test-users}

Antes de probar tu campaña de mensajería, es importante identificar a tus usuarios de prueba. Estos usuarios pueden ser ID de usuario o direcciones de correo electrónico existentes, o nuevos usuarios que se utilicen exclusivamente para probar campañas de mensajería.

### Opcional: Crea un grupo de prueba de contenido {#optional-create-a-content-test-group}

Una forma conveniente de organizar a tus usuarios de prueba es crear un [grupo de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), que incluye un grupo de usuarios que recibirán mensajes de prueba de las campañas. Puedes añadir este grupo de prueba al campo **Add Content Test Groups** en **Test Recipients** en tu campaña, y lanzar tus pruebas sin crear ni añadir usuarios de prueba individuales.

## Paso 2: Envía mensajes de prueba específicos del canal {#step-2-send-channel-specific-test-messages}

Para conocer los pasos para enviar mensajes de prueba, consulta la siguiente sección correspondiente a tu canal.

{% tabs local %}
{% tab Banners %}

{% alert important %}
Antes de poder probar mensajes de Banner en Braze, necesitarás crear una campaña de Banner en Braze. Además, verifica que la ubicación que deseas probar ya esté [colocada en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements).
{% endalert %}

Después de crear tu mensaje de Banner, puedes previsualizar tu Banner o enviar un mensaje de prueba.

1. Redacta tu mensaje de Banner.
2. Selecciona **Preview** para previsualizar tu Banner o enviar un mensaje de prueba.
3. Para enviar un mensaje de prueba, añade un grupo de prueba de contenido o uno o más usuarios individuales como **Test Recipients**, luego selecciona **Send Test**.

Podrás ver tu mensaje de prueba en el dispositivo durante un máximo de 5 minutos.

![Pestaña de vista previa del creador de Banner.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Ten en cuenta que tu vista previa puede no ser idéntica a la representación final en el dispositivo de un usuario debido a diferencias en el hardware.
{% endalert %}

### Lista de verificación de prueba {#test-checklist}

- ¿Tu campaña de Banner está asignada a una ubicación?
- ¿Las imágenes y los medios se muestran y funcionan como se espera en los tipos de dispositivos y tamaños de pantalla objetivo?
- ¿Tus enlaces y botones dirigen al usuario a donde deben ir?
- ¿Liquid funciona como se espera? ¿Has contemplado un valor de atributo predeterminado en caso de que Liquid no devuelva información?
- ¿Tu texto es claro, conciso y correcto?

{% endtab %}
{% tab Content Card %}

{% alert important %}
Para enviar una prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) o usuarios individuales, las notificaciones push deben estar habilitadas en tus dispositivos de prueba con tokens de push válidos registrados para el usuario de prueba antes de enviar. Para los usuarios de iOS, debes tocar la notificación push enviada por Braze para ver la Content Card de prueba. Este comportamiento solo se aplica a las Content Cards de prueba.
{% endalert %}

Las Content Cards de prueba se entregan a través de una notificación push. La tarjeta se empaqueta en la carga útil del push, y el SDK la extrae y almacena en caché localmente cuando se recibe el push.

Este proceso omite el sistema normal de entrega de tarjetas, por lo que las notificaciones push deben estar habilitadas aunque estés probando una Content Card.

Las Content Cards de prueba caducan aproximadamente cinco minutos después de ser enviadas.

Después de crear tu Content Card, puedes enviar una Content Card de prueba a tu aplicación para ver cómo se verá en tiempo real.

1. Redacta tu Content Card.
2. Selecciona la pestaña **Test** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba.
3. Selecciona **Send Test** para enviar tu Content Card a tu aplicación.

![Prueba de Content Card]({% image_buster /assets/img/contentcard_test.png %})

### Vista previa {#preview}

Puedes previsualizar tu tarjeta mientras la redactas en la pestaña **Preview**. Esto debería ayudarte a visualizar cómo se verá tu mensaje final desde la perspectiva de tu usuario.

{% alert note %}
En la pestaña **Preview** de tu creador, la vista de tu mensaje puede no ser idéntica a su representación real en el dispositivo del usuario. Siempre recomendamos enviar un mensaje de prueba a un dispositivo para asegurarte de que tus medios, texto, personalización y atributos personalizados se generen correctamente.
{% endalert %}

### Lista de verificación de prueba

- ¿Tu usuario de prueba ha optado por recibir notificaciones push con un token de push válido?
- ¿Las imágenes y los medios se muestran y funcionan como se espera?
- ¿Liquid funciona como se espera? ¿Has contemplado un [valor de atributo predeterminado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) en caso de que Liquid no devuelva información?
- ¿Tu texto es claro, conciso y correcto?
- ¿Tus enlaces dirigen al usuario a donde deben ir?
- ¿Tu usuario de prueba ha optado por recibir notificaciones push con un token de push válido?

### Solución de problemas con imágenes rotas {#troubleshooting-broken-images}

Si una imagen de Content Card no se renderiza o aparece rota:

- **Verifica que la URL sea correcta y esté codificada:** Los caracteres especiales en la URL (como espacios o parámetros de consulta) deben estar correctamente codificados. De lo contrario, la solicitud de imagen falla.
- **Comprueba las políticas de seguridad de contenido:** Si tu organización tiene una política de seguridad de contenido (CSP) o reglas de seguridad de TI internas, la política puede bloquear el dominio de la imagen. Confirma que el dominio de la URL de la imagen esté permitido por tu CSP.
- **Usa HTTPS:** Las URL de imágenes deben usar `https://` en lugar de `http://` para evitar el bloqueo de contenido mixto en navegadores y aplicaciones.
- **Abre la URL directamente en un navegador:** Si la imagen no se carga en un navegador, el problema está en la URL de la imagen o en el alojamiento, no en Braze.

### Depuración {#debug}

Después de enviar tus Content Cards, puedes desglosar o depurar cualquier problema desde el [registro de usuarios del evento]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) en la consola para desarrolladores.

Un caso de uso común es intentar depurar por qué un usuario no puede ver una Content Card en particular. Para hacerlo, puedes buscar en los **Event User Logs** las Content Cards entregadas al SDK al inicio de la sesión, pero antes de una impresión, y rastrearlas hasta una campaña específica:

1. Ve a **Settings** > **Event User Log**.
2. Localiza y expande la solicitud del SDK para tu usuario de prueba.
3. Haz clic en **Raw Data**.
4. Encuentra el `id` de tu sesión. A continuación se muestra un extracto de ejemplo:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

{: start="5"}
5. Usa una herramienta de decodificación como [Base64 Decode and Encode](https://www.base64decode.org/) para decodificar el `id` del formato Base64 y encontrar el `campaign_id` asociado. En nuestro ejemplo, esto resulta en lo siguiente:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Donde `4861692e-6fce-4215-bd05-3254fb9e9057` es el `campaign_id`.<br><br>

6. Ve a la página de **Campaigns** y busca el `campaign_id`.

![Buscar campaign_id en la página de Campaigns]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

Desde ahí, puedes revisar la configuración y el contenido de tu mensaje para profundizar y determinar por qué un usuario no puede ver una Content Card en particular.

{% endtab %}
{% tab Correo electrónico %}

1. Redacta tu mensaje de correo electrónico.
2. Selecciona **Preview and Test**.
3. Selecciona la pestaña **Test Send** y añade tu dirección de correo electrónico o ID de usuario en el campo **Add individual users**.
4. Selecciona **Send Test** para enviar tu correo electrónico redactado a tu buzón de entrada.

![Prueba de correo electrónico]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

Si tu campaña de correo electrónico incluye una imagen grande y no se muestra como se espera en Outlook, considera reducir las dimensiones reales del archivo de la imagen con una herramienta de edición o redimensionamiento de imágenes en lugar de solo escalarla con CSS o HTML.

{% endtab %}
{% tab Mensaje dentro de la aplicación %}

{% alert warning %}
Para enviar una prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) o usuarios individuales, las notificaciones push deben estar habilitadas en tus dispositivos de prueba antes de enviar. Por ejemplo, debes tener las notificaciones push habilitadas en tu dispositivo iOS para poder tocar la notificación antes de que se muestre el mensaje de prueba. {% endalert %}

Si tienes las notificaciones push configuradas en tu aplicación y en tu dispositivo de prueba, puedes enviar mensajes de prueba dentro de la aplicación para ver cómo se ven en tiempo real.

1. Redacta tu mensaje dentro de la aplicación.
2. Selecciona la pestaña **Test** y añade tu dirección de correo electrónico o ID de usuario en el campo **Add Individual Users**.
3. Selecciona **Send Test** para enviar tu mensaje push a tu dispositivo.

Un mensaje push de prueba aparecerá en la parte superior de la pantalla de tu dispositivo.

![Prueba de mensaje dentro de la aplicación]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Los envíos de prueba pueden resultar en que se envíe más de un mensaje dentro de la aplicación a cada destinatario.
{% endalert %}

Al hacer clic directamente y abrir el mensaje push, serás dirigido a tu aplicación, donde podrás ver tu prueba de mensaje dentro de la aplicación. Ten en cuenta que esta función de prueba de mensajes dentro de la aplicación depende de que el usuario haga clic en una notificación push de prueba para activar el mensaje dentro de la aplicación. Por lo tanto, el usuario debe ser elegible para recibir notificaciones push en la aplicación correspondiente para la entrega exitosa de la notificación push de prueba.

### Vista previa

Puedes previsualizar tu mensaje dentro de la aplicación mientras lo redactas en la pestaña **Preview**. Esto debería ayudarte a visualizar cómo se verá tu mensaje final desde la perspectiva de tu usuario. Puedes previsualizar cómo se verá tu mensaje para un usuario aleatorio, un usuario específico o un usuario personalizado. También puedes previsualizar mensajes para dispositivos móviles o tabletas.

![Pestaña de redacción al crear un mensaje dentro de la aplicación mostrando la vista previa de cómo se verá el mensaje. No se ha seleccionado un usuario, por lo que el Liquid añadido en la sección del cuerpo se muestra tal cual.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze tiene tres generaciones de mensajes dentro de la aplicación disponibles. Puedes ajustar a qué dispositivos se envían tus mensajes, según la generación que admitan.

![Cambio entre generaciones al previsualizar un mensaje dentro de la aplicación.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
En **Preview**, la vista de tu mensaje puede no ser idéntica a su representación real en el dispositivo del usuario. Siempre recomendamos enviar un mensaje de prueba a un dispositivo para asegurarte de que tus medios, texto, personalización y atributos personalizados se generen correctamente.
{% endalert %}

### Lista de verificación de prueba

- ¿Las imágenes y los medios se muestran y funcionan como se espera?
- ¿Liquid funciona como se espera? ¿Has contemplado un [valor de atributo predeterminado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) en caso de que Liquid no devuelva información?
- ¿Tu texto es claro, conciso y correcto?
- ¿Tus botones dirigen al usuario a donde deben ir?

### Escáner de accesibilidad {#accessibility-scanner}

Para apoyar las mejores prácticas de accesibilidad, Braze escanea automáticamente el contenido de los mensajes dentro de la aplicación creados con el editor HTML tradicional contra los estándares de accesibilidad. Este escáner ayuda a identificar contenido que puede no cumplir con los estándares de las Pautas de Accesibilidad para el Contenido Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). WCAG es un conjunto de estándares técnicos reconocidos internacionalmente desarrollados por el World Wide Web Consortium (W3C) para hacer que el contenido web sea más accesible para personas con discapacidades.

![Resultados del escaneo de accesibilidad]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
El escáner de accesibilidad de mensajes dentro de la aplicación solo se ejecuta en mensajes creados con HTML personalizado.
{% endalert %}

#### Cómo funciona {#how-it-works}

El escáner se ejecuta automáticamente en mensajes HTML personalizados y evalúa todo tu mensaje HTML contra el [conjunto completo de reglas WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Para cada problema detectado, muestra:

- El elemento HTML específico involucrado
- Una descripción del problema de accesibilidad
- Un enlace a contexto adicional o guía de corrección

#### Comprensión de las pruebas de accesibilidad automatizadas {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Crea tu mensaje de LINE.
2. Selecciona la pestaña **Test** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba.
3. Selecciona **Send Test** para enviar tu mensaje.

![Prueba de mensaje de LINE.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Push móvil {#mobile-push}

1. Redacta tu notificación push móvil.
2. Selecciona la pestaña **Test** y añade tu dirección de correo electrónico o ID de usuario en el campo **Add Individual Users**.
3. Selecciona **Send Test** para enviar tu mensaje redactado a tu dispositivo.

![Prueba de push]({% image_buster /assets/img_archive/testpush.png %})

Si ves un error que indica que ninguno de los usuarios seleccionados tiene tokens de push coincidentes, el usuario de prueba no tiene un token de push válido para la plataforma seleccionada. El usuario debe haber iniciado una sesión en la aplicación y habilitado las notificaciones push para ese dispositivo. Para más información, consulta [Habilitación de push y estados de suscripción push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

#### Push web {#web-push}

1. Crea tu notificación push web.
2. Selecciona la pestaña **Test**.
3. Selecciona **Send Test to Myself**.
4. Selecciona **Send Test** para enviar tu notificación push web a tu navegador web.

![Prueba de push web]({% image_buster /assets/img_archive/testwebpush.png %})

Si ya has aceptado mensajes push desde el panel de Braze, el mensaje aparecerá en la esquina de tu pantalla. De lo contrario, selecciona **Allow** cuando se te solicite, y el mensaje se mostrará.

Si ves un error que indica que ninguno de los usuarios seleccionados tiene tokens de push coincidentes para notificación push web, verifica que el usuario de prueba tenga un token de push válido registrado para la plataforma seleccionada. Para recibir un token de push, el usuario debe estar configurado para recibir notificaciones push para la aplicación en su dispositivo. Para más detalles, consulta [Habilitación de push y estados de suscripción push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

{% endtab %}
{% tab SMS/MMS y RCS %}

Después de crear tu mensaje de SMS, MMS o RCS, puedes enviar un mensaje de prueba a tu teléfono para ver cómo se verá en tiempo real.

1. Redacta tu mensaje de SMS, MMS o RCS.
2. Selecciona la pestaña **Test** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba.
3. Selecciona **Send Test** para enviar tu mensaje de prueba.

![Prueba de SMS]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Después de crear tu webhook, puedes hacer un envío de prueba para verificar la respuesta del webhook. Selecciona la pestaña **Test** y selecciona **Send Test** para enviar un envío de prueba a la URL del webhook proporcionada. También puedes seleccionar un usuario individual para previsualizar la respuesta como un usuario específico.

{% endtab %}
{% tab WhatsApp %}

1. Crea tu mensaje de WhatsApp.
2. Selecciona la pestaña **Test** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba.
3. Inicia una ventana de conversación enviando un mensaje de WhatsApp al número de teléfono asociado con el grupo de suscripción que estás usando para este mensaje. El número de teléfono asociado aparece en la alerta de la pestaña **Test**.
4. Selecciona **Send Test** para enviar tu mensaje.

![Prueba de mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Probar campañas personalizadas {#test-personalized-campaigns}

Si estás probando campañas que utilizan datos de usuario o propiedades de eventos personalizados, necesitarás seguir pasos adicionales o diferentes.

### Probar campañas personalizadas con atributos de usuario {#testing-campaigns-personalized-with-user-attributes}

Si estás usando [personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/overview) en tu mensaje, necesitarás seguir pasos adicionales para previsualizar correctamente tu campaña y verificar que los datos de usuario estén rellenando correctamente el contenido.

Al enviar un mensaje de prueba, asegúrate de elegir la opción de **Select Existing User** o previsualizar como un **Custom User**.

![Prueba de un mensaje personalizado]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Seleccionar un usuario existente {#selecting-an-existing-user}

Si seleccionas un usuario existente, introduce el ID de usuario o correo electrónico específico en el campo de búsqueda. Luego, usa la vista previa del panel para ver cómo aparecería tu mensaje para ese usuario, y envía un mensaje de prueba a tu dispositivo que refleje lo que ese usuario vería.

![Seleccionar un usuario]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Seleccionar un usuario personalizado {#selecting-a-custom-user}

Si previsualizas como un usuario personalizado, introduce texto para los distintos campos disponibles para personalización, como el nombre del usuario y cualquier atributo personalizado. Una vez más, puedes introducir tu propia dirección de correo electrónico para enviar una prueba a tu dispositivo.

![Usuario personalizado]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Personalizar un usuario existente {#customizing-an-existing-user}

Puedes editar campos individuales de un usuario aleatorio o existente para ayudar a probar contenido dinámico dentro de tu mensaje. Selecciona **Edit** para convertir al usuario seleccionado en un usuario personalizado que puedas modificar.

![La pestaña "Preview as a User" con un botón "Edit".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Probar campañas personalizadas con propiedades de eventos personalizados {#testing-campaigns-personalized-with-custom-event-properties}

Probar campañas personalizadas con [propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) difiere ligeramente de probar otros tipos de campañas descritas.

{% tabs local %}
{% tab Activar manualmente %}

#### Método 1: Activar la campaña manualmente {#method-1-triggering-campaign-manually}

Puedes activar la campaña tú mismo como una forma robusta de probar campañas personalizadas usando propiedades de eventos personalizados:

1. Redacta el texto que incluya la propiedad del evento.

![Redactar mensaje de prueba con propiedades]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Usa la [entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para entregar la campaña cuando ocurra el evento.

{% alert note %}
Si estás probando una campaña push de iOS, debes establecer el retraso en un minuto para darte tiempo de salir de la aplicación, ya que iOS no entrega notificaciones push para la aplicación actualmente abierta. Otros tipos de campañas pueden configurarse para entregarse inmediatamente.
{% endalert %}

![Entrega del mensaje de prueba]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Segmenta a los usuarios como lo harías para pruebas usando un filtro de prueba o apuntando a tu propia dirección de correo electrónico, y termina de crear la campaña.

![Segmentación del mensaje de prueba]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Ve a tu aplicación y completa el evento personalizado.

La campaña se activará y mostrará el mensaje personalizado con la propiedad del evento.

![Ejemplo de mensaje de prueba]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Mensaje de prueba %}

#### Método 2: Enviarte un mensaje de prueba {#method-2-sending-yourself-a-test-message}

Alternativamente, si estás guardando ID de usuario personalizados, también puedes probar la campaña enviándote un mensaje de prueba personalizado.

1. Redacta el texto de tu campaña.
2. Selecciona la pestaña **Test** y elige **Customized User**.
3. Añade la propiedad del evento personalizado en la parte inferior de la página, y añade tu ID de usuario o dirección de correo electrónico en el campo superior.
4. Selecciona **Send Test** para recibir un mensaje personalizado con la propiedad.

![Prueba usando usuario personalizado]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Método 3: Usar Liquid {#method-3-using-liquid}

Puedes probar propiedades de eventos personalizados introduciendo manualmente valores con Liquid.

1. En el editor de mensajes, introduce valores para tus propiedades de eventos personalizados.
2. Selecciona la pestaña **Preview as a User** para verificar que se muestre el mensaje correcto.

{% endtab %}
{% endtabs %}

## Limitaciones {#limitations}

Hay algunas situaciones en las que los mensajes de prueba no se comportan de la misma manera que las campañas o Canvas enviados a usuarios reales. En estos casos, considera lanzar la campaña o Canvas a un conjunto limitado de usuarios de prueba para validar este comportamiento.

- Ver el centro de preferencias de Braze desde mensajes de prueba hará que el botón **Save Preferences** aparezca atenuado.
- Para probar mensajes dentro de la aplicación y Content Cards, el usuario objetivo debe tener un token de push para el dispositivo objetivo.
- Para probar enlaces de cancelación de suscripción en correos electrónicos, asegúrate de que la dirección de correo electrónico de tu usuario de prueba esté en el espacio de trabajo correspondiente.
- El encabezado `List-Unsubscribe` no se incluye en los correos electrónicos enviados por la funcionalidad de mensaje de prueba.
- Los correos electrónicos enviados a usuarios del grupo semilla no actualizan la lista de campañas recibidas del perfil de usuario ni incrementan los envíos en los análisis del panel.

## Solución de problemas {#troubleshooting}

### Mensajes dentro de la aplicación {#in-app-messages}

Si tu campaña de mensaje dentro de la aplicación no se activa con una campaña push, verifica la segmentación de la campaña dentro de la aplicación para confirmar que el usuario cumple con el público objetivo **antes** de recibir el mensaje push.

Para envíos de prueba en Android e iOS, los mensajes dentro de la aplicación que usan el comportamiento de clic **Request push permission** pueden no mostrarse en algunos dispositivos. Como solución alternativa:
- **Android:** Los dispositivos deben estar en Android 13 y nuestra versión del SDK de Android 21.0.0. Otra razón puede ser que el dispositivo en el que se muestra el mensaje dentro de la aplicación ya tiene un aviso a nivel del sistema. Es posible que hayas seleccionado **Do not ask again**, por lo que puede que necesites reinstalar la aplicación para restablecer los permisos de notificación antes de probar de nuevo.
- **iOS:** Recomendamos que tu equipo de desarrolladores revise la implementación de las notificaciones push para tu aplicación y elimine manualmente cualquier código que solicite permisos push. Para más información, consulta [Mensajes dentro de la aplicación de preparación para push]({{site.baseurl}}/user_guide/channels/push/best_practices).

Para que una campaña de mensaje dentro de la aplicación basada en acciones se entregue, debes registrar eventos personalizados a través del SDK de Braze, no de las REST API, para que los usuarios puedan recibir mensajes dentro de la aplicación elegibles directamente en su dispositivo. Los usuarios reciben el mensaje dentro de la aplicación si realizan el evento durante la sesión.
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

Antes de probar tu campaña de mensajería, es importante identificar a tus usuarios de prueba. Estos usuarios pueden ser ID de usuario o direcciones de correo electrónico existentes, o bien nuevos usuarios que se utilicen exclusivamente para probar campañas de mensajería.

### Opcional: Crea un grupo de prueba de contenido {#optional-create-a-content-test-group}

Una forma práctica de organizar a tus usuarios de prueba es crear un [grupo de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), que incluye un grupo de usuarios que recibirán mensajes de prueba de las campañas. Puedes añadir este grupo de prueba al campo **Add Content Test Groups** en **Test Recipients** dentro de tu campaña, y lanzar tus pruebas sin necesidad de crear ni añadir usuarios de prueba individuales.

## Paso 2: Enviar mensajes de prueba específicos del canal {#step-2-send-channel-specific-test-messages}

Para conocer los pasos para enviar mensajes de prueba, consulta la siguiente sección correspondiente a tu canal.

{% tabs local %}
{% tab Banners %}

{% alert important %}
Antes de poder probar mensajes de tipo Banner en Braze, tendrás que crear una campaña de Banner en Braze. Además, verifica que la ubicación que deseas probar ya esté [colocada en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements).
{% endalert %}

Después de crear tu mensaje de tipo Banner, puedes previsualizar tu Banner o enviar un mensaje de prueba.

1. Redacta tu mensaje de tipo Banner.
2. Selecciona **Vista previa** para previsualizar tu Banner o enviar un mensaje de prueba.
3. Para enviar un mensaje de prueba, añade un grupo de prueba de contenido o uno o más usuarios individuales como **Destinatarios de prueba** y, a continuación, selecciona **Enviar prueba**.

Podrás ver tu mensaje de prueba en el dispositivo durante un máximo de 5 minutos.

![Pestaña de vista previa del creador de Banner.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Ten en cuenta que tu vista previa puede no ser idéntica a la representación final en el dispositivo de un usuario debido a diferencias en el hardware.
{% endalert %}

### Lista de verificación de prueba {#test-checklist}

- ¿Está tu campaña de Banner asignada a una ubicación?
- ¿Las imágenes y los medios se muestran y funcionan como se esperaba en los tipos de dispositivo y tamaños de pantalla a los que te diriges?
- ¿Tus enlaces y botones dirigen al usuario a donde deben ir?
- ¿El Liquid funciona como se esperaba? ¿Has tenido en cuenta un valor de atributo predeterminado en caso de que el Liquid no devuelva información?
- ¿Tu texto es claro, conciso y correcto?

{% endtab %}
{% tab Content Card %}

{% alert important %}
Para enviar una prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) o a usuarios individuales, push debe estar habilitado en tus dispositivos de prueba con tokens de notificaciones push válidos registrados para el usuario de prueba antes de enviar. Para usuarios de iOS, debes tocar la notificación push enviada por Braze para poder ver la Content Card de prueba. Este comportamiento solo aplica para Content Cards de prueba.
{% endalert %}

Las Content Cards de prueba se entregan a través de una notificación push. La tarjeta se incluye en la carga útil del push, y el SDK la extrae y la almacena en caché localmente cuando se recibe el push.

Este proceso omite el sistema normal de entrega de tarjetas, por lo que push debe estar habilitado aunque estés probando una Content Card.

Las Content Cards de prueba caducan aproximadamente cinco minutos después de ser enviadas.

Después de crear tu Content Card, puedes enviar una Content Card de prueba a tu aplicación para ver cómo se verá en tiempo real.

1. Redacta tu Content Card.
2. Selecciona la pestaña **Prueba** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba.
3. Selecciona **Enviar prueba** para enviar tu Content Card a tu aplicación.

![Prueba de Content Card]({% image_buster /assets/img/contentcard_test.png %})

### Vista previa {#preview}

Puedes previsualizar tu tarjeta mientras la redactas en la pestaña **Vista previa**. Esto debería ayudarte a visualizar cómo se verá tu mensaje final desde la perspectiva del usuario.

{% alert note %}
En la pestaña **Vista previa** de tu creador, la vista de tu mensaje puede no ser idéntica a su representación real en el dispositivo del usuario. Recomendamos enviar siempre un mensaje de prueba a un dispositivo para asegurarte de que tus medios, texto, personalización y atributos personalizados se generen correctamente.
{% endalert %}

### Lista de verificación de prueba

- ¿Tu usuario de prueba tiene push habilitado con un token de notificaciones push válido?
- ¿Las imágenes y los medios se muestran y funcionan como se esperaba?
- ¿El Liquid funciona como se esperaba? ¿Has tenido en cuenta un [valor de atributo predeterminado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) en caso de que el Liquid no devuelva información?
- ¿Tu texto es claro, conciso y correcto?
- ¿Tus enlaces dirigen al usuario a donde deben ir?
- ¿Tu usuario de prueba tiene push habilitado con un token de notificaciones push válido?

### Solución de problemas de imágenes rotas {#troubleshooting-broken-images}

Si una imagen de Content Card no se muestra o aparece rota:

- **Verifica que la URL sea correcta y esté codificada:** Los caracteres especiales en la URL (como espacios o parámetros de consulta) deben estar codificados correctamente. De lo contrario, la solicitud de imagen fallará.
- **Revisa las políticas de seguridad de contenido:** Si tu organización tiene una política de seguridad de contenido (CSP) o reglas internas de seguridad de TI, la política puede estar bloqueando el dominio de la imagen. Confirma que el dominio de la URL de la imagen esté permitido por tu CSP.
- **Usa HTTPS:** Las URL de imágenes deben usar `https://` en lugar de `http://` para evitar el bloqueo de contenido mixto en navegadores y aplicaciones.
- **Abre la URL directamente en un navegador:** Si la imagen no se carga en un navegador, el problema está en la URL de la imagen o en el alojamiento, no en Braze.

### Depuración {#debug}

Después de enviar tus Content Cards, puedes desglosar o depurar cualquier problema desde el [registro de usuarios del evento]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) en la consola para desarrolladores.

Un caso de uso común es intentar depurar por qué un usuario no puede ver una Content Card en particular. Para hacerlo, puedes buscar en los **registros de usuarios del evento** las Content Cards entregadas al SDK al inicio de la sesión, pero antes de una impresión, y rastrearlas hasta una campaña específica:

1. Ve a **Configuración** > **Registro de usuarios del evento**.
2. Localiza y expande la solicitud del SDK de tu usuario de prueba.
3. Haz clic en **Datos sin procesar**.
4. Busca el `id` de tu sesión. El siguiente es un extracto de ejemplo:

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
5. Usa una herramienta de decodificación como [Base64 Decode and Encode](https://www.base64decode.org/) para decodificar el `id` del formato Base64 y encontrar el `campaign_id` asociado. En nuestro ejemplo, esto da como resultado lo siguiente:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Donde `4861692e-6fce-4215-bd05-3254fb9e9057` es el `campaign_id`.<br><br>

6. Ve a la página **Campaigns** y busca el `campaign_id`.

![Buscar campaign_id en la página de Campaigns]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

Desde ahí, puedes revisar la configuración y el contenido de tu mensaje para profundizar y determinar por qué un usuario no puede ver una Content Card en particular.

{% endtab %}
{% tab Correo electrónico %}

1. Redacta tu mensaje de correo electrónico.
2. Selecciona **Vista previa y prueba**.
3. Selecciona la pestaña **Envío de prueba** y añade tu dirección de correo electrónico o ID de usuario en el campo **Agregar usuarios individuales**.
4. Selecciona **Enviar prueba** para enviar tu correo electrónico redactado a tu buzón de entrada.

![Prueba de correo electrónico]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

Si tu correo electrónico incluye un enlace de [centro de preferencias]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center), los envíos de prueba no generan un enlace funcional ni permiten guardar preferencias. Para probar el centro de preferencias, lanza el mensaje a un usuario de prueba o a un Segment interno pequeño. Para más detalles, consulta [Probar centros de preferencias]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers).

Si tu campaña de correo electrónico incluye una imagen grande y no se muestra como se esperaba en Outlook, considera reducir las dimensiones reales del archivo de la imagen con una herramienta de edición o redimensionamiento de imágenes en lugar de solo escalarla con CSS o HTML.

{% endtab %}
{% tab Mensaje dentro de la aplicación %}

{% alert warning %}
Para enviar una prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) o a usuarios individuales, push debe estar habilitado en tus dispositivos de prueba antes de enviar. Por ejemplo, debes tener push habilitado en tu dispositivo iOS para poder tocar la notificación antes de que se muestre el mensaje de prueba. {% endalert %}

Si tienes notificaciones push configuradas dentro de tu aplicación y en tu dispositivo de prueba, puedes enviar mensajes dentro de la aplicación de prueba a tu aplicación para ver cómo se ven en tiempo real.

1. Redacta tu mensaje dentro de la aplicación.
2. Selecciona la pestaña **Prueba** y añade tu dirección de correo electrónico o ID de usuario en el campo **Agregar usuarios individuales**.
3. Selecciona **Enviar prueba** para enviar tu mensaje push a tu dispositivo.

Un mensaje push de prueba aparecerá en la parte superior de la pantalla de tu dispositivo.

![Prueba de mensaje dentro de la aplicación]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Los envíos de prueba pueden resultar en que se envíe más de un mensaje dentro de la aplicación a cada destinatario.
{% endalert %}

Al hacer clic directamente y abrir el mensaje push, te llevará a tu aplicación, donde podrás ver tu mensaje dentro de la aplicación de prueba. Ten en cuenta que esta función de prueba de mensajes dentro de la aplicación depende de que el usuario haga clic en una notificación push de prueba para desencadenar el mensaje dentro de la aplicación. Por lo tanto, el usuario debe ser elegible para recibir notificaciones push en la aplicación correspondiente para la entrega exitosa de la notificación push de prueba.

### Vista previa

Puedes previsualizar tu mensaje dentro de la aplicación mientras lo redactas en la pestaña **Vista previa**. Esto debería ayudarte a visualizar cómo se verá tu mensaje final desde la perspectiva del usuario. Puedes previsualizar cómo se verá tu mensaje para un usuario aleatorio, un usuario específico o un usuario personalizado. También puedes previsualizar mensajes para dispositivos móviles o tabletas.

![Pestaña de redacción al crear un mensaje dentro de la aplicación que muestra la vista previa de cómo se verá el mensaje. No hay un usuario seleccionado, por lo que el Liquid agregado en la sección del cuerpo se muestra tal cual.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze tiene tres generaciones de mensajes dentro de la aplicación disponibles. Puedes ajustar a qué dispositivos se deben enviar tus mensajes, según la generación que admitan.

![Cambiar entre generaciones al previsualizar un mensaje dentro de la aplicación.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
En **Vista previa**, la vista de tu mensaje puede no ser idéntica a su representación real en el dispositivo del usuario. Siempre recomendamos enviar un mensaje de prueba a un dispositivo para asegurarte de que tus medios, texto, personalización y atributos personalizados se generen correctamente.
{% endalert %}

### Lista de verificación de prueba

- ¿Las imágenes y los medios se muestran y funcionan como se esperaba?
- ¿El Liquid funciona como se esperaba? ¿Has tenido en cuenta un [valor de atributo predeterminado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#accounting-for-null-nil-and-blank-attribute-values) en caso de que el Liquid no devuelva información?
- ¿Tu texto es claro, conciso y correcto?
- ¿Tus botones dirigen al usuario a donde deben ir?

### Escáner de accesibilidad {#accessibility-scanner}

Para apoyar las mejores prácticas de accesibilidad, Braze escanea automáticamente el contenido de los mensajes dentro de la aplicación creados con el editor HTML tradicional en función de los estándares de accesibilidad. Este escáner ayuda a identificar contenido que puede no cumplir con los estándares de las Pautas de Accesibilidad para el Contenido Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). WCAG es un conjunto de estándares técnicos reconocidos internacionalmente y desarrollados por el Consorcio World Wide Web (W3C) para hacer que el contenido web sea más accesible para personas con discapacidades.

![Resultados del escaneo de accesibilidad]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
El escáner de accesibilidad de mensajes dentro de la aplicación solo se ejecuta en mensajes creados con HTML personalizado.
{% endalert %}

#### Cómo funciona {#how-it-works}

El escáner se ejecuta automáticamente en mensajes HTML personalizados y evalúa todo tu mensaje HTML en función del [conjunto completo de reglas WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Para cada problema identificado, muestra:

- El elemento HTML específico involucrado
- Una descripción del problema de accesibilidad
- Un enlace a contexto adicional o guía de corrección

#### Comprender las pruebas de accesibilidad automatizadas {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Crea tu mensaje de LINE.
2. Selecciona la pestaña **Prueba** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba.
3. Selecciona **Enviar prueba** para enviar tu mensaje.

![Mensaje de prueba de LINE.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Push móvil {#mobile-push}

1. Redacta tu push móvil.
2. Selecciona la pestaña **Prueba** y añade tu dirección de correo electrónico o ID de usuario en el campo **Agregar usuarios individuales**.
3. Selecciona **Enviar prueba** para enviar tu mensaje redactado a tu dispositivo.

![Prueba de push]({% image_buster /assets/img_archive/testpush.png %})

Si ves un error indicando que ninguno de los usuarios seleccionados tiene tokens de notificaciones push coincidentes, el usuario de prueba no tiene un token de notificaciones push válido para la plataforma seleccionada. El usuario debe haber iniciado una sesión en la aplicación y habilitado push en ese dispositivo. Para más información, consulta [Habilitación de push y estado de suscripción a push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

#### Push web {#web-push}

1. Crea tu push web.
2. Selecciona la pestaña **Prueba**.
3. Selecciona **Enviarme una prueba**.
4. Selecciona **Enviar prueba** para enviar tu push web a tu navegador web.

![Prueba de push web]({% image_buster /assets/img_archive/testwebpush.png %})

Si ya has aceptado mensajes push desde el panel de Braze, el mensaje aparecerá en la esquina de tu pantalla. De lo contrario, selecciona **Permitir** cuando se te solicite, y el mensaje aparecerá.

Si ves un error indicando que ninguno de los usuarios seleccionados tiene tokens de notificaciones push coincidentes para push web, verifica que el usuario de prueba tenga un token de notificaciones push válido registrado para la plataforma seleccionada. Para recibir un token de notificaciones push, el usuario debe estar configurado para recibir notificaciones push de la aplicación en su dispositivo. Para más detalles, consulta [Habilitación de push y estado de suscripción a push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

{% endtab %}
{% tab SMS/MMS y RCS %}

Después de crear tu mensaje SMS, MMS o RCS, puedes enviar un mensaje de prueba a tu teléfono para ver cómo se verá en tiempo real. El destinatario debe pertenecer al grupo de suscripción de SMS que selecciones al enviar la prueba, tener un número de teléfono válido y tener al menos un país seleccionado en **Permisos geográficos**. Para más detalles, consulta las [Preguntas frecuentes sobre SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages).

1. Redacta tu mensaje SMS, MMS o RCS.
2. Selecciona la pestaña **Prueba** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba.
3. Selecciona **Enviar prueba** para enviar tu mensaje de prueba.

![Prueba de Content Card]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Después de crear tu webhook, puedes hacer un envío de prueba para verificar la respuesta del webhook. Selecciona la pestaña **Prueba** y selecciona **Enviar prueba** para enviar una prueba a la URL del webhook proporcionada. También puedes seleccionar un usuario individual para previsualizar la respuesta como un usuario específico.

{% endtab %}
{% tab WhatsApp %}

1. Crea tu mensaje de WhatsApp.
2. Selecciona la pestaña **Prueba** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba.
3. Inicia una ventana de conversación enviando un mensaje de WhatsApp al número de teléfono asociado con el grupo de suscripción que estás usando para este mensaje. El número de teléfono asociado aparece en la alerta de la pestaña **Prueba**.
4. Selecciona **Enviar prueba** para enviar tu mensaje.

![Mensaje de prueba de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Prueba de campañas personalizadas {#test-personalized-campaigns}

Si estás probando campañas que rellenan datos de usuario o utilizan propiedades de eventos personalizados, tendrás que seguir pasos adicionales o diferentes.

### Prueba de campañas personalizadas con atributos de usuario {#testing-campaigns-personalized-with-user-attributes}

Si estás utilizando la [personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) en tu mensaje, tendrás que seguir pasos adicionales para previsualizar correctamente tu campaña y comprobar que los datos de usuario rellenan correctamente el contenido.

Al enviar un mensaje de prueba, asegúrate de elegir la opción de **Seleccionar usuario existente** o previsualizar como un **Usuario personalizado**.

![Prueba de un mensaje personalizado]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Seleccionar un usuario existente {#selecting-an-existing-user}

Si seleccionas un usuario existente, introduce el ID de usuario específico o el correo electrónico en el campo de búsqueda. A continuación, utiliza la vista previa del panel para ver cómo aparecería tu mensaje para ese usuario, y envía un mensaje de prueba a tu dispositivo que refleje lo que vería ese usuario.

![Seleccionar un usuario]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Seleccionar un usuario personalizado {#selecting-a-custom-user}

Si previsualizas como un usuario personalizado, introduce texto en los distintos campos disponibles para la personalización, como el nombre del usuario y cualquier atributo personalizado. Una vez más, puedes introducir tu propia dirección de correo electrónico para enviar una prueba a tu dispositivo.

![Usuario personalizado]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Personalizar un usuario existente {#customizing-an-existing-user}

Puedes editar campos individuales de un usuario aleatorio o existente para ayudar a probar el contenido dinámico dentro de tu mensaje. Selecciona **Editar** para convertir al usuario seleccionado en un usuario personalizado que puedas modificar.

![La pestaña "Vista previa como usuario" con un botón "Editar".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Prueba de campañas personalizadas con propiedades de eventos personalizados {#testing-campaigns-personalized-with-custom-event-properties}

La prueba de campañas personalizadas con [propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) difiere ligeramente de la prueba de otros tipos de campañas descritas.

{% tabs local %}
{% tab Desencadenar manualmente %}

#### Método 1: Desencadenar la campaña manualmente {#method-1-triggering-campaign-manually}

Puedes desencadenar la campaña tú mismo como una forma robusta de probar campañas personalizadas que utilizan propiedades de eventos personalizados:

1. Redacta el texto que incluya la propiedad del evento.

![Redacción de un mensaje de prueba con propiedades]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Utiliza la [entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para entregar la campaña cuando se produzca el evento.

{% alert note %}
Si estás probando una campaña push de iOS, debes configurar el retraso a un minuto para darte tiempo a salir de la aplicación, ya que iOS no entrega notificaciones push para la aplicación actualmente abierta. Otros tipos de campañas pueden configurarse para entregarse de inmediato.
{% endalert %}

![Entrega del mensaje de prueba]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Segmenta a los usuarios como lo harías para una prueba, utilizando un filtro de prueba o segmentando tu propia dirección de correo electrónico, y termina de crear la campaña.

![Segmentación del mensaje de prueba]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Entra en tu aplicación y completa el evento personalizado.

La campaña se desencadenará y mostrará el mensaje personalizado con la propiedad del evento.

![Ejemplo de mensaje de prueba]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Mensaje de prueba %}

#### Método 2: Enviarte un mensaje de prueba {#method-2-sending-yourself-a-test-message}

Como alternativa, si guardas ID de usuario personalizados, también puedes probar la campaña enviándote un mensaje de prueba personalizado.

1. Redacta el texto de tu campaña.
2. Selecciona la pestaña **Prueba** y elige **Usuario personalizado**.
3. Añade la propiedad del evento personalizado en la parte inferior de la página, y añade tu ID de usuario o dirección de correo electrónico en el campo superior.
4. Selecciona **Enviar prueba** para recibir un mensaje personalizado con la propiedad.

![Prueba con un usuario personalizado]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Método 3: Utilizar Liquid {#method-3-using-liquid}

Puedes probar propiedades de eventos personalizados introduciendo manualmente valores con Liquid.

1. En el editor de mensajes, introduce valores para tus propiedades de eventos personalizados.
2. Selecciona la pestaña **Vista previa como usuario** para comprobar que se muestra el mensaje correcto.

{% endtab %}
{% endtabs %}

## Limitaciones {#limitations}

Hay algunas situaciones en las que los mensajes de prueba no se comportan de la misma forma que las Campaigns o Canvas enviados a usuarios reales. En estos casos, considera lanzar la Campaign o Canvas a un conjunto limitado de usuarios de prueba para validar este comportamiento.

- Ver el [centro de preferencias]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) de Braze desde los mensajes de prueba hace que el botón **Guardar preferencias** se deshabilite. Las etiquetas de Liquid del centro de preferencias también podrían no resolverse en enlaces válidos. Este es el comportamiento esperado. Para probar de extremo a extremo, consulta [Probar centros de preferencias]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#testing-preference-centers).
- Para probar mensajes dentro de la aplicación y Content Cards, el usuario objetivo debe tener un token de notificaciones push para el dispositivo objetivo.
- Para probar enlaces de cancelar suscripción en correos electrónicos, asegúrate de que la dirección de correo electrónico de tu usuario de prueba esté en el espacio de trabajo correspondiente.
- El encabezado `List-Unsubscribe` no se incluye en los correos electrónicos enviados mediante la funcionalidad de mensaje de prueba.
- Los correos electrónicos enviados a usuarios del grupo semilla no actualizan la lista de Campaigns recibidas del perfil de usuario ni incrementan los envíos en los análisis del panel.

## Solución de problemas {#troubleshooting}

### Mensajes dentro de la aplicación {#in-app-messages}

Si tu campaña de mensajes dentro de la aplicación no se desencadena mediante una campaña push, comprueba la segmentación de la campaña de mensajes dentro de la aplicación para confirmar que el usuario cumple con el público objetivo **antes** de recibir el mensaje push.

Para envíos de prueba en Android e iOS, los mensajes dentro de la aplicación que utilizan el comportamiento de clic **Solicitar permiso push** pueden no mostrarse en algunos dispositivos. Como solución alternativa:
- **Android:** Los dispositivos deben tener Android 13 y la versión 21.0.0 de nuestro SDK para Android. Otra razón puede ser que el dispositivo en el que se muestra el mensaje dentro de la aplicación ya tenga un aviso a nivel de sistema. Es posible que hayas seleccionado **No volver a preguntar**, por lo que quizá necesites reinstalar la aplicación para restablecer los permisos de notificación antes de volver a probar.
- **iOS:** Recomendamos que tu equipo de desarrolladores revise la implementación de las notificaciones push de tu aplicación y elimine manualmente cualquier código que solicite permisos push. Para más información, consulta [Mensajes dentro de la aplicación de introducción a push]({{site.baseurl}}/user_guide/channels/push/best_practices).

Para que una campaña de mensajes dentro de la aplicación basada en acciones se entregue, debes registrar eventos personalizados a través del SDK de Braze, no de las REST API, para que los usuarios puedan recibir mensajes dentro de la aplicación elegibles directamente en su dispositivo. Los usuarios reciben el mensaje dentro de la aplicación si realizan el evento durante la sesión.
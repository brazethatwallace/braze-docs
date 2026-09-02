---
nav_title: URL de acción y multimedia
article_title: Personalizar URL de acción y multimedia con Liquid
page_order: 2
description: "Este artículo de referencia describe cómo personalizar URL de acción y multimedia usando Liquid."
---

# Personalizar URL de acción y multimedia con Liquid {#personalize-action-and-media-urls-with-liquid}

> Personaliza los destinos de los enlaces y el contenido para cada usuario que recibe tu mensaje añadiendo variables Liquid a las URL de botones, enlaces, imágenes y videos.

## Vínculo profundo a contenido dentro de la aplicación {#deep-link-to-in-app-content}

{% alert tip %}
**Para desarrolladores:** Para instrucciones de integración, consulta [Vinculación en profundidad en Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=android) o [Vinculación en profundidad en Swift]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=swift). Para ayuda al elegir un tipo de enlace en iOS, consulta la [guía de vinculación en profundidad en iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Para diagnosticar problemas, consulta [Solución de problemas de vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).
{% endalert %}

### ¿Qué es la vinculación en profundidad? {#what-is-deep-linking}

La vinculación en profundidad es una forma de lanzar una aplicación nativa y proporcionar información adicional que le indica realizar una acción específica o mostrar contenido específico.

Esto tiene tres partes:

1. Identificar qué aplicación lanzar.
2. Indicar a la aplicación qué acción realizar.
3. Proporcionar a la acción cualquier dato adicional que necesite.

Los vínculos profundos son URI personalizados que enlazan a una parte específica de la aplicación y contienen estas tres partes. La clave es definir un esquema personalizado. `http:` es el esquema con el que casi todos están familiarizados, pero los esquemas pueden comenzar con cualquier palabra. Un esquema debe empezar con una letra, pero luego puede contener letras, números, signos de más, signos de menos o puntos. En la práctica, no existe un registro central para prevenir conflictos, por lo que es una buena práctica incluir tu nombre de dominio en el esquema. Por ejemplo, `twitter://` es la URI de iOS para lanzar la aplicación móvil de X, anteriormente Twitter.

Todo lo que aparece después de los dos puntos dentro de un vínculo profundo es texto de formato libre. Tú defines su estructura e interpretación; sin embargo, una convención común es modelarlo como las URL `http:`, incluyendo un `//` inicial y parámetros de consulta (por ejemplo, `?foo=1&bar=2`). Para el ejemplo anterior, `twitter://user?screen_name=[id]` se usaría para lanzar un perfil específico en la aplicación.

{% alert important %}
Para aplicaciones creadas con frameworks de envoltorio (por ejemplo, Flutter o Cordova), Braze no proporciona soporte de vinculación en profundidad específico para el envoltorio. Debes configurar los vínculos profundos en las capas nativas de iOS y Android. Para Cordova, consulta [Vinculación en profundidad en notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/deep_linking?sdktab=cordova).
{% endalert %}

### Esquemas de URI del sistema {#system-uri-schemes}

Los esquemas de URI estándar gestionados de forma nativa por iOS y Android (como `tel:`, `mailto:` y `sms:`) se pueden introducir directamente en el campo de URL del vínculo profundo sin necesidad de una integración de vínculo profundo personalizada en tu aplicación.

| Esquema | Ejemplo | Acción |
| ------ | ------- | ------ |
| `tel:` | `tel:+18005555555` | Abre el marcador telefónico |
| `mailto:` | `mailto:support@example.com` | Abre la composición de correo electrónico |
| `sms:` | `sms:+18005555555` | Abre la composición de servicio de mensajes cortos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquemas de URI del sistema"}

Estos funcionan para los comportamientos al hacer clic en notificaciones push y las acciones de botones de mensajes dentro de la aplicación. No se necesitan configuraciones adicionales del SDK or kit de desarrollo de software ni cambios en el código de la aplicación.

### Vínculo profundo a la aplicación {#deep-link-into-application}

Al componer notificaciones push, mensajes dentro de la aplicación, Banners o Content Cards, selecciona **Vínculo profundo a la aplicación** para abrir una pantalla o acción específica en tu aplicación. En algunos creadores, esta opción aparece como **Deep Link Into App**.

Antes de usar esta opción, trabaja con tus desarrolladores para definir el formato de URI y configurar tu aplicación para abrirlo. Los esquemas personalizados, como `myapp://`, abren la aplicación instalada directamente. Los enlaces universales (iOS) y los App Links (Android) usan URL `https://` que pueden abrir la aplicación cuando está instalada y recurrir a una página web cuando la aplicación no está instalada.

Para configurar este comportamiento al hacer clic:

1. En el creador de tu Campaign o Canvas, localiza **Comportamiento al hacer clic**:
   - Para notificaciones push y Content Cards, ve a la pestaña **Redactar**.
   - Para mensajes dentro de la aplicación, ve a la pestaña **Redactar**. En el editor de arrastrar y soltar, selecciona un bloque de botón o imagen y abre su panel de propiedades.
2. Selecciona **Vínculo profundo a la aplicación** o **Deep Link Into App**.
3. Introduce el enlace en el campo de URL, por ejemplo, `myapp://products/12345` para un esquema personalizado o `https://example.com/products/12345` para un enlace universal o App Link.
4. Envía un mensaje de prueba a un dispositivo físico. Una prueba exitosa abre la aplicación y navega a la pantalla o acción prevista. Para un enlace universal o App Link, también prueba en un dispositivo sin la aplicación instalada para confirmar la alternativa web esperada.

### Etiquetas UTM y atribución de Campaign {#utm-tags-and-campaign-attribution}

#### ¿Qué es una etiqueta UTM? {#what-is-a-utm-tag}

Las [etiquetas UTM (Urchin Traffic Administrador)](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) te permiten incluir detalles de atribución de Campaign directamente dentro de los enlaces. Las etiquetas UTM son utilizadas por Google Analytics para recopilar datos de atribución de Campaign y se pueden usar para rastrear las siguientes propiedades:

- `utm_source`: El identificador de la fuente del tráfico (por ejemplo, `my_app`)
- `utm_medium`: El medio de la Campaign (por ejemplo, `newsfeed`)
- `utm_campaign`: El identificador de la Campaign (por ejemplo, `spring_2016_campaign`)
- `utm_term`: Identificador de un término de búsqueda de pago que llevó al usuario a tu aplicación o sitio web (por ejemplo, `pizza`)
- `utm_content`: Un identificador del enlace o contenido específico en el que el usuario hizo clic (por ejemplo, `toplink` o `android_iam_button2`)

Las etiquetas UTM se pueden incrustar tanto en enlaces HTTP regulares (web) como en vínculos profundos y rastrearse mediante Google Analytics.

##### Cálculos de etiquetas UTM {#utm-tag-calculations}

Braze reporta _Clics totales_ para todos los enlaces en una Campaign o paso en Canvas, lo que puede incluir enlaces que no tienen etiquetas UTM. Esto significa que puedes ver un resultado diferente (a menudo menor) en los enlaces de seguimiento de Campaign de Google Analytics en comparación con los _Clics totales_ mostrados en el rendimiento de tu Campaign o en el generador de informes.

#### Uso de etiquetas UTM con Braze {#using-utm-tags-with-braze}

Si deseas usar etiquetas UTM con enlaces HTTP regulares (web) (por ejemplo, para hacer atribución de Campaign para tus campañas de correo electrónico) y tu organización ya usa Google Analytics, puedes utilizar el [constructor de URL de Google](https://ga-dev-tools.google/ga4/campaign-url-builder/) para generar enlaces UTM. Estos enlaces se pueden incrustar fácilmente en el texto de tu Campaign de Braze como cualquier otro enlace.

Para usar etiquetas UTM en vínculos profundos a tu aplicación, tu aplicación debe tener el [SDK or kit de desarrollo de software de Google Analytics](https://developers.google.com/analytics/devguides/collection/) relevante integrado y correctamente configurado para gestionar vínculos profundos. Consulta con tus desarrolladores si no estás seguro de esto.

Una vez que el SDK or kit de desarrollo de software de Analytics esté integrado y configurado, las etiquetas UTM se pueden usar con vínculos profundos en Campaigns de Braze. Para configurar etiquetas UTM para tu Campaign, incluye las etiquetas UTM necesarias en la URL de destino o en los vínculos profundos. Los siguientes ejemplos muestran cómo usar etiquetas UTM en notificaciones push y mensajes dentro de la aplicación.

##### Atribuir aperturas push y clics en mensajes dentro de la aplicación con etiquetas UTM {#attribute-push-opens-and-in-app-message-clicks-with-utm-tags}

{% tabs %}
{% tab Aperturas push %}

Para incluir etiquetas UTM en tus vínculos profundos para notificaciones push, configura el comportamiento al hacer clic del mensaje push como un vínculo profundo, luego escribe la dirección del vínculo profundo e incluye las etiquetas UTM deseadas de la siguiente manera:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![Captura de pantalla relacionada con la atribución de aperturas push y clics en mensajes dentro de la aplicación con etiquetas UTM.]({% image_buster /assets/img_archive/push_utm_tags.png %})

{% endtab %}
{% tab Clics en mensajes dentro de la aplicación %}

Para incluir etiquetas UTM en los vínculos profundos de tus mensajes dentro de la aplicación, usa lo siguiente:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![Captura de pantalla relacionada con la atribución de aperturas push y clics en mensajes dentro de la aplicación con etiquetas UTM.]({% image_buster /assets/img_archive/iam_utm_tags.png %})

{% endtab %}
{% endtabs %}

## Usa la personalización Liquid en las URL {#use-liquid-personalization-in-urls}

Puedes construir dinámicamente tu URL directamente dentro del creador de Braze, lo que te permite añadir parámetros UTM dinámicos a tus URL o enviar a los usuarios vínculos únicos (como dirigirlos a su carrito abandonado o a un producto específico que vuelve a estar disponible).

### Crear una URL con etiquetas de personalización Liquid compatibles {#create-a-url-with-supported-liquid-personalization-tags}

Las URL pueden generarse dinámicamente mediante el uso de cualquier [etiqueta de personalización Liquid compatible]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

También admitimos el acortamiento de variables Liquid definidas de forma personalizada, como en los siguientes ejemplos:

### Crear una URL usando variables Liquid {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Acortar URL generadas por variables Liquid {#shorten-urls-rendered-by-liquid-variables}

**Canales compatibles:** KakaoTalk, LINE, servicio de mensajes cortos, RCS, WhatsApp

Acortamos las URL que son generadas por Liquid, incluso aquellas incluidas en propiedades de desencadenamiento por API. Por ejemplo, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa una URL válida, acortamos y rastreamos esa URL antes de enviar el mensaje.

### Acortar URL en el endpoint `/messages/send` {#shorten-urls-in-messagessend-endpoint}

El acortamiento de enlaces también está habilitado para mensajes exclusivos de API a través del [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Para obtener una lista completa de los parámetros de solicitud, consulta [parámetros de solicitud]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters).

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Sí | Booleano | Establece `link_shortening_enabled` en `true` para activar el acortamiento de enlaces. Para usar el seguimiento, deben estar presentes un `campaign_id` y un `message_variation_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Acortar URL en el endpoint /messages/send" }
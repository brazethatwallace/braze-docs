---
nav_title: Crear notificaciones enriquecidas
article_title: "Creación de notificaciones push enriquecidas para iOS"
page_order: 3
page_type: tutorial
description: "Este tutorial cubre los requisitos y pasos para crear notificaciones enriquecidas de iOS para tus Campaigns de Braze."

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Crear notificaciones push enriquecidas para iOS {#create-rich-push-notifications-for-ios}

> Las notificaciones enriquecidas permiten una mayor personalización en tus notificaciones push al añadir contenido adicional más allá del texto. Las notificaciones de Android incluyen imágenes en las notificaciones push desde hace tiempo, lo que se conoce como "imagen de notificación expandida". A partir de iOS 10, tus clientes podrán recibir notificaciones push de iOS que incluyan GIF, imágenes, videos o audio.

## Requisitos previos {#prerequisites}

Antes de crear una notificación push enriquecida para iOS, ten en cuenta los siguientes detalles:

- Para asegurarte de que tu aplicación pueda enviar notificaciones enriquecidas, sigue las instrucciones de [integración push de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#ios-10-rich-notifications), ya que tu desarrollador necesitará añadir una extensión de servicio a tu aplicación.
- Los tipos de archivo que actualmente admitimos para carga directa en nuestro panel incluyen JPEG, PNG o GIF. Estos archivos también se pueden introducir en el campo de URL con plantilla junto con estos tipos de archivo adicionales: AIF, M4A, MP3, MP4 o WAV.
- Consulta la [documentación de Apple](https://developer.apple.com/reference/usernotifications/unnotificationattachment) para conocer las limitaciones y especificaciones de medios.
- iOS escalará las imágenes para que se ajusten a la pantalla y escalará las imágenes enriquecidas para la vista activa o de bloqueo.

{% alert note %}
Desde enero de 2020, las notificaciones push enriquecidas de iOS pueden manejar imágenes de 1038x1038 que pesen menos de 10&nbsp;MB, pero recomendamos usar el tamaño de archivo más pequeño posible. En la práctica, enviar archivos grandes puede causar estrés innecesario en la red y hacer que los tiempos de espera de descarga sean más frecuentes.
{% endalert %}

{% alert important %}
Es posible que las imágenes de las notificaciones push no se muestren como se espera si el tamaño del archivo de la imagen es demasiado grande, la relación de aspecto es incorrecta, el texto excede la longitud máxima del mensaje o el texto del título excede la longitud máxima del título.
{% endalert %}

### Recuento de caracteres {#character-count}

Aunque no podemos proporcionar una regla estricta sobre el número preciso de caracteres a incluir en un push, [proporcionamos algunas directrices]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats) a considerar al diseñar mensajes de iOS. Puede haber cierta variación dependiendo de la presencia de una imagen, el estado de la notificación y la configuración de visualización del dispositivo del usuario, y el tamaño del dispositivo. En caso de duda, mantenlo breve y conciso.

Como práctica recomendada, Braze recomienda mantener cada línea de texto tanto para el título opcional como para el cuerpo del mensaje en aproximadamente 30-40 caracteres en una notificación push móvil.

#### Estados de notificación {#notification-states}

Tus usuarios pueden ver las notificaciones push en una variedad de situaciones diferentes, y podrían ver diferentes longitudes de texto como se indica a continuación.

<table aria-label="Estados de notificación">
  <caption>Estados de notificación</caption>
<thead>
  <tr>
    <th>Pantalla de bloqueo o centro de notificaciones</th>
    <th>Expandida</th>
    <th>Dispositivo activo</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">Este es el escenario más común.<br><br><b>Título:</b> 1 línea de texto<br><b>Cuerpo:</b> 4 líneas de texto<br><b>Imagen:</b> miniatura cuadrada</td>
    <td width="33%">Cuando un usuario mantiene presionado un mensaje.<br><br><b>Título:</b> 1 línea de texto<br><b>Cuerpo:</b> 7 líneas de texto<br><b>Imagen:</b> relación de aspecto 2:1 (recomendada, consulta la siguiente nota)</td>
    <td width="33%">Cuando un usuario recibe un push mientras su teléfono está desbloqueado y activo.<br><br><b>Título:</b> 1 línea de texto<br><b>Cuerpo:</b> 2 líneas de texto</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Estados de notificación" }

![Ejemplos de notificaciones push mostradas en la pantalla de bloqueo, expandidas y con el dispositivo activo.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Aunque recomendamos una relación de aspecto 2:1 para las notificaciones push expandidas, se admite prácticamente cualquier relación de aspecto. Las imágenes siempre abarcarán todo el ancho de la notificación, y la altura se ajustará en consecuencia.
{% endalert %}

#### Variables en el truncamiento de texto {#variables-in-text-truncation}

Al crear contenido, considera los siguientes escenarios que pueden afectar la cantidad de texto que se muestra.

{% tabs %}
{% tab Temporización %}

Dependiendo de cuándo un usuario interactúe con una notificación push, la marca de tiempo puede acortar el texto del título.

![Ejemplo de notificación push con una marca de tiempo de "ahora" y un recuento de caracteres del título de 35.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Recuento de caracteres del título: **35**

![Ejemplo de notificación push con una marca de tiempo de "hace 3h" y un recuento de caracteres del título de 33.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Recuento de caracteres del título: **33**

![Ejemplo de notificación push con una marca de tiempo de "Ayer, 8:37 AM" y un recuento de caracteres del título de 22.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Recuento de caracteres del título: **22**

{% endtab %}
{% tab Imágenes %}

El texto del cuerpo se acorta aproximadamente 10 caracteres por línea cuando hay una imagen presente.

![Ejemplo de notificación push sin imagen y un recuento de caracteres del cuerpo de 179.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Recuento de caracteres del cuerpo: **179**

![Ejemplo de notificación push con una imagen y un recuento de caracteres del cuerpo de 154.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Recuento de caracteres del cuerpo: **154**

{% endtab %}
{% tab Nivel de interrupción %}

Para iOS 15, las designaciones de Urgente y Crítica empujan el título a una nueva línea sin la marca de tiempo, dándole un poco más de espacio.

![Ejemplo de notificación push sin designación de Urgente o Crítica y un recuento de caracteres del título de 35.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Recuento de caracteres del título: **35**

![Ejemplo de notificación push con una designación de Urgente y un recuento de caracteres del título de 39.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Recuento de caracteres del título: **39**

{% endtab %}
{% tab Más %}

Los siguientes detalles también pueden afectar el truncamiento de texto:

- **Configuración de pantalla del teléfono:** un usuario puede aumentar o disminuir el tamaño de fuente global de la interfaz en su teléfono, generalmente por razones de accesibilidad.
- **Ancho del dispositivo:** el mensaje podría mostrarse en un teléfono pequeño o en un iPad ancho.
- **Tipos de contenido:** los emojis y caracteres anchos como "m" y "w" ocupan más espacio que "i" o "t", y las palabras más largas como "interacción" pueden ajustarse de línea de forma más abrupta que las palabras más cortas.

{% endtab %}
{% endtabs %}

## Configurar tu notificación enriquecida de iOS {#setting-up-your-ios-rich-notification}

### Paso 1: Crear una Campaign push {#step-1-create-a-push-campaign}

Sigue los [pasos de la Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#create-a-push-message) para redactar una notificación push para iOS. Usarás el mismo creador que utilizas para configurar notificaciones push que no contienen contenido enriquecido.

### Paso 2: Añadir medios {#step-2-add-media}

Añade tu archivo de imagen, GIF, audio o video en el campo **iOS Notification Image** en el creador del mensaje. Consulta los [requisitos](#requirements) sobre cómo añadir tus archivos de contenido.

![Un ejemplo de texto de resumen para una notificación push.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

También puedes limitar este mensaje para que solo se envíe a usuarios que tengan un dispositivo con iOS 10. Para los usuarios que no hayan actualizado a iOS 10, aparecerá como notificaciones de solo texto sin el contenido enriquecido si dejas la opción **Only send to devices with Rich Notification support** sin marcar.

![La sección de imagen de notificación expandida donde puedes añadir una imagen o introducir una URL de imagen.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### Paso 3: Continuar creando tu Campaign {#step-3-continue-creating-your-campaign}

Una vez que el contenido de tu notificación enriquecida se haya cargado en el panel, puedes continuar [planificando tu Campaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#choose-delivery-schedule-or-trigger).

Cuando un usuario reciba la notificación push, puede presionar con fuerza el mensaje push para expandir la imagen.

![Un usuario recibe una notificación push y presiona con fuerza el mensaje para mostrar una imagen expandida que dice "¡Hola!".]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }
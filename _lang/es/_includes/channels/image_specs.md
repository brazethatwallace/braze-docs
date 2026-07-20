{% if include.variable_name == "image behavior" %}


| Diseño | Comportamiento |
| --- | --- |
| Imagen y texto | Las imágenes altas o estrechas se reducirán y se centrarán horizontalmente. Las imágenes anchas se recortarán por los bordes horizontales. |
| Solo imagen | El mensaje cambiará de tamaño para adaptarse a imágenes de la mayoría de las relaciones de aspecto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabla" }

{% endif %}

{% if include.variable_name == "payload size" %}

Recomendamos los siguientes tamaños de carga útil:

| Sistema de mensajería | Carga útil recomendada |
| --- | --- |
| iOS (pre-iOS 8) | 0,256 KB |
| iOS (post-iOS 8) | 2 KB |
| Android (FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabla" }

{% endif %}

{% if include.variable_name == "in-app messages" %}

Los mensajes modales dentro de la aplicación están diseñados para ajustarse al dispositivo en las proporciones mejores y más completas posibles, manteniéndose fieles al tamaño y las proporciones de la imagen o el texto que elijas para tu mensaje.

Aunque no hay límites en cuanto al número de caracteres de texto que puedes incluir en un mensaje dentro de la aplicación (así como en los botones, el titular, el cuerpo principal y otros), te recomendamos moderar el número de caracteres de texto que utilizas. Demasiado texto obligará a los usuarios a ampliar y desplazar el mensaje.

Todos los mensajes dentro de la aplicación tienen un tamaño de imagen recomendado de 500 KB, un tamaño máximo de 5 MB y admiten los tipos de archivo PNG, JPEG y GIF. Las imágenes WebP no son compatibles con todos los dispositivos o navegadores; recomendamos convertir las imágenes WebP a PNG o JPEG antes de añadirlas a los mensajes dentro de la aplicación.

{% tabs %}
{% tab Portrait %}

| Tipo | Relación de aspecto | Calidad de imagen | Notas |
| --- | --- | --- | --- |
| Retrato a pantalla completa con texto | 6:5 | Alta resolución 1200 x 1000 px <br>Resolución mínima 600 x 500 px | Se puede recortar por todos los lados, pero la imagen siempre ocupará el 50% superior de la ventana. |
| Retrato a pantalla completa (solo imagen, con o sin botones) | 3:5 | Alta resolución 1200 x 2000 px <br> Resolución mínima 600 x 1000 px | El recorte puede producirse en los bordes horizontales en los dispositivos más altos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabla" }

{% endtab %}
{% tab Landscape %}

| Tipo | Relación de aspecto | Calidad de imagen | Notas |
| --- | --- | --- | --- |
| Pantalla completa apaisada con texto | 10:3 | Alta resolución 2000 x 600 px <br>Resolución mínima 1000 x 300 px | Se puede recortar por todos los lados, pero la imagen siempre ocupará el 50% superior de la ventana. |
| Pantalla completa apaisada (solo imagen, con o sin botones) | 5:3 | Alta resolución 2000 x 600 px <br> Resolución mínima 1000 x 600 px | El recorte puede producirse en los bordes horizontales en los dispositivos más altos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabla" }

{% endtab %}
{% tab Slideup %}

| Tipo | Relación de aspecto | Calidad de imagen | Notas |
| --- | --- | --- | --- |
| Deslizamiento hacia arriba | 1:1 | Alta resolución 150 x 150 px <br> Resolución mínima 50 x 50 px | Las imágenes de distintas relaciones de aspecto cabrán en un contenedor de imágenes cuadrado, sin recortar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabla" }

{% endtab %}
{% tab Modal %}

| Tipo | Relación de aspecto | Calidad de imagen | Notas |
| --- | --- | --- | --- |
| Modal (solo imagen) | 1:1 | Resolución máxima recomendada: 1200 x 2000 px <br> Resolución mínima: 600 x 600 px | El mensaje cambiará de tamaño para adaptarse a imágenes de la mayoría de las relaciones de aspecto. La resolución máxima recomendada tiene una relación de aspecto de 3:5, lo que puede no proporcionar resultados óptimos. Aunque las imágenes más grandes son utilizables, pueden provocar tiempos de carga más largos. <br> La relación de aspecto ideal para las imágenes es 1:1, y si no se cumple esta relación, puede aparecer una advertencia durante la carga. Esta advertencia es una sugerencia para obtener mejores resultados y no impide la carga de imágenes más grandes. |
| Modal con texto | 29:10 | Alta resolución 1450 x 500 px <br> Resolución mínima 600 x 205 px | Las imágenes altas se reducirán y se centrarán horizontalmente. Las imágenes anchas se recortarán por los bordes horizontales. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tabla" }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| Tipo de mensaje | Longitud máxima del mensaje | Longitud máxima del título |
| --- | --- | --- |
| Pantalla de bloqueo de iOS | 175 caracteres | 43 caracteres |
| Notificación de iOS | 175 caracteres | 43 caracteres |
| Alerta de banner en iOS | 85 caracteres | 43 caracteres |
| Pantalla de bloqueo de Android | 49 caracteres | 43 caracteres |
| Cajón de notificaciones de Android | 597 caracteres | 43 caracteres |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tabla" }

El tamaño recomendado para todas las imágenes push es de 500 KB.

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="Tabla">
  <thead>
    <tr>
      <th>Tipo de imagen</th>
      <th>Relación de aspecto</th>
      <th>Píxeles máximos</th>
      <th>Tamaño máximo de la imagen</th>
      <th>Tipos de archivo</th>
      <th>Notas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1 (recomendado)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG, JPEG, GIF</td>
      <td>A partir de enero de 2020, las notificaciones push enriquecidas de iOS pueden manejar imágenes de 1038 x 1038 px siempre que no superen los 10 MB, pero recomendamos utilizar un tamaño de archivo lo más pequeño posible. En la práctica, enviar archivos de gran tamaño puede causar una tensión innecesaria en la red y hacer que los tiempos de espera de descarga sean más frecuentes.<br><br>Para más información, consulta <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">Notificaciones enriquecidas de iOS</a>.</td>
    </tr>
    <tr>
      <td>Icono push de Android</td>
      <td>1:1</td>
      <td>N/A</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Imagen de notificación ampliada de Android</td>
      <td>2:1</td>
      <td><b>Pequeña:</b><br>512 x 256<br><br><b>Mediana:</b><br>1024 x 512<br><br><b>Grande:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td>Se utiliza en las <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">notificaciones enriquecidas de Android</a>.</td>
    </tr>
    <tr>
      <td>Imagen en línea de Android</td>
      <td>3:2</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>PNG, JPEG</td>
      <td>Para más detalles, consulta <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Push de imagen en línea de Android</a>.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 aria-label="Tabla" }

{% endif %}

{% if include.variable_name == "email" %}

| Tipo de correo electrónico | Propiedades máximas recomendadas |
| --- | --- |
| Solo texto | 25 KB |
| Texto con imágenes | 60 KB |
| Anchura del correo electrónico | 600 px |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabla" }

| Especificaciones de imagen | Propiedades máximas recomendadas |
| --- | --- |
| Tamaño | 5 MB |
| Ancho | Encabezado: 600 px<br>Cuerpo: 480 px |
| Tipos de archivo | PNG, JPEG, GIF<br><br> La compatibilidad con imágenes WebP varía según el cliente de correo electrónico. Para garantizar una visualización fiable, convierte las imágenes WebP a PNG o JPEG antes de añadirlas a los mensajes de correo electrónico.<br><br>Las imágenes SVG no se recomiendan para mensajes de correo electrónico debido a problemas de compatibilidad con Gmail y otros clientes de correo electrónico importantes. Usa PNG, JPEG o GIF en su lugar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabla" }

| Especificaciones del texto | Propiedades máximas recomendadas |
| --- | --- |
| Longitud de la línea del asunto | 35 caracteres<br>De 6 a 10 palabras |
| Longitud de `"From: Name"` | 25 caracteres |
| Longitud del preencabezado | 85 caracteres |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabla" }

{% endif %}

{% if include.variable_name == "content cards" %}

| Tipo de tarjeta | Relación de aspecto     | Calidad de imagen       |
| --------- | ---------------- | ------------------- |
| Clásica   | Relación de aspecto 1:1 | 60 x 60&nbsp;px        |
| Con subtítulo | Relación de aspecto 4:3 | 600&nbsp;px de anchura mínima |
| Banner    | Cualquier relación de aspecto | 600&nbsp;px de anchura mínima |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tabla" }

Para más información, consulta [Detalles creativos de Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details).

{% endif %}

{% if include.variable_name == "WhatsApp images" %}

Estas especificaciones se aplican a los encabezados de plantilla, los mensajes multimedia de respuesta y los mensajes de imagen.

| Propiedad | Especificaciones | Notas |
|---|---|---|
| Formatos compatibles | JPEG, PNG | Meta solo admite oficialmente JPEG y PNG para mensajes de imagen. WebP solo es compatible con stickers (no con mensajes de imagen estándar). |
| Tamaño máximo de archivo | 5 MB | |
| Modo de color | 8 bits, RGB o RGBA | |
| Pie de imagen (solo mensajes de imagen) | Opcional; 1024 caracteres como máximo | |
| Dimensiones recomendadas | 1125 × 600 px | Recomendamos usar imágenes JPEG o PNG de 1125×600 px (1,91:1) para una visualización uniforme en todos los dispositivos y cumplir con los requisitos de Meta. |
| Relación de aspecto recomendada | 1,91:1 (panorámica) | Se aceptan los formatos cuadrado (1:1) y panorámico (16:9), pero las imágenes pueden recortarse o ampliarse según el dispositivo del usuario.<br><br> Para las tarjetas de carrusel, WhatsApp recorta automáticamente las imágenes del encabezado a una relación panorámica, a menos que no haya texto del cuerpo, en cuyo caso se muestra como cuadrada.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tabla" }

{% endif %}

{% if include.variable_name == "WhatsApp videos" %}

Las siguientes especificaciones se aplican a los encabezados de plantilla, los mensajes multimedia de respuesta, los mensajes de video y los encabezados de tarjetas de carrusel.

| Propiedad | Especificaciones |
|---|---|
| Formatos compatibles | MP4, 3GPP |
| Tamaño de archivo | 16 MB como máximo |
| Códec de video | Solo H.264 |
| Códec de audio | Solo AAC |
| Pistas de audio | Una sola pista de audio o sin pista de audio |
| Pie de video (solo mensajes de video) | Opcional; 1024 caracteres como máximo |
| Relación de aspecto recomendada | 1,91:1 (panorámica) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabla" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

{% endif %}
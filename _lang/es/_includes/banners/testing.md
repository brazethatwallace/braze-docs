{% if include.page == "testing" %}Mientras [redactas tu mensaje de banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#compose-a-banner), selecciona{% elsif include.page == "campaigns" %}Selecciona{% endif %} **vista previa** para obtener una vista previa de tu banner o enviar un mensaje de prueba.

![Pestaña Vista previa del compositor de banners.]({% image_buster /assets/img/banners/select_preview.png %}){: style="max-width:50%;"}

Ten en cuenta que la vista previa puede no ser idéntica al renderizado final en el dispositivo del usuario debido a las diferencias entre los distintos equipos.

Para enviar un mensaje de prueba, añade un grupo de prueba de contenido o uno o varios usuarios individuales como **Test Recipients** y, a continuación, selecciona **Send Test**. Podrás ver tu mensaje de prueba en el dispositivo durante un máximo de 5 minutos. A continuación, puedes seleccionar **Copy vista previa link** para generar y copiar un enlace de vista previa compartible que muestra cómo se verá el banner para un usuario aleatorio. El enlace tendrá una validez de siete días antes de que sea necesario volver a generarlo.

![Pestaña Vista previa del compositor de banners.]({% image_buster /assets/img/banners/preview_banner.png %})

Mientras revisas tu banner de prueba, verifica lo siguiente:

- ¿Tu Campaign de banner está asignada a una ubicación?
- ¿Las imágenes y los medios se muestran y funcionan como esperabas en los tipos de dispositivos y tamaños de pantalla a los que te diriges?
- ¿Tus enlaces y botones dirigen al usuario adonde deben ir?
- ¿Funciona Liquid como se esperaba? ¿Has previsto un valor de atributo predeterminado en caso de que Liquid no devuelva ninguna información?
- ¿Tu texto es claro, conciso y correcto?

Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/).
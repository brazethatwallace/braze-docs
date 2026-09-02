---
nav_title: Seguimiento de la ubicación
article_title: Seguimiento de ubicación
page_order: 0
page_type: reference
description: "Este artículo de referencia explica cómo utilizar el seguimiento de ubicación y la segmentación por ubicación en tus aplicaciones, y qué partners admiten el seguimiento de ubicación."
tool: Location
search_rank: 2
---

# Seguimiento de ubicación {#location-tracking}

> La recopilación de ubicación captura la ubicación más reciente de un usuario cuando se abrió la aplicación utilizando datos de ubicación GPS. Puedes utilizar esta información para segmentar datos basándote en los usuarios que se encontraban en una ubicación definida.

## Habilitar el seguimiento de ubicación {#enabling-location-tracking}

Para habilitar la recopilación de ubicación en tu aplicación, consulta la guía del desarrollador para la plataforma que estés utilizando:

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)

En general, las aplicaciones móviles utilizan el chip GPS del dispositivo y otros sistemas (como el escaneo de Wi-Fi) para rastrear la ubicación de un usuario. Las aplicaciones Web utilizan WPS (sistema de posicionamiento Wi-Fi) para rastrear la ubicación de un usuario. Todas estas plataformas requieren que los usuarios opten por el seguimiento de ubicación. La precisión de tus datos de seguimiento de ubicación puede verse afectada por si tus usuarios tienen o no el Wi-Fi habilitado en sus dispositivos. Los usuarios de Android también pueden elegir diferentes modos de ubicación: los usuarios que están en modo "Ahorro de batería" o "Solo dispositivo" pueden tener datos imprecisos.

### Ubicación del usuario del SDK or kit de desarrollo de software por dirección IP {#sdk-user-location-by-ip-address}

Braze detecta las ubicaciones de los usuarios a partir del país geolocalizado utilizando la dirección IP desde el inicio de la primera sesión del SDK or kit de desarrollo de software.

Anteriormente, Braze utilizaba el código de país de la configuración regional del dispositivo durante la creación del usuario del SDK or kit de desarrollo de software y durante la primera sesión. Solo después de procesar el inicio de la primera sesión se utilizaba la dirección IP para establecer el país más fiable en el usuario. Esto significaba que el país del usuario se establecía con mayor precisión solo a partir de la segunda sesión en adelante, solo después de que se procesara el inicio de la primera sesión.

Ahora, Braze utiliza la dirección IP para establecer el valor del país en los perfiles de usuario creados a través del SDK or kit de desarrollo de software, y esa configuración de país basada en IP está disponible durante y después de la primera sesión.

#### Recopilación automática de ubicación {#automatic-location-collection}

Cuando está habilitada, la recopilación automática de ubicación en el SDK or kit de desarrollo de software es independiente del comportamiento de país basado en IP. Se relaciona con las señales de ubicación del dispositivo, como el GPS cuando el usuario ha concedido permiso, lo que alimenta filtros como `Most Recent Location`. No rellena automáticamente campos detallados como la ciudad solo a partir de la IP.

Para la segmentación por ciudad o código postal, utiliza [`setLastKnownLocation()`]({{site.baseurl}}/developer_guide/analytics/tracking_location) (consulta el artículo del SDK or kit de desarrollo de software para tu plataforma), tu propio servicio de geolocalización por IP que escriba atributos personalizados, o la [segmentación por ubicación]({{site.baseurl}}/user_guide/audience/segments/location_targeting) con los datos que recopiles.

## Segmentación por ubicación {#location-targeting}

Utilizando los datos de seguimiento de ubicación y los segmentos, puedes configurar campañas y estrategias basadas en la ubicación. Por ejemplo, es posible que quieras ejecutar una campaña promocional para los usuarios que viven en una región particular o excluir a los usuarios de una región que tiene regulaciones más estrictas.

Consulta [Segmentación por ubicación]({{site.baseurl}}/user_guide/audience/segments/location_targeting) para obtener más información sobre cómo crear un segmento de ubicación.

## Establecer manualmente el atributo de ubicación predeterminado {#hard-setting-the-default-location-attribute}

También puedes utilizar el [endpoint `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) en nuestra API para actualizar el atributo estándar [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields). Un ejemplo es:

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## Soporte de partners para balizas y geovallas {#partnership-support-for-beacon-and-geofence}

Combinar el soporte existente de balizas o geovallas con nuestras características de segmentación y mensajería te proporciona más información sobre las acciones físicas de tus usuarios para que puedas enviarles mensajes en consecuencia. Puedes aprovechar el seguimiento de ubicación con algunos de nuestros partners:

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare)

## Diferencias entre geovallas y seguimiento de ubicación {#differences-between-geofences-and-location-tracking}

{% multi_lang_include locations_and_geofences/geofences_vs_location_tracking.md %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cuándo recopila Braze los datos de ubicación? {#when-does-braze-collect-location-data}

Braze solo recopila la ubicación cuando la aplicación está abierta en primer plano. Como resultado, nuestro filtro `Most Recent Location` segmenta a los usuarios en función de dónde abrieron la aplicación por última vez (también conocido como inicio de sesión).

También debes tener en cuenta los siguientes matices:

- Si la ubicación está deshabilitada, el filtro `Most Recent Location` muestra la última ubicación registrada.
- Si un usuario alguna vez ha tenido una ubicación almacenada en su perfil, califica para el filtro `Location Available`, incluso si ha dejado de participar en el seguimiento de ubicación desde entonces.

### ¿Cuál es la diferencia entre los filtros Most Recent Device Locale y Most Recent Location? {#whats-the-difference-between-the-most-recent-device-locale-and-most-recent-location-filters}

El filtro `Most Recent Device Locale` proviene de la configuración del dispositivo del usuario. Por ejemplo, para los usuarios de iPhone aparece en su dispositivo en **Configuración** > **General** > **Idioma y región**. Este filtro se utiliza para capturar el idioma y el formato regional, como fechas y direcciones, y es independiente del filtro `Most Recent Location`.

El filtro `Most Recent Location` es la última ubicación GPS conocida del dispositivo. Se actualiza al inicio de la sesión y se almacena en el perfil del usuario.

### Si un usuario deja de participar en el seguimiento de ubicación, ¿se eliminan sus datos de ubicación anteriores de Braze? {#if-a-user-opts-out-of-location-tracking-is-their-previous-location-data-removed-from-braze}

No. Si un usuario alguna vez ha tenido una ubicación almacenada en su perfil, esos datos no se eliminan automáticamente si posteriormente deja de participar en el seguimiento de ubicación.

## Solución de problemas {#troubleshooting}

### Ningún usuario tiene ubicaciones disponibles {#no-users-have-available-locations}

Braze captura la ubicación más reciente de un usuario de forma predeterminada a través del SDK or kit de desarrollo de software. Esto normalmente significa que la "ubicación reciente" es la ubicación desde la cual tu usuario utilizó tu aplicación más recientemente. Si envías datos de ubicación en segundo plano a Braze, es posible que tengas datos más detallados disponibles.

Si ningún usuario tiene ubicaciones disponibles, dos comprobaciones rápidas pueden ayudarte a confirmar la recopilación de datos y la transferencia de datos.

#### Recopilación de datos {#data-collection}

Confirma que tu aplicación está recopilando datos de ubicación:

- Para iOS, esto significa que los usuarios optan por compartir sus datos de ubicación a través de un aviso en algún momento del recorrido del usuario.
- Para Android, confirma que tu aplicación solicita permisos de ubicación precisa o aproximada durante la instalación.

Para ver si los datos de ubicación del usuario se están enviando a Braze, utiliza el filtro **Location Available**. Este filtro te permite ver el porcentaje de usuarios con una "ubicación más reciente".

![Un segmento "Test Location" que utiliza el filtro "Location Available".]({% image_buster /assets/img_archive/trouble7.png %})

#### Transferencia de datos {#data-transfer}

Confirma que tus desarrolladores están pasando datos de ubicación a Braze. Normalmente, el paso de datos de ubicación se gestiona automáticamente por el SDK or kit de desarrollo de software después de que el usuario concede los permisos, pero tus desarrolladores pueden haber deshabilitado el seguimiento de ubicación en Braze. Puedes encontrar más información sobre el seguimiento de ubicación para:
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)
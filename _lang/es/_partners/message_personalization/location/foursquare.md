---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Este artículo de referencia describe la asociación entre Braze y Foursquare, una plataforma de datos de ubicación, que permite desencadenar eventos en tiempo real basados en la ubicación."
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) es una plataforma de datos de ubicación que proporciona orientación de datos de ubicación en tus Campaigns de Braze. Utiliza el SDK Pilgrim de Foursquare en aplicaciones iOS y Android para desencadenar eventos en tiempo real basados en la ubicación, lo que te permitirá aprovechar las potentes capacidades de orientación geográfica de Foursquare para enviar mensajes relevantes y personalizados con Braze.

_Esta integración está mantenida por Foursquare._

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Foursquare | Se requiere una cuenta de Foursquare para aprovechar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos de `users.track`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Espacio de trabajo e ID de aplicación de Braze | El espacio de trabajo y los ID de aplicación de Braze se pueden encontrar en la [consola para desarrolladores]({{site.baseurl}}/api/api_key). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Para integrar las dos plataformas, debes integrar los dos SDK y mapear los campos de usuario correspondientes. Después de integrar el SDK de Pilgrim, recibirás eventos de ubicación en el dispositivo o a través de un webhook.

### Paso 1: Mapear los campos de ID de usuario {#step-1-map-user-id-fields}

Para mapear correctamente los campos entre los dos SDK, establece el mismo ID de usuario en ambos sistemas usando el [método `changeUser`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#setting-user-ids) en el SDK de Braze y el método `setUserId` de [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) en el SDK de Pilgrim.

### Paso 2: Configurar la consola de Pilgrim {#step-2-configure-pilgrim-console}
![Una imagen de la consola de Pilgrim solicitando el ID de grupo, el ID de aplicación Android y el ID de aplicación iOS.]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Busca el espacio de trabajo y los ID de aplicación en la consola para desarrolladores de Braze. A continuación, introduce tu clave de API REST de Braze y los ID de aplicación en la consola de Foursquare Pilgrim.

Una vez que hayas configurado la consola de Pilgrim, el SDK de Pilgrim registrará los eventos de ubicación y los reenviará a Braze, lo que te permitirá reorientar y segmentar a los clientes cualificados. Consulta el [sitio para desarrolladores de Foursquare](https://developer.foursquare.com/) para obtener más detalles.

{% alert important %}
El SDK de Pilgrim requiere que habilites los servicios de ubicación.
{% endalert %}

## Desencadenar mensajes {#triggering-messages}

Una vez configurada la integración, puedes configurar una Campaign o Canvas que actúe en función de los eventos de ubicación generados por el SDK de Pilgrim. Esta ruta de integración es ideal para enviar mensajes en tiempo real justo después de que los usuarios entren en un lugar de interés, o para comunicaciones de seguimiento diferidas después de que se hayan ido, como una nota de agradecimiento o un recordatorio.

Para enviar una Campaign que enviará mensajes según una ubicación establecida:
- Crea una Campaign o Canvas de Braze que se envíe con **entrega basada en acciones**
- Para tu desencadenador, utiliza un evento personalizado de `arrival` con un filtro de propiedad de evento para `locationType`, como se muestra en la siguiente captura de pantalla.

![Una Campaign basada en acciones en el paso de entrega que muestra "arrival" seleccionado como la opción "realizar evento personalizado", donde "locationType" es igual a "home".]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Reorientar {#retargeting}

Para reorientar a tus usuarios, usa el SDK de Pilgrim para configurar un atributo personalizado `last_location` en los perfiles de usuario de tus usuarios de Braze. Luego puedes usar la comparación `matches regex` para reorientar a los usuarios que fueron a un lugar particular en el mundo real; por ejemplo, segmentar a todos los usuarios que estuvieron recientemente en una pizzería.

![Una Campaign basada en acciones en el paso de usuarios objetivo que muestra "last_location" igual a "Pizza Place".]({% image_buster /assets/img_archive/last-location-segment.png %})

También puedes segmentar usuarios en Braze que visitaron un tipo particular de lugar basándote en el `primaryCategoryId` de Foursquare en un periodo de tiempo determinado. Para aprovechar este punto de datos en tus ejemplos de reorientación, registra `primaryCategoryId` como una propiedad de evento durante tu proceso de segmentación de audiencia. Para identificar los usuarios y las propiedades utilizados por la API de Foursquare y el SDK de Pilgrim, consulta el [sitio para desarrolladores de Foursquare](https://developer.foursquare.com/).
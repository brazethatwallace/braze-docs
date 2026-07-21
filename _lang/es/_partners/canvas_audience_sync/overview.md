---
nav_title: Acerca de Audience Sync
article_title: Acerca de Audience Sync
alias: /partners/about_audience_sync/
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con Facebook para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 0
tool:
  - Canvas

---

# Acerca de Audience Sync {#about-audience-sync}

> La característica Braze Audience Sync te ayuda a ampliar el alcance de tus campañas a muchas de las principales tecnologías sociales y publicitarias. A través de [Braze Canvas]({{site.baseurl}}/user_guide/messaging/canvas), las marcas pueden sincronizar de forma dinámica y segura datos de usuarios de primera mano en el ecosistema publicitario para impulsar el marketing y la eficiencia operativa.

## Disponibilidad de la característica {#feature-availability}

Todos los clientes de Braze tienen acceso inmediato a Audience Sync con Google y Facebook, pero los clientes con Action Credits pueden acceder a todos los partners de Audience Sync. Para desbloquear destinos adicionales de Audience Sync para clientes que no utilizan Action Credits, compra Audience Sync Pro. Ponte en contacto con tu director de cuentas de Braze para obtener más información.

## Casos de uso {#use-cases}

- Dirigirse a usuarios de alto valor utilizando canales propios y de pago para aumentar las compras o la participación.
- Crear audiencias similares de tus usuarios de alto valor para optimizar los costes de adquisición de nuevos usuarios y las conversiones.
- Reorientar con anuncios a los usuarios que son menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de tu marca.

## Resumen {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| Destino | Tiempo para que el destino coincida con los miembros de la audiencia | Límite de velocidad | Similitud o semejanza | Consejos |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync) | Hasta 24 horas | 250.000 solicitudes por minuto. Por lotes cada 5 segundos con un reintento automático. | Sí | {::nomarkdown}<ul><li>Criteo admite hasta 1.000 audiencias de anuncios.</li><li>La audiencia mínima es de 500 personas, y la recomendada es de más de 20.000.</li></ul>{:/} |
| [Facebook o Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) | Hasta 24 horas | 190.000 cuentas de anuncios por hora | Sí | {::nomarkdown}<ul><li>Facebook admite hasta 500 audiencias de anuncios.</li><li>Facebook requiere audiencias de al menos 1.000 usuarios.</li></ul>{:/} |
| [Google Ads o YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) | Entre 6 y 12 horas | Por lotes cada 5 segundos con un reintento automático basado en la respuesta de Google | No | {::nomarkdown}<ul><li><b>Customer match:</b> Utiliza el identificador de anuncio del móvil, la dirección de correo electrónico o el número de teléfono.</li><li>Google Audiences requiere al menos 5.000 usuarios para empezar a publicar anuncios.</li><li>El tamaño de la audiencia se mostrará como cero hasta que haya al menos 1.000 usuarios.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync) | 48 horas | LinkedIn procesa 10 consultas por segundo y 100.000 usuarios por solicitud. Braze agrupa a los usuarios cada 5 segundos. | Audiencias predictivas con IA | {::nomarkdown}<ul><li>El tamaño mínimo de la audiencia es de 300 miembros, teniendo en cuenta la segmentación por ubicación.</li><li>LinkedIn muestra la tasa de coincidencia en el panel de Braze.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync) | Entre 24 y 48 horas | Pinterest procesa 7 consultas por segundo y 1.900 usuarios por solicitud. Braze agrupa a los usuarios cada 5 segundos. | Sí | Las audiencias de Pinterest requieren al menos 100 usuarios. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync) | N/A | Snapchat procesa 10 consultas por segundo y 100.000 usuarios por solicitud. Braze agrupa a los usuarios cada 5 segundos. | Sí | Snapchat admite hasta 1.000 audiencias de anuncios. |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync) | Hasta 24 horas | N/A | Sí | {::nomarkdown}<ul><li>No hay un tamaño mínimo de audiencia para las audiencias de CRM en The Trade Desk.</li><li>No hay límite en la cantidad de audiencias que admite The Trade Desk.</li><li>Si sincronizas con una audiencia con una región configurada en la UE, el número de teléfono no es compatible.</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync) | Entre 24 y 48 horas | TikTok procesa 50 consultas por segundo y 10.000 usuarios por solicitud. Braze agrupa a los usuarios cada 5 segundos. | Sí | {::nomarkdown}<ul><li>TikTok admite hasta 400 audiencias de anuncios.</li><li>Las audiencias de TikTok requieren al menos 1.000 usuarios para empezar a mostrar anuncios.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Resumen" }
<sup>Cuando se alcance el límite de velocidad, Braze reintentará las sincronizaciones durante 13 horas.</sup>

## Cómo funciona {#how-it-works}

Para utilizar Audience Sync con Google o Facebook, conecta tu cuenta de anuncios buscando al partner en la página de **Socios tecnológicos**.

![Partner tecnológico de Facebook.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Partner tecnológico de Google Ads.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Después de conectar tu cuenta publicitaria, puedes crear un Canvas con un paso de Audience Sync.

![Menú del componente Canvas para añadir el paso Audience Sync al recorrido del usuario.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

A continuación, selecciona el partner para sincronizar audiencias.

![Opción para seleccionar tu partner de sincronización de audiencia en el paso Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Para cada partner, tendrás que configurar lo siguiente como parte del paso de Audience Sync:

- Cuenta publicitaria
- Audiencia
- Acción de añadir o eliminar usuarios
- Campos que deben coincidir

Ten en cuenta que Braze sincronizará a los usuarios en cuanto entren en el paso de Audience Sync dentro de tu Canvas.

Para cada destino de Audience Sync, el partner puede tener diferentes requisitos sobre los campos que podemos enviar. Consulta la documentación específica del partner para más detalles.

### Audience Sync Pro

Para utilizar un partner de Audience Sync Pro, como TikTok, Pinterest, Snapchat o Criteo, podrás seleccionar tus partners en función de tus asignaciones de compra de Audience Sync Pro en la sección **Audience Sync Pro** de la página de **Socios tecnológicos**.

![Audience Sync Pro sin partners seleccionados todavía.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Primero, selecciona los partners que pretendes utilizar haciendo clic en **Select Partners**. Cada compra de Audience Sync Pro te proporcionará 3 destinos asignados de Audience Sync Pro, que estarán disponibles en cada uno de tus espacios de trabajo dentro de tu panel.

![Opción de seleccionar hasta tres partners para conectarse a Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Después de seleccionar tus destinos de Audience Sync Pro, conecta la cuenta publicitaria de tu partner seleccionado haciendo clic en el mosaico del partner.

![Un ejemplo de Snapchat y TikTok seleccionados como partners para Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Configuración de Audience Sync de Snapchat con el mensaje: "Has conectado correctamente 1 cuenta de Snapchat".]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Por último, crea tu paso de Audience Sync en Canvas utilizando este destino de Audience Sync Pro.

### Procesamiento por lotes y latencia {#batching-and-latency}

Cuando los usuarios entran en un paso de Audience Sync en Canvas, Braze los pone en cola en un sistema de procesamiento por lotes que agrega las actualizaciones de usuarios antes de enviarlas a la API del partner. Un lote se envía cuando ocurre alguna de las siguientes situaciones:

- **El lote alcanza su límite de tamaño.** Esto varía según el partner:
  - El valor predeterminado admite hasta 2.000 usuarios
  - Google Ads admite hasta 10.000 usuarios
  - Facebook y TikTok admiten hasta 2.000 usuarios
- **El temporizador de latencia del lote expira.** El valor predeterminado es de una hora, pero es configurable por partner. Por ejemplo, The Trade Desk utiliza 10 minutos.

Los Canvas de alto volumen pueden enviar antes porque los lotes se llenan más rápido. Los Canvas de bajo volumen esperan hasta que el temporizador de latencia expire. Braze no garantiza un tiempo de envío fijo; el momento depende del tamaño del lote y la ventana de latencia configurada.

Braze registra la actividad de envío en registros internos para monitoreo y solución de problemas, pero estas marcas de tiempo no están expuestas como campos consultables. Después de que Braze envía un lote a la API del partner, el partner procesa la actualización de la audiencia de acuerdo con sus propios acuerdos de nivel de servicio, normalmente entre 6 y 48 horas.

Braze no recibe confirmación de los partners de que los usuarios individuales hayan sido emparejados o sincronizados. Las respuestas de los partners son confirmaciones HTTP de recepción, no confirmaciones de coincidencia. Para verificar que una audiencia se ha completado, consulta la plataforma publicitaria del partner (como Google Ads Audience Manager o Meta Business Manager).

### Correos electrónicos de error de Audience Sync {#audience-sync-error-emails}

Si el error está relacionado con la integración general del partner (como un problema de autorización), se envía un correo electrónico al usuario que conectó la integración. Si ese usuario ya no existe, los administradores recibirán los correos electrónicos.

Si el error está relacionado con problemas con el componente de Audience Sync (como "La audiencia no existe") en Canvas, se envía un correo electrónico al usuario que configuró el Canvas. Si ese usuario ya no existe, entonces recae en el administrador de la empresa.

Para configurar quién recibirá estos correos electrónicos, ponte en contacto con tu administrador de éxito de cliente para añadir destinatarios en **Preferencias de notificación**. Dado que esta característica cambiará el comportamiento actual, tendrás que añadir inmediatamente destinatarios a esta nueva preferencia de notificación, ya que Braze no incluye a nadie de forma predeterminada, y así asegurarte de que no se pierda ningún correo electrónico de error.

## Consideraciones sobre la privacidad de datos {#data-privacy-considerations}

{% alert important %}
Esta documentación no pretende ofrecer asesoramiento jurídico ni puede considerarse como tal. El uso de Audience Sync está sujeto a requisitos legales específicos. Para asegurarte de que lo utilizas de conformidad con la legislación vigente, consulta a tu asesor jurídico.
{% endalert %}

Al crear audiencias para el seguimiento de anuncios, es posible que desees incluir o excluir a determinados usuarios en función de sus preferencias y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la [CCPA](https://oag.ca.gov/privacy/ccpa). Los especialistas en marketing deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada en Canvas. A continuación enumeramos algunas opciones.

Si has recopilado el [IDFA de iOS a través del SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), podrás utilizar el filtro "Ads Tracking Enabled". Selecciona el valor como `true` para enviar solo a los usuarios a los destinos de Audience Sync en los que hayan dado su adhesión voluntaria.

![Un Canvas con una audiencia de entrada de "Ad Tracking Enabled is true".]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Si estás recopilando `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, o cualquier otro atributo personalizado relevante, debes incluirlos dentro de tus criterios de entrada en Canvas como filtro:

![Un Canvas con una audiencia de entrada de "opted_in_marketing equals true".]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Para saber más sobre cómo cumplir estas leyes de protección de datos dentro de la plataforma Braze, consulta la [Asistencia técnica sobre protección de datos]({{site.baseurl}}/dp-technical-assistance).

## Gestión del consentimiento para la segmentación publicitaria {#managing-consent-for-ad-targeting}

Como anunciante, es tu responsabilidad gestionar el consentimiento para el seguimiento de anuncios o la segmentación de tus usuarios.

Para enviar anuncios a tus usuarios, debes cumplir todas las leyes y normativas aplicables, así como las políticas y requisitos de la plataforma publicitaria. Utiliza Braze solo para segmentar y sincronizar usuarios cuando hayas obtenido su consentimiento.

Para mantener actualizadas tus listas de audiencia en estas plataformas publicitarias y eliminar a los usuarios que hayan revocado su consentimiento, configura un Canvas para eliminar a los usuarios de estas listas de audiencia existentes mediante un paso de Audience Sync.
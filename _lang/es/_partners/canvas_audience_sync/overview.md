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

> La característica Braze Audience Sync te ayuda a ampliar el alcance de tus campañas a muchas de las principales tecnologías sociales y publicitarias. A través de [BRAZE CANVAS]({{site.baseurl}}/user_guide/messaging/canvas), las marcas pueden sincronizar de forma dinámica y segura datos de usuarios de primera mano en el ecosistema publicitario para impulsar el marketing y la eficiencia operativa.

## Disponibilidad de la característica {#feature-availability}

Todos los clientes de Braze tienen acceso inmediato a Audience Sync con Google y Facebook, pero los clientes con Action Credits pueden acceder a todos los partners de Audience Sync. Para desbloquear destinos adicionales de Audience Sync para clientes que no tienen Action Credits, adquiere Audience Sync Pro. Ponte en contacto con tu director de cuentas de Braze para obtener más información.

## Ejemplos {#use-cases}

- Segmentar usuarios de alto valor mediante canales propios y de pago para impulsar compras o participación incrementales.
- Crear audiencias similares de tus usuarios de alto valor para optimizar los costes de adquisición de nuevos usuarios y las conversiones.
- Reorientar con anuncios a los usuarios que son menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban publicidad cuando ya son consumidores fieles de tu marca.

## Resumen {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| Destino | Tiempo para que el destino coincida con los miembros de la audiencia | Límite de velocidad | Audiencias similares o actalike | Consejos |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync) | Hasta 24 horas | 250 000 solicitudes por minuto. Se agrupan cada 5 segundos con reintento automático. | Sí | {::nomarkdown}<ul><li>Criteo admite hasta 1000 audiencias publicitarias.</li><li>El tamaño mínimo de audiencia es 500, y se recomienda más de 20 000.</li></ul>{:/} |
| [Facebook o Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) | Hasta 24 horas | 190 000 cuentas publicitarias por hora | Sí | {::nomarkdown}<ul><li>Facebook admite hasta 500 audiencias publicitarias.</li><li>Facebook requiere que las audiencias tengan al menos 1000 usuarios.</li></ul>{:/} |
| [Google Ads o YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) | Entre 6 y 12 horas | Se agrupan cada 5 segundos con reintento automático basado en la respuesta de Google | No | {::nomarkdown}<ul><li><b>Customer match:</b> Usa el ID de anuncio móvil, o la dirección de correo electrónico o el número de teléfono.</li><li>Las audiencias de Google requieren al menos 5000 usuarios para comenzar a mostrar anuncios.</li><li>El tamaño de la audiencia se mostrará como cero hasta que haya al menos 1000 usuarios.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync) | Hasta 48 horas | Braze agrupa hasta 2000 usuarios por solicitud con reintento automático de hasta ~13 horas. | Audiencias predictivas de IA | {::nomarkdown}<ul><li>El tamaño mínimo de audiencia es de 300 miembros, tomando en cuenta la segmentación por ubicación.</li><li>LinkedIn muestra la tasa de coincidencia en el panel de Braze.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync) | Entre 24 y 48 horas | Pinterest procesa 7 consultas por segundo y 1900 usuarios por solicitud. Braze agrupa usuarios cada 5 segundos. | Sí | Las audiencias de Pinterest requieren al menos 100 usuarios. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync) | N/A | Snapchat procesa 10 consultas por segundo y 100 000 usuarios por solicitud. Braze agrupa usuarios cada 5 segundos. | Sí | Snapchat admite hasta 1000 audiencias publicitarias. |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync) | Hasta 24 horas | N/A | Sí | {::nomarkdown}<ul><li>No hay un tamaño mínimo de audiencia para las audiencias CRM en The Trade Desk.</li><li>No hay límite en la cantidad de audiencias que admite The Trade Desk.</li><li>Si sincronizas con una audiencia con la región configurada en la UE, el número de teléfono no es compatible.</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync) | Entre 24 y 48 horas | TikTok procesa 50 consultas por segundo y 10 000 usuarios por solicitud. Braze agrupa usuarios cada 5 segundos. | Sí | {::nomarkdown}<ul><li>TikTok admite hasta 400 audiencias publicitarias.</li><li>Las audiencias de TikTok requieren al menos 1000 usuarios para comenzar a mostrar anuncios.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Resumen" }
<sup>Cuando se alcanza el límite de velocidad, Braze reintenta las sincronizaciones durante 13 horas.</sup>

## Cómo funciona {#how-it-works}

Para usar Audience Sync con Google o Facebook, conecta tu cuenta de anuncios buscando al partner en la página **Technology Partners**.

![Partner tecnológico de Facebook.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Partner tecnológico de Google Ads.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Después de conectar tu cuenta de anuncios, puedes crear un Canvas con un paso de Audience Sync.

![Menú de componentes de Canvas para añadir el paso de Audience Sync al recorrido del usuario.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

A continuación, selecciona el partner con el que sincronizar las audiencias.

![Opción para seleccionar tu partner de Audience Sync en el paso de Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Para cada partner, deberás configurar lo siguiente como parte de tu paso de Audience Sync:

- Cuenta de anuncios
- Audiencia
- Acción para añadir o eliminar usuarios
- Campos para emparejar

Ten en cuenta que Braze sincroniza a los usuarios en cuanto entran en el paso de Audience Sync dentro de tu Canvas.

Para cada destino de Audience Sync, el partner puede tener distintos requisitos sobre qué campos puede enviar Braze. Consulta la documentación específica del partner para más detalles.

### Audience Sync Pro

Para usar un partner de Audience Sync Pro, incluidos Criteo, LinkedIn, Pinterest, Snapchat o TikTok, puedes seleccionar tus partners en función de tus asignaciones de compra de Audience Sync Pro en la sección **Audience Sync Pro** de la página **Technology Partners**.

![Audience Sync Pro sin partners seleccionados aún.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Primero, selecciona los partners que pretendes utilizar. Cada compra de Audience Sync Pro te proporciona 3 destinos de Audience Sync Pro asignados, que están disponibles en cada uno de tus espacios de trabajo dentro de tu panel.

![Opción para seleccionar hasta tres partners para conectar con Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Después de seleccionar tus destinos de Audience Sync Pro, conecta la cuenta de anuncios del partner seleccionado haciendo clic en el mosaico del partner.

![Un ejemplo de Snapchat y TikTok seleccionados como partners para Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Configuración de Audience Sync de Snapchat con el mensaje: "Has conectado correctamente 1 cuenta de Snapchat".]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Por último, crea tu paso de Audience Sync en Canvas usando este destino de Audience Sync Pro.

### Procesamiento por lotes y latencia {#batching-and-latency}

Cuando los usuarios entran en un paso de Audience Sync en Canvas, Braze los pone en cola en un sistema de procesamiento por lotes que agrega las actualizaciones de usuarios antes de enviarlas a la API del partner. Un lote se envía cuando ocurre una de las siguientes condiciones:

- **El lote alcanza su límite de tamaño.** Esto varía según el partner:
  - El valor predeterminado admite hasta 2000 usuarios
  - Google Ads admite hasta 10 000 usuarios
  - Facebook y TikTok admiten hasta 2000 usuarios
- **El temporizador de latencia del lote expira.** El valor predeterminado es una hora, pero se puede configurar por partner. Por ejemplo, The Trade Desk usa 10 minutos.

Los Canvas de alto volumen pueden enviar antes porque los lotes se llenan más rápido. Los Canvas de bajo volumen esperan hasta que expire el temporizador de latencia. Braze no garantiza un tiempo de envío fijo; el momento depende del tamaño del lote y la ventana de latencia configurada.

Braze registra la actividad de envío en registros internos para supervisión y solución de problemas, pero estas marcas de tiempo no se exponen como campos consultables. Después de que Braze envía un lote a la API del partner, el partner procesa la actualización de audiencia de acuerdo con sus propios acuerdos de nivel de servicio, normalmente entre 6 y 48 horas.

Braze no recibe confirmación de los partners de que los usuarios individuales hayan sido emparejados o sincronizados. Las respuestas del partner son confirmaciones HTTP de recepción, no confirmaciones de emparejamiento. Para verificar que una audiencia se ha completado, comprueba la plataforma de anuncios del partner (como Google Ads Audience Manager o Meta Business Manager).

### Correos electrónicos de error de Audience Sync {#audience-sync-error-emails}

Si el error está relacionado con la integración general del partner (como un problema de autorización), se envía un correo electrónico al usuario que conectó la integración. Si ese usuario ya no existe, los administradores reciben los correos electrónicos.

Si el error está relacionado con problemas del componente Audience Sync (como "La audiencia no existe") en Canvas, se envía un correo electrónico al usuario que configuró el Canvas. Si ese usuario ya no existe, se remite al administrador de la empresa.

Para configurar quién recibe estos correos electrónicos, contacta con tu administrador de éxito de cliente para añadir destinatarios en **Notification Preferences**. Esta preferencia cubre tanto los errores de integración como los errores del componente Audience Sync. Los destinatarios que añadas reciben estos correos electrónicos además del usuario asociado con el error.

## Consideraciones sobre la privacidad de datos {#data-privacy-considerations}

{% alert important %}
Esta documentación no pretende proporcionar, ni debe considerarse como asesoramiento legal. El uso de Audience Sync está sujeto a requisitos legales específicos. Para asegurarte de que lo utilizas de conformidad con todas las leyes aplicables, debes buscar el asesoramiento de tu departamento legal.
{% endalert %}

Al crear audiencias para el seguimiento de anuncios, es posible que desees incluir o excluir a determinados usuarios en función de sus preferencias, y cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la [CCPA](https://oag.ca.gov/privacy/ccpa). Los especialistas en marketing deben implementar los filtros relevantes para la elegibilidad de los usuarios dentro de los criterios de entrada de su Canvas. Las siguientes opciones pueden ser de ayuda.

Si has recopilado el [IDFA de iOS a través del SDK de Braze]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations), podrás utilizar el filtro "Ads Tracking Enabled". Selecciona el valor como `true` para enviar usuarios únicamente a los destinos de Audience Sync donde hayan dado su adhesión voluntaria.

![Un Canvas con un público de entrada de "Ad Tracking Enabled is true".]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Si estás recopilando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` u otros atributos personalizados relevantes, deberías incluirlos dentro de los criterios de entrada de tu Canvas como filtro:

![Un Canvas con un público de entrada de "opted_in_marketing equals true".]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Para obtener más información sobre cómo cumplir con estas leyes de protección de datos dentro de la plataforma Braze, consulta [Asistencia técnica de protección de datos]({{site.baseurl}}/dp-technical-assistance).

## Gestión del consentimiento para la segmentación publicitaria {#managing-consent-for-ad-targeting}

Como anunciante, es tu responsabilidad gestionar el consentimiento para el seguimiento o la segmentación publicitaria de tus usuarios.

Para enviar anuncios a tus usuarios, debes cumplir con todas las leyes y regulaciones aplicables, así como con las políticas y requisitos de la plataforma publicitaria. Utiliza Braze únicamente para segmentar y sincronizar usuarios de los que hayas obtenido su consentimiento.

Para mantener actualizadas tus listas de audiencias en estas plataformas publicitarias y eliminar a los usuarios que hayan revocado su consentimiento, configura un Canvas para eliminar usuarios de estas listas de audiencias existentes mediante un paso de Audience Sync.
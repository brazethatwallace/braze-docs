---
nav_title: Recurly
article_title: Recurly
description: "Recurly es la plataforma líder de gestión de suscripciones y facturación para marcas de venta directa al consumidor que buscan aumentar sus suscripciones e ingresos recurrentes."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/) es una plataforma de gestión de suscripciones y facturación. La plataforma integrada de Recurly simplifica la automatización del ciclo de vida de la suscripción a escala, habilitando a los equipos para que gestionen y optimicen la experiencia del suscriptor&#8212;desde la prueba de nuevos planes, ofertas y promociones hasta la gestión de métodos de pago, integraciones e información.

_Esta integración está mantenida por Recurly._

## Sobre la integración {#about-the-integration}

La integración entre Recurly y Braze simplifica el proceso de compartir datos de suscripción con Braze, habilitando la comunicación personalizada con los clientes.

- Aprovecha los eventos del ciclo de vida de la suscripción de Recurly (por ejemplo, renovaciones, pausas o cancelaciones de la suscripción) en Braze para desencadenar campañas y comunicaciones personalizadas.
- Aprovecha los datos de suscripción de Recurly (por ejemplo, planes de suscripción, complementos o estado) para crear y gestionar usuarios de la empresa, Segments y Canvas para ejecutar campañas y comunicaciones específicas de cohorte.
- Envía los datos de Recurly directamente a Braze, habilitando casos de uso adicionales de mensajería y reduciendo los costes generales de desarrollo.

Puedes encontrar más información sobre el uso de Recurly con Braze en [los documentos de Recurly](https://docs.recurly.com/docs/braze-integration).

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Recurly | Se requiere un plan de suscripción Elite de [Recurly](https://recurly.com/) con el conmutador de características de Braze habilitado para aprovechar esta asociación. También es necesaria la activación de las facturas de crédito en tu plataforma Recurly. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel de Braze desde **Settings** > **API Keys**. Como Recurly solo utiliza el punto de conexión `users.track`, recomendamos aprovisionar una clave específica de Recurly solo con este permiso. |
| Punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

Antes de empezar, asegúrate de que tienes cuentas activas tanto en Braze como en Recurly.

### Conecta Recurly a Braze {#connect-recurly-to-braze}

1. En Recurly, ve a **Integrations** > **Braze**. Cuando navegues por primera vez a la página de configuración de la integración de Braze en Recurly, la interfaz te pedirá que conectes los dos sistemas.

2. Proporciona las siguientes credenciales:

- **Instance URL:** El punto de conexión REST de Braze de la instancia a la que estás aprovisionado.
- **API Key (Identifier):** La clave de API REST de Braze que Recurly debe utilizar al enviar solicitudes a Braze.

Recuerda copiar la URL de tu instancia de Braze. Por ejemplo, tu URL podría ser así:

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3. Después de introducir tus credenciales, haz clic en **Connect**.

## Uso de esta integración {#using-this-integration}

### Identificadores admitidos {#supported-identifiers}

Recurly utiliza el `account_code` de una cuenta como `external_id` en Braze. Por ello, el `account_code` de tus cuentas de Recurly debe coincidir con el `external_id` de tu usuario de Braze.

### Eventos personalizados {#custom-events}

Para una interacción eficaz con los clientes, debes [configurar eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) en Braze para recibir eventos desencadenados por Recurly. Asegúrate de incluir cada evento de Recurly para una integración de datos completa. Estos eventos también pueden rastrearse en los [análisis de Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics). Una vez configurados, estos eventos personalizados pueden utilizarse para segmentar a los usuarios o personalizar la mensajería.

| Evento personalizado de Braze | Evento de Recurly |
| ----------- | ----------- |
| Recurly New Subscription              | Se desencadena cuando se crea una suscripción                            |
| Recurly Renewed Subscription          | Se desencadena cuando se renueva una suscripción                                |
| Recurly Updated Subscription          | Se desencadena cuando cambian los atributos de una suscripción (cambio de plan, cambio de precio o cambio de cantidad) |
| Recurly Canceled Subscription         | Se desencadena cuando se cancela una suscripción                           |
| Recurly Reactivated Subscription      | Se desencadena cuando se reactiva una suscripción cancelada               |
| Recurly Paused Subscription           | Se desencadena cuando una suscripción se pone en pausa                   |
| Recurly Resumed Subscription          | Se desencadena cuando se reanuda una suscripción                              |
| Recurly Subscription Expired          | Se desencadena cuando caduca una suscripción                               |
| Recurly Invoice Created               | Se desencadena cuando se crea una factura                                |
| Recurly Successful Payment            | Se desencadena cuando se cobra correctamente una factura                 |
| Recurly Refund Issued                 | Se desencadena cuando se emite un reembolso                                   |
| Recurly Failed Recurring Payment      | Se desencadena cuando falla una factura de renovación de una suscripción          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos personalizados" }

### Agrupación y límite de velocidad {#batching-and-rate-limiting}

Dado que Recurly utiliza el punto de conexión `/users/track` de Braze, la integración está sujeta a los límites de velocidad estándar de Braze de 50 000 solicitudes por minuto.

Recurly agrupa determinados eventos del ciclo de vida de la suscripción en llamadas únicas a la API de Braze para reducir el número de solicitudes.

- Recurly agrupa y envía múltiples suscripciones creadas al mismo tiempo como una única solicitud.
- Recurly agrupa varias renovaciones simultáneas de una cuenta en una sola solicitud.
- Recurly envía los eventos del ciclo de vida de la suscripción del mismo modelo en una sola solicitud. Por ejemplo, una factura recién creada con un pago da lugar a una solicitud de API que contiene los eventos personalizados `Recurly Invoice Created` y `Recurly Successful Payment`.

Los lotes se envían a Braze en grupos de hasta 75 eventos a la vez. Por ejemplo, si se crearan 100 suscripciones a la vez, Recurly haría dos solicitudes de API a Braze. Para más detalles, consulta [agrupar solicitudes de seguimiento de usuarios]({{site.baseurl}}/api/api_limits/#batch-user-track).
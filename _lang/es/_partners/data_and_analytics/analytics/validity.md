---
nav_title: Validity
article_title: Validity
alias: /partners/validity/
description: "Este artículo de referencia describe la asociación entre Braze y Validity, una plataforma de capacidad de entrega de correo electrónico que sincroniza las listas de semillas de Everest con Braze y automatiza las pruebas de colocación en el buzón de entrada para Campaigns y Canvas."
page_type: partner
search_tag: Partner
---

# Validity

> [Validity Everest](https://www.validity.com/everest/) es una plataforma de capacidad de entrega de correo electrónico que te ayuda a medir la colocación en el buzón de entrada y proteger tu reputación de envío. La integración de Braze y Validity sincroniza tu lista de semillas de Everest con Braze, siembra automáticamente las Campaigns y los Canvas que califican, y extrae las métricas de participación de vuelta a Validity Inbox para que puedas comparar la colocación basada en semillas con la participación real de los suscriptores.

_Esta integración es mantenida por Validity._

## Acerca de la integración {#about-the-integration}

Validity crea y mantiene usuarios de listas de semillas de correo electrónico en Braze para que las direcciones de semillas permanezcan activas y no suprimidas. Cuando una Campaign o un Canvas está listo para ser sembrado, Validity envía una copia a esa lista de semillas y muestra las métricas de participación —entregas, rebotes, aperturas, clics y cancelaciones de suscripción— en Validity Inbox junto con los datos de colocación en el buzón de entrada.

## Ejemplos {#use-cases}

### Siembra automática {#auto-seeding}

Con la siembra automática de Validity, Validity detecta cuándo una Campaign o un Canvas de Braze alcanza un volumen de envío que califica y envía una copia del contenido de esa campaña a tu lista de semillas de Validity. Los envíos de semillas se dirigen a usuarios donde el atributo personalizado `validity_seed` está establecido en `true`.

## Requisitos previos {#prerequisites}

Antes de comenzar, necesitas lo siguiente:

| Requisito | Descripción |
| ----------- | ----------- |
| Una cuenta de Validity | Se requiere una cuenta de Validity para aprovechar esta asociación. |
| Una clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con los siguientes permisos: `users.track`, `users.delete`, `email.bounce.remove`, `email.spam.remove`, `campaigns.list`, `campaigns.details`, `campaigns.data_series`, `canvas.list`, `canvas.details`, `canvas.data_series`, `content_blocks.list`, `content_blocks.info` y `messages.send`. <br><br> Crea esta clave en el panel de Braze desde **Configuración** > **API e identificadores**. |
| Un endpoint REST or transferencia de estado representacional de Braze | [La URL de tu endpoint REST or transferencia de estado representacional]({{site.baseurl}}/api/basics#endpoints). Tu endpoint depende de la URL de Braze para tu instancia. Por ejemplo, `rest.iad-01.braze.com`. |
| Un identificador de aplicación de Braze | El identificador de aplicación de Braze al que deben atribuirse los envíos de semillas. Encuéntralo en **Configuración** > **API e identificadores** > **Identificadores de aplicación**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de Validity {#integrating-validity}

### Paso 1: Comparte las credenciales de Braze con Validity {#step-1-share-braze-credentials-with-validity}

Validity requiere tres credenciales de **Configuración** > **API e identificadores** en tu panel de Braze:

- Tu clave de API REST or transferencia de estado representacional (con los permisos listados en [Requisitos previos](#prerequisites))
- Tu endpoint REST or transferencia de estado representacional
- Tu identificador de aplicación

Comparte estas credenciales con tu representante de Validity, quien completará la configuración de la integración por ti. Validity valida las credenciales con una llamada de prueba en vivo a Braze antes de habilitar la integración. Si no estás seguro de quién es tu contacto en Validity, envía un correo electrónico a [support@validity.com](mailto:support@validity.com).

Después de que la integración esté habilitada, Validity sincroniza tu lista de semillas de Everest con Braze en un ciclo recurrente (cada 10 minutos). Validity crea, actualiza y elimina usuarios de semillas en Braze para mantenerlos alineados con tu lista de semillas actual en Everest.

### Paso 2: Opcionalmente, crea un Segment de Braze para los usuarios de semillas de Validity {#step-2-optionally-create-a-braze-segment-for-validity-seed-users}

Crear un Segment es opcional. La siembra automática envía correos electrónicos de prueba usando un objeto [Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience) filtrado por el atributo personalizado `validity_seed` cada vez que se detecta un envío que califica. No necesitas crear un Segment ni adjuntarlo a tus Campaigns.

Si deseas una forma de ver esta audiencia dentro de Braze como referencia, crea un Segment en **Audiencia** > **Segments** con el filtro `validity_seed` es `true`.

Validity crea usuarios a través del endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) usando el siguiente esquema:

```bash
curl -X POST "https://YOUR_API_ENDPOINT/users/track" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_BRAZE_API_KEY" \
  -d '{
    "attributes": [
      {
        "email": "example1@example.com",
        "validity_seed": true
      },
      {
        "email": "example2@example.com",
        "validity_seed": true
      }
    ],
    "events": [
      {
        "email": "example1@example.com",
        "name": "validity_seed_event",
        "time": "2026-07-02T18:00:00.000Z"
      }
    ]
  }'
```

Estos usuarios siempre incluyen el atributo personalizado `validity_seed` con el valor booleano `true`. Validity también envía un evento personalizado `validity_seed_event` para cada usuario de semilla, de modo que se registren como usuarios activos en tu cuenta de Braze.

## Consideraciones {#considerations}

### Cómo funcionan los envíos de semillas {#how-seed-sends-work}

Validity extrae el cuerpo de la campaña, el asunto y la dirección del remitente a través de los endpoints de detalles de Campaign y Canvas, y luego entrega una copia de ese contenido a la lista de semillas a través del endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) de Braze. Tu panel de Braze sigue mostrando solo la Campaign original.

### Umbral de siembra automática {#auto-seeding-threshold}

Validity detecta cuándo una Campaign o un Canvas cruza tu umbral de volumen de envío configurado (10 000 envíos de forma predeterminada) y envía la prueba de semilla en ese punto. No necesitas agregar la audiencia de semillas a tus Campaigns o Canvas.

Una prueba de semilla envía tu campaña de correo electrónico a las direcciones de la lista de semillas, recopila datos de colocación y te ayuda a identificar problemas antes o junto con los envíos a tu audiencia. Las métricas de colocación en el buzón de entrada muestran si tu campaña llega al buzón de entrada, a la carpeta de correo no deseado o se pierde. Usa estas métricas para confirmar la colocación en el buzón de entrada y detectar problemas de capacidad de entrega.

Las pruebas de semillas también pueden ayudarte a diagnosticar por qué los correos electrónicos llegan a la carpeta de correo no deseado o se pierden. Verificar los datos del encabezado, la autenticación (SPF, DKIM y DMARC), la validación de enlaces y la representación del diseño puede mostrarte qué pasos tomar para mejorar tu tasa de colocación en el buzón de entrada.

### Salud de la lista de semillas {#seed-list-health}

Validity monitorea los usuarios de la lista de semillas y puede actualizarlos o eliminarlos si comienzan a perder efectividad; por ejemplo, si los proveedores de servicios de correo electrónico (ESP) comienzan a marcar a los miembros de la audiencia de la lista de semillas como correo no deseado. Estos permisos permiten a Validity monitorear la salud de la lista de semillas y actualizar la lista en consecuencia.

### Cómo se maneja el contenido dinámico {#how-dynamic-content-is-handled}

Los correos electrónicos de Braze a menudo usan personalización Liquid vinculada al perfil de un destinatario real. Debido a que las direcciones de semillas no tienen esos datos de perfil, Validity ejecuta cada correo electrónico a través de un sanitizador antes de sembrarlo. El sanitizador resuelve Content Blocks, evalúa la lógica básica de Liquid y reemplaza todo lo que no puede resolver (como un nombre) con un marcador de posición visible `[REDACTED]`. Las secciones construidas completamente a partir de API de contenido conectado en vivo se renderizan en blanco en la semilla.

Puedes activar o desactivar el sanitizador. Cuando está desactivado, Braze resuelve la personalización Liquid para los envíos de semillas de la misma manera que lo haría para un destinatario real.

### Inbox Aggregate

Habilitar la siembra automática también habilita Inbox Aggregate. Esta característica extrae métricas de participación —enviados, entregados, rebotes, aperturas, clics y cancelaciones de suscripción— de tus envíos reales de Braze (por separado de los envíos de semillas) y las muestra en Validity Inbox junto con tus datos de colocación en el buzón de entrada. Las dos características funcionan en programaciones independientes y no necesitan gestionarse por separado.
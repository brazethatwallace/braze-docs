---
nav_title: Notify
article_title: Notify
description: "Este artículo de referencia describe la asociación entre Braze y Notify, una solución de personalización omnicanal en tiempo real que ofrece personalización en todo el ciclo de vida del cliente."
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Notify

> [Notify](https://fr.notify-group.com/) es una solución de software basada en IA que se integra fácilmente con las herramientas de administración de las relaciones con los clientes para mejorar las estrategias de marketing y facilitar la interacción a través de múltiples canales.

La integración de Braze y Notify permite a los especialistas en marketing impulsar eficazmente la interacción en varias plataformas. En lugar de depender de los métodos de marketing tradicionales, una campaña de Braze desencadenada por API puede utilizar las capacidades de Notify para entregar mensajes personalizados a través de múltiples canales, como correo electrónico, SMS, notificaciones push, etc.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

| Requisito | Descripción |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.export.segment` y `campaigns.trigger.send`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Configuración CNAME | Debe crearse un subdominio para el píxel de seguimiento utilizado en el correo electrónico para que Notify realice un seguimiento de la interacción del usuario con la mensajería y así informar mejor al modelo. Comparte la URL del subdominio con Notify después de crearlo. |
| Exportación de la adhesión voluntaria a la base de datos | Envía los datos de campaña y compra del último año (12 meses) a Notify. ​Esta exportación se utilizará para entrenar el modelo predictivo de Notify. <br><br> **Campos:** <br><br> **Correo electrónico:** Un hash SHA256 del correo electrónico, convertido a minúsculas y sin espacios iniciales ni finales.<br><br>**Segmento:** La información del segmento que define el nivel de actividad (activo o inactivo).<br><br>**Subsegmento:** Cualquier otra información de actividad relevante, como el nivel de actividad de compra.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crea tu campaña {#step-1-create-your-campaign}

Crea una [campaña desencadenada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) en Braze. Después, comparte el `api_identifier` de la campaña con Notify.

### Paso 2: Crea tu segmento en Braze {#step-2-create-your-segment-in-braze}

A continuación, crea el segmento de usuarios al que te gustaría dirigirte con la campaña creada en el [paso 1](#step-1-create-your-campaign). Después, comparte el ID del segmento con Notify.

### Paso 3: Obtén tu segmento {#step-3-fetch-your-segment}

A continuación, Notify exportará los usuarios del segmento asociado a la campaña.

### Paso 4: Notify desencadena la campaña {#step-4-notify-triggers-the-campaign}

Utilizando el punto de conexión `/campaigns/trigger/send`, la IA de Notify desencadena la campaña de Braze creada en el [paso 1](#step-1-create-your-campaign) para enviarla a los usuarios en el momento en que se considere más probable su interacción.
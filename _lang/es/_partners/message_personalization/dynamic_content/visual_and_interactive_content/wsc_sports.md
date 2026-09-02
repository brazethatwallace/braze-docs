---
nav_title: WSC Sports
article_title: WSC Sports
description: "Este artículo de referencia describe la asociación entre Braze y WSC Sports, una plataforma de video deportivo que te permite incluir medios deportivos ricos y sólidos en tus notificaciones push de Braze."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> La plataforma [WSC Sports](https://wsc-sports.com/) genera videos deportivos personalizados para cada plataforma digital y cada aficionado al deporte, de forma automática y en tiempo real.

_Esta integración está mantenida por WSC Sports._

## Sobre la integración {#about-the-integration}

La integración de Braze y WSC Sports te permite incluir medios deportivos ricos y sólidos en tus notificaciones push de Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta WSC | Se necesita una cuenta WSC para beneficiarse de esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos de **Messages**, **Segments**, **Campaigns** y **Canvas**. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

La aplicación WSC Sports gestiona el proceso de extremo a extremo, desde la selección del video hasta la llegada de la notificación push al dispositivo del usuario final.

### Paso 1: Selecciona los ajustes de envío {#step-1-select-send-settings}

![Panel de ajustes de envío de WSC Sports con selección de Campaign y Segment de Braze.]({% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"){: style="float:right;max-width:25%;margin-bottom:15px;"}

Antes de iniciar la integración, asegúrate de que tienes las campañas y los segmentos de usuarios deseados creados en Braze. Una vez completado, en la plataforma WSC Sports, selecciona el video que desees y, en los ajustes de envío, selecciona el segmento de usuarios de Braze y el ID de Campaign que quieras utilizar. Por último, elige la hora a la que quieres que se envíe tu mensaje push.

#### Llamada a la API {#api-call}

Una vez enviada, WSC Sports entregará la notificación push a los segmentos de usuarios elegidos, utilizando los siguientes endpoints de Braze, en función de las opciones seleccionadas:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)

El cuerpo resultante del mensaje es el siguiente:
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### Paso 2: Prueba de envío {#step-2-test-send}

En este punto, tu campaña debería estar lista para probarla y enviarla. Comprueba los registros de mensajes de error de Braze si te encuentras con errores.
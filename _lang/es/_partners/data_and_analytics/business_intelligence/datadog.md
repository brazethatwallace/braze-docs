---
nav_title: Datadog
article_title: Datadog
description: "Este artículo de referencia describe la asociación entre Braze y Datadog, un servicio de observabilidad para aplicaciones a escala de nube, que proporciona supervisión de servidores, bases de datos, herramientas y servicios a través de una plataforma de análisis de datos basada en SaaS."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) es un servicio de observabilidad para aplicaciones a escala de nube, que proporciona supervisión de servidores, bases de datos, herramientas y servicios a través de una plataforma de análisis de datos basada en SaaS.

La integración de Braze y Datadog permite a los clientes recopilar datos de Braze en Datadog y crear alertas sobre los datos que enviamos. Por ejemplo, configurar un monitor y una alerta si tu Campaign de boletín semanal envía un volumen anormalmente bajo de mensajes, o si un paso en Canvas que normalmente solo envía unos pocos mensajes al día empieza a enviar miles.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Datadog | Se necesita una cuenta de Datadog para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración {#integration}

### Paso 1: Generar clave de Datadog {#step-1-generate-datadog-key}

En Datadog, tendrás que crear una [clave de API](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). Para añadir una clave de API, ve a **Organization Settings** > **API Keys** > **New Key**.

### Paso 2: Añadir la clave a Braze {#step-2-add-key-to-braze}

En el panel de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y busca **Datadog**. En la página del socio de Datadog, proporciona la clave de API de Datadog. Esto creará una conexión que permitirá a Braze enviar datos a Datadog.

## Eventos de Braze {#braze-events}

Una vez integrada la conexión, Braze enviará los siguientes eventos a Datadog:

- `braze.messaging.sent` – El recuento de envíos

Cada uno de estos eventos tendrá metadatos en forma de etiquetas de Datadog para darte información como:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (si está disponible)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (si está disponible)

Estos eventos y etiquetas pueden supervisarse en la página **Metrics Explorer** de Datadog. Estas métricas se registran como [distribuciones](https://docs.datadoghq.com/metrics/distributions/) en DataDog. Dada la naturaleza de las métricas y la imprecisión de las agregaciones y rollups de DataDog, Braze no reintenta errores de red intermitentes u otros errores de la API de DataDog que puedan encontrarse durante la transmisión. Esto significa que estos recuentos de métricas pueden diferir ligeramente de los recuentos vistos en el panel de Braze o a través de Currents.

![]({% image_buster /assets/img/datadog.png %})
---
nav_title: Datadog
article_title: Datadog
description: "Este artículo de referencia describe la asociación entre Braze y Datadog, un servicio de observabilidad para aplicaciones a escala de nube, que proporciona supervisión de servidores, bases de datos, herramientas y servicios a través de una plataforma de análisis de datos basada en software como servicio (SaaS)."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) es un servicio de observabilidad para aplicaciones a escala de nube, que proporciona supervisión de servidores, bases de datos, herramientas y servicios a través de una plataforma de análisis de datos basada en software como servicio (SaaS).

La integración de Braze y Datadog permite a los clientes recopilar datos de Braze en Datadog y crear alertas sobre los datos que enviamos. Por ejemplo, configurar un monitor y una alerta si tu campaña de boletín semanal envía un volumen anormalmente bajo de mensajes, o si un paso en Canvas que normalmente solo envía unos pocos mensajes al día empieza a enviar miles.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Datadog | Se requiere una cuenta de Datadog para aprovechar esta integración del partner. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Genera una clave de Datadog {#step-1-generate-datadog-key}

En Datadog, tendrás que crear una [clave de API](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). Para añadir una clave de API, ve a **Organization Settings** > **API Keys** > **New Key**.

### Paso 2: Añade la clave a Braze {#step-2-add-key-to-braze}

En el panel de Braze, ve a **Integraciones de partners** > **Partners tecnológicos** y busca **Datadog**. En la página del partner de Datadog, proporciona la clave de API de Datadog. Esto creará una conexión que permitirá a Braze enviar datos a Datadog.

## Eventos de Braze {#braze-events}

Una vez integrada la conexión, Braze envía los siguientes eventos a Datadog:

- `braze.messaging.sent` - El recuento de envíos

Cada uno de estos eventos tiene metadatos en forma de etiquetas de Datadog que te proporcionan información como:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (si está disponible)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (si está disponible)

Estos eventos y etiquetas se pueden monitorizar en la página **Metrics Explorer** de Datadog. Estas métricas se registran como [distribuciones](https://docs.datadoghq.com/metrics/distributions/) en DataDog. Dada la naturaleza de las métricas y la imprecisión de las agregaciones y rollups de DataDog, Braze no reintenta errores de red intermitentes ni otros errores de la API de DataDog que puedan producirse durante la transmisión. Esto significa que estos recuentos de métricas pueden diferir ligeramente de los recuentos que se ven en el panel de Braze o a través de Currents.

![Metrics Explorer de Datadog mostrando métricas y etiquetas de eventos de Braze.]({% image_buster /assets/img/datadog.png %})

## Solución de problemas {#troubleshooting}

### ¿Por qué faltan las métricas `braze.messaging.sent` en Datadog? {#why-are-brazemessagingsent-metrics-missing-in-datadog}

Si conectaste Braze a Datadog pero no ves `braze.messaging.sent` en el Metrics Explorer, confirma que el **sitio de Datadog** seleccionado en Braze coincide con la URL del sitio de tu organización de Datadog. Los sitios disponibles son:

- `datadoghq.com` (predeterminado)
- `us3.datadoghq.com`
- `us5.datadoghq.com`
- `datadoghq.eu`
- `ddog-gov.com`
- `ap1.datadoghq.com`

Una discrepancia de sitio puede impedir que las métricas aparezcan en el espacio de trabajo donde buscas. En el panel de Braze, ve a **Partner Integrations** > **Technology Partners** > **Datadog** y comprueba que el sitio coincide con el subdominio en la URL de tu cuenta de Datadog.

El campo **Datadog site** se bloquea después de conectar. Para cambiarlo, desconecta la integración y vuelve a conectar con el sitio correcto.

Después de corregir el sitio, espera a que haya nueva actividad de envío antes de que aparezcan las métricas. Los datos históricos no se rellenan retroactivamente.
---
nav_title: Limbik
article_title: Limbik
description: "Este artículo de referencia describe la integración entre Braze y Limbik, una capa de resonancia de IA que predice cómo las audiencias interpretan y responden a los mensajes utilizando audiencias sintéticas y pronósticos."
alias: /partners/limbik/
page_type: partner
search_tag: Partner
---

# Limbik

> [Limbik](https://limbik.com/cognitive-ai) es tu capa de resonancia de IA: predice cómo las audiencias reales interpretan y responden a mensajes, conceptos y resultados de IA antes de que lleguen al mercado. Impulsado por investigación primaria continua en más de 60 países y más de 25 idiomas, Limbik ofrece audiencias sintéticas validadas por humanos: poblaciones digitales que simulan la respuesta real de la audiencia a velocidad de máquina y con precisión de grado de investigación (95 % de confianza, margen de error del 1,5 % al 3 %). Limbik te da la capacidad de asegurar de inmediato que tu mensajería resuene con lo que tu audiencia objetivo cree y siente.

_Esta integración es mantenida por Limbik._

## Requisitos previos {#prerequisites}

Se requiere lo siguiente para usar Limbik con Braze:

| Requisitos | Descripción |
| --- | --- |
| `account_id` de Limbik | Habla con tu equipo de cuenta de Limbik o realiza una solicitud GET al punto de conexión `/rest/api/organizations` de Limbik |
| Token de acceso de Limbik (`access_token`) | Realiza una solicitud POST al punto de conexión `login` de Limbik y usa el valor `access_token` devuelto como token Bearer en el encabezado `Authorization`. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos de "Messages". Crea una en el dashboard de Braze en **Settings** > **API Keys**. |
| `campaign_id` de Braze | Ve a **Messaging** > **Campaigns** y selecciona una Campaign. Si la Campaign que deseas aún no existe, crea una y guárdala. En la parte inferior de la página de la Campaign, encuentra el identificador de API de Campaign. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

Antes de usar cualquiera de los puntos de conexión de pronóstico, primero debes identificar a qué organización (`account_id`) tienes acceso. Aunque la mayoría de los clientes tienen solo una organización, algunas cuentas pueden tener múltiples organizaciones disponibles.

{% details Recuperar organizaciones disponibles %}

Consulta el punto de conexión de organizaciones para recuperar tus organizaciones disponibles:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/organizations' \
  -H 'accept: application/json'
```

{% enddetails %}

{% details Ejemplo de respuesta %}

```json
{
  "data": [
    {
      "uid": "aca61bd5-7132-499c-946e-42d092cc1156",
      "name": "Braze API"
    }
  ]
}
```

Selecciona el `uid` de la organización deseada para usarlo como encabezado `account_id` en todas las solicitudes de API posteriores.

{% enddetails %}

## Autenticación {#authentication}

Para acceder a los puntos de conexión de la API, necesitas un token bearer para la autenticación. Obtén tu token autenticándote con tus credenciales.

{% details Solicitud de inicio de sesión %}

```sh
curl -X 'POST' \
  'https://cortex.prod.limbik.com/rest/api/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "your_username",
  "password": "your_password"
}'
```

{% enddetails %}

{% details Ejemplo de respuesta %}

La respuesta contiene un `access_token` que puedes usar como token bearer en todas las solicitudes de API posteriores:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer"
}
```

Incluye este token en el encabezado `Authorization` para todas las solicitudes de API:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

{% alert note %}
Puedes usar plataformas de API como Postman para configurar flujos de trabajo automatizados que llamen a múltiples puntos de conexión de REST or transferencia de estado representacional API desde diferentes organizaciones, como el siguiente flujo de trabajo.
{% endalert %}

{% enddetails %}

## Caso de uso: generar texto de mensaje {#use-case-generating-message-copy}

Al usar los puntos de conexión de REST or transferencia de estado representacional API de Braze y Limbik, puedes utilizar los pronósticos generativos de Limbik para crear texto de mensaje y enviarlo a través de los canales de mensajería de Braze, o ajustar el texto existente para mejorar el impacto en tu audiencia. Ambas plataformas exponen funcionalidades que puedes llamar programáticamente para construir flujos de trabajo sofisticados.

Esta documentación describe dos ejemplos: generar texto de mensaje en Limbik y usar este texto en un mensaje posterior enviado a través de Braze, así como usar Limbik para evaluar la calidad de un mensaje dado para tu audiencia elegida.

{% details Solicitud de pronóstico generativo de Limbik %}

Usa este punto de conexión para generar un mensaje y devolverlo en una plantilla de pronóstico. Ejemplo de solicitud:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/generate/template?prompt=YOUR_PROMPT' \
  -H 'account_id: YOUR_ACCOUNT_ID' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'accept: application/json'
```

Reemplaza `YOUR_PROMPT`, `YOUR_ACCOUNT_ID` y `YOUR_ACCESS_TOKEN` con tu texto de prompt, el ID de organización (del punto de conexión de organizaciones) y el token bearer del punto de conexión de inicio de sesión.

{% enddetails %}

{% details Ejemplo de respuesta %}

Ejemplo de respuesta de plantilla de pronóstico de Limbik:

```json
[
  {
    "type": "Message",
    "displayText": "Formula one next race",
    "additionalDetail": "The latest dev in Formula...",
    "messages": [
      {
        "body": "The latest dev in Formula ..."
      }
    ],
    "population": {
      "id": 56,
      "name": "us2",
      "org_enabled": true,
      "org_visible": true,
      "categories": [],
      "display_name": "US Adults",
      "composite_key": "us2",
      "enabled": true
    }
  }
]
```

El elemento clave para este caso de uso es el campo `additionalDetail`, que contiene el texto de mensaje que Limbik generó.

Usa este valor para completar un mensaje enviado a Braze. Por ejemplo, con el punto de conexión POST `/campaigns/trigger/send`, usa `additionalDetail` para completar un campo de carga útil. Con el punto de conexión POST `/messages/send`, úsalo para completar el objeto de mensaje de tu elección.

{% enddetails %}

### Campos de respuesta {#response-fields}

La respuesta contiene los siguientes campos clave:

- **`type`:** El tipo de mensaje (por ejemplo, `"Generate"` para contenido generado por IA, `"Message"` para mensajes validados)
- **`displayText`:** Un título corto o resumen del mensaje
- **`additionalDetail`**: **El texto de mensaje completo generado por IA** - Este es el campo principal que contiene el texto completo del mensaje que puedes enviar a través de tu plataforma de mensajería
- **`population`:** La población objetivo y los segmentos para este mensaje

### Uso con Braze {#using-with-braze}

El campo `additionalDetail` de la respuesta de Limbik contiene el texto de mensaje que envías a Braze. Un patrón de integración común es pasar ese valor en `trigger_properties.payload` al llamar al punto de conexión de envío por trigger de Braze. En el siguiente ejemplo, reemplaza `{{additionalDetail}}` con la cadena real del campo `additionalDetail` de Limbik, y reemplaza `{{YOUR_CAMPAIGN_ID}}` con tu ID de Campaign.

### Ejemplo de solicitud de mensaje por trigger de Braze {#braze-trigger-message-request-example}

```json
{
  "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
  "trigger_properties": {
    "payload": "{{additionalDetail}}"
  },
  "broadcast": true
}
```

## Caso de uso: detalles de audiencia sintética {#use-case-synthetic-audience-details}

Para ampliar el primer caso de uso, utiliza el punto de conexión de Limbik `/rest/api/populations/{account_id}/{population_id}`.

Este punto de conexión devuelve puntos de datos clave que describen la composición de las audiencias sintéticas de Limbik, como género, ubicación, etc. Puedes usar estos valores para completar objetos de Connected Audience al llamar a los puntos de conexión de mensajería de Braze.

{% alert note %}
Los objetos de Connected Audience no pueden segmentar usuarios basándose en los atributos "predeterminados" de Braze, por lo que debes almacenar cualquier atributo que desees segmentar en Braze como atributos personalizados.
{% endalert %}

Para obtener puntuaciones de pronóstico para segmentos específicos, identifica los países disponibles y sus segmentos correspondientes.

### Paso 1: Listar países disponibles {#step-1-list-available-countries}

Recupera la lista de países disponibles para tu cuenta:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/list/aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'accept: application/json'
```

De la respuesta, identifica el país que deseas usar. Por ejemplo, Estados Unidos tiene un `id` de `56`.

### Paso 2: Recuperar segmentos disponibles {#step-2-retrieve-available-segments}

Después de recuperar el ID del país, recupera la lista completa de segmentos para ese país.

{% details Ejemplo de llamada %}

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/aca61bd5-7132-499c-946e-42d092cc1156/56' \
  -H 'accept: application/json'
```

{% alert note %}
La respuesta puede ser grande. Almacena estos datos en caché (por ejemplo, en Redis) por nombre o clave para un mejor rendimiento.
{% endalert %}

{% enddetails %}

{% details Ejemplo de respuesta %}

Por ejemplo, para segmentar mujeres en la población adulta de EE. UU.:

```json
[
  {
    "id": 56,
    "name": "us2",
    "composite_key": "us2",
    "categories": [
      {
        "id": 9331,
        "name": "gender",
        "composite_key": "us2::gender",
        "segments": [
          {
            "id": 63793,
            "name": "female",
            "composite_key": "us2::gender::female"
          }
        ]
      }
    ]
  }
]
```

{% alert note %}
- Los segmentos se especifican usando un formato de clave compuesta simplificado (por ejemplo, `gender::female`).
- La clave compuesta completa de la respuesta de la API (`us2::gender::female`) se acorta a solo el nombre de la categoría y el segmento.
- Para una referencia completa de las poblaciones y segmentos disponibles, consulta [Audiencias de Limbik](https://audiences.limbik.com/).
{% endalert %}

Usando el valor de clave compuesta para tu mensaje de pronóstico elegido, puedes mapear estos descriptores de audiencia sintética a valores en perfiles de usuario reales en Braze.

Por ejemplo, puedes usar la clave compuesta (`fr1::education_level::master_s_degree`) en un objeto de Connected Audience de Braze de la siguiente manera:

```json
{
  "AND": [
    {
      "custom_attribute": {
        "custom_attribute_name": "education_level",
        "comparison": "equals",
        "value": "masters"
      }
    }
  ]
}
```

{% enddetails %}

## Caso de uso: evaluar puntuación de pronóstico {#use-case-evaluating-forecast-score}

Puedes usar Limbik para crear una puntuación estimada de un mensaje contra una audiencia sintética. Hazlo programáticamente con el punto de conexión `forecasts/synchronous` de Limbik.

### Opción 1: Pronóstico sincrónico {#option-1-synchronous-forecast}

Puedes usar la carga útil de respuesta de la generación de plantilla directamente con el punto de conexión de pronóstico sincrónico:

{% details Ejemplo de solicitud genérica %}

```sh
curl -X 'POST' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/synchronous' \
  -H 'accept: application/json' \
  -H 'account_id: aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'Content-Type: application/json' \
  -d '{
  "type": "Generate",
  "displayText": "Formula one season testing 2026",
  "additionalDetail": "Day 1 of the 2026 Formula 1 Bahrain testing session has concluded. Lando Norris recorded the fastest time in the McLaren, with Ferrari in second place. Cadillac drivers Sergio Perez and Valtteri Bottas completed 107 laps, nearly two race distances, and Audi introduced significant upgrades. Which team do you expect to perform best in Australia? #F12026 #BahrainTesting #LandoNorris",
  "population": {
    "population": "us2",
    "segments": []
  }
}'
```

{% enddetails %}

{% details Ejemplo de respuesta (abreviada) %}

```json
{
  "uid": "6c5e28ef-8796-4659-a743-d842a06c9bf7",
  "datetime": "2026-02-11T20:04:06.545+00:00",
  "userId": "9cdd921c-f62f-46a6-902f-a6b0d1702f99",
  "accountId": "aca61bd5-7132-499c-946e-42d092cc1156",
  "name": "Formula one season t...",
  "user_message_context": "",
  "population": [
    {
      "name": "us2",
      "display_name": "US Adults",
      "categories": []
    }
  ],
  "privacy_compliant": false,
  "model_outputs": {
    "belmetrics": {
      "metrics": {
        "moe": 0.02144,
        "pfi": "0.3611",
        "min_val": 0.2941,
        "mean_val": 0.41831
      }
    },
    "virmetrics": {
      "metrics": {
        "moe": 0.02381,
        "pfi": "0.3611",
        "min_val": 0.2,
        "mean_val": 0.30395
      }
    },
    "model_variant": "v4_0_0"
  }
}
```

{% enddetails %}

### Opción 2: Preparar carga útil de pronóstico con segmentos {#option-2-prepare-forecast-payload-with-segments}

Crea tu carga útil de pronóstico usando los segmentos seleccionados. Los segmentos usan un formato de clave compuesta simplificado.

{% details Ejemplo de solicitud específica por segmento %}

```json
{
  "type": "Generate",
  "displayText": "Formula one season testing 2026",
  "additionalDetail": "🚀 Day 1 of 2026 F1 Bahrain testing just dropped BOMBS! Lando Norris edged out Max Verstappen for P1 in McLaren's beast, with Ferrari hot on their heels 🔥. But the real shocker? Cadillac's debutants Sergio Perez & Valtteri Bottas smashed 107 laps – nearly TWO race distances! New kids on the block are HERE to stay. Audi's radical upgrades already turning heads too. Who's your early fave for Australia? 👀 #F12026 #BahrainTesting #LandoNorris",
  "population": {
    "population": "us2",
    "segments": [
      "gender::female"
    ]
  }
}
```

{% enddetails %}
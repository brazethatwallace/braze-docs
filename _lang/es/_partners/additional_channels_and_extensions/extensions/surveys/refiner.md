---
nav_title: Refiner
article_title: Refiner
alias: /partners/refiner/
description: "Este artículo de referencia describe la asociación entre Braze y Refiner, que te permite enviar eventos de cuestionarios y datos de respuestas a Braze para desencadenar campañas, segmentar usuarios y actualizar perfiles de usuario."
page_type: partner
search_tag: Partner

---

# Refiner

> [Refiner](https://refiner.io) es una plataforma de cuestionarios dentro de la aplicación para software como servicio (SaaS) y aplicaciones móviles. Permite a los equipos de producto y de voz del cliente lanzar cuestionarios segmentados dentro de la aplicación y recopilar continuamente datos de NPS, CSAT, CES, comentarios sobre el producto y datos de usuario de tipo zero-party.

_Esta integración es mantenida por Refiner._

## Acerca de la integración {#about-the-integration}

Usa la integración de Refiner y Braze para enviar eventos de cuestionarios y datos de respuestas desde Refiner a tu cuenta de Braze. Utiliza estos datos para desencadenar campañas en Braze basadas en interacciones con cuestionarios (como un cuestionario completado), segmentar usuarios según sus respuestas y actualizar perfiles de usuario de Braze con atributos derivados de las respuestas del cuestionario.

## Ejemplos {#use-cases}

- Segmentar usuarios según las respuestas de cuestionarios, como puntuaciones NPS o calificaciones CSAT.
- Desencadenar campañas personalizadas en Braze basadas en los resultados de cuestionarios.
- Impulsar recorridos multicanal usando BRAZE Canvas u otras herramientas de orquestación.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Refiner | Se requiere una cuenta de [Refiner](https://refiner.io) para usar esta integración. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos de `users.track`. Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST or transferencia de estado representacional de Braze | La URL de tu endpoint REST or transferencia de estado representacional. Tu endpoint depende de la [URL de Braze para tu instancia]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Conecta tu cuenta de Braze {#step-1-connect-your-braze-account}

En la sección **Integrations** de tu proyecto de Refiner, selecciona **Connect Braze**. Introduce tu clave de API REST or transferencia de estado representacional de Braze y tu identificador de instancia de Braze.

### Paso 2: Mapea los identificadores de usuario {#step-2-map-user-identifiers}

Mapea el identificador de usuario de Refiner al identificador de Braze que utilizas, como un `external_id` de Braze o una dirección de correo electrónico. Esto garantiza que los eventos se asocien con el usuario correcto en Braze.

### Paso 3: Elige los datos a sincronizar {#step-3-choose-data-to-sync}

- Selecciona los cuestionarios cuyos datos quieres sincronizar con Braze.
- Selecciona qué eventos de Refiner enviar a Braze, como **Survey Seen**, **Survey Dismissed** y **Survey Completed**.

![El panel de configuración de la integración de Refiner mostrando las opciones de selección de cuestionarios y mapeado de eventos.]({% image_buster /assets/img/refiner.jpg %})

## Personalizar Refiner {#customize-refiner}

- Elige si los datos enviados a Braze incluyen solo las respuestas del cuestionario o también campos de datos de contacto adicionales.
- Elige si los campos de datos sincronizados deben tener el prefijo `refiner_` para facilitar su identificación en tu cuenta de Braze.

## Usar datos de cuestionarios en Braze {#use-survey-data-in-braze}

Después de conectar Braze y Refiner, los eventos de cuestionarios como **Saw Survey** o **Completed Survey** aparecen en los perfiles de usuario de tu cuenta de Braze. Usa estos eventos para desencadenar y personalizar mensajes en Braze, o utiliza los datos de respuestas de cuestionarios para segmentar usuarios.

{% alert note %}
También puedes enviar cuestionarios de Refiner por correo electrónico a través de Braze. Para más detalles, consulta la [documentación de integración de Refiner](https://refiner.io/docs/kb/integrations/braze-integration/).
{% endalert %}

## Solución de problemas {#troubleshooting}

Si experimentas problemas con la integración, consulta los siguientes recursos:

- [Guía de integración de Refiner y Braze](https://refiner.io/docs/kb/integrations/braze-integration/)
- [Contactar con el soporte de Refiner](https://refiner.io/docs/kb/getting-started/contact-support/)
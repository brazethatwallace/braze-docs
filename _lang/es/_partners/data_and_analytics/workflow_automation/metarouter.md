---
nav_title: MetaRouter
article_title: MetaRouter
description: "Eleva tu administración de datos de los clientes en Braze con MetaRouter. Esta solución de gestión de etiquetas del lado del servidor de alto rendimiento ofrece el máximo cumplimiento y control con opciones de despliegue sencillas, ya sea en una nube privada alojada en MetaRouter o en tu propia infraestructura."
alias: /partners/metarouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [MetaRouter](https://www.metarouter.io/) eleva tu experiencia con Braze integrándose fácilmente como una potente plataforma de gestión de etiquetas del lado del servidor. Te permite orquestar un recorrido completo de los datos del cliente dentro de Braze, desde la recopilación de datos propios totalmente fiable y enriquecida hasta en un 30 %, hasta la activación de flujos de eventos en tiempo real para recorridos personalizados. Además, MetaRouter agiliza la implementación al eliminar la necesidad de etiquetas de Braze u otras etiquetas de terceros, otorgándote un control granular, parámetro por parámetro, sobre los datos que fluyen hacia Braze.

_Esta integración está mantenida por Metarouter._

## Características compatibles {#supported-features}

- Se pueden incorporar reintentos.
- Las solicitudes se procesan por lotes.
- Los problemas de límite de velocidad se gestionan con un reintento.
- Se admiten ID externo y PII. MetaRouter pasa su ID anónimo y cualquier PII (correo electrónico, número de teléfono, nombre) que los clientes deseen.
- Puedes enviar datos de compras y eventos personalizados de Braze.
  - Se admiten propiedades del evento.
  - No se admiten propiedades de eventos anidados.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

| Requisito | Descripción |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta MetaRouter | Una [cuenta MetaRouter Enterprise](https://enterprise.metarouter.io/). |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`. Para crear una, ve a **Settings** > **API Keys**. |
| Un punto de conexión REST or transferencia de estado representacional de Braze | [La URL de tu punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuración de MetaRouter {#setting-up-metarouter}

Para configurar MetaRouter para tu integración con Braze:

1. Ve a MetaRouter y crea un nuevo clúster.
2. Elige los eventos que deseas rastrear.
3. Instala un SDK or kit de desarrollo de software de MetaRouter e integra eventos en tu sitio web.
4. Conecta tu clúster a la interfaz de usuario de tu sitio web.
5. Crea una nueva canalización.
6. Verifica que tu sitio web está enviando eventos a MetaRouter.

## Integración de Braze {#integrating-braze}

### Paso 1: Añadir la integración de Braze {#step-1-add-the-braze-integration}

En Enterprise MetaRouter, selecciona **Integrations** > **New Integration** > **Braze** y luego asigna un nombre a tu integración. A continuación, introduce la URL de tu instancia y la clave de API, y selecciona **Apply Changes**.

![Añadir Braze como integración en MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### Paso 2: Añadir mapeado de eventos {#step-2-add-event-mapping}

Añade el mapeado de eventos para cada salida de identidad y, a continuación, configura los eventos que deseas enviar a Braze. Cuando hayas terminado, selecciona **Save as New Revision**.

![Añade mapeados de eventos para cada una de las salidas de identidad.]({% image_buster /assets/img/metarouter/img2.png %})
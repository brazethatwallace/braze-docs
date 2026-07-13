---
nav_title: loplat
article_title: loplat
description: "Este artículo de referencia describe la asociación entre Braze y loplat, una plataforma de marketing offline basada en la ubicación, que te permite ejecutar campañas de marketing de proximidad añadiendo contexto de ubicación."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [Loplat](https://www.loplat.com/) es la principal plataforma offline basada en la ubicación. Usa el SDK de loplat para aumentar la afluencia a tu tienda de forma inteligente y ejecutar campañas de marketing que fomenten las compras en tienda. Puedes medir el rendimiento de la tienda mediante el análisis de afluencia una vez finalizada la campaña.

_Esta integración está mantenida por Loplat._

## Sobre la integración {#about-the-integration}

La integración de Braze y loplat te permite usar los servicios de ubicación de loplat (POI de la tienda y geovalla personalizada) para activar campañas de marketing geocontextuales y crear eventos personalizados mediante segmentación offline. Cuando los usuarios visitan la ubicación seleccionada en loplat X, la información sobre la campaña y la ubicación se envía inmediatamente a Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| --- | --- |
| Cuenta loplat X | Se necesita una cuenta loplat X para aprovechar esta integración.<br><br>Envía un correo electrónico a [support@loplat.com](mailto:support@loplat.com) para solicitar una cuenta loplat X. |
| SDK de loplat | El SDK de loplat reconoce las visitas de los usuarios a las tiendas, procesa los eventos de ubicación y distingue si los usuarios permanecen en un lugar o se desplazan. Puedes usar el SDK de loplat para analizar la afluencia a tu tienda, enviar mensajes push cuando los usuarios entren en ella, etc.<br><br>Ten en cuenta que el SDK solo está disponible para Android e iOS. |
| Clave de API REST de Braze | Una clave de API REST de Braze con los siguientes permisos:<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

La información de ubicación de eventos personalizados que proporciona loplat puede utilizarse en tus campañas para lograr ejemplos como:

- [Alerta de promoción en tiendas libres de impuestos](https://www.loplat.com/loplat-x#usecase)
    - Envía cupones de descuento de tiendas libres de impuestos a los usuarios que se encuentren cerca de las puertas de embarque en el aeropuerto.
- Push de ubicación de estaciones de recarga de vehículos eléctricos (VE)
    - Establece geovallas alrededor de las estaciones de recarga de VE y notifica a los usuarios cuando estén cerca de la estación, animándolos a cargar.

## Integración {#integration}

### Paso 1: Integrar los SDK {#step-1-integrate-the-sdks}

Integra el SDK de loplat y el SDK de Braze en tu aplicación siguiendo los pasos indicados en la documentación de [integración de loplat-Braze](https://developers.loplat.com/braze/).

### Paso 2: Sincronizar los paneles de Braze y loplat X y crear una campaña {#step-2-sync-the-braze-and-loplat-x-dashboards-and-create-a-campaign}

Crea una nueva clave de API en el panel de Braze. Copia la clave de API y pégala en **Settings > API Settings** en el panel de loplat X. Consulta la [guía del usuario de loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25) para más detalles.

#### Entrega activada por API {#api-triggered-delivery}

1. Crea una Campaign o un Canvas en Braze que se envíe con **API-Triggered Delivery** y copia el ID de la campaña.
2. Lanza la campaña en Braze una vez completados todos los pasos.
3. Ve a loplat X y crea una campaña siguiendo las instrucciones de la [guía del usuario de loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb).
4. Pega el ID de la Campaign de Braze en **Campaign Message Settings** y lanza la campaña.

![Configuración de campaña en loplat X mostrando el ID de Campaign de Braze para la entrega activada por API.]({% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %})

#### Entrega basada en acciones {#action-based-delivery}

Con la integración, puedes aplicar condiciones de ubicación mediante el envío de información de geovalla, región, marca o nombre de la tienda. Además, puedes añadir segmentos o asignar conversiones con el evento personalizado que hayas creado.
1. Crea una campaña en loplat X siguiendo las instrucciones de la [guía del usuario de loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598).
2. Añade un evento personalizado en **Campaign Message Settings** y lanza la campaña.
3. Ve al panel de Braze y crea una Campaign o un Canvas que se envíe con **Action-Based Delivery**.
4. Selecciona el evento personalizado que creaste en loplat X para establecer una acción desencadenante de ubicación.

![Configuración de Campaign basada en acciones en Braze usando un evento personalizado de loplat como desencadenante.]({% image_buster /assets/img/loplat/loplat_action_based_delivery.png %})
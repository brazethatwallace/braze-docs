---
nav_title: Swym
article_title: Swym
description: "Este artículo de referencia describe la asociación entre Braze y Swym, que permite a los compradores guardar productos y continuar fácilmente su recorrido a través de sitios web, aplicaciones móviles y tiendas minoristas."
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# Swym

> [Swym](https://getswym.com/) ayuda a las marcas de comercio electrónico a captar la intención de compra con listas de deseos, guardar para más tarde, registro de regalos y alertas de disponibilidad. Utilizando datos ricos y basados en permisos, puedes crear campañas hiperdirigidas y entregar experiencias de compra personalizadas que impulsen la interacción, aumenten las conversiones e incrementen la fidelización.

*Esta integración está mantenida por Swym.*

## Sobre la integración {#about-the-integration}

La integración de Swym y Braze te permite entregar campañas de marketing personalizadas y basadas en eventos que convierten la intención del comprador en ventas. Utiliza la integración para que los compradores puedan continuar donde lo dejaron, colaborar con otros a lo largo de su recorrido de compra y recibir campañas de reorientación de alto rendimiento.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

| Requisito          | Descripción                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym  | Las aplicaciones Swym Wishlist Plus, Back in Stock, o ambas, deben estar instaladas en tu plataforma de comercio electrónico (Shopify o BigCommerce), y debes tener el plan Enterprise.       |
| Una clave de API REST de Braze  | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el dashboard de Braze desde **Settings** > **API Keys**. |
| Un punto de conexión REST de Braze | [La URL de tu punto de conexión REST]({{site.baseurl}}/api/basics/#endpoints). Tu punto de conexión dependerá de la URL de Braze para tu instancia.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Al conectar las aplicaciones Wishlist Plus y Back in Stock Alerts de Swym con Braze, puedes enviar automáticamente a Braze eventos de actividad de los compradores, como adiciones a la lista de deseos, suscripciones a alertas de disponibilidad, alertas de bajada de precios y recordatorios, como eventos personalizados. Estos eventos pueden utilizarse para desencadenar mensajes automatizados en Braze, facilitando una comunicación oportuna, relevante y atractiva que haga que los compradores vuelvan a realizar una compra.

## Integración de Swym {#integrating-swym}

### Paso 1: Conecta tu aplicación Swym a Braze {#step-1-connect-your-swym-app-to-braze}

Actualmente, la integración de Braze con Swym es una integración gestionada y no es autoservicio. Para empezar, ponte en contacto con el equipo de soporte de Swym en [support@getswym.com](mailto:support@getswym.com) y proporciona la siguiente información para que Swym pueda configurar la integración en tu nombre:

1. Genera una [clave de API REST]({{site.baseurl}}/api/basics/#about-rest-api-keys) en tu dashboard de Braze con el permiso `users.track`.

![Generación de una clave de API en Braze.]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
Para proteger tus claves de API, Swym recomienda que compartas las credenciales de forma segura utilizando una herramienta de enlace único y autodestructivo (por ejemplo, [OneTimeSecret](https://onetimesecret.com/)).
{% endalert %}

{: start="2"}
2. Braze gestiona varias instancias para su dashboard y sus puntos de conexión REST. Proporciona el [punto de conexión REST]({{site.baseurl}}/api/basics/#endpoints) de la instancia que tienes aprovisionada.

3. Después de compartir la clave de API y la URL de instancia con el equipo de soporte de Swym, ellos configurarán la integración por ti y te responderán con una confirmación.

4. Una vez completada la configuración, los eventos personalizados de Swym se registrarán automáticamente en Braze. Puedes ver la lista de eventos Swym registrados en el dashboard de Braze yendo a **Data Settings** > **Custom Events**.

5. Visualiza las propiedades de cada evento Swym seleccionando **Manage Properties** del evento personalizado correspondiente. Estas propiedades contienen los valores del evento que pueden utilizarse para personalizar tus mensajes.

![Propiedades personalizadas en Braze.]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### Paso 2: Suscríbete a los eventos que quieras enviar a Braze {#step-2-subscribe-to-events-you-want-to-send-to-braze}

Desde tu aplicación Wishlist Plus, ve a la pestaña **Marketing** y busca la sección **Automations**. Aquí puedes seleccionar los eventos a los que quieres suscribirte.

![Eventos a los que suscribirse.]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Eventos de la aplicación Swym Wishlist Plus {#swym-wishlist-plus-app-events}

| Nombre de evento | Cuándo se desencadena este evento |
|------------|------------------------------|
| Compartir lista de deseos | Cuando un comprador comparte una lista de deseos con otra persona |
| Añadir a la lista de deseos | Cuando un comprador añade un artículo a su lista de deseos |
| Recordatorio de la lista de deseos | Recordatorio sobre los artículos de la lista de deseos de un comprador |
| Recordatorio de guardado para más tarde | Recordatorio sobre los artículos guardados para más tarde de un comprador |
| Alerta de bajada de precios | Un producto de una lista de deseos se pone en oferta |
| Alerta de existencias bajas | Un producto de una lista de deseos se está agotando |
| Alerta de nuevo en stock | Se repone un producto de una lista de deseos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos de la aplicación Swym Wishlist Plus" }

#### Eventos de la aplicación Swym Back in Stock Alerts {#swym-back-in-stock-alerts-app-events}

| Nombre de evento | Cuándo se desencadena este evento |
|------------|------------------------------|
| Confirmación de disponibilidad | El comprador se suscribe para recibir una notificación cuando un producto vuelva a estar en stock |
| Alerta de reabastecimiento | Se repone el producto para el que un comprador solicitó una alerta de disponibilidad |
| Recordatorio de reabastecimiento | Alerta de seguimiento (normalmente unas 24 horas después de la primera alerta de reabastecimiento, configurable) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos de la aplicación Swym Back in Stock Alerts" }

### Paso 3: Crea una campaña o Canvas en Braze {#step-3-create-a-braze-campaign-or-canvas}

Para automatizar la entrega de mensajes personalizados para tus compradores, debes crear una campaña o Canvas independiente en Braze para cada evento al que te hayas suscrito. Cada campaña o Canvas debe configurarse para desencadenarse en función del evento específico y utilizar las propiedades del evento correspondientes para rellenar contenido dinámico en tus mensajes. Para una guía paso a paso, puedes consultar [Primeros pasos: campañas y Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases/).

![Un evento basado en la acción.]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

Para más información, consulta el [centro de ayuda de Swym](https://help.getswym.com/en/articles/12344153-braze-integration) o ponte en contacto con el equipo de soporte de Swym en [support@getswym.com](mailto:support@getswym.com).
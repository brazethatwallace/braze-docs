---
nav_title: Shopify para Currents
article_title: Shopify para Currents
description: "Este artículo de referencia describe la asociación entre Braze Currents y Shopify, una empresa de comercio global que te permite conectar fácilmente Braze con tu tienda Shopify para potenciar los informes internos y realizar un mejor seguimiento de la atribución de último contacto para las compras."
page_type: partner
tool: Currents
search_tag: Partner
alias: /shopify_for_currents/
hidden: true
noindex: true

---

# Shopify para Currents {#shopify-for-currents}

> [Shopify](https://www.shopify.com/) es una empresa líder en comercio global que proporciona herramientas de confianza para iniciar, hacer crecer, comercializar y administrar un negocio de cualquier tamaño. La plataforma y los servicios de Shopify están diseñados para ofrecer fiabilidad y una mejor experiencia de compra para los consumidores en todas partes.

{% alert important %}
Esta integración se encuentra actualmente en fase beta. Para más información, ponte en contacto con tu administrador del éxito del cliente de Braze.
{% endalert %}

La integración de Braze con Shopify proporciona una solución potente para los negocios de comercio electrónico que buscan mejorar la interacción con los clientes e impulsar esfuerzos de marketing personalizados. Con [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), puedes conectar datos a Shopify para potenciar los informes internos y realizar un mejor seguimiento de la atribución de último contacto para las compras.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Currents | Para exportar datos a Shopify, debes tener [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado para tu cuenta. |
| Tienda Shopify | Asegúrate de haber [configurado al menos una tienda Shopify con Braze]({{site.baseurl}}/shopify_standard_integration/). |
| Permisos de propietario o miembro del personal de la tienda Shopify | {::nomarkdown}<ul><li>Acceso a toda la configuración de <b>General</b> y <b>Online Store</b>.</li><li> Permisos de administrador adicionales:</li><ul><li>Orders: View</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>Manage Settings</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración {#integration}

### Paso 1: Configura tu tienda Shopify {#step-1-set-up-your-shopify-store}

Si aún no lo has hecho, sigue los pasos de [configuración de la integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration/) para configurar al menos una tienda Shopify con Braze.

### Paso 2: Crea un Braze Current {#step-2-create-braze-current}

1. En Braze, ve a **Partner Integrations** > **Currents** > **+ Create New Current** > **Shopify Export**.
2. Proporciona un nombre de integración y un correo electrónico de contacto.
3. En la sección **Credentials**, selecciona la tienda Shopify que configuraste en el [Paso 1](#step-1-set-up-your-shopify-store).
4. Selecciona los eventos que deseas rastrear. Se proporciona una lista de eventos disponibles.
5. Selecciona **Launch Current**.

![La página de Braze Shopify Currents. Esta página incluye campos para el nombre de la integración, el correo electrónico de contacto y la tienda Shopify.]({% image_buster /assets/img/shopify/shopify_currents.png %})
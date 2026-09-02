---
nav_title: Integración estándar de Shopify con etiquetado de terceros
article_title: Integración estándar de Shopify con etiquetado de terceros
description: "Este artículo de referencia describe cómo configurar la integración estándar de Shopify con una herramienta de etiquetado de terceros."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# Integración estándar de Shopify con herramienta de etiquetado de terceros {#shopify-standard-integration-with-third-party-tagging-tool}

> Esta página te guía a través del uso de herramientas de terceros, como Google Tag Administrador, con la [integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration) para inicializar y cargar el SDK or kit de desarrollo de software Web de Braze.

Para las tiendas online de Shopify, recomendamos utilizar el método de integración estándar de Braze para admitir los SDK or kit de desarrollo de software de Braze en tu sitio. Sin embargo, entendemos que prefieras utilizar una herramienta de terceros, como Google Tag Administrador. Si decides utilizar una herramienta de terceros con el conector de Shopify de Braze, ten en cuenta que la integración de Braze y la incrustación de la aplicación gestionarán el SDK or kit de desarrollo de software durante el proceso de pago.

## Requisitos {#requirements}

- **Clave de API coherente entre tu herramienta de terceros y el conector de Shopify:** La clave de API debe ser coherente tanto en Braze como en tu herramienta de terceros. Esto evita la creación de usuarios duplicados y mantiene la compatibilidad entre SDK or kit de desarrollo de software.
  - **Ubicación de la clave de API:** Tras la incorporación de la ruta de integración estándar, la integración creará automáticamente una aplicación Web de Braze llamada "Shopify". Recupera la clave de API dentro de la integración que se utiliza con la configuración de tu herramienta de terceros.
- **Versiones de SDK or kit de desarrollo de software coherentes entre tu herramienta de terceros y el conector de Shopify:** Los nuevos clientes se aprovisionan con la última versión del SDK or kit de desarrollo de software durante la configuración. Tu herramienta de terceros debe utilizar la misma versión del SDK or kit de desarrollo de software configurada en la configuración de integración de Braze. Los clientes existentes reciben una notificación cuando hay una versión más reciente disponible y pueden actualizar por su cuenta desde la configuración de integración.
- **Tiempo de inicialización del SDK or kit de desarrollo de software coherente:** Dentro de la configuración de integración estándar de Shopify, puedes seleccionar los SDK or kit de desarrollo de software que se inicializarán al inicio de sesión o cuando se produzca un inicio de sesión en la cuenta. Esta configuración debe ser coherente entre tu herramienta de terceros y Braze. Las incoherencias podrían provocar problemas posteriores para el usuario y la sincronización de datos.

{% alert note %}
Recomendamos utilizar exclusivamente el método de integración estándar en lugar de utilizarlo junto con administradores de etiquetas de terceros, lo que puede causar conflictos entre el SDK or kit de desarrollo de software de Braze y las herramientas de terceros. Si utilizas una herramienta de terceros, haz pruebas para confirmar que todo funciona como se espera.
{% endalert %}

## Configuración de la integración con una herramienta de terceros {#setting-up-the-integration-with-a-third-party-tool}

Apartarse de los pasos indicados puede provocar problemas inesperados, así que asegúrate de seguirlos al pie de la letra.

1. Sigue los pasos indicados en la [configuración de la integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration). Al [habilitar los SDK or kit de desarrollo de software Web de Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#step-2-enable-braze-web-sdks), marca la casilla que indica que estás utilizando una herramienta de terceros para añadir el SDK or kit de desarrollo de software Web de Braze a tu sitio de Shopify.
2. Ve a **Configuración** > **Configuración de la aplicación**, selecciona la aplicación Web **Shopify** y, a continuación, copia la **clave de API para Shopify en Web**.
3. Pega la clave de API en la configuración del SDK or kit de desarrollo de software Web de tu herramienta de terceros y establece la versión del SDK or kit de desarrollo de software para que coincida con la integración de Braze con Shopify.

{% alert note %}
Si utilizas Google Tag Administrador, mantén las versiones del SDK or kit de desarrollo de software alineadas tanto en GTM como en la configuración de tu integración de Braze con Shopify.
{% endalert %}

## Captura de datos de Shopify y sincronización de usuarios {#capturing-shopify-data-and-syncing-users}

Siempre que el SDK or kit de desarrollo de software Web sea accesible en el front-end de tu sitio Shopify a través de una herramienta de terceros, la integración estándar capturará los datos de Shopify y sincronizará a los usuarios como se espera.

## Consideraciones y descargos de responsabilidad {#considerations-and-disclaimers}

- **Configuración de inicialización:** Si modificas la configuración de inicialización a través de tu herramienta de terceros, la sincronización de usuarios y datos puede verse afectada. Por ejemplo, si decides inicializar tu SDK or kit de desarrollo de software cuando se acepte un formulario de consentimiento de cookies, Braze no recibirá seguimiento de usuarios anónimos ni datos hasta que el usuario dé su consentimiento.
- **No se admite configurar atributos directamente a través de `dataLayer`:** Utiliza `window.braze` en lugar de `dataLayer` para establecer atributos.
- **Posibles usuarios duplicados:** Si la clave de API no coincide entre Braze y tu herramienta de terceros, pueden crearse usuarios duplicados.
- **Incompatibilidad del SDK or kit de desarrollo de software:** Utilizar un número de versión incorrecto puede causar problemas con los métodos del SDK or kit de desarrollo de software.
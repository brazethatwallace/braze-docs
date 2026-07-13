---
nav_title: Shopify checkout y Liquid
page_order: 7
description: "Este artículo explica la obsolescencia de checkout&#46;liquid de Shopify, incluyendo el impacto en tu integración con Shopify y una guía para desarrolladores."
page_type: update

---

# Obsolescencia de checkout&#46;liquid de Shopify {#shopify-checkout46liquid-deprecation}

Shopify ha informado a todos los comerciantes sobre la obsolescencia de `checkout.liquid` y la migración a [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions), una nueva base para crear experiencias de pago personalizadas.

Shopify dejará de utilizar `checkout.liquid` en dos fases:

1. **[13 de agosto de 2024](#phase-one-august-13-2024):** Fecha límite para actualizar tus páginas de información, envío y pago.
2. **[28 de agosto de 2025](#phase-two-august-28-2025):** Fecha límite para actualizar tus páginas de agradecimiento y estado del pedido, incluyendo tus aplicaciones que utilizan etiquetas de script y scripts adicionales.

Para obtener información general sobre la actualización a Checkout Extensibility, consulta [la guía de actualización de Shopify](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility).

## Impacto en tu integración {#impact-to-your-integration}

La integración de Braze y Shopify utiliza [ScriptTags de Shopify](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) para cargar el SDK Web de Braze en sitios sin encabezado. Tenemos previsto lanzar una nueva versión de la integración antes de la fecha límite de 2025 para dar soporte a todos los clientes antes de que `checkout.liquid` quede totalmente obsoleto.

Para los próximos cambios del 13 de agosto de 2024, consulta los detalles a continuación para ver si tu equipo de desarrollo se verá afectado.

### Primera fase: 13 de agosto de 2024 {#phase-one-august-13-2024}

La integración predeterminada de Braze y Shopify no utiliza las páginas de información, envío y pago dentro de la experiencia de pago. En consecuencia, la integración predeterminada no se verá afectada.

#### Shopify Plus

Para los clientes de Shopify Plus, cualquier fragmento de código SDK personalizado que modifique `checkout.liquid` para las páginas de información, envío o pago quedará inactivo después de esta fecha. Por ejemplo, el código personalizado que registra eventos de estas páginas ya no funcionará. Si tienes código SDK personalizado, consulta nuestra [guía del desarrollador](#developer-guidance) para la migración.

#### No Shopify Plus {#non-shopify-plus}

Para los clientes que no son de Shopify Plus, si necesitas personalizar las páginas de información, pago y envío, [debes actualizar a Shopify Plus](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) y luego seguir la [guía del desarrollador](#developer-guidance).

### Segunda fase: 28 de agosto de 2025 {#phase-two-august-28-2025}

Shopify dejará de admitir [ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) en las páginas `checkout.liquid`, que se utilizan en la integración. En respuesta, estamos construyendo activamente una nueva versión de la integración de Shopify que tenemos previsto publicar mucho antes de la fecha límite de agosto de 2025. Permanece atento para recibir más información del equipo de productos de Braze.

## Guía del desarrollador {#developer-guidance}

Esta guía se aplica a los clientes de Shopify Plus que hayan añadido fragmentos de código SDK personalizados a las páginas de información, envío o pago en `checkout.liquid`. Si no has realizado estas personalizaciones, puedes hacer caso omiso de esta guía.

Ya no podrás añadir fragmentos de código SDK personalizados a las páginas de información, envío o pago en `checkout.liquid`. En su lugar, tendrás que añadir fragmentos de código SDK personalizados a las páginas de agradecimiento o de estado del pedido. Esto te permite conciliar los usuarios que completaron el pago.
1. Carga el SDK Web de Braze en las páginas de agradecimiento y estado del pedido.
2. Recupera el correo electrónico del usuario.
3. Llama a `setEmail`.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4. En Braze, fusiona los perfiles de usuario por correo electrónico.

Si encuentras perfiles de usuario duplicados, puedes utilizar nuestra [herramienta de fusión masiva]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) para ayudar a optimizar tus datos.
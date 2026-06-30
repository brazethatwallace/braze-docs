---
nav_title: Perfil de usuario
article_title: Perfil de usuario
page_order: 0
description: "Aprende a personalizar mensajes con datos del perfil de usuario, incluyendo atributos estándar, atributos personalizados y propiedades del evento."
---

# Perfil de usuario {#user-profile}

> Personaliza tus mensajes con datos almacenados en el perfil de cada usuario, incluyendo atributos estándar, atributos personalizados y propiedades del evento. Braze pone estos datos a tu disposición a través de etiquetas [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) que insertas directamente en el contenido de tu mensaje.

## Atributos estándar {#standard-attributes}

{% raw %}
Los atributos estándar son campos de perfil predefinidos que Braze rastrea automáticamente, como `{{${first_name}}}`, `{{${email_address}}}` y `{{${city}}}`. Dado que estos atributos siguen una convención de nomenclatura consistente, puedes hacer referencia a ellos en cualquier mensaje sin configuración adicional.

Por ejemplo, para saludar a un usuario por su nombre:

```liquid
Hi {{${first_name} | default: 'there'}}, check out our latest picks for you!
```
{% endraw %}

Para ver una lista completa de etiquetas de atributos estándar, consulta [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

## Atributos personalizados {#custom-attributes}

{% raw %}
Los atributos personalizados son campos de perfil únicos de tu espacio de trabajo, como nivel de fidelización, categoría favorita o tipo de cuenta. Haz referencia a ellos usando la etiqueta `{{custom_attribute.${attribute_name}}}`.

Por ejemplo, para personalizar un mensaje según el nivel de membresía de un usuario:

```liquid
{% if custom_attribute.${membership_tier} == 'gold' %}
  As a Gold member, you get early access to our new collection.
{% else %}
  Upgrade your membership for early access to new collections.
{% endif %}
```
{% endraw %}

Para más información sobre cómo crear y gestionar atributos personalizados, consulta [Atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

## Propiedades del evento {#event-properties}

{% raw %}
Cuando una campaña o Canvas se desencadena por un evento personalizado o una compra, las propiedades del evento están disponibles para la personalización. Haz referencia a ellas usando `{{event_properties.${property_name}}}`.

Por ejemplo, si un evento personalizado `completed_purchase` incluye una propiedad `product_name`:

```liquid
Thanks for purchasing {{event_properties.${product_name}}}! Your order is on its way.
```
{% endraw %}

Las propiedades del evento están disponibles en campañas basadas en acciones y en el primer paso de un Canvas basado en acciones. Para más información, consulta [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events).

## Propiedades de activación de API {#api-trigger-properties}

{% raw %}
Para campañas y Canvas desencadenados a través de la API, puedes pasar datos adicionales usando el objeto de propiedades de activación. Haz referencia a estos valores con `{{api_trigger_properties.${property_name}}}`.

Por ejemplo:

```liquid
Your verification code is {{api_trigger_properties.${verification_code}}}.
```
{% endraw %}

Para más información, consulta [Objeto de propiedades de activación de API]({{site.baseurl}}/api/objects_filters/trigger_properties_object).

## Atributos del dispositivo {#device-attributes}

{% raw %}
También puedes hacer referencia a atributos del dispositivo usado más recientemente por el usuario. Por ejemplo, `{{most_recently_used_device.${model}}}` devuelve el nombre del modelo del dispositivo, y `{{most_recently_used_device.${os}}}` devuelve el sistema operativo.
{% endraw %}

Para ver la lista completa de etiquetas de atributos de dispositivo, consulta [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#most-recently-used-device-information).

## Configurar valores predeterminados {#setting-default-values}

Si un campo de perfil está vacío para un usuario determinado, Braze muestra una cadena vacía de forma predeterminada. Para evitar mensajes con apariencia incompleta, establece un valor alternativo usando el filtro Liquid `default`.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}},
```
{% endraw %}

Para más información, consulta [Configurar valores predeterminados]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values).
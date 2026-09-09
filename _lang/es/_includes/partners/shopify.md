{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
La integración estándar está diseñada para las tiendas online de Shopify y ofrece un proceso de configuración fácil y sin complicaciones. Esta opción te permite conectar rápidamente tu tienda Shopify a Braze, lo que te permite aprovechar potentes herramientas de interacción con los clientes sin necesidad de tener amplios conocimientos técnicos. Con esta opción de integración, puedes sincronizar los datos de clientes, automatizar la mensajería personalizada y mejorar tus iniciativas de marketing gracias a las completas características de Braze.

Para utilizar la integración estándar de Shopify, consulta [Configuración de la integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration).
{% endtab %}

{% tab custom %}
La integración personalizada ofrece una solución más flexible y modulable si utilizas Shopify Hydrogen o admites una tienda headless. Esta opción te permite implementar los SDK de Braze directamente en tu entorno Shopify, lo que habilita una integración más profunda y funcionalidades personalizadas. Tanto si deseas crear experiencias del cliente únicas como optimizar flujos de trabajo específicos, la integración personalizada te proporciona las herramientas necesarias para aprovechar al máximo las capacidades de Braze en una configuración headless.

Para utilizar la integración personalizada de Shopify, consulta [Configuración de la integración personalizada de Shopify]({{site.baseurl}}/shopify_custom_integration).
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == 'Custom external ID historical backfill' %}

Si planeas integrar con un ID externo personalizado (ya sea para la [integración estándar]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#step-4) o la [integración personalizada]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-6)), deberás añadir tu ID externo personalizado como metacampo de cliente de Shopify a todos los perfiles de clientes de Shopify existentes y, a continuación, realizar el backfill histórico.

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

Puedes combinar [`message_extras`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras) con [códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) para enviar información sobre códigos promocionales a Currents. Utiliza la etiqueta `capture` para almacenar el código promocional en una variable y, a continuación, haz referencia a esa variable en `message_extras`:

{% raw %}
```liquid
{% capture code %}
{% promotion('puttshacktest2') %}
{% endcapture %}
Use {{code}} for an exclusive discount!
{% message_extras :key cardscode :value {{code}} %}
```
{% endraw %}

{% endif %}
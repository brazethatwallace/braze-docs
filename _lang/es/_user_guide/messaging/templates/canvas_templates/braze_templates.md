---
nav_title: Usar plantillas de Braze
article_title: Usar plantillas de Canvas de Braze
alias: "/canvas_templates/templates/"
page_order: 2
description: "Este artículo de referencia explica cómo crear plantillas de Canvas disponibles."
page_type: reference
---

# Usar plantillas de Canvas de Braze {#use-braze-canvas-templates}

> Braze tiene una selección de plantillas de Canvas disponibles para que las consultes y uses como mejores prácticas para casos de uso comunes. Aunque estas plantillas no se pueden editar, puedes verlas en **Templates** > **Braze templates** o usarlas en tus Canvas.

![Plantillas de Braze en la sección de plantillas de Canvas con trece plantillas disponibles.]({% image_buster /assets/img/braze_canvas_templates.png %})

Selecciona entre las siguientes plantillas disponibles para consultar o usar como tu Canvas.

## Plantillas de Canvas estándar {#standard-canvas-templates}

{% tabs %}
{% tab Abandoned Intent %}

### Intención abandonada {#abandoned-intent}

Interactúa con los usuarios en tiempo real para animarlos a completar sus compras.

Ten en cuenta lo siguiente al usar esta plantilla:

- Añade una audiencia específica. Actualmente, las rutas de audiencia se desencadenan en función de "Made Any Purchase", pero puedes adaptarlo a productos específicos que quieras segmentar.
- Esta plantilla asume que tienes un recorrido post-compra separado, por lo que realizar una compra hará que los usuarios salgan del Canvas.
- Completa los detalles en el paso de Audience Sync.

{% endtab %}
{% tab Back In Stock %}

### De vuelta en stock {#back-in-stock}

Impulsa las compras notificando a tus usuarios cuando un artículo vuelve a estar disponible con mensajería personalizada. Ten en cuenta lo siguiente al usar esta plantilla:

- En **Entry Schedule**, selecciona un catálogo para usar. Esto te permite acceder a datos, como productos, descuentos y promociones, para segmentar aún más a tus usuarios.
- En **Target Audience**, añade un segmento para segmentar a los usuarios que indicaron interés en un artículo determinado.
- En los pasos de mensaje a lo largo del Canvas, actualiza el Liquid para hacer referencia a tu catálogo.

{% endtab %}
{% tab Feature Adoption %}

### Adopción de características {#feature-adoption}

Entrega mensajes personalizados oportunos para destacar los beneficios y consejos de uso. Ten en cuenta lo siguiente al usar esta plantilla:

- Excluye a los usuarios que ya hayan adoptado la característica. Por ejemplo, en **Target Audience**, añade un filtro para un evento personalizado como "Activated Feature" que ya haya ocurrido.
- Para usar el paso de ruta de experimentos, define un evento de conversión. Este evento debe ser el que señale la adopción de la característica.
- Configura el paso de ruta de acción en la plantilla con eventos personalizados para "Activated Feature" y "Taken Tour".
- Configura los atributos personalizados en el paso de mensaje llamado "Feedback Survey" para capturar el sentimiento de la retroalimentación.

{% endtab %}
{% tab Lapsed User %}

### Usuario inactivo {#lapsed-user}

Haz que los usuarios vuelvan a tu aplicación con incentivos basados en sus interacciones pasadas. Ten en cuenta lo siguiente al usar esta plantilla:

- En **Basics**, selecciona una aplicación específica para la que rastrear conversiones.
- En el editor de Canvas, añade aplicaciones específicas para los pasos de rutas de acción.
- Configura el paso de Audience Sync con los socios y audiencias para tu caso de uso.

{% endtab %}
{% tab Onboarding %}

### Incorporación {#onboarding}

Crea recorridos de incorporación que promuevan una adopción inicial sólida y fomenten relaciones duraderas con tus usuarios. Ten en cuenta lo siguiente al usar esta plantilla:

- En el paso de rutas de audiencia llamado "Audience Split", considera personalizar las acciones clave para los usuarios comprometidos. En la plantilla, el filtro de segmento es "Has clicked email for step Welcome Email".

{% endtab %}
{% tab Post-Purchase Feedback %}

### Opinión post-compra {#post-purchase-feedback}

Orquesta experiencias personalizadas que te permitan responder a la retroalimentación y construir una relación con tus usuarios. Ten en cuenta lo siguiente al usar esta plantilla:

- En el primer paso del editor de Canvas:
    - Especifica los atributos personalizados en el mensaje dentro de la aplicación para indicar el sentimiento de la retroalimentación según la opción del cuestionario seleccionada.
    - Especifica atributos en los enlaces para cada llamada a la acción para capturar qué opción se selecciona. Estos atributos se referencian en la ruta de audiencia posterior.
- Personaliza la ruta de audiencia con los atributos del primer paso de esta plantilla.
- Configura el paso de Audience Sync llamado "Ad Retargeting".

{% endtab %}
{% endtabs %}

## Plantillas de Canvas de comercio electrónico {#ecommerce-canvas-templates}

Las plantillas de Canvas de comercio electrónico están diseñadas específicamente para especialistas en marketing de comercio electrónico, lo que facilita la implementación de estrategias esenciales.

{% multi_lang_include canvas/ecommerce_templates.md %}
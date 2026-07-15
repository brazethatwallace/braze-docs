{%- assign portal_url = site.baseurl | append: '/user_guide/administer/personal/product_portal' -%}
{%- assign feature_label = include.feature | default: 'this capability' -%}
{%- assign pain_point_channel = include.channel | default: '' | downcase -%}
{%- if include.context == 'gap' -%}
Si te interesa {{ feature_label }}, envía [comentarios sobre el producto]({{ portal_url }}).
{%- elsif include.context == 'new_feature' -%}
{%- assign feature_label = include.feature | default: 'This capability' -%}
{{ feature_label }} está disponible de forma general. Comparte cómo funciona para tu equipo a través de [comentarios sobre el producto]({{ portal_url }}).
{%- elsif include.context == 'pain_point' -%}
{%- if pain_point_channel == 'feature' -%}
¿Quieres {{ feature_label }}? Considera dejar [comentarios sobre el producto]({{ portal_url }}).
{%- elsif pain_point_channel == 'ux' -%}
Si tienes comentarios sobre {{ feature_label }}, abre el menú **Support** en el encabezado global y selecciona **Share feedback** para enviarnos tus opiniones.
{%- else -%}
<!-- product_feedback_cta fallback: missing or invalid pain_point channel; expected feature or ux -->
¿Quieres {{ feature_label }}? Considera dejar [comentarios sobre el producto]({{ portal_url }}).
{%- endif -%}
{%- endif -%}
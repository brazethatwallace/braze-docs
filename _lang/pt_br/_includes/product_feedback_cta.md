{%- assign portal_url = site.baseurl | append: '/user_guide/administer/personal/product_portal' -%}
{%- assign feature_label = include.feature | default: 'este recurso' -%}
{%- assign pain_point_channel = include.channel | default: '' | downcase -%}
{%- if include.context == 'gap' -%}
Se você tem interesse em {{ feature_label }}, envie [feedback de produto]({{ portal_url }}).
{%- elsif include.context == 'new_feature' -%}
{%- assign feature_label = include.feature | default: 'Este recurso' -%}
{{ feature_label }} está disponível para todos. Compartilhe como está funcionando para sua equipe por meio do [feedback de produto]({{ portal_url }}).
{%- elsif include.context == 'pain_point' -%}
{%- if pain_point_channel == 'feature' -%}
Quer {{ feature_label }}? Considere deixar um [feedback de produto]({{ portal_url }}).
{%- elsif pain_point_channel == 'ux' -%}
Se você tem feedback sobre {{ feature_label }}, abra o menu **Suporte** no cabeçalho global e selecione **Compartilhar feedback** para nos enviar suas opiniões.
{%- else -%}
<!-- product_feedback_cta fallback: missing or invalid pain_point channel; expected feature or ux -->
Quer {{ feature_label }}? Considere deixar um [feedback de produto]({{ portal_url }}).
{%- endif -%}
{%- endif -%}
{%- assign portal_url = site.baseurl | append: '/user_guide/administer/personal/product_portal' -%}
{%- assign feature_label = include.feature | default: 'cette fonctionnalité' -%}
{%- assign pain_point_channel = include.channel | default: '' | downcase -%}
{%- if include.context == 'gap' -%}
Si {{ feature_label }} vous intéresse, envoyez un [retour produit]({{ portal_url }}).
{%- elsif include.context == 'new_feature' -%}
{%- assign feature_label = include.feature | default: 'Cette fonctionnalité' -%}
{{ feature_label }} est disponible de manière générale. Dites-nous comment cela fonctionne pour votre équipe en laissant un [retour produit]({{ portal_url }}).
{%- elsif include.context == 'pain_point' -%}
{%- if pain_point_channel == 'feature' -%}
Vous souhaitez {{ feature_label }} ? N'hésitez pas à laisser un [retour produit]({{ portal_url }}).
{%- elsif pain_point_channel == 'ux' -%}
Si vous avez des commentaires sur {{ feature_label }}, ouvrez le menu **Support** dans l'en-tête global et sélectionnez **Partager un retour** pour nous faire part de vos impressions.
{%- else -%}
<!-- product_feedback_cta fallback: missing or invalid pain_point channel; expected feature or ux -->
Vous souhaitez {{ feature_label }} ? N'hésitez pas à laisser un [retour produit]({{ portal_url }}).
{%- endif -%}
{%- endif -%}
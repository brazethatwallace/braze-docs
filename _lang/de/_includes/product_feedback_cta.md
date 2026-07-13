{%- assign portal_url = site.baseurl | append: '/user_guide/administer/personal/product_portal' -%}
{%- assign feature_label = include.feature | default: 'this capability' -%}
{%- assign pain_point_channel = include.channel | default: '' | downcase -%}
{%- if include.context == 'gap' -%}
Wenn Sie an {{ feature_label }} interessiert sind, reichen Sie [Produktfeedback]({{ portal_url }}) ein.
{%- elsif include.context == 'new_feature' -%}
{%- assign feature_label = include.feature | default: 'This capability' -%}
{{ feature_label }} ist allgemein verfügbar. Teilen Sie uns über [Produktfeedback]({{ portal_url }}) mit, wie es für Ihr Team funktioniert.
{%- elsif include.context == 'pain_point' -%}
{%- if pain_point_channel == 'feature' -%}
Sie wünschen sich {{ feature_label }}? Hinterlassen Sie gerne [Produktfeedback]({{ portal_url }}).
{%- elsif pain_point_channel == 'ux' -%}
Wenn Sie Feedback zu {{ feature_label }} haben, öffnen Sie das Menü **Support** in der globalen Kopfzeile und wählen Sie **Feedback teilen** aus, um uns Ihre Gedanken mitzuteilen.
{%- else -%}
<!-- product_feedback_cta fallback: missing or invalid pain_point channel; expected feature or ux -->
Sie wünschen sich {{ feature_label }}? Hinterlassen Sie gerne [Produktfeedback]({{ portal_url }}).
{%- endif -%}
{%- endif -%}
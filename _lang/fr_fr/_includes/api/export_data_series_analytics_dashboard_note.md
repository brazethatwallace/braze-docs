{% comment %}
  Moved into the includes/api subfolder; previously, this wasn't in a subfolder.
  Note for GET export campaign/canvas/send data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "campaign", "canvas", or "send" — selects the opening phrase and dashboard analytics label.
{% endcomment %}

{% if include.type == 'send' %}
{% capture counts_subject %}Les comptages `data_series` au niveau de l'envoi{% endcapture %}
{% capture dashboard_match %}l'analyse d'engagement du tableau de bord{% endcapture %}
{% elsif include.type == 'canvas' %}
{% capture counts_subject %}Les chiffres renvoyés par cet endpoint{% endcapture %}
{% capture dashboard_match %}l'analyse Canvas du tableau de bord{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture counts_subject %}Les chiffres renvoyés par cet endpoint{% endcapture %}
{% capture dashboard_match %}l'analyse d'engagement du tableau de bord{% endcapture %}
{% endif %}
{% alert note %}
{{ counts_subject }} ne correspondent pas toujours exactement à {{ dashboard_match }} ni aux agrégats que vous construisez à partir de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/). Les indicateurs du tableau de bord et les séries temporelles de l'API utilisent des fenêtres d'agrégation et des définitions différentes de celles des événements bruts de Currents. Pour les notes de rapprochement courantes, consultez la [FAQ Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq/).
{% endalert %}
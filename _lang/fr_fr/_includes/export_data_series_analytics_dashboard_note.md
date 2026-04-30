{% comment %}
  Note for GET export campaign/canvas data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "canvas" or "campaign" — selects the dashboard analytics label in the sentence.
{% endcomment %}
{% if include.type == 'canvas' %}
{% capture dashboard_match %}l'analyse Canvas du tableau de bord{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture dashboard_match %}l'analyse d'engagement du tableau de bord{% endcapture %}
{% endif %}
{% alert note %}
Les chiffres renvoyés par cet endpoint ne correspondent pas toujours exactement à {{ dashboard_match }} ni aux agrégats que vous construisez à partir de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/). Les indicateurs du tableau de bord et les séries temporelles de l'API utilisent des fenêtres d'agrégation et des définitions différentes de celles des événements bruts de Currents.
{% endalert %}
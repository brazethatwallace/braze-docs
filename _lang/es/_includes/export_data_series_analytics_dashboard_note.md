{% comment %}
  Note for GET export campaign/canvas data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "canvas" or "campaign" — selects the dashboard analytics label in the sentence.
{% endcomment %}
{% if include.type == 'canvas' %}
{% capture dashboard_match %}análisis de Canvas en el dashboard{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture dashboard_match %}análisis de interacción en el dashboard{% endcapture %}
{% endif %}
{% alert note %}
Los recuentos de este punto de conexión no siempre coincidirán exactamente con los {{ dashboard_match }} o con los agregados que construyas a partir de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/). Las métricas del dashboard y las series temporales de la API utilizan ventanas de agregación y definiciones diferentes a las de los eventos sin procesar de Currents.
{% endalert %}
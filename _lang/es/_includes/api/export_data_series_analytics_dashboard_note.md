{% comment %}
  Moved into the includes/api subfolder; previously, this wasn't in a subfolder.
  Note for GET export campaign/Canvas/send data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "campaign", "Canvas", or "send" — selects the opening phrase and dashboard analytics label.
{% endcomment %}

{% if include.type == 'send' %}
{% capture counts_subject %}Los recuentos de `data_series` a nivel de envío{% endcapture %}
{% capture dashboard_match %}análisis de interacción en el dashboard{% endcapture %}
{% elsif include.type == 'Canvas' %}
{% capture counts_subject %}Los recuentos de este punto de conexión{% endcapture %}
{% capture dashboard_match %}análisis de Canvas en el dashboard{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture counts_subject %}Los recuentos de este punto de conexión{% endcapture %}
{% capture dashboard_match %}análisis de interacción en el dashboard{% endcapture %}
{% endif %}
{% alert note %}
{{ counts_subject }} no siempre coincidirán exactamente con los {{ dashboard_match }} o con los agregados que construyas a partir de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/). Las métricas del dashboard y las series temporales de la API utilizan ventanas de agregación y definiciones diferentes a las de los eventos sin procesar de Currents. Para notas comunes de conciliación, consulta las [preguntas frecuentes de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq/).
{% endalert %}
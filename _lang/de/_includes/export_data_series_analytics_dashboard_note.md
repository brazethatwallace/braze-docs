{% comment %}
  Note for GET export campaign/canvas data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "canvas" or "campaign" — selects the dashboard analytics label in the sentence.
{% endcomment %}
{% if include.type == 'canvas' %}
{% capture dashboard_match %}Dashboard-Canvas-Analytics{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture dashboard_match %}Dashboard-Engagement-Analytics{% endcapture %}
{% endif %}
{% alert note %}
Die Zahlen dieses Endpunkts stimmen nicht immer exakt mit den {{ dashboard_match }} oder mit Aggregaten überein, die Sie aus [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) erstellen. Dashboard-Metriken und API-Zeitreihen verwenden andere Aggregationsfenster und Definitionen als unverarbeitete Currents-Ereignisse.
{% endalert %}
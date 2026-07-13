{% comment %}
  Moved into the includes/api subfolder; previously, this wasn't in a subfolder.
  Note for GET export campaign/canvas/send data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "campaign", "canvas", or "send" — selects the opening phrase and dashboard analytics label.
{% endcomment %}

{% if include.type == 'send' %}
{% capture counts_subject %}`data_series`-Zählwerte auf Versandebene{% endcapture %}
{% capture dashboard_match %}Engagement-Analytics im Dashboard{% endcapture %}
{% elsif include.type == 'canvas' %}
{% capture counts_subject %}Die Zählwerte dieses Endpunkts{% endcapture %}
{% capture dashboard_match %}Canvas-Analytics im Dashboard{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture counts_subject %}Die Zählwerte dieses Endpunkts{% endcapture %}
{% capture dashboard_match %}Engagement-Analytics im Dashboard{% endcapture %}
{% endif %}
{% alert note %}
{{ counts_subject }} stimmen nicht immer exakt mit den {{ dashboard_match }} oder mit Aggregaten überein, die Sie aus [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) erstellen. Dashboard-Metriken und API-Zeitreihen verwenden andere Aggregationsfenster und Definitionen als unverarbeitete Currents-Ereignisse. Allgemeine Hinweise zum Abgleich finden Sie in den [Currents-FAQ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq/).
{% endalert %}
{% comment %}
  Moved into the includes/api subfolder; previously, this wasn't in a subfolder.
  Note for GET export campaign/canvas/send data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "campaign", "canvas", or "send" — selects the opening phrase and dashboard analytics label.
{% endcomment %}

{% if include.type == 'send' %}
{% capture counts_subject %}Send-level `data_series` counts{% endcapture %}
{% capture dashboard_match %}dashboard engagement analytics{% endcapture %}
{% elsif include.type == 'canvas' %}
{% capture counts_subject %}Counts from this endpoint{% endcapture %}
{% capture dashboard_match %}dashboard Canvas analytics{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture counts_subject %}Counts from this endpoint{% endcapture %}
{% capture dashboard_match %}dashboard engagement analytics{% endcapture %}
{% endif %}
{% alert note %}
{{ counts_subject }} do not always match {{ dashboard_match }} or aggregates you build from [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) one-for-one. Dashboard metrics and API time series use different aggregation windows and definitions than raw Currents events. For common reconciliation notes, see [Currents FAQ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq/).
{% endalert %}

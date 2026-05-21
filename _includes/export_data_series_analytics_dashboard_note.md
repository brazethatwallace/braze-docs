{% comment %}
  Note for GET export campaign/canvas data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "canvas" or "campaign" — selects the dashboard analytics label in the sentence.
{% endcomment %}
{% if include.type == 'canvas' %}
{% capture dashboard_match %}dashboard Canvas analytics{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture dashboard_match %}dashboard Engagement analytics{% endcapture %}
{% endif %}
{% alert note %}
Counts from this endpoint won't always exactly match {{ dashboard_match }} or aggregates you build from [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/). Dashboard metrics and API time series use different aggregation windows and definitions than raw Currents events.
{% endalert %}

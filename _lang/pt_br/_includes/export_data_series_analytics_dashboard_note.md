{% comment %}
  Note for GET export campaign/canvas data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "canvas" or "campaign" — selects the dashboard analytics label in the sentence.
{% endcomment %}
{% if include.type == 'canvas' %}
{% capture dashboard_match %}análise de dados do Canvas no dashboard{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture dashboard_match %}análise de dados de engajamento no dashboard{% endcapture %}
{% endif %}
{% alert note %}
As contagens deste endpoint nem sempre correspondem exatamente à {{ dashboard_match }} ou aos agregados que você cria a partir do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/). As métricas do dashboard e as séries temporais da API usam janelas de agregação e definições diferentes dos eventos brutos do Currents.
{% endalert %}
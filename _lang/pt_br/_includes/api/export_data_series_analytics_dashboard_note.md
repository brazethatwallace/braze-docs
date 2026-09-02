{% comment %}
  Moved into the includes/api subfolder; previously, this wasn't in a subfolder.
  Note for GET export campaign/canvas/send data_series analytics endpoints.
  Use with multi_lang_include.

  Parameters:
  - type (required): "campaign", "canvas", or "send" — selects the opening phrase and dashboard analytics label.
{% endcomment %}

{% if include.type == 'send' %}
{% capture counts_subject %}As contagens de `data_series` no nível de envio{% endcapture %}
{% capture dashboard_match %}análise de dados de engajamento no dashboard{% endcapture %}
{% elsif include.type == 'canvas' %}
{% capture counts_subject %}As contagens deste endpoint{% endcapture %}
{% capture dashboard_match %}análise de dados do Canvas no dashboard{% endcapture %}
{% elsif include.type == 'campaign' %}
{% capture counts_subject %}As contagens deste endpoint{% endcapture %}
{% capture dashboard_match %}análise de dados de engajamento no dashboard{% endcapture %}
{% endif %}
{% alert note %}
{{ counts_subject }} nem sempre correspondem exatamente à {{ dashboard_match }} ou aos agregados que você cria a partir do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/). As métricas do dashboard e as séries temporais da API usam janelas de agregação e definições diferentes dos eventos brutos do Currents. Para notas comuns de reconciliação, consulte as [Perguntas frequentes sobre o Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq/).
{% endalert %}
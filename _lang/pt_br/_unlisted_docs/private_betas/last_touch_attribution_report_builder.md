---
nav_title: "Atribuição de último ponto de contato"
permalink: /last-touch_attribution_metrics/
hidden: true
---

# Métricas de atribuição de último ponto de contato {#last-touch-attribution-metrics}

> Adicione métricas de atribuição de último ponto de contato aos seus relatórios no Criador de relatórios.

{% alert note %}
As métricas de atribuição de último ponto de contato estão em acesso antecipado. Se você tiver interesse em participar do acesso antecipado, entre em contato com seu CSM.
{% endalert %}

A atribuição de último ponto de contato (LTA) é um modelo de atribuição de conversão que dá crédito total por uma conversão à última mensagem com a qual o usuário interagiu antes de converter. Diferentemente das janelas de conversão no nível de Campaign, a LTA usa janelas de atribuição padrão do setor para cada canal:

| Canal | Janela de atribuição |
| --- | --- |
| E-mail | 30 dias |
| SMS | 7 dias |
| WhatsApp | 7 dias |
| Push | 7 dias |
| Mensagem no app | 3 dias |
| Content Cards | 3 dias |
| Webhook | excluído deste modelo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Se uma conversão ocorrer fora da janela de atribuição de um canal, ela não será contabilizada neste modelo.
{% endalert %}

## Benefícios {#benefits}

A atribuição de último ponto de contato oferece vantagens importantes em relação ao rastreamento de conversão padrão:

* Ela permite atribuir conversões a pontos de contato específicos, possibilitando entender quais canais (não apenas Campaigns ou Canvas) estão gerando resultados.
* O crédito é dado exclusivamente à última mensagem tocada, então cada conversão é contada apenas uma vez, eliminando conversões sobrepostas entre Campaigns ou Canvas com eventos de conversão e públicos compartilhados.

## Adicionar métricas de atribuição de último ponto de contato ao seu relatório {#add-last-touch-attribution-metrics-to-your-report}

1. Acesse o **Report Builder**, em **Analytics**.
2. Selecione **Create report** > **Create custom report**.
3. No menu suspenso **Rows**, selecione sobre o que você deseja criar um relatório.
4. (Opcional) Selecione **Add drilldown** e escolha uma área para aprofundar seus relatórios.
5. Em **Columns**, selecione **Customize metrics**
6. Em **Conversions**, selecione **Last Touch Attribution** e depois selecione **Select All**.

{% alert note %}
As métricas de receita e compra não estão disponíveis.
{% endalert %}

![O painel Customize metrics com métricas de atribuição de último ponto de contato.]({% image_buster /assets/unlisted_docs/img/report_builder_2/lta_report_builder.png %})

{: start="7" }
7. Siga as etapas 7 a 9 na página do [Report Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

{% alert note %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="last-touch attribution metrics in Report Builder" %}
{% endalert %}
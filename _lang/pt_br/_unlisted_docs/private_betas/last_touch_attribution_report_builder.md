---
nav_title: "Atribuição de último ponto de contato"
permalink: /last-touch_attribution_metrics/
hidden: true
---

# Métricas de atribuição de último ponto de contato {#last-touch-attribution-metrics}

> Adicione métricas de atribuição de último ponto de contato aos seus relatórios no Criador de relatórios.

{% alert note %}
As métricas de atribuição de último ponto de contato estão em acesso antecipado. Se você tiver interesse em participar do acesso antecipado, entre em contato com seu gerente de sucesso do cliente.
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

* Permite atribuir conversões a pontos de contato específicos, possibilitando entender quais canais (não apenas Campaigns ou Canvas) estão gerando resultados.
* O crédito é dado exclusivamente à última mensagem tocada, então cada conversão é contabilizada apenas uma vez, eliminando conversões sobrepostas entre Campaigns ou Canvas com eventos de conversão e públicos compartilhados.

## Adicionar métricas de atribuição de último ponto de contato ao seu relatório {#add-last-touch-attribution-metrics-to-your-report}

1. Acesse o **Criador de relatórios**, em **Analytics**.
2. Selecione **Criar relatório** > **Criar relatório personalizado**.
3. No menu suspenso **Linhas**, selecione sobre o que você deseja criar um relatório.
4. (Opcional) Selecione **Adicionar detalhamento** e escolha uma área para aprofundar sua análise.
5. Em **Colunas**, selecione **Personalizar métricas**.
6. Em **Conversões**, selecione **Atribuição de último ponto de contato** e depois selecione **Selecionar tudo**.

{% alert note %}
Métricas de receita e compra não estão disponíveis.
{% endalert %}

![O painel Personalizar métricas com métricas de atribuição de último ponto de contato.]({% image_buster /assets/unlisted_docs/img/report_builder_2/lta_report_builder.png %})

{: start="7" }
7. Siga as etapas 7 a 9 na página do [Criador de relatórios](https://www.braze.com/docs/user_guide/analytics/reporting/report_builder).

{% alert note %}
Envie feedback ao seu gerente de sucesso do cliente ou forneça-o após selecionar o botão **Enviar feedback**.
{% endalert %}
---
nav_title: Comportamento do cliente e eventos do usuário
article_title: Comportamento do cliente e eventos do usuário
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glossário lista os vários eventos de comportamento do cliente e do usuário que a Braze pode rastrear e enviar para os data warehouses escolhidos usando o Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details Escopo do esquema e recursos relacionados %}

Os esquemas de armazenamento se aplicam aos dados de eventos de arquivo simples que enviamos aos parceiros de armazenamento de data warehouse (Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage). Algumas combinações de eventos e destinos listadas aqui ainda não estão disponíveis para todos. Para saber quais eventos são compatíveis com cada parceiro, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) e verifique suas respectivas páginas.

{% alert tip %}
Esses eventos também estão disponíveis como tabelas SQL no [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), nas [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) e no [Compartilhamento de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Para esquemas de tabelas SQL e detalhes das colunas, consulte a [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Fale com seu representante da Braze ou abra um [ticket de suporte]({{site.baseurl}}/braze_support/) se precisar de acesso a direitos de eventos adicionais. Se não encontrar o que precisa nesta página, consulte nossa [Biblioteca de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) ou nossos [exemplos de dados de amostra do Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explicação da estrutura de comportamento do cliente e eventos do usuário e valores de plataforma %}

### Estrutura do evento {#event-structure}

Este detalhamento do comportamento do cliente e dos eventos do usuário mostra que tipo de informação é geralmente incluído em um evento de comportamento do cliente ou do usuário. Com uma compreensão sólida de seus componentes, seus desenvolvedores e a equipe de estratégia de business intelligence podem usar os dados de eventos recebidos do Currents para criar relatórios e gráficos orientados por dados e aproveitar outras métricas de dados valiosas.

![Detalhamento de um evento do usuário mostrando um evento de compra com as propriedades listadas agrupadas por propriedades específicas do usuário, propriedades específicas do comportamento e propriedades específicas do dispositivo]({% image_buster /assets/img/customer_engagement_event.png %})

O comportamento do cliente e os eventos do usuário são compostos por propriedades **específicas do usuário**, propriedades **específicas do comportamento** e propriedades **específicas do dispositivo**.

### Valores de plataforma {#platform-values}

Certos eventos retornam um valor `platform` que especifica a plataforma do dispositivo do usuário.
<br>A tabela a seguir detalha os possíveis valores retornados:

| Dispositivo do usuário | Valor da plataforma |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Platform values" }

{% enddetails %}

{% details Considerações sobre comportamento do cliente e eventos do usuário %}

- O Currents descarta eventos com cargas úteis excessivamente grandes, superiores a 900&nbsp;KB.
- Muitos dos eventos neste glossário são iniciados pelo SDK. Alguns eventos, como `token_state_change`, podem ser iniciados pelo SDK ou pelo backend (por exemplo, em resposta a um bounce de push). Os campos `sdk_version`, `gender`, `language` e `country` são definidos apenas para eventos iniciados pelo SDK. Para eventos iniciados pelo backend, ou quando essas informações não estão disponíveis ou não foram definidas para o usuário, esses campos podem ser `null`.

{% enddetails %}

</div>

<!--overview-end-->
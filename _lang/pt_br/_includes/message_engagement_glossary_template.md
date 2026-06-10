---
nav_title: Eventos de engajamento com mensagem
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Este glossário lista os vários eventos de engajamento com mensagem que a Braze pode rastrear e enviar para data warehouses escolhidos usando o Currents."
tool: Currents
search_rank: 6
lazy_partner_tabs: true
---

<div class="api-glossary-preamble" markdown="1">

{% details Escopo do esquema e recursos relacionados %}

Os esquemas de armazenamento se aplicam aos dados de eventos de arquivo simples que enviamos aos parceiros de armazenamento de data warehouse (Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage). Para esquemas que se aplicam a outros parceiros, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) e verifique suas respectivas páginas.

{% alert tip %}
Esses eventos também estão disponíveis como tabelas SQL no [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/), nas [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/) e no [Compartilhamento de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Para esquemas de tabelas SQL e detalhes das colunas, consulte a [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Fale com o gerente da sua conta ou abra um [ticket de suporte]({{site.baseurl}}/braze_support/) se precisar de acesso a direitos de eventos adicionais. Se não encontrar o que precisa neste artigo, consulte nossa [Biblioteca de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) ou nossos [exemplos de dados de amostra do Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explicação da estrutura de eventos de engajamento com mensagem e valores de plataforma %}

### Estrutura do evento {#event-structure}

Este detalhamento do evento mostra que tipo de informação geralmente é incluído em um evento de engajamento com mensagem. Com uma compreensão sólida de seus componentes, seus desenvolvedores e a equipe de estratégia de business intelligence podem usar os dados de eventos recebidos do Currents para criar relatórios e gráficos orientados por dados, além de aproveitar outras métricas valiosas.

![Detalhamento de um evento de engajamento com mensagem mostrando um evento de cancelamento de inscrição de e-mail com as propriedades listadas agrupadas por propriedades específicas do usuário, propriedades de rastreamento de Campaign ou Canvas e propriedades específicas do evento]({% image_buster /assets/img/message_engagement_event.png %})

Os eventos de engajamento com mensagem são compostos por propriedades **específicas do usuário**, propriedades de **rastreamento de Campaign/Canvas** e propriedades **específicas do evento**.

### Esquema de ID do usuário {#user-id-schema}

Observe as convenções de nomenclatura para IDs de usuário.

| Esquema da Braze | Esquema do Currents | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | O identificador exclusivo atribuído automaticamente pela Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | O identificador exclusivo do perfil de um usuário, definido pelo cliente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="User ID schema" }

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

{% details Considerações sobre eventos de engajamento com mensagem %}

- O Currents descarta eventos com cargas úteis superiores a 900&nbsp;KB.
- Os objetos relacionados ao Canvas Flow têm IDs que podem ser usados para agrupamento e traduzidos em nomes legíveis por meio do [endpoint Exportar detalhes do Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/).
- Alguns campos podem não exibir seu estado mais recente imediatamente após a atualização de uma Campaign ou Canvas:
  - `campaign_name`
  - `canvas_name`
  - `canvas_step_name`
  - `conversion_behavior`
  - `canvas_variation_name`
  - `experiment_split_name`
  - `message_variation_name`
- Se for necessária consistência completa para esses campos, aguarde uma hora após a última atualização antes de enviar as mensagens aos seus usuários.

{% enddetails %}

</div>

<!--overview-end-->
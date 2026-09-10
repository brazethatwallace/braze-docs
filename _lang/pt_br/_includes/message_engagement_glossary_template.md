---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: Eventos de engajamento com mensagem
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Este glossário lista os diversos eventos de engajamento com mensagem que a Braze pode rastrear e enviar para data warehouses escolhidos usando o Currents."
tool: Currents
search_rank: 6
lazy_partner_tabs: true
---

<div class="api-glossary-preamble" markdown="1">

{% details Escopo do esquema e recursos relacionados %}

Os esquemas de armazenamento se aplicam aos dados de eventos em arquivo simples que enviamos para parceiros de armazenamento em data warehouse (Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage). Para esquemas que se aplicam a outros parceiros, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) e verifique suas respectivas páginas.

{% alert tip %}
Esses eventos também estão disponíveis como tabelas SQL no [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), nas [extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) e no [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Para esquemas de tabelas SQL e detalhes de colunas, consulte a [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).
{% endalert %}

Entre em contato com seu gerente de conta ou abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) se precisar de acesso a direitos de eventos adicionais. Se você não encontrar o que precisa neste artigo, confira nossa [Biblioteca de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) ou nossos [exemplos de dados de amostra do Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explicação da estrutura de eventos de engajamento com mensagem e valores de plataforma %}

## Estrutura do evento {#event-structure}

Este detalhamento de eventos mostra que tipo de informação geralmente está incluída em um evento de engajamento com mensagem. Com uma compreensão sólida de seus componentes, seus desenvolvedores e a equipe de estratégia de business intelligence podem usar os dados de eventos recebidos do Currents para criar relatórios e gráficos orientados por dados, além de aproveitar outras métricas de dados valiosas.

![Detalhamento de um evento de engajamento com mensagem mostrando um evento de cancelamento de inscrição de e-mail com as propriedades listadas agrupadas por propriedades específicas do usuário, propriedades de rastreamento de Campaign ou Canvas e propriedades específicas do evento]({% image_buster /assets/img/message_engagement_event.png %}){: width="2300" height="770" style="max-width:100%;height:auto;"}

Os eventos de engajamento com mensagem são compostos por propriedades **específicas do usuário**, propriedades de **rastreamento de Campaign/Canvas** e propriedades **específicas do evento**.

### Esquema de ID do usuário {#user-id-schema}

Observe as convenções de nomenclatura para IDs de usuário.

| Esquema Braze | Esquema Currents | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | O identificador único que é atribuído automaticamente pela Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | O identificador único do perfil de um usuário que é definido pelo cliente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de ID do usuário" }

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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Valores de plataforma" }

{% enddetails %}

{% details Considerações para eventos de engajamento com mensagem %}

- O Currents descarta eventos com cargas úteis maiores que 900&nbsp;KB.
- Objetos relacionados ao Canvas Flow possuem IDs que você pode usar para agrupamento e traduzir para nomes legíveis por meio do [endpoint Exportar detalhes do Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details).
- Certos campos podem não mostrar seu estado mais recente imediatamente após você atualizar uma Campaign ou Canvas:
  - `campaign_name`
  - `canvas_name`
  - `canvas_step_name`
  - `conversion_behavior`
  - `canvas_variation_name`
  - `experiment_split_name`
  - `message_variation_name`
- Se você precisar de consistência completa para esses campos, aguarde uma hora após a última atualização antes de enviar mensagens aos seus usuários.

{% enddetails %}

</div>

<!--overview-end-->
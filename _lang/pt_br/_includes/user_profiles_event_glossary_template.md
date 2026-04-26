---
nav_title: Perfis de usuário
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glossário lista as atualizações de perfil de usuário que a Braze pode rastrear e enviar para data warehouses escolhidos usando o Currents."
tool: Currents
search_rank: 7
---

{% alert tip %}
Esses eventos também estão disponíveis como tabelas SQL no [Criador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/), nas [Extensões de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) e no [Compartilhamento de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Para esquemas de tabelas SQL e detalhes das colunas, consulte a [referência de tabelas SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Fale com o representante da Braze ou abra um [tíquete de suporte]({{site.baseurl}}/braze_support/) se precisar de acesso a direitos de eventos adicionais. Se não encontrar o que precisa nesta página, consulte a [Biblioteca de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/), a [Biblioteca de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) ou os [exemplos de dados de amostra do Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explicação da estrutura do evento de atualização de perfil de usuário %}

### Estrutura do evento {#event-structure}

Este detalhamento de comportamento do cliente e eventos de usuário mostra que tipo de informação geralmente está incluído em um evento de atualização de perfil de usuário. Com uma compreensão sólida de seus componentes, seus desenvolvedores e a equipe de estratégia de business intelligence podem usar os dados de eventos recebidos do Currents para criar relatórios e gráficos orientados por dados, além de aproveitar outras métricas de dados valiosas.

{% alert important %}
Os esquemas de armazenamento se aplicam a dados de eventos em arquivo simples enviados para parceiros de armazenamento em data warehouse, como Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage. Algumas combinações de eventos e destinos listadas aqui ainda não estão disponíveis de forma geral. Para informações sobre eventos compatíveis por parceiro, consulte os [parceiros disponíveis]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) e as páginas relacionadas dos parceiros.

O Currents descarta eventos com cargas úteis maiores que 900 KB.
{% endalert %}
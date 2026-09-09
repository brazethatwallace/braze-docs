---
nav_title: "Relatórios"
article_title: "Relatórios"
page_order: 21
description: "Este artigo de referência aborda as métricas de SMS, MMS e RCS usadas na Braze, bem como como visualizá-las nas suas campanhas de SMS, MMS e RCS."
alias: /sms_mms_rcs_reporting/
page_type: reference
tool:
  - Reports
channel:
  - SMS
  - MMS
  - RCS



---

# Relatórios de SMS, MMS e RCS {#reporting-for-sms-mms-and-rcs}

> Este artigo de referência aborda as métricas de SMS, MMS e RCS usadas na Braze, bem como como visualizá-las nas suas campanhas de SMS, MMS e RCS.

{% multi_lang_include analytics/campaign_analytics.md channel="SMS" %}

{% alert note %}
As métricas de cliques do dashboard, como *Total de cliques*, excluem atividades suspeitas de bots, mas o Currents ainda exporta todos os eventos de clique com `is_suspected_bot_click` e `suspected_bot_click_reason` para reconciliação no data warehouse. Para métricas afetadas no dashboard, segmentação e orquestração, consulte [Filtragem de cliques de bots para links de SMS/RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering).
{% endalert %}

## Rastrear aceitações e cancelamentos de inscrição de SMS {#track-sms-opt-ins-and-opt-outs}

Você pode rastrear aceitações e cancelamentos de inscrição de SMS com os seguintes métodos:

| Método | Descrição |
|--------|-----------|
| Segmentador | O segmentador exibe o número de usuários em um [grupo de inscrições]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group) específico. Ele não faz deduplicação por número de telefone — se vários usuários compartilharem o mesmo número de telefone, cada instância é contada separadamente. |
| Série temporal do grupo de inscrições | Fornece um snapshot diário de inscrições para e-mails e números de telefone. A série temporal conta inscrições, cancelamentos de inscrição e reinscrições. Por exemplo, se um usuário se inscrever, cancelar a inscrição e depois se reinscrever, ele é contado como um usuário inscrito. |
| Currents | Use o Currents para exportar [eventos de inscrição e engajamento]({{site.baseurl}}/message_events_glossary) para seus próprios relatórios. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rastrear aceitações e cancelamentos de inscrição de SMS" }

{% alert note %}
As estatísticas de _Aceitação_ e _Cancelamento de inscrição_ no painel **SMS/MMS/RCS Performance** refletem usuários que aceitaram ou cancelaram a inscrição por meio de palavras-chave de entrada (por exemplo, enviando "START" para aceitar ou "STOP" para cancelar). Esses números são geralmente menores do que os exibidos no segmentador, pois contam o número de vezes que essas palavras-chave foram enviadas por mensagem de texto, não o número total de usuários inscritos em SMS.
{% endalert %}

### Rastrear cancelamentos de inscrição de SMS em Campaigns {#track-sms-campaign-opt-outs}

Rastreie cancelamentos de inscrição de SMS no nível da campanha usando a tabela de recebimento de entrada em vez da tabela de mudança de estado do grupo de inscrições. Por exemplo, no [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) ou no seu data warehouse, você pode executar uma consulta que referencia a tabela `USERS_MESSAGES_SMS_INBOUNDRECEIVE` ou [`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED).

Este exemplo de consulta referencia a tabela `USERS_MESSAGES_SMS_INBOUNDRECEIVE`:

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

Isso retorna os usuários que cancelaram a inscrição de comunicações por SMS para o espaço de trabalho e grupo de inscrições fornecidos, filtrados apenas para aqueles associados a Campaigns ou Canvas.

### Momento do cancelamento de inscrição {#opt-out-timing}

Eventos de palavras-chave e mensagens de entrada no Currents ou no seu data warehouse, como timestamps em [`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) ou eventos de mudança de estado do grupo de inscrições, são a fonte oficial de quando a Braze registrou o cancelamento de inscrição.

{% alert note %}
Os timestamps dos eventos refletem quando a Braze recebeu ou processou a mensagem de entrada, não necessariamente quando o usuário enviou o SMS ou quando uma operadora ou provedor de SMS o recebeu. Se a sua análise trata cancelamentos de inscrição como o momento em que a Braze processou a jornada de cancelamento de inscrição de entrada, esses timestamps correspondem a essa definição.
{% endalert %}

O perfil de usuário exibe o estado atual da inscrição, mas pode não apresentar um único campo "SMS cancelou inscrição em" a menos que você defina um [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) ou similar ao processar cancelamentos de inscrição.

## Cobranças aplicadas aos resultados de envio de SMS {#charges-applied-to-sms-sending-outcomes}

Esta tabela reflete a cobrança da Braze, não a do seu provedor. Resultados que não são cobrados pela Braze podem ser cobrados pelo seu provedor.

| Resultado | Definição | Cobrado pela Braze |
|--------|------------|--------|
| Enviado | Uma Campaign ou etapa do Canvas foi lançada ou disparada, e uma carga útil de SMS foi enviada ao provedor de SMS. | Sem cobrança |
| Falha na entrega | A carga útil de SMS não pôde ser enviada ao provedor de SMS. Isso pode ocorrer devido a filas sobrecarregadas, contas suspensas ou erros de mídia (no caso de MMS). | Sem cobrança |
| Entregue | O provedor de SMS recebeu confirmação de entrega da mensagem pela operadora upstream (e, quando disponível, pelo dispositivo de destino). | Cobrança |
| Rejeitado | O provedor de SMS recebeu um recibo de rejeição indicando que a mensagem não foi entregue. Isso pode acontecer por vários motivos, incluindo filtragem de conteúdo pela operadora ou disponibilidade do dispositivo de destino. | Cobrança |
| **Sends to Carrier** | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} Descontinuado para novos dashboards. Alguns dashboards ainda podem exibir essa métrica como **Sent to Carrier**. | Cobranças podem ser aplicadas com base nos resultados individuais de envio de mensagens |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cobranças aplicadas aos resultados de envio de SMS" }

{% alert note %}
**Sends to Carrier** foi descontinuado para novos dashboards. Use **Sent**, **Confirmed Delivery**, **Delivery Failed** e **Rejections** para relatórios atuais. Consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary) para definições.
{% endalert %}

## Relatórios de mensagens RCS Card {#rcs-card-message-reporting}

Para mensagens RCS Card, o *Total de cliques* na análise de dados de Campaign e Canvas inclui toques em botões do cartão (como **Message reply** e **Open URL**) e interações de sugestão. A métrica pode ser incrementada mais de uma vez se um usuário tocar no mesmo controle várias vezes.

Os cliques em botões e sugestões do cartão não são rastreados por meio do [encurtamento de links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) nem pelas configurações avançadas de rastreamento para URLs encurtadas. Os filtros de [redirecionamento de usuários]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links) que fazem referência a links de SMS encurtados não se aplicam às interações com botões do cartão.

Para dados de interação no nível do usuário, exporte os [eventos de clique RCS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#rcs-click-events) (`users.messages.rcs.Click`) por meio do Currents. Esses eventos incluem campos como `interaction_type` e `element_type` para distinguir toques em botões de sugestões.

## Relatórios de RCS e fallback de SMS {#rcs-and-sms-fallback-reporting}

Para o comportamento de eventos de fallback de SMS do RCS (incluindo `IS_SMS_FALLBACK=TRUE`), consulte [Como o fallback de SMS funciona com eventos e segmentação]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup#how-sms-fallback-works-with-events-and-segmentation).

{% alert note %}
A análise de dados de Campaigns no dashboard e as exportações do Snowflake podem diferir ligeiramente em relação ao tempo e à agregação. Para reconciliação no data warehouse, trate os fluxos de eventos do Snowflake ou do Currents como a fonte mais granular quando as métricas não corresponderem exatamente ao dashboard.
{% endalert %}

## Reconciliar *Rejeições* com o Snowflake ou Currents {#reconcile-rejections-with-snowflake-or-currents}

A métrica *Rejeições* no dashboard é uma contagem agregada do espaço de trabalho. Ela não é uma exportação em nível de linha, então nem sempre é possível associar cada rejeição a uma única linha no Snowflake ou a um único evento `users.messages.sms.Rejection` no Currents. Por exemplo, se o perfil de usuário foi excluído antes de a Braze concluir o processamento da rejeição para exportação ao data warehouse, essa rejeição não aparece na sua tabela `USERS_MESSAGES_SMS_REJECTION_SHARED` nem na carga útil do Currents, embora os relatórios agregados de SMS ainda possam refletir o resultado. Para saber mais, consulte a [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles) e os [eventos de rejeição de SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) no glossário de eventos do Currents.
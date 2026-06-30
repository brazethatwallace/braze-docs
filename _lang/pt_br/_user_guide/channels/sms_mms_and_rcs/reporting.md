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

## Rastrear opt-ins e descadastramentos de SMS {#track-sms-opt-ins-and-opt-outs}

Você pode rastrear opt-ins e descadastramentos de SMS com os seguintes métodos:

| Método | Descrição |
|--------|-------------|
| Segmentador | O segmentador exibe o número de usuários em um [grupo de inscrições]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group) específico. Ele não faz deduplicação por número de telefone — se vários usuários compartilham o mesmo número de telefone, cada instância é contada separadamente. |
| Série temporal do grupo de inscrições | Fornece um snapshot diário das inscrições para e-mail e números de telefone. A série temporal conta inscrições, cancelamentos de inscrição e reinscrições. Por exemplo, se um usuário se inscreve, cancela a inscrição e depois se reinscreve, ele é contado como um usuário inscrito. |
| Currents | Use o Currents para exportar [eventos de inscrição e engajamento]({{site.baseurl}}/message_events_glossary) para seus próprios relatórios. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rastrear opt-ins e descadastramentos de SMS" }

{% alert note %}
As estatísticas de _Opt-In_ e _Descadastramento_ no painel **Desempenho de SMS/MMS/RCS** refletem os usuários que fizeram opt-in ou descadastramento por meio de palavras-chave de entrada (por exemplo, enviando "START" para opt-in ou "STOP" para descadastramento). Esses números são geralmente menores do que o exibido no segmentador, pois contam o número de vezes que essas palavras-chave foram enviadas, e não o número total de usuários inscritos em SMS.
{% endalert %}

### Rastrear descadastramentos de SMS em Campaigns {#track-sms-campaign-opt-outs}

Rastreie descadastramentos de SMS no nível da campanha usando a tabela de recebimento de entrada em vez da tabela de mudança de estado do grupo de inscrições. Por exemplo, no [Criador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder) ou no seu data warehouse, você pode executar uma consulta que referencia a tabela `USERS_MESSAGES_SMS_INBOUNDRECEIVE` ou [`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED).

Este exemplo de consulta referencia a tabela `USERS_MESSAGES_SMS_INBOUNDRECEIVE`:

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

Isso retorna os usuários que cancelaram a inscrição de comunicações por SMS para o espaço de trabalho e grupo de inscrições especificados, filtrados para aqueles associados a Campaigns ou Canvas.

### Momento do descadastramento {#opt-out-timing}

Eventos de palavras-chave e mensagens de entrada no Currents ou no seu data warehouse, como timestamps em [`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) ou eventos de mudança de estado do grupo de inscrições, são a fonte oficial de quando a Braze registrou o descadastramento.

{% alert note %}
Os timestamps dos eventos refletem quando a Braze recebeu ou processou a mensagem de entrada, não necessariamente quando o usuário enviou o SMS ou quando a operadora ou o provedor de SMS o recebeu. Se a sua análise trata os descadastramentos como o momento em que a Braze processou a jornada de descadastramento de entrada, esses timestamps correspondem a essa definição.
{% endalert %}

O perfil de usuário mostra o estado atual da inscrição, mas pode não exibir um campo único de "SMS cancelado em", a menos que você defina um [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes) ou similar ao processar descadastramentos.

## Cobranças aplicadas aos resultados de envio de SMS {#charges-applied-to-sms-sending-outcomes}

Esta tabela reflete a cobrança da Braze, não a cobrança do seu provedor. Resultados que não são cobrados pela Braze podem ser cobrados pelo seu provedor.

| Resultado | Definição | Cobrado pela Braze |
|--------|------------|--------|
| Enviado | Uma Campaign ou etapa do Canvas foi lançada ou disparada, e uma carga útil de SMS foi enviada ao provedor de SMS. | Sem cobrança |
| Falha na entrega | A carga útil de SMS não pôde ser enviada ao provedor de SMS. Isso pode ocorrer devido a filas sobrecarregadas, contas suspensas ou erros de mídia (no caso de MMS). | Sem cobrança |
| Entregue | O provedor de SMS recebeu confirmação de entrega da mensagem pela operadora upstream (e, quando disponível, pelo dispositivo de destino). | Cobrança |
| Rejeitado | O provedor de SMS recebeu um recibo de rejeição indicando que a mensagem não foi entregue. Isso pode acontecer por vários motivos, incluindo filtragem de conteúdo pela operadora ou indisponibilidade do dispositivo de destino. | Cobrança |
| Enviado à operadora | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} | Cobranças podem ser aplicadas com base nos resultados individuais de envio de mensagens |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cobranças aplicadas aos resultados de envio de SMS" }

## Conciliar *Rejeições* com Snowflake ou Currents {#reconcile-rejections-with-snowflake-or-currents}

A métrica de *Rejeições* no dashboard é uma contagem agregada do espaço de trabalho. Ela não é uma exportação em nível de linha, então nem sempre é possível associar cada rejeição a uma única linha no Snowflake ou a um único evento `users.messages.sms.Rejection` no Currents. Por exemplo, se o perfil de usuário foi excluído antes de a Braze concluir o processamento da rejeição para exportação ao data warehouse, essa rejeição não aparece na tabela `USERS_MESSAGES_SMS_REJECTION_SHARED` nem na carga útil do Currents, enquanto os relatórios agregados de SMS ainda podem refletir o resultado. Para saber mais, consulte a [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles) e os [eventos de rejeição de SMS]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) no glossário de eventos do Currents.
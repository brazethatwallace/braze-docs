---
nav_title: ID de despacho
article_title: Comportamento da ID de despacho
page_order: 5.2
page_type: reference
description: "Este artigo de referência descreve o comportamento da ID de despacho para Campaigns, Canvas, Liquid e Currents."
---

# Comportamento da ID de despacho {#dispatch-id-behavior}

> O `dispatch_id` é uma ID única para cada despacho de mensagem, ou "transmissão", enviada pela Braze.

## Comportamento da ID de despacho em Campaigns {#dispatch-id-behavior-in-campaigns}

Mensagens de Campaigns agendadas recebem o mesmo `dispatch_id`. Mensagens de Campaigns baseadas em ação ou disparadas por API podem receber um `dispatch_id` exclusivo por usuário, ou o `dispatch_id` pode ser o mesmo para vários usuários quando enviadas em proximidade temporal ou na mesma chamada de API. Por exemplo, dois usuários no público da sua Campaign agendada terão o mesmo `dispatch_id` cada vez que a Campaign for agendada. No entanto, dois usuários no público de uma Campaign disparada por API podem ter IDs de despacho diferentes se as Campaigns tiverem sido enviadas em chamadas de API separadas e não em proximidade temporal.

Campaigns multicanal têm o mesmo comportamento para seu tipo de entrega.

{% alert warning %}
Um `dispatch_id` é gerado aleatoriamente para todas as etapas do Canvas porque a Braze trata as etapas do Canvas como eventos disparados, mesmo quando são "agendadas". Isso pode resultar em inconsistências na geração das IDs. Às vezes, um componente do Canvas tem um `dispatch_id` único por usuário por envio, ou pode ter IDs de despacho compartilhadas entre usuários por envio.
{% endalert %}

## Inserir a ID de despacho em mensagens com Liquid {#template-dispatch-id-into-messages-with-liquid}

Se você quiser rastrear o despacho de uma mensagem de dentro da própria mensagem (em uma URL, por exemplo), pode inserir o `dispatch_id` usando template. Você pode encontrar a formatação para isso em Atributos do Canvas na lista de [tags de personalização compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

O comportamento é semelhante ao do `api_id`: como o `api_id` não está disponível na criação da Campaign, a Braze o insere como um placeholder que é pré-visualizado como `dispatch_id_for_unsent_campaign`. A ID é gerada antes do envio da mensagem e é incluída no momento do envio.

{% alert warning %}
O template Liquid de `dispatch_id_for_unsent_campaign` não funciona com mensagens no app, pois mensagens no app não possuem um `dispatch_id`.
{% endalert %}

## Campo de ID de despacho no Currents para e-mail {#dispatch-id-currents-field-for-email}

O campo `dispatch_id` está disponível nos eventos de e-mail do Currents em todos os tipos de conector. O `dispatch_id` é a ID única gerada para cada transmissão, ou despacho, enviada pela plataforma Braze.

Embora todos os clientes que recebem uma mensagem agendada tenham o mesmo `dispatch_id`, clientes que recebem mensagens baseadas em ação ou disparadas por API recebem um `dispatch_id` único por mensagem. O campo `dispatch_id` permite identificar qual instância de uma Campaign recorrente é responsável pela conversão, para que você possa ver quais tipos de Campaigns geram resultados.

Você pode usar o `dispatch_id` como uma [tag de personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), em [eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), ou ao usar [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents#email-events) ou [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents) para Currents.
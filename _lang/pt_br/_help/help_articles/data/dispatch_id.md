---
nav_title: Comportamento da ID de despacho
article_title: Comportamento da ID de despacho
page_order: 0

page_type: solution
description: "Este artigo de ajuda aborda o comportamento da ID de despacho, incluindo seu uso, implicações e limitações."
---

# Comportamento da ID de despacho {#dispatch-id-behavior}

Um `dispatch_id` é a ID do envio da mensagem — uma ID única para cada "transmissão" enviada pela Braze. Os usuários que recebem uma mensagem agendada recebem o mesmo `dispatch_id`. Normalmente, mensagens baseadas em ações ou disparadas por API receberão um `dispatch_id` único por usuário, mas mensagens enviadas em proximidade temporal com outra podem compartilhar o mesmo `dispatch_id` entre vários usuários.

Isso pode resultar em dois usuários diferentes tendo IDs de despacho diferentes para uma única Campaign, caso as mensagens tenham sido enviadas em dois momentos diferentes. Isso costuma acontecer porque as solicitações da API foram feitas separadamente. Se ambos os usuários estivessem no mesmo público da Campaign em um único envio, seus IDs de despacho seriam os mesmos.

## Comportamento da ID de despacho em Campaigns {#dispatch-id-behavior-in-campaigns}

Mensagens de Campaigns agendadas recebem o mesmo `dispatch_id`. Mensagens de Campaigns baseadas em ação ou disparadas por API podem receber um `dispatch_id` exclusivo por usuário, ou o `dispatch_id` pode ser o mesmo para vários usuários quando enviadas em proximidade ou na mesma chamada de API, conforme descrito acima. Por exemplo, dois usuários no público da sua Campaign agendada terão o mesmo `dispatch_id` cada vez que a Campaign for agendada. No entanto, dois usuários no público de uma Campaign disparada por API podem ter IDs de despacho diferentes se foram enviados em chamadas de API separadas e não em proximidade um do outro.

Campaigns multicanal terão o mesmo comportamento descrito para o seu tipo de entrega.

{% alert warning %}
Um `dispatch_id` é gerado aleatoriamente para todas as etapas do Canvas porque a Braze trata as etapas do Canvas como eventos disparados, mesmo quando estão "agendadas". Isso pode resultar em inconsistências na geração dos IDs. Às vezes, um componente do Canvas terá um `dispatch_id` exclusivo por usuário por envio, ou poderá ter IDs de despacho compartilhados entre usuários por envio.
{% endalert %}

## Usar o template da ID de despacho em mensagens com Liquid {#template-dispatch-id-into-messages-with-liquid}

Se você quiser rastrear o envio de uma mensagem de dentro da própria mensagem (em uma URL, por exemplo), pode usar o template do `dispatch_id`. Você pode encontrar a formatação para isso em Atributos do Canvas na nossa lista de [tags de personalização compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

Isso se comporta exatamente como o `api_id`: como o `api_id` não está disponível na criação da Campaign, ele é inserido como um espaço reservado e será exibido como `dispatch_id_for_unsent_campaign`. A ID é gerada antes que a mensagem seja enviada e será incluída no momento do envio.

{% alert warning %}
O template Liquid de `dispatch_id_for_unsent_campaign` não funciona com mensagens no app, pois as mensagens no app não possuem um `dispatch_id`.
{% endalert %}

## Campo de ID de despacho do Currents para e-mail {#dispatch-id-currents-field-for-email}

Para continuar aprimorando nossos recursos do Currents, `dispatch_id` também é um campo nos eventos de e-mail do Currents em todos os tipos de conector. O `dispatch_id` é a ID única gerada para cada transmissão, ou despacho, enviado da plataforma Braze.

Embora todos os clientes que recebem uma mensagem agendada recebam o mesmo `dispatch_id`, os clientes que recebem mensagens baseadas em ações ou disparadas por API receberão um `dispatch_id` único por mensagem. O campo `dispatch_id` permite que você identifique qual instância de uma Campaign recorrente é responsável pela conversão, fornecendo assim mais insights e informações sobre quais tipos de Campaigns estão ajudando a impulsionar suas metas comerciais.

Você pode usar `dispatch_id` como uma [tag de personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), em [eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/), ou quando você usa [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events) ou [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/) para Currents.

_Última atualização em 15 de julho de 2021_
---
nav_title: Tipos de entrega e entrada
article_title: Tipos de entrega e entrada
page_order: 5
page_type: reference
description: "Este artigo de referência descreve os tipos de entrega para Campaigns, os tipos de entrada para Canvas e os recursos baseados em tempo ao configurar uma Campaign ou um Canvas."
tool:
    - Campaigns
    - Canvas
---

# Tipos de entrega e entrada {#delivery-and-entry-types}

> Na Braze, existem três formas diferentes de programar sua mensagem: agendada, baseada em ação e disparada por API or interface de programação do aplicativo (API). Escolher como e quando sua mensagem será entregue é fundamental para desenvolver uma mensagem eficaz.

Para Campaigns, o tipo de entrega determina quando seus usuários entrarão na Campaign e quando ela será enviada. Como um Canvas é construído como uma jornada contínua do usuário, o conceito de agendamento de mensagens é chamado de tipo de entrada.

| Tipos de entrega<nobr> e entrada | Descrição |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Agendado** | Esse tipo de agendamento é projetado para mensagens únicas que você deseja enviar imediatamente, como Campaigns sobre um evento atual. <br><br>Ao enviar mensagens de teste destinadas apenas a você ou à sua equipe, essa opção permite entregá-las imediatamente. |
| **Baseada em ação** | Mensagens de entrega baseada em ação, ou Campaigns e Canvas disparados por eventos, são muito eficazes para mensagens transacionais ou baseadas em conquistas. Você pode configurá-las para serem enviadas após o usuário concluir um determinado evento, em vez de enviar sua mensagem em dias específicos. |
| **Disparada por API or interface de programação do aplicativo (API)** | Mensagens disparadas por API or interface de programação do aplicativo (API) permitem que você gerencie o texto da mensagem, testes multivariantes e regras de reelegibilidade no dashboard da Braze, enquanto dispara a entrega desse conteúdo a partir dos seus próprios servidores e sistemas. <br><br>A solicitação de API or interface de programação do aplicativo (API) para disparar a mensagem também pode incluir dados adicionais para serem inseridos na mensagem em tempo real por meio de templates. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de entrega e entrada" }

## Opções baseadas em tempo {#time-based-options}

{% tabs %}
{% tab campaign %}
Você pode escolher entre as seguintes opções ao usar a entrega agendada:

- Enviar assim que a Campaign for lançada
- Enviar em um horário designado
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)
{% endtab %}

{% tab canvas %}
Com a entrega agendada, os usuários entrarão em um cronograma, de forma semelhante a como você agendaria uma Campaign. Você pode inscrever usuários em um Canvas assim que ele for lançado ou em um horário designado.

### Horários designados {#designated-times}

Você pode escolher enviar seu Canvas com uma frequência de entrada específica, incluindo apenas uma vez, diariamente, semanalmente ou mensalmente. Para Canvas com entrega agendada recorrente, você pode definir a recorrência para permitir que os usuários entrem no Canvas em até 30 horários designados.
{% endtab %}
{% endtabs %}

## Opções baseadas em ação {#action-based-options}

{% tabs %}
{% tab campaign %}
A entrega baseada em ação enviará Campaigns para usuários que realizarem uma ação específica. Após essa ação ocorrer, você pode decidir quando enviar a Campaign: imediatamente, após um tempo específico, em um horário específico ou em um momento futuro.
{% endtab %}

{% tab canvas %}
As opções baseadas em ação determinam quais ações (ou gatilhos) um usuário precisa realizar para entrar em um Canvas e em que momento específico ele poderá começar a entrar. Por exemplo, você pode avaliar seus usuários pelas seguintes ações:

- Abrir seu app
- Adicionar um endereço de e-mail
- Entrar em um local

### Período de entrada {#entry-window}

O período de entrada do seu Canvas determina quais usuários podem entrar no Canvas no horário de início designado (e horário de término opcional). De forma semelhante às Campaigns baseadas em ação, você pode optar por inscrever os usuários no fuso horário local deles.
{% endtab %}
{% endtabs %}

## Opções de disparo por API or interface de programação do aplicativo (API) {#api-trigger-options}

{% tabs %}
{% tab campaign %}
Ao selecionar disparada por API or interface de programação do aplicativo (API) como sua opção de entrega, você receberá um ID de Campaign para identificar qual Campaign enviar com o [endpoint `/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#prerequisites).
{% endtab %}

{% tab canvas %}
Ao selecionar disparado por API or interface de programação do aplicativo (API) como seu tipo de entrada, você receberá um ID de Canvas para identificar qual Canvas enviar com o [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endtab %}
{% endtabs %}
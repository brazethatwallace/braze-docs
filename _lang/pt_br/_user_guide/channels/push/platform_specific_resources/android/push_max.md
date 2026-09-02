---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "O Push Max amplifica as notificações por push para Android rastreando notificações por push que falharam e reenviando o push quando o usuário tem mais chances de recebê-lo."

permalink: /user_guide/channels/push/platform_specific_resources/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Saiba mais sobre o Push Max e como você pode usar esse recurso para potencialmente melhorar a entregabilidade das notificações por push para Android em [dispositivos OEM chineses]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability).

## O que é o Push Max? {#what-is-push-max}

O Push Max amplifica as notificações por push para Android rastreando notificações por push que falharam e reenviando o push quando o usuário tem mais chances de recebê-lo.

Alguns dispositivos Android fabricados por fabricantes de equipamentos originais (OEMs) chineses, como Xiaomi, OPPO e Vivo, empregam um esquema robusto de otimização de bateria para prolongar a vida útil da bateria. Esse comportamento pode ter a consequência não intencional de encerrar o processamento de apps em segundo plano, o que reduz a entregabilidade das notificações por push nesses dispositivos se o app não estiver em primeiro plano. Essa circunstância ocorre com mais frequência nos mercados da Ásia-Pacífico (APAC).

## Disponibilidade {#availability}

- Disponível apenas para notificações por push para Android
- Não é compatível com mensagens baseadas em ação ou disparadas por API or interface de programação do aplicativo (API)
- Não é compatível quando a opção de [enviar apenas para o último dispositivo usado pelo usuário]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#most-recently-used-device) está selecionada

## Pré-requisitos {#prerequisites}

As notificações por push enviadas usando o Push Max serão entregues apenas a dispositivos que tenham pelo menos a seguinte [versão mínima do SDK or kit de desenvolvimento de software]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions):

{% sdk_min_versions android:29.0.1 %}

## Usando o Push Max {#using-push-max}

{% tabs %}
{% tab Campaigns %}

Para usar o Push Max na sua Campaign:

1. Crie uma Campaign de push.
2. Selecione **Android Push** como sua plataforma.
3. Acesse a etapa **agendar/cronograma Delivery**.
4. Selecione **Send using Push Max**.

![Seção de entregabilidade de push para Android na etapa agendar/cronograma Delivery com a opção "Send using Push Max".]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

Para usar o Push Max no seu Canvas:

1. Adicione uma etapa de mensagem ao seu Canvas.
2. Selecione **Android Push** como sua plataforma.
3. Acesse a guia **Delivery Settings**.
4. Selecione **Send using Push Max**.

![Guia Delivery Settings de uma etapa de mensagem de push para Android com a opção "Send using Push Max".]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Os dois recursos a seguir, Intelligent Timing e TTL, podem ser usados em conjunto com o Push Max para potencialmente aumentar a entregabilidade das suas notificações por push para Android.

### Intelligent Timing {#intelligent-timing}

O Push Max funciona melhor quando o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) está ativado. O Intelligent Timing pode calcular e enviar a notificação por push no momento em que o usuário tem mais chances de estar usando o app e o push tem mais chances de ser entregue.

### TTL (Time to Live) {#time-to-live-ttl}

O TTL (Time to Live) pode rastrear notificações por push que falharam no Firebase Cloud Messaging (FCM) e tentar novamente a notificação quando o usuário tiver mais chances de recebê-la.

Por padrão, o TTL é definido como 28 dias, que é o máximo. Você pode diminuir o TTL padrão para todas as novas mensagens de push para Android em **Configurações** > **Configurações do espaço de trabalho** > **Configurações de push**, ou pode configurar o número de dias por mensagem na guia **Settings** ao compor uma notificação por push para Android.

![Campo TTL definido como 28 dias.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Informações importantes {#things-to-know}

### Códigos de promoção {#promotion-codes}

Recomendamos que você não use [códigos de promoção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) da Braze em mensagens com o Push Max ativado.

Isso porque os códigos de promoção são únicos. Se uma notificação por push que contém um código de promoção falhar na entrega, quando essa notificação for reenviada pelo Push Max, um novo código de promoção será enviado. Isso pode resultar no consumo de códigos de promoção mais rápido do que o esperado.

### Propriedades de evento e propriedades de entrada do Canvas {#canvas-event-properties-and-entry-properties}

O Push Max pode não funcionar como esperado se você incluir referências Liquid a [propriedades de entrada ou propriedades de evento do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) na sua mensagem. Isso porque as propriedades de entrada e de evento não estão disponíveis quando o Push Max está tentando reenviar a mensagem.
---
nav_title: "Tipos de mensagem"
article_title: Tipos de mensagem push
page_order: 3
page_type: reference
description: "Este artigo de referência lista os diferentes tipos de notificações por push que você pode enviar com a Braze."
channel: push
---

# Tipos de mensagem push {#push-message-types}

> Existem muitos tipos de notificações por push que você pode usar para interagir com seus clientes. A maioria dessas configurações pode ser definida nas suas Campaigns de push, mas algumas exigem configurações de backend, conforme indicado nas descrições.

## Push padrão {#standard-push}

A mensagem push mais abrangente. Ela aparece no dispositivo do usuário com um som de notificação e uma mensagem que desliza ou aparece em uma barra ou pilha de notificações.

**Compatível com:** Web, Android, iOS

Para saber mais, consulte [Criar uma mensagem push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/).

## Push para a web {#web-push}

Essas mensagens push aparecem em apps da web ou navegadores. Elas exigem permissão para alcançar o cliente. O push para a web não funciona se o usuário estiver usando um navegador oculto.

**Compatível com:** Web

Para saber mais, consulte [Notificações por push para a web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/).

## Campaigns de push primer {#push-primer-campaigns}

Campaigns de mensagem no app usadas para obter um sinal explícito de opt-in ou descadastramento de push dos usuários. Por meio do primer, você pode evitar o envio de notificações para usuários que provavelmente desativariam o push nas configurações do dispositivo. Para iOS, as Campaigns de push são relevantes porque as notificações por push em primeiro plano (como notificações que ativam o dispositivo) não são habilitadas até que o usuário aceite explicitamente o prompt nativo de push do iOS.

**Compatível com:** Web, Android, iOS

Para saber mais, consulte [Mensagens no app de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/).

## Push Stories

Push Stories são mensagens imersivas que levam o usuário por uma jornada visual em formato de carrossel. Estão disponíveis apenas para dispositivos móveis.

**Compatível com:** iOS, Android

Para saber mais, consulte [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories/).

## Push com botões de ação {#push-with-action-buttons}

Push com botões de ação são mensagens que permitem oferecer opções aos seus usuários e várias chamadas para ação.

**Compatível com:** Web, Android, iOS

Para saber mais, consulte [Botões de ação por push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/).

## Notificações Rich push {#rich-push-notifications}

Notificações Rich push são notificações com imagens imersivas e conteúdo criativo que podem se expandir além de um ícone e texto de chamada para ação.

**Compatível com:** iOS, Android

Para saber mais, consulte [Criar notificações Rich para iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/) ou [Criar notificações Rich para Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/).

## Notificações por push provisórias para iOS {#provisional-push-notifications-for-ios}

Introduzida pela Apple no iOS 12, a autorização provisória ocorre automaticamente na instalação de apps iOS, permitindo que as marcas enviem notificações silenciosas sem exibir um prompt de push aos usuários. Quando o push silencioso é enviado e visualizado na bandeja de notificações do dispositivo, os usuários têm a opção de permitir ou interromper as notificações por push.

**Compatível com:** iOS

Para saber mais, consulte [Opções de notificação do iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/#provisional-push).

## Notificações por push em HTML {#html-push-notifications}

Notificações por push em HTML são mensagens push codificadas diretamente em HTML e que não usam os modelos de push predefinidos fornecidos pela Braze. Ter a opção de criar notificações por push em HTML permite que sua empresa tenha total liberdade criativa e branding consistente na aparência dessas mensagens push.

**Compatível com:** Android

## IDs de notificação e IDs de canal {#notification-ids-and-channel-ids}

IDs de notificação e IDs de canal permitem substituir ou atualizar notificações por push já recebidas, mas ainda não abertas pelo usuário.

**Compatível com:** iOS, Android

Para saber mais, consulte [Canais de notificação]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels/) e [Configurações avançadas de Campaign de push]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/).

## Notificações por push em segundo plano ou silenciosas {#background-push-notifications}

Notificações por push que não são exibidas no dispositivo. Geralmente usadas para enviar pacotes de informações ao app para processos em segundo plano e rastreamento de desinstalação. Um token por push habilitado para segundo plano é necessário para que um push em segundo plano ou silencioso seja enviado.

**Compatível com:** Web, Android, iOS

Para saber mais, consulte [Notificações por push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/).

## Notificações por push para wearables {#wearable-push-notifications}

Essas notificações por push permitem que as marcas enviem mensagens diretamente para dispositivos vestíveis, como o Apple Watch.

**Compatível com:** iOS
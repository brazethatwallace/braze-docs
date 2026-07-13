---
nav_title: "Opções de notificação"
article_title: Opções de notificação para Android
page_order: 2
page_type: reference
description: "Este artigo de referência aborda diversas opções de notificação para Android e como utilizá-las da melhor forma em Campaigns na Braze."

platform: Android
channel:
  - Push

---

# Opções de notificação {#notification-options}

> Estas são algumas das opções de notificação por push específicas para Android disponíveis na Braze.

## Notificações silenciosas {#silent-notifications}

Ao [redigir sua mensagem de notificação por push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message?tab=android#step-4-compose-your-push-message), você **não pode** enviar uma mensagem push para Android sem um título&#8212;no entanto, é possível inserir um único espaço. Tenha em mente que, se sua mensagem contiver apenas um espaço, ela será enviada como uma notificação por push silenciosa. Para saber mais, consulte [Notificações por push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android).

## Grupos de notificação {#notification-groups}

Se você deseja categorizar suas mensagens e agrupá-las na bandeja de notificações do usuário, é possível utilizar o recurso de canais de notificação do Android por meio da Braze.

Primeiro, crie sua Campaign de push para Android e, em seguida, procure no topo da guia **Compose** o menu suspenso **Notification Channel**.

![Crie sua Campaign de push para Android e procure no topo da guia Compose o menu suspenso Notification Channel.]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

Selecione seu canal de notificação no menu suspenso. Você também deve selecionar um canal de fallback para o caso de as configurações do seu canal de notificação apresentarem problemas.

Se você não tiver nenhum [canal de notificação]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels) listado aqui, é possível adicionar um usando o ID do canal de notificação. Fale com seus desenvolvedores para identificar quais são os IDs dos canais de notificação ou para criar novos IDs conforme necessário.

Para adicionar um ID de notificação ao seu canal de notificação, clique em **Manage Notification Channel** no menu suspenso **Notification Channel** e preencha os campos obrigatórios. Os canais de notificação devem ser definidos no app antes de poderem ser usados na plataforma Braze.

![Clique em Manage Notification Channel no menu suspenso Notification Channel e preencha os campos obrigatórios. Os canais de notificação devem ser definidos no app antes de poderem ser usados na plataforma Braze.]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }
---
nav_title: "Mensagens push rápidas"
article_title: "Mensagens push rápidas"
alias: "/quick_push/"
description: "Este artigo descreve o que você precisa saber ao criar uma campanha push ou Canvas usando a experiência de edição de push rápido."
page_order: 4
---

# Mensagens push rápidas {#quick-push-messages}

> Este artigo descreve o que você precisa saber ao criar uma Campaign push ou Canvas usando a experiência de edição de push rápido para direcionar múltiplas plataformas e dispositivos a partir de um único criador.

Ao criar uma Campaign push ou Canvas na Braze, você pode selecionar múltiplas plataformas e dispositivos para criar uma mensagem para todas as plataformas em uma única experiência de edição chamada push rápido.

## Casos de uso {#use-cases}

Essa experiência de edição é ideal para os seguintes casos de uso:

- Campaigns push para celular e etapas de mensagem do Canvas que precisam ser enviadas para múltiplos tipos de dispositivo (como iOS e Android).
- Notificações por push urgentes que precisam direcionar múltiplas plataformas de forma rápida e precisa, onde o conteúdo é o mesmo em todas as plataformas (como notícias de última hora ou atualizações de jogos ao vivo).

## Criando uma Campaign ou Canvas de push rápido {#creating-a-quick-push-campaign-or-canvas}

Para criar uma Campaign direcionada a múltiplas plataformas e dispositivos:

1. Crie uma Campaign ou adicione uma [etapa de mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) a um Canvas.
2. Selecione **Push notification**.
3. Selecione as plataformas desejadas (Mobile, Web, Kindle) e os dispositivos móveis (iOS, Android). Se você selecionar múltiplos dispositivos, os testes multivariantes não estarão disponíveis para sua Campaign.

### Selecionando plataformas para uma Campaign {#selecting-platforms-for-a-campaign}
![Opções para selecionar múltiplas plataformas para uma Campaign push, como Mobile, Web e Kindle, e múltiplos dispositivos, como iOS e Android.]({% image_buster /assets/img_archive/quick_push_1.png %})

### Selecionando plataformas para uma etapa do Canvas {#selecting-platforms-for-a-canvas-step}
![Opções para selecionar múltiplas plataformas para uma etapa de mensagem push, como Mobile, Web e Kindle, e múltiplos dispositivos, como iOS e Android.]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4. Selecione **Confirm**. Após selecionar **Confirm**, você não poderá alterar as plataformas ou dispositivos selecionados.
5. Continue configurando sua Campaign ou Canvas.

Seu criador terá uma aparência um pouco diferente do habitual. Continue lendo para ver o que mudou.

### O que é diferente {#whats-different}

Na guia **Compose**, você pode especificar um título, uma mensagem e um comportamento ao clicar para todas as plataformas e dispositivos escolhidos.

O painel de pré-visualização mostra uma aproximação de como sua mensagem aparecerá em cada plataforma. Embora ele possa dar uma boa indicação de onde você pode atingir os limites de caracteres, lembre-se de sempre testar suas mensagens em um dispositivo real antes de enviar sua Campaign.

![Visualização de edição única com um título, mensagem e campo de comportamento ao clicar para três tipos de push: iOS, Android e Web.]({% image_buster /assets/img_archive/quick_push_2.png %})

Na seção **Assets**, selecione ou faça upload das imagens que deseja exibir para cada plataforma. Tenha em mente que diferentes dispositivos possuem especificações diferentes para imagens e contagem de caracteres. Consulte [Formatos de mensagem e imagem push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/) para obter ajuda.

![Seção de ativos da visualização de edição única com campos para Push Icon Image, imagem de notificação iOS, imagem de notificação Android e imagem de notificação Web.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

Em seguida, finalize a configuração da sua Campaign push normalmente. Consulte [Criando uma Campaign push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/) para mais detalhes.

## O que você precisa saber {#things-to-know}

### Tipo de notificação {#notification-type}

O tipo de notificação é definido como "Standard Push" por padrão e não pode ser alterado. Se você quiser criar um tipo diferente de push, como Push Stories ou imagem inline (Android), crie Campaigns separadas para cada tipo de dispositivo.

### Testes multivariantes {#multivariate-testing}

Se você selecionar múltiplos dispositivos para plataformas móveis, como iOS e Android, os testes multivariantes não estarão disponíveis para sua Campaign. Se você quiser realizar testes multivariantes, crie Campaigns separadas para cada tipo de dispositivo.

### Configurações específicas do dispositivo {#device-specific-settings}

Você pode editar configurações específicas da plataforma no editor. Isso inclui configurações como [botões de ação por push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/), canais e grupos de notificação, TTL, prioridade de exibição, sons e muito mais.

Os botões de ação por push não são compatíveis ao direcionar tanto iOS quanto Android usando Campaigns de push rápido. Para saber mais sobre configurações específicas do dispositivo, consulte as seguintes coleções de artigos:

- [Opções para iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/)
- [Opções para Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/)
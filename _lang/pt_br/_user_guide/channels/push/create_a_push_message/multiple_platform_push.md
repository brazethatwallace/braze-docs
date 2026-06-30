---
nav_title: "Mensagens push para múltiplas plataformas"
article_title: "Mensagens para múltiplas plataformas"
alias: "/multiple_platform_push/"
description: "Este artigo descreve o que você precisa saber ao criar uma Campaign de push ou Canvas com múltiplas plataformas selecionadas."
page_order: 4
---

# Mensagens push para múltiplas plataformas {#multiple-platform-push-messages}

> Este artigo descreve o que você precisa saber ao criar uma Campaign ou Canvas de push para direcionar múltiplas plataformas e dispositivos a partir de um único criador.

Ao criar uma Campaign ou Canvas de push na Braze, você pode selecionar múltiplas plataformas e dispositivos para criar uma mensagem para todas as plataformas em uma única experiência de edição.

## Casos de uso {#use-cases}

Essa experiência de edição é ideal para os seguintes casos de uso:

- Campaigns de push para celular e etapas de mensagem do Canvas que precisam ser enviadas para múltiplos tipos de dispositivo (como iOS e Android).
- Notificações por push urgentes que precisam direcionar múltiplas plataformas de forma rápida e precisa, onde o conteúdo é o mesmo em todas as plataformas (como notícias de última hora ou atualizações de jogos ao vivo).

## Criando uma Campaign ou Canvas de push para múltiplas plataformas {#creating-a-multiple-platform-push-campaign-or-canvas}

Para criar uma Campaign direcionada a múltiplas plataformas e dispositivos:

1. Crie uma Campaign ou adicione uma [etapa de mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) a um Canvas.
2. Selecione **Notificação por push**.
3. Selecione as plataformas desejadas (Celular, Web, Kindle) e os dispositivos móveis (iOS, Android). Se você selecionar múltiplos dispositivos, os testes multivariantes não estarão disponíveis para sua Campaign.

### Selecionando plataformas para uma Campaign {#selecting-platforms-for-a-campaign}
![Opções para selecionar múltiplas plataformas para uma Campaign de push, como Celular, Web e Kindle, e múltiplos dispositivos, como iOS e Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### Selecionando plataformas para uma etapa do Canvas {#selecting-platforms-for-a-canvas-step}
![Opções para selecionar múltiplas plataformas para uma etapa de mensagem de push, como Celular, Web e Kindle, e múltiplos dispositivos, como iOS e Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. Selecione **Confirmar**. Após selecionar **Confirmar**, você não poderá alterar as plataformas ou dispositivos selecionados.
5. Continue configurando sua Campaign ou Canvas.

## Executando um teste multivariante em múltiplas plataformas {#running-a-multi-platform-multivariate-test}

Os testes multivariantes são compatíveis com Campaigns de múltiplas plataformas. Basta selecionar o ícone de adição ao lado do nome da variante, como você faria normalmente em Campaigns de plataforma única. Recomendamos que você [leia nosso guia]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) sobre como criar testes multivariantes e utilize a [Seleção de Variante com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) para automatizar e maximizar seu engajamento.

![Testes multivariantes fáceis em múltiplas plataformas]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## O que você precisa saber {#things-to-know}

### Envio de mensagens unificado {#unified-messaging}
Na guia **Redigir**, você pode especificar um título, uma mensagem e um comportamento ao clicar para todas as plataformas e dispositivos escolhidos.

O painel de pré-visualização mostra uma aproximação de como sua mensagem aparece em cada plataforma. Embora ele possa dar uma boa indicação de onde você pode atingir os limites de caracteres, lembre-se de sempre testar suas mensagens em um dispositivo real antes de enviar sua Campaign.

![Visualização de edição única com um título, uma mensagem e um campo de comportamento ao clicar para três tipos de push: iOS, Android e Web.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### Ativos separados {#separate-assets}
Na seção **Ativos**, selecione ou faça upload das imagens que deseja exibir para cada plataforma. Lembre-se de que diferentes dispositivos têm especificações diferentes para imagens e contagem de caracteres. Consulte [Formatos de mensagem e imagem de push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats) para obter ajuda.

![Seção de ativos da visualização de edição única com campos para imagem do ícone de push, imagem de notificação do iOS, imagem de notificação do Android e imagem de notificação da Web.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### Tipo de notificação {#notification-type}

O tipo de notificação é definido como "Push padrão" por padrão e não pode ser alterado. Se você quiser criar um push diferente, como Push Stories ou imagem inline (Android), crie Campaigns separadas para cada tipo de dispositivo.

### Configurações específicas do dispositivo {#device-specific-settings}

Você pode editar configurações específicas da plataforma no editor. Isso inclui configurações como [botões de ação por push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), canais e grupos de notificação, TTL, prioridade de exibição, sons e muito mais.

Para saber mais sobre configurações específicas do dispositivo, consulte as seguintes coleções de artigos:

- [Opções do iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios)
- [Opções do Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android)

### Push Stories

Push Stories estão disponíveis em múltiplas plataformas apenas no Android e iOS. Se você selecionar Web ou Kindle como plataforma de envio, essa opção não estará disponível.
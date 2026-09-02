---
nav_title: Prévia dinâmica de link para SMS
article_title: Prévia dinâmica de link para SMS
description: "Este artigo de referência descreve como ativar e usar o recurso de prévia de links para SMS da Movable Ink."
page_type: partner
search_tag: Partner
---

# Prévia dinâmica de link para SMS {#dynamic-sms-link-preview}

> Com a prévia dinâmica de link para SMS da Movable Ink, você aproveita a imersão do MMS pelo mesmo custo do SMS. Isso permite usar a Braze e a Movable Ink para entregar experiências de mensagens ricas, personalizadas e econômicas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta da Movable Ink | É necessário ter uma conta da Movable Ink para aproveitar essa parceria. |
| Fonte de dados | Você precisa conectar uma fonte de dados à Movable Ink. Isso pode ser feito por CSV, importação do site ou API or interface de programação do aplicativo (API). |
| Recursos de envio de MMS | Confirme que você está configurado para MMS por meio da Braze.
| [Encurtamento de links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) | Confirme que o encurtamento de links está ativado. |
| Cartão de contato | Sua marca (o remetente) deve ser salva como um contato no telefone do usuário para que a prévia do link funcione no iOS. Isso pode ser feito com um cartão de contato ou outro método. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Siga as respectivas etapas nesta seção para enviar links dinâmicos de SMS para os sistemas operacionais iOS e Android.

### iOS

{% alert important %}
Para permitir imagens de prévia de links no iOS, os usuários devem adicionar sua marca (o remetente) como um contato.
{% endalert %}

#### Etapa 1: Crie uma campanha de cartão de contato {#step-1-create-a-contact-card-campaign}

Depois que os usuários salvarem sua marca como um contato, seja por meio de um [cartão de contato]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card) ou outro método, eles poderão ver os prompts **Tap to Load prévia** e os links da Movable Ink.

![Prompt de prévia de link no iOS][1]{: style="max-width:30%;"}

#### Etapa 2: Envie links da Movable Ink {#step-2-send-movable-ink-links}

1. Crie uma campanha de SMS na Movable Ink e gere seu URL de cliques.
2. No dashboard da Braze, acesse **Campaigns** e configure uma nova campanha de SMS/MMS no menu suspenso **Create Campaign**.
3. No criador da campanha de SMS:
    - Defina o grupo de inscrições.
    - Digite sua mensagem.
    - Adicione o link da Movable Ink **por último**, depois de todos os outros textos no corpo da mensagem. <br><br>![Corpo da mensagem SMS com link da Movable Ink][2]{: style="max-width:50%;"}

{% alert tip %}
Confira o [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) para relembrar a personalização com Liquid.
{% endalert %}

{: start="4"}
4. Você está pronto para testar e lançar sua campanha de prévia dinâmica de link para SMS.

![Tela de teste e lançamento da campanha][3]{: style="max-width:70%;"}

Depois que os usuários carregarem a prévia do link, uma imagem personalizada será renderizada com a possibilidade de direcionar para o seu website, app ou landing page.

![Exemplo de imagem personalizada renderizada][4]{: style="max-width:30%;"}

### Android (dispositivos Google e Samsung) {#android-google-and-samsung-devices}

Os usuários do Android não precisam salvar sua marca como um contato para receber prévias dinâmicas de links de SMS. No entanto, isso ainda é recomendado para que o dispositivo possa carregar automaticamente as prévias dos links.

![Prévia automática de link no Android][5]{: style="max-width:30%;"}

Os usuários que não salvaram sua marca como contato e ativaram as prévias automáticas terão que selecionar **Tap to load prévia** para carregar a imagem da prévia.

![Opção de toque para carregar prévia no Android][6]{: style="max-width:30%;"}

## Considerações {#considerations}

- Inclua apenas um link de prévia na sua mensagem. O conteúdo não será gerado com vários links no corpo do SMS.
- Não inclua nenhum caractere após o link de prévia, ou a experiência poderá ser interrompida.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}
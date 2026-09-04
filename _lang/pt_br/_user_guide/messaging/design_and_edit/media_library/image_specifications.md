---
nav_title: Especificações de imagem
article_title: Especificações de imagem
page_order: 1
page_type: reference
description: "Este artigo de referência descreve os tamanhos e especificações de imagem recomendados para cada tipo de canal."
tool:
  - Templates
  - Media

---

# Especificações de imagem {#image-specifications}

> De modo geral, imagens menores e de alta qualidade carregam mais rápido, por isso recomendamos usar o menor ativo possível para alcançar o resultado desejado. Para maximizar o uso de imagens em canais específicos, consulte os detalhes neste artigo.

Você deve sempre [pré-visualizar e testar suas mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) em diversos dispositivos para confirmar que as áreas mais importantes da sua imagem e mensagem apareçam conforme esperado.

## Comportamento da imagem {#image-behavior}

{% multi_lang_include channels/image_specs.md variable_name='image behavior' %}

## Vídeo {#video}

Os vídeos enviados para a biblioteca de mídia só podem ser usados em mensagens do WhatsApp. Para saber mais, consulte [Criando uma mensagem do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#outbound-messages).

## GIFs {#gifs}

GIFs são compatíveis com push no iOS, mensagens no app, e-mail, Content Cards e mensagens MMS ou RCS. GIFs com formatos muito alongados (por exemplo, 3000 x 2 pixels) ou com 300 ou mais quadros podem não ser enviados, mesmo que o tamanho total do arquivo seja pequeno. Para o comportamento específico de GIFs em RCS no iOS, consulte [RCS](#rcs).

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

## Orientações por canal {#channel-guidance}

### Content Cards

{% multi_lang_include channels/image_specs.md variable_name='content cards' %}

### E-mail {#email}

{% multi_lang_include channels/image_specs.md variable_name='email' %}

### Mensagens no app {#in-app-messages}

{% multi_lang_include channels/image_specs.md variable_name='in-app messages' %}

{% alert tip %} Crie ativos com confiança! Nossos modelos de imagem para mensagens no app e sobreposições de zona segura foram projetados para funcionar bem em dispositivos de todos os tamanhos. [Baixar ZIP dos modelos de design]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

Para saber mais, consulte [Detalhes criativos de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize).

#### Font Awesome

A Braze oferece suporte ao uso do [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) para ícones de mensagens no app do tipo modal.

### Notificações por push {#push-notifications}

{% multi_lang_include channels/image_specs.md variable_name='payload size' %}

{% multi_lang_include channels/image_specs.md variable_name='push notifications' %}

#### Comprimentos de mensagem recomendados {#recommended-message-lengths}

Para melhores resultados, consulte as diretrizes de comprimento de mensagem a seguir ao criar mensagens push. Pode haver alguma variação dependendo da presença de uma imagem, do estado da notificação (iOS) e da configuração de exibição do dispositivo do usuário, bem como do tamanho do dispositivo.

| Tipo de mensagem | Comprimento recomendado (somente texto) | Comprimento recomendado (rich) |
| --- | --- | --- |
| Tela de bloqueio do iOS | 160 caracteres | 130 caracteres |
| Central de Notificações do iOS | 160 caracteres | 130 caracteres |
| Banner de alerta do iOS | 80 caracteres | 65 caracteres |
| Tela de bloqueio do Android | 49 caracteres | N/D |
| Gaveta de notificações do Android | 597 caracteres | N/D |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comprimentos de mensagem recomendados" }

Para saber mais sobre contagem de caracteres no iOS, consulte [Diretrizes de contagem de caracteres no iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count).

#### Web push {#web-push}

{% tabs %}
{% tab Imagens %}

| Navegador | Tamanho de ícone recomendado |
| --- | --- |
| Chrome | 192 x 192 px ou maior |
| Firefox | 192 x 192 px ou maior |
| Safari | 192 x 192 px ou maior (configurável por campanha com Safari 16 no macOS 13+) |
| Opera | 192 x 192 px ou maior |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web push" }

| Navegador | Plataforma | Tamanho de imagem grande |
| --- | --- | --- |
| Chrome | Android | Proporção 2:1 |
| Firefox | Android | N/D |
| Chrome | Windows | Proporção 2:1 |
| Edge | Windows | Proporção 2:1 |
| Firefox | Windows | N/D |
| Opera | Windows | Proporção 2:1 |
| Chrome | macOS | N/D |
| Safari | macOS | N/D |
| Firefox | macOS | N/D |
| Opera | macOS | N/D |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web push" }

{% endtab %}
{% tab Texto %}

| Navegador | Plataforma | Comprimento máximo do título | Comprimento máximo do corpo |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Web push" }

{% endtab %}
{% endtabs %}

#### Exemplos de notificações por push {#push-notification-examples}

{% tabs %}
{% tab iOS %}

![Notificação por push no iOS com o texto: "Hi! This is an iOS Push with an image" com um emoji. Há uma imagem pequena ao lado do texto.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notificação por push no iOS expandida com o mesmo texto da mensagem anterior e uma imagem expandida antes do texto.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![Notificação por push no Android com uma imagem grande abaixo do texto da mensagem.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Notificações com imagens grandes ficam melhores ao usar uma imagem de pelo menos 600 x 300 pixels.
{% endalert %}

{% endtab %}
{% endtabs %}

Para recursos adicionais, consulte [Especificações de imagem e texto para push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats).

### SMS e MMS {#sms-and-mms}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

Para compor mensagens MMS, consulte [Criar uma mensagem SMS, MMS ou RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create).

### RCS {#rcs}

As mensagens de mídia RCS suportam imagens JPG, JPEG e GIF. Para detalhes sobre tamanho de arquivo e formato, consulte [Criar uma mensagem SMS, MMS ou RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create).

No iOS, GIFs em rich cards RCS são exibidos como imagens estáticas. No Android, eles são animados normalmente. Para mais detalhes, consulte [Por que GIFs em rich cards RCS aparecem estáticos no iOS?]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios).
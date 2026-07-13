---
nav_title: "Formatos de mensagem e imagem"
article_title: "Formatos de mensagem e imagem"
page_order: 1
page_type: reference
description: "Este artigo descreve os formatos de mensagem e imagem para notificações por push."
channel: push

---

# Formatos de mensagem e imagem para push {#push-message-and-image-formats}

> Este artigo de referência descreve os formatos de mensagem e imagem para notificações por push.

Para obter os melhores resultados, consulte as diretrizes de tamanho de imagem e comprimento de mensagem a seguir ao criar suas mensagens push. Pode haver alguma variação dependendo da presença de uma imagem, do estado da notificação (iOS) e da configuração de exibição do dispositivo do usuário, bem como do tamanho do dispositivo. Em caso de dúvida, mantenha seu texto curto e direto.

## Push para iOS e Android {#ios-and-android-push}

{% tabs local %}
{% tab Imagens %}

**Tipo de imagem** | **Tamanho de imagem recomendado** | **Tamanho máximo de imagem** | **Tipos de arquivo**
--- | --- | --- | ---
(iOS) 2:1 *Recomendado* | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG, GIF
(Android) Ícone de push | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG
(Android) Notificação expandida | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Push para iOS e Android" }

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

{% endtab %}
{% tab Texto %}

| Tipo de mensagem | Comprimento recomendado da mensagem (somente texto) | Comprimento recomendado da mensagem (rich)
--- | ---
(iOS) Tela de bloqueio | 160 caracteres | 130 caracteres
(iOS) Central de notificações | 160 caracteres | 130 caracteres
(iOS) Alerta em banner | 80 caracteres | 65 caracteres
(Android) Tela de bloqueio | 49 caracteres | N/A
(Android) Gaveta de notificações | 597 caracteres | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push para iOS e Android" }

Quer saber quantos caracteres você pode usar em uma notificação por push no iOS sem que ela seja truncada? Confira nossas [diretrizes de contagem de caracteres para iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count).

{% endtab %}
{% tab Tamanho da carga útil %}

**Plataforma** | **Tamanho**
--- | ---
iOS anterior ao 8 | 0,256 KB
iOS 8 em diante | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push para iOS e Android" }

{% endtab %}
{% tab Exemplo de imagem %}
{% subtabs %}
{% subtab iOS %}

![Notificação por push no iOS com o texto "Hi! This is an iOS Push with an image" e um emoji. Há uma pequena imagem ao lado do texto.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notificação por push no iOS em um push completo com o mesmo texto da mensagem anterior e uma imagem expandida antes do texto.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![Notificação por push no Android com uma imagem grande abaixo do texto da mensagem.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Notificações com imagens grandes ficam melhores ao usar uma imagem de pelo menos 600x300 pixels.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Exemplo de texto %}
{% subtabs %}
{% subtab iOS %}

![Notificação por push no iOS com o texto "Hi! This is an iOS Push".]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
![Notificação por push no Android exibida na tela inicial.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Push para a web {#web-push}

{% tabs local %}
{% tab Imagens %}

| **Navegador** | **Tamanho de ícone recomendado**
| --- | ---
| Chrome | 192 x 192 ≥
| Firefox | 192 x 192 ≥
| Safari | 192 x 192 ≥ (Os ícones são configuráveis por campanha no Safari 16+ no macOS 13+)
| Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push para a web" }

| **Navegador** | **Plataforma** | **Tamanho de imagem grande**
| --- | --- | ---
| Chrome | Android | Proporção 2:1
| Firefox | Android | N/A
| Chrome | Windows | Proporção 2:1
| Edge | Windows | Proporção 2:1
| Firefox | Windows | N/A
| Firefox | Windows | Proporção 2:1
| Safari | macOS | N/A
| Chrome | macOS | N/A
| Firefox | macOS | N/A
| Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push para a web" }

{% endtab %}
{% tab Texto %}

| **Navegador** | **Plataforma** | **Comprimento máximo do título**  | **Comprimento máximo do corpo da mensagem**
| --- | --- | --- | ---
| Chrome | Android | 35 | 50
| Firefox | Android | 35 | 50
| Chrome | Windows | 50 | 120
| Edge | Windows | 50 | 120
| Firefox | Windows | 54 | 200
| Opera | Windows | 50 | 120
| Chrome | macOS | 35 | 50
| Safari | macOS | 38 | 84
| Firefox | macOS | 38 | 42
| Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Push para a web" }

{% endtab %}
{% endtabs %}
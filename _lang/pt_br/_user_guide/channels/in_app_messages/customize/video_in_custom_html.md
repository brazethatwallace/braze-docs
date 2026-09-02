---
nav_title: "Vídeo em HTML personalizado"
article_title: "Vídeo em HTML personalizado"
page_order: 4
page_type: reference
description: "Este artigo descreve como incorporar vídeos nas suas mensagens no app em HTML."
channel:
  - in-app messages
---

# Vídeo em mensagens no app com HTML personalizado {#video}

> Este artigo se aplica a [mensagens em HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) no [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

## Incorporar vídeos {#embed-videos}

Para reproduzir um vídeo em uma mensagem no app em HTML, inclua o seguinte elemento `<video>` no seu HTML e substitua os nomes dos vídeos pelo nome do seu arquivo (ou pela URL do ativo remoto). Você pode encontrar outras opções possíveis de `<video>` no [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

Para usar um ativo de vídeo local, inclua esse arquivo ao fazer upload dos ativos para a sua campaign.

{% alert note %}
O conteúdo de vídeo só está disponível quando o dispositivo tem uma velocidade de rede razoável, a menos que o vídeo seja originado localmente do dispositivo.
{% endalert %}

## Considerações para Android {#android-considerations}

Para incorporar vídeo e outros conteúdos HTML5 em mensagens no app em HTML no Android, é necessário que a aceleração de hardware esteja ativada na Activity onde a mensagem no app é exibida. Para saber mais, consulte o [guia do desenvolvedor Android]({{site.baseurl}}/developer_guide/in_app_messages/html_messages#android_embedding-youtube-content).

**Reprodução automática**: Mesmo com a aceleração de hardware ativada, os WebViews do Android podem exigir um gesto do usuário para iniciar a reprodução de mídia. Se você precisa de reprodução automática, configure o WebView usado para renderizar mensagens no app em HTML para desativar a exigência de gesto do usuário definindo [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). Isso requer personalização no nível do SDK de como as mensagens no app em HTML são exibidas. Para orientações de configuração, consulte [Personalizar mensagens no app para o SDK da Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android).

## Considerações para iOS {#ios-considerations}

Para oferecer suporte a dispositivos iOS:

- Você deve incluir o atributo `playsinline` porque a reprodução em tela cheia não é suportada.
- **A reprodução automática não é garantida no iOS**. O comportamento de reprodução no iOS depende do `WKWebView` e das políticas de mídia no nível do sistema operacional, e pode exigir um gesto do usuário mesmo quando `autoplay` e `muted` estão definidos. Teste sua mensagem no app em HTML nas versões e dispositivos iOS de destino.

Se a reprodução automática for necessária e seus testes mostrarem que ela não funciona por padrão, você pode personalizar a `WKWebViewConfiguration` usada pelas mensagens no app em HTML para ajustar a exigência de ação do usuário para reprodução de mídia, por exemplo, definindo a propriedade `mediaTypesRequiringUserActionForPlayback`. Isso requer personalização no nível do SDK. Para recursos em Swift, consulte [Personalizar mensagens no app para o SDK da Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=swift) e [Adicionar a interface JavaScript da Braze a WebViews para Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages?sdktab=swift).

## Considerações para web {#web-considerations}

A maioria dos navegadores modernos permite a reprodução automática apenas sob certas condições (geralmente quando o vídeo está sem som). Se você usar `autoplay` em uma mensagem no app na web, inclua `muted` e teste nos navegadores e dispositivos suportados, pois as políticas dos navegadores variam e ainda podem exigir um gesto do usuário em alguns casos.

Para reproduzir automaticamente vídeos do YouTube em uma mensagem no app na web, adicione o parâmetro de URL `&autoplay=1`. Por exemplo, o vídeo a seguir será reproduzido automaticamente, estará sem som (`&mute=1`) e não mostrará controles (`&controls=0`):

```html
<iframe class="video" src="https://www.youtube.com/embed/VPIPAc4oQqw?autoplay=1&mute=1&controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Como os vídeos do YouTube são exibidos {#how-youtube-videos-display}

- Mensagens no app com vídeos incorporados do YouTube podem ser exibidas diretamente dentro do app ou em uma guia separada dentro do app, dependendo da plataforma.
- O texto da mensagem no app pode não ser exibido quando o vídeo incorporado do YouTube é mostrado.

## Solução de problemas {#troubleshooting}

Se a sua mensagem no app não exibir o vídeo:

- Confirme se a URL é válida.
- Confirme se não está faltando a declaração `type="video/mp4"` (para vídeos que não são do YouTube).
- Adicione quaisquer tags de fechamento ausentes e corrija erros de digitação.
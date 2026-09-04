{% multi_lang_include developer_guide/prerequisites/web.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) para o Web SDK. Observe que você só pode enviar notificações por push para usuários de iOS e iPadOS que estão usando [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) ou posterior.

## Configurando push do Safari para dispositivos móveis {#setting-up-safari-push-for-mobile}

### Etapa 1: Crie um arquivo de manifesto {#manifest}

Um [Manifesto de Aplicativo Web](https://developer.mozilla.org/en-US/docs/Web/Manifest) é um arquivo JSON que controla como seu website é apresentado quando instalado na tela inicial do usuário.

Por exemplo, você pode definir a cor do tema de fundo e o ícone que o [App Switcher](https://support.apple.com/en-us/HT202070) utiliza, se ele é renderizado em tela cheia para se parecer com um app nativo, ou se o app deve abrir no modo paisagem ou retrato.

Crie um novo arquivo `manifest.json` no diretório raiz do seu website, com os seguintes campos obrigatórios.

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

A lista completa de campos compatíveis pode ser encontrada na [documentação de Manifesto de App Web do MDN](https://developer.mozilla.org/en-US/docs/Web/Manifest).

### Etapa 2: Vincule o arquivo de manifesto {#manifest-link}

Adicione a seguinte tag `<link>` ao elemento `<head>` do seu website, apontando para onde o arquivo de manifesto está hospedado.

```html
<link rel="manifest" href="/manifest.json" />
```

### Etapa 3: Adicione um service worker {#service-worker}

Seu website deve ter um arquivo de service worker que importa a biblioteca de service worker da Braze, conforme descrito em nosso [guia de integração de web push]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-1-configure-your-sites-service-worker).

### Etapa 4: Adicione à tela inicial {#add-to-homescreen}

Navegadores populares (como Safari, Chrome, Firefox e Edge) suportam notificações por web push em suas versões mais recentes. Para solicitar permissão de push no iOS ou iPadOS, seu website deve ser adicionado à tela inicial do usuário selecionando **Compartilhar** > **Adicionar à Tela de Início**. A opção [Adicionar à Tela de Início](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) permite que os usuários salvem seu website como favorito, adicionando seu ícone ao valioso espaço da tela inicial.

![Um iPhone mostrando opções para favoritar um website e salvar na tela inicial]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Etapa 5: Exiba o prompt nativo de push {#push-prompt}
Depois que o app for adicionado à tela inicial, você pode solicitar permissão de push quando o usuário realizar uma ação (como clicar em um botão). Isso pode ser feito usando o método [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission), ou com uma [mensagem no app de push primer sem código]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

{% alert note %}
Após aceitar ou recusar o prompt, você precisa excluir e reinstalar o website na tela inicial para poder exibir o prompt novamente.
{% endalert %}

![Um prompt de push perguntando se deseja "permitir" ou "não permitir" notificações]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

Por exemplo:

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```

## Próximas etapas {#next-steps}

Em seguida, envie uma [mensagem de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages) para validar a integração. Após a conclusão da integração, você pode usar nossas [mensagens push primer sem código]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) para otimizar suas taxas de aceitação de push.
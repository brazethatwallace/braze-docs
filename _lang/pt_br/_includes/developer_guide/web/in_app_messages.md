{% multi_lang_include developer_guide/prerequisites/web.md %} No entanto, não é necessária nenhuma configuração adicional.

## Tipos de mensagem {#message-types}

Todas as mensagens no app herdam seu protótipo de [`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html), que define o comportamento básico e as características de todas as mensagens no app. As subclasses prototípicas são [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) e [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

Cada tipo de mensagem no app é personalizável em relação a conteúdo, imagens, ícones, ações de clique, análise de dados, exibição e entrega.

{% tabs %}
{% tab Slideup %}

As mensagens no app [`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) recebem esse nome porque, tradicionalmente em plataformas móveis, elas "deslizam para cima" ou "deslizam para baixo" a partir do topo ou da parte inferior da tela. No SDK da Braze para web, essas mensagens são exibidas mais como uma notificação no estilo Growl ou Toast, para se alinhar ao paradigma dominante da web. Elas cobrem uma pequena parte da tela e oferecem uma capacidade de envio de mensagens eficaz e não intrusiva.

![Uma mensagem no app deslizando a partir da parte inferior da tela de um celular exibindo "Humans are complicated. Custom engagement shouldn't be." No fundo, a mesma mensagem no app é exibida no canto inferior de uma página web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

As mensagens no app [`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) aparecem no centro da tela e são emolduradas por um painel translúcido. Úteis para mensagens mais críticas, elas podem ser equipadas com até dois botões com ação de clique e análise de dados habilitada.

![Uma mensagem no app modal no centro da tela de um celular exibindo "Humans are complicated. Custom engagement shouldn't be." No fundo, a mesma mensagem no app é exibida no centro de uma página web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Tela inteira %}

As mensagens no app [`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) são úteis para maximizar o conteúdo e o impacto da sua comunicação com o usuário. Em janelas de navegador estreitas (por exemplo, na web mobile), as mensagens no app `full` ocupam toda a janela do navegador. Em janelas de navegador maiores, as mensagens no app `full` aparecem de forma semelhante às mensagens no app `modal`. A metade superior de uma mensagem no app `full` contém uma imagem, e a metade inferior permite até oito linhas de texto, além de até dois botões com ação de clique e análise de dados habilitada.

![Uma mensagem no app em tela inteira exibida em toda a tela de um celular mostrando "Humans are complicated. Custom engagement shouldn't be." No fundo, a mesma mensagem no app é exibida de forma grande no centro de uma página web.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab HTML personalizado %}

As mensagens no app [`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) são úteis para criar conteúdo de usuário totalmente personalizado. O HTML definido pelo usuário é exibido em um iFrame e pode conter conteúdo rico, como imagens, fontes, vídeos e elementos interativos, permitindo controle total sobre a aparência e a funcionalidade da mensagem. Elas suportam uma interface JavaScript `brazeBridge` para chamar métodos no SDK da Braze para web a partir do seu HTML. Consulte nossas [melhores práticas]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices) para mais detalhes.

{% alert important %}
Para ativar mensagens no app em HTML por meio do SDK para web, você **deve** fornecer a opção de inicialização `allowUserSuppliedJavascript` à Braze, por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso é por motivos de segurança. Mensagens no app em HTML podem executar JavaScript, então exigimos que um mantenedor do site as ative.
{% endalert %}

O exemplo a seguir mostra uma mensagem no app em HTML paginada:

![Uma mensagem no app em HTML com um carrossel de conteúdo e botões interativos.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}
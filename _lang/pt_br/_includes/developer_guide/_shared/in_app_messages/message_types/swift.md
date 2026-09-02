{% tab swift %}
Cada tipo de mensagem no app é altamente personalizável em termos de conteúdo, imagens, ícones, ações de clique, análise de dados, exibição e entrega. Eles são tipos enumerados de `Braze.InAppMessage`, que define o comportamento básico e as características de todas as mensagens no app. Para obter a lista completa de propriedades e uso de mensagens no app, consulte a [classe `InAppMessage`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

Estes são os tipos de mensagens no app disponíveis na Braze e como eles serão exibidos para os usuários finais.

{% subtabs %}
{% subtab Slideup %}

As mensagens no app [`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) recebem esse nome porque "deslizam para cima" ou "deslizam para baixo" a partir da parte superior ou inferior da tela. Elas cobrem uma pequena parte da tela e fornecem um recurso de envio de mensagens eficaz e não intrusivo.

![Uma mensagem no app em slideup na parte inferior e superior da tela do telefone.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endsubtab %}
{% subtab Modal %}

As mensagens no app [`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) aparecem no centro da tela e são emolduradas por um painel translúcido. Úteis para o envio de mensagens mais críticas, elas podem ser equipadas com até dois botões habilitados para análise de dados.

![Uma mensagem modal no app no centro da tela do telefone.]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Modal Image %}

As mensagens no app [`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) aparecem no centro da tela e são emolduradas por um painel translúcido. Essas mensagens são semelhantes ao tipo `Modal`, mas sem cabeçalho ou texto de mensagem. Úteis para o envio de mensagens mais críticas, elas podem ser equipadas com até dois botões habilitados para análise de dados.

![Uma mensagem no app com imagem modal no centro da tela do telefone.]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Fullscreen %}

As mensagens no app [`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) são úteis para maximizar o conteúdo e o impacto da sua comunicação com o usuário. A metade superior de uma mensagem no app `Full` contém uma imagem, e a metade inferior exibe texto e até dois botões habilitados para análise de dados.

![Uma mensagem no app em tela inteira exibida em toda a tela do telefone.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Full Screen Image %}

As mensagens no app [`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) são semelhantes às mensagens no app `Full`, exceto pelo fato de não terem cabeçalho ou texto de mensagem. Esse tipo de mensagem é útil para maximizar o conteúdo e o impacto da sua comunicação com o usuário. Uma mensagem no app `Full Image` contém uma imagem que abrange toda a tela, com a opção de exibir até dois botões habilitados para análise de dados.

![Uma mensagem no app com imagem em tela inteira exibida em toda a tela do telefone.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Custom HTML %}

As mensagens no app [`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) são úteis para criar conteúdo totalmente personalizado para o usuário. O conteúdo completo da mensagem no app em HTML definido pelo usuário é exibido em um `WKWebView` e pode, opcionalmente, conter outros conteúdos avançados, como imagens e fontes, permitindo controle total sobre a aparência e a funcionalidade da mensagem. <br><br>As mensagens no app do iOS suportam uma interface JavaScript `brazeBridge` para chamar métodos no Braze Web SDK or kit de desenvolvimento de software a partir do seu HTML; consulte nossas [práticas recomendadas]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices) para obter mais detalhes.

O exemplo a seguir mostra uma mensagem no app paginada em HTML Full:

![Uma mensagem no app em HTML com um carrossel de conteúdo e botões interativos.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Observe que atualmente não oferecemos suporte à exibição de mensagens no app em HTML personalizado em um iFrame nas plataformas iOS e Android.

{% endsubtab %}
{% subtab Control %}

As mensagens no app [`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) não contêm um componente de interface do usuário e são usadas principalmente para fins de análise de dados. Esse tipo é usado para verificar o recebimento de uma mensagem no app enviada a um grupo de controle.

Para mais detalhes sobre otimização automática de variantes e grupos de controle, consulte [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
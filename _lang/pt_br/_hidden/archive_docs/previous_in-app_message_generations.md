---
nav_title: Gerações anteriores
article_title: Gerações anteriores de mensagens no app
page_order: 20
page_type: reference
description: "Este artigo revisa informações anteriores sobre mensagens no app na Braze."
channel: in-app messages
noindex: true
hidden : true
---

# Gerações anteriores de mensagens no app {#previous-in-app-message-generations}

{% alert important %}
Esta página revisa informações anteriores sobre nossas mensagens no app. Para ver as informações mais atualizadas sobre nossa geração atual de mensagens no app, consulte nossa documentação atual de [mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/).
{% endalert %}

## Universal

Esta seção revisa informações anteriores sobre nossas mensagens no app. Para ver as informações mais atualizadas sobre nossa geração atual de mensagens no app, consulte nossa [documentação de visão geral de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/).

{% details Tela cheia %}
Estas são as mais envolventes, mas também as mais intrusivas, pois cobrem toda a tela do usuário. São ótimas para exibir imagens grandes e ricas, e podem ser úteis para transmitir informações muito importantes, como novos recursos cruciais e promoções que estão expirando. Como são mais disruptivas para a experiência do usuário, use-as com moderação para conteúdo de alta prioridade.

![Mensagem em tela cheia]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**Recursos personalizáveis**

- Texto de cabeçalho e corpo
- Uma imagem grande
- Até dois botões de call to action com comportamento ao clicar e deep links separados
- Cores diferentes para o texto do cabeçalho e do corpo, botões e fundo
- Pares chave-valor

{% enddetails %}
{% details  Modal %}
Essas mensagens não são tão intrusivas quanto as mensagens em tela cheia, pois ainda permitem que os usuários vejam parte da interface do seu app. Como ainda contêm botões e imagens, as mensagens modais podem ser uma opção melhor do que os slideups se você deseja uma campanha mais interativa e visual. São ótimas para conteúdo de prioridade média, como atualizações de app e ofertas e eventos não urgentes.

![Mensagem modal]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**Recursos personalizáveis**

- Texto de cabeçalho e corpo
- Uma imagem ou ícone de emblema personalizável
- Até dois botões de call to action com comportamento ao clicar e deep links separados
- Cores diferentes para o texto do cabeçalho e do corpo, botões e fundo
- Pares chave-valor

{% enddetails %}

{% details Slideup tradicional %}
Estas são as mensagens menos intrusivas, embora possam ser mais ou menos chamativas dependendo do seu uso de cores e ícones de emblema. Este pode ser o formato de mensagem a ser usado ao integrar novos usuários e direcioná-los para recursos específicos no app, pois não pausam a experiência do app e permitem uma exploração contínua.

![Mensagem slideup]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**Recursos personalizáveis**

- Texto do corpo
- Uma imagem ou ícone de emblema personalizável
- Cores diferentes para o fundo, texto e ícone do slideup
- Comportamento de fechamento de mensagem
- Posição do slideup (parte superior ou inferior da tela do app)
- Pares chave-valor

{% enddetails %}

<br>

## Web

Esta seção revisa informações anteriores sobre mensagens no app mais personalizadas. Para ver as informações mais atualizadas sobre nossa geração atual de mensagens no app, consulte nossa [documentação de personalização]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/).

{% details Mensagem de captura de e-mail %}
Mensagens de captura de e-mail permitem que você solicite facilmente aos usuários do seu site que enviem seu endereço de e-mail, após o qual ele estará disponível no sistema da Braze para uso em todas as suas campanhas de envio de mensagens.

![Mensagem de captura de e-mail]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  Para ativar mensagens no app de captura de e-mail através do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` para a Braze, por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso ocorre por motivos de segurança, pois as mensagens HTML no app podem executar JavaScript, portanto, exigimos que um mantenedor do site as ative.

**Recursos personalizáveis**

- Texto do cabeçalho, corpo e botão de envio
- Uma imagem opcional
- Um link opcional para os "Termos de Serviço"
- Cores diferentes para o texto do cabeçalho e do corpo, botões e fundo
- Pares chave-valor

{% enddetails %}

{% details Mensagem HTML personalizada %}

Embora as mensagens no app padrão da Braze possam ser personalizadas de várias maneiras, você pode ter um controle ainda maior sobre a aparência das suas campanhas usando mensagens projetadas e construídas com HTML, CSS e JavaScript. Com algumas composições simples, você pode desbloquear funcionalidades e identidade visual personalizadas para atender a qualquer uma das suas necessidades. Mensagens no app em HTML permitem maior controle sobre a aparência de uma mensagem, e tudo o que é compatível com HTML5 também é compatível com a Braze.

**Ponte JavaScript (appboyBridge)**

As mensagens em HTML no app suportam uma interface de "ponte" JavaScript para o Braze Web SDK, permitindo que você dispare ações personalizadas da Braze quando os usuários clicam em elementos com links ou interagem de outra forma com seu conteúdo. Os seguintes métodos JavaScript são suportados nas mensagens no app em HTML da Braze:

{% multi_lang_include archive/appboyBridge.md platform="web" %}

Além disso, para rastreamento de análise de dados, quaisquer elementos `<a>` ou `<button>` no seu HTML registrarão automaticamente uma ação de "clique" na campanha associada à mensagem no app. Para registrar um "clique no botão" em vez de um "clique no corpo", forneça um valor de string de consulta abButtonId no href do seu link (por exemplo, `<a href="http://mysite.com?abButtonId=0">click me</a>`), ou forneça um id no elemento HTML (por exemplo, `<a id="0" href="http://mysite.com">click me</a>`). Observe que os únicos IDs de botões atualmente aceitos são "0" e "1". Um link com um id de botão 0 será representado como "Button 1" no dashboard, enquanto um link com um id de botão 1 será representado como "Button 2".

>  Para ativar mensagens no app em HTML através do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` para a Braze, por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso ocorre por motivos de segurança, pois as mensagens HTML no app podem executar JavaScript, portanto, exigimos que um mantenedor do site as ative.

{% enddetails %}

{% details Modelos de mensagens no app em HTML %}

Nós projetamos um conjunto de modelos de mensagens no app em HTML5 para ajudar você a dar os primeiros passos. Confira nosso [repositório GitHub](https://github.com/braze-inc/in-app-message-templates) que contém instruções detalhadas sobre como usar e personalizar esses modelos para suas necessidades.

**Recursos personalizáveis**

- Fontes
- Estilos
- Imagens + Vídeos
- Comportamentos ao clicar
- Componentes interativos

{% enddetails %}

<br>

## Especificações {#specifications}

Esta seção revisa informações anteriores sobre nossas especificações criativas de mensagens no app. Para ver as informações mais atualizadas sobre nossa geração atual de mensagens no app, consulte nossa [documentação de especificações criativas]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/).

### Limites de caracteres e imagens {#character-and-image-limits}

Para todos os tipos de mensagens no app listados na tabela a seguir, aplicam-se as seguintes diretrizes adicionais:

- **Tamanho de imagem recomendado:** 500&nbsp;KB
- **Tamanho máximo da imagem:** 5&nbsp;MB
- **Tipos de arquivos suportados:** PNG, JPEG, GIF

| Tipo                               | Proporção | Contagem máxima de caracteres |
| :--------------------------------- | :----------: | :-----------------: |
| Retrato em tela cheia (apenas imagem)  |    10:16     |         240         |
| Retrato em tela cheia (com texto)   |     5:4      |         240         |
| Paisagem em tela cheia (com texto)  |     16:5     |         240         |
| Paisagem em tela cheia (apenas imagem) |    16:10     |         240         |
| Slideup                            |     1:1      |         140         |
| Modal (apenas imagem)                 |     1:1      |         140         |
| Modal (com texto)                  |    29:10     |         140         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Limites de caracteres e imagens" }

### Manter os tamanhos dos arquivos de mensagens no app pequenos {#keeping-in-app-message-file-sizes-small}

A Braze recomenda que você mantenha suas imagens e arquivos ZIP de ativos HTML o menor possível por várias razões:

- Cargas úteis menores de HTML e imagens serão baixadas mais rapidamente e exibidas de forma mais rápida e confiável para seus clientes.
- Cargas úteis menores de HTML e imagens também manterão os custos de dados dos seus clientes baixos. As mensagens no app da Braze são baixadas em segundo plano no início da sessão para que possam ser disparadas em tempo real com base em qualquer critério que você selecionar. Como resultado, se você tiver 10 mensagens HTML no app de 1&nbsp;MB cada, seus clientes incorrerão em 10&nbsp;MB de cobranças de dados, mesmo que nunca tenham disparado todas essas mensagens. Isso pode se acumular rapidamente ao longo do tempo, mesmo que as mensagens no app sejam armazenadas em cache e não sejam baixadas novamente de sessão para sessão.

As seguintes estratégias são úteis para manter o tamanho dos arquivos baixo:

- Referencie fontes incorporadas no seu aplicativo ou site para personalizar suas mensagens HTML no app em vez de incluir os arquivos de fontes na sua pasta ZIP de ativos HTML.
- Certifique-se de que não haja CSS ou JavaScript extra ou duplicado nos ZIPs de ativos HTML.
- Use [ImageOptim](https://imageoptim.com/) em todas as imagens para comprimi-las ao tamanho mínimo possível sem redução na qualidade.

### Especificações do iPhone 5 {#iphone-5-specs}

![Especificações do iPhone 5]({% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %})

### Especificações do iPhone 6 {#iphone-6-specs}

![Especificações do iPhone 6]({% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %})
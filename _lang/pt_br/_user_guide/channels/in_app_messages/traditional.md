---
nav_title: Editor tradicional
article_title: Criar uma mensagem no app no editor tradicional
page_order: 2
description: "Este artigo de referência aborda como criar uma mensagem no app usando a plataforma da Braze por meio de Campaigns ou Canvas."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Criar uma mensagem no app com o editor tradicional {#create-an-in-app-message-with-the-traditional-editor}

> Você pode criar uma mensagem no app ou uma mensagem no navegador usando a plataforma da Braze por meio de Campaigns, Canvas ou como uma campanha da API or interface de programação do aplicativo (API). Recomendamos fortemente que você planeje suas mensagens e prepare todos os materiais com antecedência usando nosso prático [Guia de preparação de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices).

## Etapa 1: Escolha onde criar sua mensagem {#create-new-campaign-in-app}

Não tem certeza se sua mensagem deve ser enviada usando uma Campaign ou um Canvas? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas são melhores para jornadas de usuários com várias etapas.

{% tabs %}
{% tab Campaign %}

1. Acesse **Messaging** > **Campaigns** e selecione **Create Campaign**.
2. Selecione **In-App Message**. Observe que mensagens no app não estão disponíveis em campanhas multicanal.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.
   * Tags facilitam a busca e a criação de relatórios das suas campanhas. Por exemplo, ao usar o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagem e layouts para cada variante adicionada. Para saber mais sobre esse tópico, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Se todas as mensagens da sua campanha forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes extras. Em seguida, escolha **Copy from Variant** no menu suspenso **Add Variant**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

{% multi_lang_include messaging/canvas_message_step_setup.md in_app_message=true %}

{% alert important %}
Não é possível ter múltiplas variantes de mensagem no app em uma única etapa.
{% endalert %}

Você pode encontrar mais informações específicas sobre Canvas em [Mensagens no app no Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Etapa 2: Especificar plataformas de entrega {#step-2-specify-delivery-platforms}

Comece escolhendo quais plataformas devem receber a mensagem. Use essa seleção para limitar a entrega de uma campanha a um conjunto específico de apps. Por exemplo, você pode escolher **Navegadores web** para uma mensagem no navegador incentivando os usuários a baixar seu app mobile, garantindo que eles não recebam a mensagem depois de já terem baixado o app. Como as seleções de plataforma são específicas para cada variante, você pode testar o engajamento com mensagem por plataforma.

| Plataforma                        | Entrega de mensagem             |
|---------------------------------|------------------------------|
| Apps mobile                     | SDKs para iOS, Android e Vega |
| Navegadores web                    | SDK or kit de desenvolvimento de software para web                      |
| Apps mobile e navegadores web | SDKs para iOS, Android, Vega e web |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Especificar plataformas de entrega" }

## Etapa 3: Especifique seus tipos de mensagem {#step-3-specify-your-message-types}

Depois de selecionar uma plataforma de envio, navegue pelos tipos de mensagem, layouts e outras opções associadas a ela. Saiba mais sobre o comportamento esperado e a aparência de cada uma dessas mensagens na nossa página [Tipos de mensagem]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types), ou clicando nos tipos de mensagem vinculados nas tabelas a seguir.

Ao decidir qual tipo de mensagem usar, considere quanto espaço sua mensagem vai ocupar e o quanto ela pode ser disruptiva para a experiência do usuário.

- As mensagens **Slideup** são as menos intrusivas, aparecendo sutilmente sem bloquear o conteúdo.
- As mensagens **Modal** ficam no meio-termo — visíveis o suficiente para chamar a atenção sem tomar a tela inteira.
- As mensagens **Fullscreen** são as que mais chamam a atenção e são ideais para anúncios críticos ou promoções.

Quanto mais complexo for o seu conteúdo, mais espaço você vai precisar — e mais provável será que sua mensagem interrompa o fluxo do usuário.

### Tipos de mensagem {#message-types}

Essas mensagens no app são aceitas tanto por apps para dispositivos móveis quanto por aplicações web.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table aria-label="Tipos de mensagem" class="tg">
  <caption>Tipos de mensagem</caption>
<thead>
  <tr>
    <th>Tipo de mensagem</th>
    <th>Descrição do tipo</th>
    <th>Layouts disponíveis</th>
    <th>Outras opções</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/fullscreen'>Fullscreen</a></td>
    <td>Mensagens que cobrem a tela inteira com um bloco de mensagem.</td>
    <td>
      <ul>
      <li>Imagem e texto</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>Orientação do dispositivo forçada (retrato ou paisagem)</td>
    <td>Grande e ousada! Use quando quiser garantir que os usuários vejam seu conteúdo, como nas Campaigns mais importantes, notificações essenciais ou grandes promoções.<br><br>Observe que, em dispositivos móveis, as mensagens em retrato e paisagem não serão exibidas se a orientação do dispositivo não corresponder à orientação da mensagem.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/modal'>Modal</a></td>
    <td>Mensagens que cobrem a tela inteira com uma sobreposição e um bloco de mensagem.</td>
    <td>
      <ul>
      <li>Texto (com imagem opcional)</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>N/D</td>
    <td>Um bom meio-termo. Use quando precisar de uma forma visível de chamar a atenção do usuário, como incentivar usuários a experimentar um novo recurso ou aproveitar uma promoção.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/slideup'>Slideup</a></td>
    <td>Mensagens que deslizam para a visualização em um local designado sem bloquear o restante da tela.</td>
    <td>N/D</td>
    <td>N/D</td>
    <td>Discretas — ocupam a menor quantidade de espaço na tela. Use para alertar os usuários sobre pequenas informações, como novos recursos, anúncios, uso de cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Tipos de mensagem avançados {#advanced-message-types}

Essas mensagens no app são personalizáveis de acordo com suas necessidades.

<table aria-label="Tipos de mensagem avançados" class="tg">
  <caption>Tipos de mensagem avançados</caption>
<thead>
  <tr>
    <th>Tipo de mensagem</th>
    <th>Descrição do tipo</th>
    <th>Layouts disponíveis</th>
    <th>Requisitos</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/custom_html'>Mensagem HTML personalizada</a></td>
    <td>Mensagens personalizadas que funcionam conforme definido no seu código personalizado (HTML, CSS e/ou JavaScript).</td>
    <td>N/D</td>
    <td>É necessário definir a opção de inicialização <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> como <code>true</code> para que sua mensagem no app funcione.</td>
    <td>Essa é uma boa opção se você quer todas as vantagens das mensagens no app, mas precisa de funcionalidades adicionais ou que a aparência permaneça "dentro da marca". Você pode alterar cada detalhe da mensagem — fonte, cor, formato, tamanho, botões, etc. <br><br>Exemplos de casos de uso incluem solicitar feedback dos usuários sobre o app, formulários de captura de e-mail ou mensagens paginadas</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/email_capture_form'>Formulário de captura de e-mail</a></td>
    <td>Geralmente usado para capturar o e-mail do visualizador.</td>
    <td>N/D</td>
    <td>É necessário definir a opção de inicialização <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> como <code>true</code> para que sua mensagem no app funcione.</td>
    <td>Quando você quer solicitar que os usuários enviem seu endereço de e-mail.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/customize#web-modal-css'>Modal web com CSS</a></td>
    <td>Mensagens modais para web com CSS personalizável.</td>
    <td>
      <ul>
      <li>Texto (com imagem opcional)</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>Modal web com CSS é exclusivo do SDK or kit de desenvolvimento de software para web e só pode ser usado após selecionar <b>Web Browsers</b>.</td>
    <td>Quando você quer fazer upload ou escrever CSS personalizado para criar mensagens estilizadas e bonitas. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Se a Braze detectar que você não incluiu um botão de fechar ou dispensar no seu código, solicitaremos que você adicione um. Para sua conveniência, fornecemos um snippet que você pode copiar e colar no seu código: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Etapa 4: Componha sua mensagem no app {#step-4-compose-your-in-app-message}

A guia **Composição** permite que você edite todos os aspectos do conteúdo e do comportamento da sua mensagem.

![Exemplo de mensagem no app de uma marca para dar as boas-vindas a novos clientes e solicitar que configurem um perfil de usuário.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

O conteúdo da guia **Composição** varia de acordo com as opções de mensagem escolhidas na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

### Idioma {#language}

Selecione **Adicionar idiomas** e escolha os idiomas desejados na lista fornecida. Isso inserirá [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) na sua mensagem. Recomendamos selecionar os idiomas antes de escrever o conteúdo para que você possa preencher o texto nos locais adequados no Liquid. Consulte nossa [lista completa de idiomas disponíveis]({{site.baseurl}}/developer_guide/localization?tab=android).

### Imagem {#image}

Dependendo do tipo de mensagem, você pode **Fazer upload de imagem**, **Escolher um selo** ou usar o **Font Awesome**. Para fazer upload de uma imagem, selecione **Adicionar imagem** ou forneça uma URL de imagem. Ao selecionar **Adicionar imagem**, a **Biblioteca de mídia** será aberta, onde você pode selecionar uma imagem carregada anteriormente ou adicionar uma nova. Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos — verifique quais são antes de encomendar ou criar uma imagem do zero.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Cabeçalho e corpo {#header-and-body}

Escreva o que quiser! Inclua textos totalmente personalizados (muitas vezes com recursos de HTML personalizado) com as opções de incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) e outros tipos de personalização. Quanto mais rápido você conseguir transmitir sua mensagem e levar o cliente a clicar, melhor! Recomendamos cabeçalhos e conteúdos de mensagem claros e concisos.

Alguns tipos de mensagem não precisam de cabeçalhos e, portanto, não os solicitam.

#### Dicas {#tips}

##### Gerando textos com IA {#generating-ai-copy}

Precisa de ajuda para criar textos incríveis? Experimente usar o [Assistente de Copywriting com IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Insira o nome ou a descrição de um produto e a IA gerará textos de marketing semelhantes aos escritos por humanos para uso nas suas mensagens.

![Botão para iniciar o Assistente de Copywriting com IA, localizado no campo Mensagem do criador de mensagens no app.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Criando mensagens da direita para a esquerda {#creating-right-to-left-messages}

Precisa de ajuda para criar mensagens da direita para a esquerda em idiomas como árabe e hebraico? Consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) para conhecer as práticas recomendadas.

### Texto do botão {#buttons}

Quando disponível para o tipo de mensagem, você pode ter até dois botões exibidos abaixo do corpo do texto. Você pode criar e editar texto e cor personalizados para os botões. Também é possível adicionar um link de Termos de Serviço nos formulários de captura de e-mail.

Se você optar por usar apenas um botão, ele se ajustará automaticamente para ocupar o espaço disponível na parte inferior da mensagem, em vez de deixar espaço para um botão adicional.

#### Escolhendo um botão principal {#choosing-a-primary-button}

Se você decidir formatar esses botões com suas próprias cores, recomendamos que use o Botão 2 para o resultado que você mais deseja.

Em outras palavras, se você quer que o usuário clique em um botão mais do que no outro, certifique-se de que ele seja o botão secundário. O botão secundário costuma apresentar melhor potencial de cliques, especialmente se tiver uma cor de certo contraste ou destaque em relação ao restante da mensagem. Esse efeito é ainda mais acentuado quando o botão principal se mistura visualmente com a mensagem.

![Botões principal e secundário em uma mensagem no app]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportamento ao clicar {#button-actions}

Quando o cliente clica em um botão na mensagem no app, as seguintes ações estão disponíveis.

| Ação | Descrição |
|---|---|
| Redirecionar para URL da web | Abre uma página web não nativa. |
| [Deep link no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Faz um deep link para uma tela existente no seu app. |
| Fechar mensagem | Fecha a mensagem ativa no momento. |
| Registrar evento personalizado | Escolha um [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events) para disparar. Pode ser usado para exibir outra mensagem no app ou disparar envios de mensagens adicionais. |
| Registrar atributo personalizado | Escolha um [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) para definir para o usuário atual. |
| Solicitar permissão de push | Exibe a solicitação nativa de permissão de push. Saiba mais sobre [push priming]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), além das [práticas recomendadas]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#best-practices) para preparar os usuários para push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamento ao clicar #button-actions" }

Observação: as opções __Solicitar permissão de push__, __Registrar evento personalizado__ e __Registrar atributo personalizado__ exigem as seguintes versões mínimas do SDK or kit de desenvolvimento de software:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Para combinar várias ações ou realizar ações adicionais do SDK or kit de desenvolvimento de software não disponíveis no dashboard (como adicionar a um grupo de inscrições ou definir um tipo de inscrição de e-mail), você pode usar os [deep links do Braze Actions]({{site.baseurl}}/developer_guide/braze_actions).

### Opções de dispositivos iOS {#ios-device-options}

Se desejar, você pode restringir sua mensagem no app para envio apenas a dispositivos iOS. Para isso, clique em **Alterar** e selecione **Enviar apenas para dispositivos iOS**.

### Fechamento da mensagem {#message-close}

Escolha entre as seguintes opções:

- **Dispensar automaticamente:** selecione por quantos segundos a mensagem permanecerá na tela.
- **Aguardar deslize ou toque do usuário:** requer uma opção de dispensa ou fechamento.

Dispensar uma mensagem registra uma impressão, mas não um clique. Para saber como os cliques são rastreados por ação do usuário, consulte [Rastreamento de cliques]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting#click-tracking).

### Posição do slideup {#slide-up-position}

Essa configuração se aplica apenas ao tipo de mensagem slideup. Escolha entre fazer o slideup aparecer **A partir da parte inferior da tela do app** ou **A partir da parte superior da tela do app**.

### HTML e ativos {#html-and-assets}

Essa configuração se aplica apenas ao tipo de mensagem de código personalizado. Copie e cole o HTML no espaço disponível e faça upload dos seus ativos usando um [arquivo ZIP]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#zip-file-uploads).

### Texto de placeholder para captura de e-mail {#email-capture-input-placeholder}

Essa configuração se aplica apenas ao tipo de mensagem de formulário de captura de e-mail. Insira um texto personalizado que aparecerá como placeholder no campo de entrada de e-mail. O texto padrão é "Enter your email address".

## Etapa 5: Estilize sua mensagem no app {#step-5-style-your-in-app-message}

A guia **Style** permite que você ajuste todos os aspectos visuais da sua mensagem. Faça upload de uma imagem ou badge, ou escolha um ícone de badge pré-projetado. Altere as cores do texto do cabeçalho e do corpo, botões e fundo selecionando de uma paleta ou inserindo um código hex, RGB ou HSB.

O conteúdo da guia **Style** varia com base nas opções de mensagem escolhidas na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

| Formatação | Entrada | Descrição |
|---|---|---|
| [Perfil de cor]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#reusable-color-profiles) | Aplicar a partir da galeria de modelos de mensagens no app. | Selecione **Apply Template** e escolha na galeria. Em seguida, selecione **Save**. |
| Alinhamento do texto | Esquerda, centro ou direita. | Disponível apenas para versões mais recentes do SDK or kit de desenvolvimento de software da Braze. |
| Cabeçalho | Código de cor HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
| Texto | Código de cor HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
| Botões | Código de cor HEX. | As cores HEX desejadas serão exibidas. Você também poderá escolher a opacidade das cores. Você pode escolher cores para: o fundo do botão de fechar da mensagem, bem como o fundo, texto e borda de cada botão. |
| Borda do botão | Código de cor HEX. | Novo! Isso permitirá que você diferencie seus botões principal e secundário. Sugerimos contornar os botões com cores contrastantes. |
| Cor de fundo | Código de cor HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. Este é o fundo de toda a mensagem e será exibido claramente atrás do corpo do texto. |
| Sobreposição de tela | Código de cor HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. Disponível apenas para versões mais recentes do SDK or kit de desenvolvimento de software da Braze. Este é o quadro ao redor de toda a mensagem. |
| Seta ou outra opção de fechar mensagem | Código de cor HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 5: Estilize sua mensagem no app" }

Sempre [pré-visualize e teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) sua mensagem antes de enviar.

{% alert important %}
Alguns tipos de mensagem no app não possuem a opção de estilização além do upload de HTML personalizado (ou CSS ou JavaScript) e ativos usando um arquivo ZIP. [Modal web com CSS]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#web-modal-css) permite que você faça upload ou escreva CSS personalizado para criar mensagens bonitas e totalmente estilizadas.
{% endalert %}

## Etapa 6: Configurar definições adicionais (opcional) {#step-6-configure-additional-settings-optional}

### Pares de chave-valor {#key-value-pairs}

Você pode adicionar [pares de chave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) para enviar campos personalizados extras para os dispositivos dos usuários.

## Etapa 7: Monte o restante da sua campanha ou Canvas {#step-7-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Monte o restante da sua campanha; consulte as seções a seguir para mais orientações sobre como usar nossas ferramentas para criar mensagens no app.

### Escolha um gatilho {#choose-a-trigger}

Selecione a ação que deseja usar para disparar sua mensagem, bem como os horários de início e término da sua campanha ou Canvas.

{% alert important %}
Se você pretende disparar sua mensagem no app com base em um evento personalizado, esse evento personalizado deve ser enviado pelo SDK or kit de desenvolvimento de software.
{% endalert %}

![Campaign baseada em ação com a ação-gatilho definida como "Start Session".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

A entrega de mensagens no app é inteiramente baseada nos seguintes gatilhos de ação:

- Realizar um pedido
- Abrir o app ou a página da web
- Executar um evento personalizado (funciona apenas com eventos enviados pelo SDK or kit de desenvolvimento de software)
- Abrir uma mensagem push específica
- Agendar automaticamente campanhas para envio em um horário específico com base no fuso local de cada usuário.
- As mensagens também podem ser configuradas para recorrer diariamente, semanalmente (opcionalmente em dias específicos) ou mensalmente.

Uma data e horário de início devem ser selecionados; no entanto, uma data de término é opcional. Uma data de término impede que a mensagem no app específica seja exibida nos dispositivos após a data/horário especificado.

Consulte nossa documentação para desenvolvedores sobre [disparo de eventos no lado do servidor]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web) e [entrega local de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web).

#### Disparo online versus offline {#online-versus-offline-triggering}

As mensagens no app funcionam enviando a mensagem e os gatilhos para o dispositivo do usuário. Quando as mensagens no app estão no dispositivo, elas aguardam até que a condição de disparo seja atendida. Se as mensagens no app já estiverem em cache no dispositivo do usuário, você pode até disparar mensagens no app offline, sem conexão com a Braze (por exemplo, em modo avião).

{% alert important %}
Quando uma mensagem no app é interrompida, alguns usuários podem continuar vendo a mensagem se iniciaram uma sessão antes da interrupção e, em seguida, realizaram o evento-gatilho. Esses usuários serão contabilizados como uma impressão única mesmo depois que a campanha for interrompida.
{% endalert %}

### Escolha uma prioridade {#choose-a-priority}

Por fim, depois de selecionar a ação que disparará a mensagem no app, você também deve definir uma prioridade. Se duas mensagens forem disparadas pela mesma ação, as mensagens de alta prioridade serão agendadas para exibição nos dispositivos dos usuários antes das mensagens com prioridades mais baixas.

Você pode escolher entre as seguintes prioridades de mensagem:

- Alta prioridade (exibida antes de outras mensagens)
- Média prioridade (padrão)
- Baixa prioridade (exibida após outras mensagens)

As opções de alta, média e baixa prioridade para mensagens disparadas são agrupamentos, e, portanto, várias mensagens podem ter a mesma prioridade selecionada. Quando várias mensagens compartilham a mesma prioridade, a mensagem criada ou atribuída mais recentemente tem precedência e é exibida primeiro:

- **Agrupamento de prioridade padrão:** quando duas campanhas compartilham o mesmo gatilho e usam a prioridade padrão (média), a campanha criada por último recebe o disparo.
- **Agrupamento de prioridade específica:** quando várias campanhas compartilham o mesmo gatilho e são atribuídas a um agrupamento de prioridade específica, a campanha atribuída mais recentemente a esse agrupamento recebe o disparo.

Para definir prioridades dentro desses agrupamentos, clique em **Set exact priority** e você poderá arrastar e soltar campanhas para ordená-las com a prioridade correta.

![Um exemplo de como a prioridade é definida para uma campanha de mensagem no app e Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

### Escolha os usuários-alvo {#choose-users-to-target}

Em seguida, você deve [direcionar os usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) escolhendo Segments ou filtros para refinar seu público. Você recebe automaticamente um snapshot da população aproximada desse Segment or segmento. Lembre-se de que a associação exata ao Segment or segmento é sempre calculada antes do envio da mensagem.

{% alert note %}
Se houver uma postergação na etapa de mensagem no app, a associação ao Segment or segmento será avaliada após a postergação. Se o usuário for elegível, a mensagem no app será sincronizada na próxima sessão disponível.
{% endalert %}

#### Reavaliar a elegibilidade da campanha e Liquid {#re-evaluate-campaign-eligibility-and-liquid}

Em alguns cenários, você pode querer reavaliar a elegibilidade de um usuário quando ele dispara uma mensagem no app para exibição. Exemplos incluem campanhas que segmentam um atributo personalizado que muda com frequência ou mensagens que devem refletir quaisquer mudanças de última hora no perfil.

![Caixa de seleção "Re-evaluate campaign eligibility before displaying" marcada.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Quando você seleciona **Re-evaluate campaign eligibility before displaying**, uma solicitação adicional à Braze será feita para confirmar que o usuário ainda é elegível para esta mensagem antes do envio. Além disso, quaisquer variáveis [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ou [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) serão processadas nesse momento, antes de a mensagem ser exibida.

Isso impede que mensagens no app sejam enviadas a usuários em campanhas expiradas ou arquivadas. Se você não reavaliar a elegibilidade de um usuário, ele receberá a mensagem no app mesmo após a campanha ter expirado ou sido arquivada, pois a mensagem está no SDK or kit de desenvolvimento de software e aguardando o disparo pelo usuário.

{% alert note %}
Ativar esta opção resultará em um leve atraso (< 100ms) entre o momento em que o usuário dispara a mensagem no app e o momento em que a mensagem é exibida, devido à solicitação adicional de elegibilidade e processamento de templates.
<br><br>
Não use esta opção para mensagens que podem ser disparadas enquanto o usuário está offline ou quando a reavaliação de elegibilidade e Liquid não é necessária.
{% endalert %}

#### Usar dados adicionados pela REST or transferir estado representacional API or interface de programação do aplicativo (API) em uma mensagem {#use-data-added-by-rest-api-in-a-message}

Os dados do usuário que o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) adiciona na mesma sessão às vezes podem ser usados na mensagem no app desse usuário. Por exemplo, se um usuário está no público de uma mensagem no app que aguarda um gatilho, inicia uma sessão e, nessa mesma sessão, a REST or transferir estado representacional API or interface de programação do aplicativo (API) atualiza o perfil dele, esses novos dados podem aparecer na mensagem no app quando **Re-evaluate campaign eligibility before displaying** estiver selecionado. A Braze não processa o template da mensagem no app até que seja hora de renderizá-la.

Se um gatilho envia dados para a Braze e dispara a mensagem no app ao mesmo tempo, a mensagem não pode usar esses dados de perfil recém-atualizados, mesmo com uma postergação agendada. Em vez disso, use dois gatilhos separados: um para enviar os dados e outro para disparar a mensagem no app.

### Escolha eventos de conversão {#choose-conversion-events}

A Braze permite que você rastreie a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), após receberem uma campanha. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão será contabilizada se o usuário realizar a ação especificada.

{% endtab %}
{% tab Canvas %}

Se ainda não o fez, conclua as seções restantes do seu componente de Canvas. Para mais detalhes sobre como montar o restante do Canvas, incluindo testes multivariantes e [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consulte [Monte seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

Para informações sobre opções de mensagens no app específicas do Canvas, consulte [Mensagens no app no Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Etapa 8: Revisar e implantar {#step-8-review-and-deploy}

Depois de terminar de criar a última parte da sua Campaign ou Canvas, revise os detalhes, [faça um teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) e envie!

Em seguida, confira os [relatórios de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) para saber como acessar os resultados das suas campanhas de mensagens.

## Informações importantes {#things-to-know}

### Limites de campanhas de mensagem no app ativas {#active-in-app-message-campaign-limits}

A Braze valoriza confiabilidade e velocidade. Sugerimos que você envie apenas os dados necessários para a Braze e desative quaisquer campanhas que não agregam mais valor à sua marca.

O processamento de campanhas de mensagem no app baseadas em ações que ainda estão em estado ativo, mas que não estão mais enviando mensagens ou não são mais necessárias, prejudica o desempenho geral dos serviços da Braze para você e para outros clientes. O tempo extra necessário para processar esse grande número de campanhas sem atividades significa que qualquer mensagem no app levará mais tempo para aparecer nos dispositivos do usuário final, o que impacta a experiência do usuário final.

{% alert important %}
Você pode ter até 200 campanhas de mensagem no app ativas e baseadas em ações por espaço de trabalho para otimizar a velocidade de entrega de mensagens e evitar timeouts. Isso não se aplica a Canvas.
{% endalert %}

O limite de 200 inclui campanhas de mensagem no app ativas que ainda não atingiram a data de término e aquelas que não possuem data de término. Campanhas de mensagem no app ativas que já passaram da data de término não serão contabilizadas. O cliente médio da Braze tem um total de 26 campanhas ativas ao mesmo tempo, então é improvável que essa limitação tenha impacto para você.

### Avaliação da entrega no horário local {#local-time-delivery-evaluation}

Quando uma campanha de mensagem no app é agendada usando o fuso local do usuário, a avaliação do horário de início e término da campanha é feita no próprio dispositivo.

As campanhas de mensagem no app normalmente são enviadas ao dispositivo do usuário quando a sessão do app começa ou é atualizada. Nesse momento:

1. O SDK or kit de desenvolvimento de software avalia se o usuário se qualifica para alguma mensagem no app baseada em gatilho.
2. O dispositivo verifica se o evento-gatilho do usuário ocorreu dentro do horário de início e término da campanha (conforme definido pelo fuso local do usuário).
3. Se ambas as condições forem atendidas, a mensagem no app estará elegível para exibição.

#### Considerações {#considerations}

- Se um usuário dispara um evento (como o toque em um botão) logo após a mensagem no app ser entregue, a mensagem pode não aparecer até a próxima atualização de sessão — desde que todos os critérios de elegibilidade ainda sejam atendidos.
- Assim como outros tipos de canal, as campanhas de mensagem no app devem ser lançadas idealmente com 24 a 48 horas de antecedência. Essa margem dá aos usuários tempo suficiente para atender aos critérios de elegibilidade e iniciar uma sessão para que a mensagem seja avaliada e exibida.
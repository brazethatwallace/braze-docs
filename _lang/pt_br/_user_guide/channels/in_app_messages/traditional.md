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

> Você pode criar uma mensagem no app ou uma mensagem no navegador usando a plataforma da Braze por meio de Campaigns, Canvas ou como uma campanha da API. Recomendamos fortemente que você planeje suas mensagens e prepare todos os materiais com antecedência usando nosso prático [Guia de preparação de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices).

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

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando o criador de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor de Canvas. Dê à sua etapa um nome claro e significativo.
3. Escolha um [agendamento de etapa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) e especifique uma postergação conforme necessário. Observe que etapas contendo mensagens no app não podem ser baseadas em ação.
4. Filtre seu público para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários desta etapa especificando Segments e adicionando filtros adicionais. As opções de público serão verificadas após a postergação, no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
6. Escolha quaisquer outros canais de envio de mensagens que você deseja combinar com sua mensagem.

{% alert important %}
Não é possível ter múltiplas variantes de mensagem no app em uma única etapa.
{% endalert %}

Você pode encontrar mais informações específicas sobre Canvas em [Mensagens no app no Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Etapa 2: Especifique as plataformas de entrega {#step-2-specify-delivery-platforms}

Comece escolhendo quais plataformas devem receber a mensagem. Use essa seleção para limitar a entrega de uma campanha a um conjunto específico de apps. Por exemplo, você pode escolher **Web Browsers** para uma mensagem no navegador incentivando os usuários a baixar seu app móvel, garantindo que eles não recebam a mensagem depois de já terem obtido seu app. Como as seleções de plataforma são específicas para cada variante, você pode testar o engajamento com mensagem por plataforma.

| Plataforma | Entrega da mensagem |
|---------------------------------|------------------------------|
| Apps móveis | SDKs iOS, Android e Vega |
| Navegadores web | SDK Web |
| Apps móveis e navegadores web | SDKs iOS, Android, Vega e Web |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Especifique as plataformas de entrega" }

## Etapa 3: Especifique seus tipos de mensagem {#step-3-specify-your-message-types}

Depois de selecionar uma plataforma de envio, navegue pelos tipos de mensagem, layouts e outras opções associadas a ela. Saiba mais sobre o comportamento esperado e a aparência de cada uma dessas mensagens na nossa página de [Tipos de mensagem]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types), ou clicando nos tipos de mensagem vinculados nas tabelas a seguir.

Ao decidir qual tipo de mensagem usar, considere quanto espaço sua mensagem ocupará e o quão disruptiva ela pode parecer para a experiência do usuário.

- Mensagens **slideup** são as menos intrusivas, aparecendo sutilmente sem bloquear o conteúdo.
- Mensagens **modal** ficam no meio-termo — proeminentes o suficiente para chamar a atenção sem tomar conta totalmente da tela.
- Mensagens em **tela cheia** são as que mais chamam a atenção e são ideais para anúncios críticos ou promoções.

Quanto mais complexo for seu conteúdo, mais espaço você precisará — e maior a probabilidade de sua mensagem interromper o fluxo do usuário.

### Tipos de mensagem {#message-types}

Essas mensagens no app são aceitas tanto por apps móveis quanto por aplicações web.

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
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/fullscreen'>Tela cheia</a></td>
    <td>Mensagens que cobrem toda a tela com um bloco de mensagem.</td>
    <td>
      <ul>
      <li>Imagem e texto</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>Orientação do dispositivo forçada (retrato ou paisagem)</td>
    <td>Grande e impactante! Use quando quiser garantir que os usuários vejam seu conteúdo, como suas campanhas mais importantes, notificações essenciais ou grandes promoções.<br><br>Observe que em dispositivos móveis, mensagens em retrato e paisagem não serão exibidas se a orientação do dispositivo não corresponder à orientação da mensagem.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/modal'>Modal</a></td>
    <td>Mensagens que cobrem toda a tela com uma sobreposição e um bloco de mensagem.</td>
    <td>
      <ul>
      <li>Texto (com imagem opcional)</li>
      <li>Somente imagem</li>
      </ul>
    </td>
    <td>N/D</td>
    <td>Um bom meio-termo. Use quando precisar de uma forma evidente de chamar a atenção do usuário, como incentivar os usuários a experimentar um novo recurso ou aproveitar uma promoção.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/slideup'>Slideup</a></td>
    <td>Mensagens que deslizam para a visualização em um local designado sem bloquear o restante da tela.</td>
    <td>N/D</td>
    <td>N/D</td>
    <td>Discreta — ocupa a menor quantidade de espaço na tela. Use para alertar os usuários sobre pequenas informações, como novos recursos, anúncios, uso de cookies, etc.<br></td>
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
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/custom_html#custom-html-messages'>Mensagem HTML personalizada</a></td>
    <td>Mensagens personalizadas que funcionam conforme definido no seu código personalizado (HTML, CSS e/ou JavaScript).</td>
    <td>N/D</td>
    <td>É necessário definir a opção de inicialização <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> como <code>true</code> para que sua mensagem no app funcione.</td>
    <td>Essa é uma boa opção se você quer todas as vantagens das mensagens no app, mas precisa de funcionalidades adicionais ou que a aparência permaneça "dentro da marca". Você pode alterar cada detalhe da mensagem — fonte, cor, forma, tamanho, botões, etc. <br><br>Exemplos de casos de uso incluem pedir feedback sobre o app, formulários de captura de e-mail ou mensagens paginadas</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/channels/in_app_messages/message_types/email_capture_form#email-capture-form'>Formulário de captura de e-mail</a></td>
    <td>Normalmente usado para capturar o e-mail do visualizador.</td>
    <td>N/D</td>
    <td>É necessário definir a opção de inicialização <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> como <code>true</code> para que sua mensagem no app funcione.</td>
    <td>Quando solicitar que os usuários enviem seu endereço de e-mail.</td>
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
    <td>Modal web com CSS é exclusivo do SDK Web e só pode ser usado após selecionar <b>Web Browsers</b>.</td>
    <td>Quando você deseja fazer upload ou escrever CSS personalizado para criar mensagens bonitas e totalmente estilizadas.</td>
  </tr>
</tbody>
</table>

{% alert important %}
Se a Braze detectar que você não incluiu um botão de fechar ou dispensar no seu código, solicitaremos que você adicione um. Para sua conveniência, fornecemos um snippet que você pode copiar e colar no seu código: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Etapa 4: Redija sua mensagem no app {#step-4-compose-your-in-app-message}

A guia **Compose** permite que você edite todos os aspectos do conteúdo e comportamento da sua mensagem.

![Um exemplo de mensagem no app de uma marca para dar boas-vindas a novos clientes e incentivá-los a configurar um perfil de usuário.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

O conteúdo da guia **Compose** varia com base nas opções de mensagem escolhidas na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

### Idioma {#language}

Selecione **Add Languages** e escolha os idiomas desejados na lista fornecida. Isso inserirá [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) na sua mensagem. Recomendamos selecionar seus idiomas antes de escrever o conteúdo para que você possa preencher o texto nos locais corretos no Liquid. Consulte nossa [lista completa de idiomas disponíveis]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

### Imagem {#image}

Dependendo do tipo de mensagem, você pode **Upload Image**, **Pick a Badge** ou usar **Font Awesome**. Para fazer upload de uma imagem, selecione **Add Image** ou forneça uma URL de imagem. Selecionar **Add Image** abre a **Biblioteca de mídia**, onde você pode selecionar uma imagem carregada anteriormente ou adicionar uma nova. Cada tipo de mensagem e plataforma pode ter suas próprias proporções e requisitos sugeridos — certifique-se de verificar quais são antes de encomendar ou criar uma imagem do zero.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Cabeçalho e corpo {#header-and-body}

Escreva o que quiser! Inclua texto totalmente personalizado (frequentemente com recursos de HTML personalizado) com as opções de incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) e outros tipos de personalização. Quanto mais rápido você conseguir transmitir sua mensagem e fazer seu cliente clicar, melhor! Recomendamos cabeçalhos e conteúdo de mensagem claros e concisos.

Alguns tipos de mensagem não precisam e, portanto, não solicitam cabeçalhos.

#### Dicas {#tips}

##### Gerando texto com IA {#generating-ai-copy}

Precisa de ajuda para criar textos incríveis? Experimente usar o [Assistente de Copywriting com IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Insira o nome ou a descrição de um produto e a IA gerará um texto de marketing semelhante ao humano para uso no seu envio de mensagens.

![Botão Iniciar Assistente de Copywriting com IA, localizado no campo Mensagem do criador de mensagens no app.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Criando mensagens da direita para a esquerda {#creating-right-to-left-messages}

Precisa de ajuda para criar mensagens da direita para a esquerda para idiomas como árabe e hebraico? Consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages) para melhores práticas.

### Texto do botão {#buttons}

Quando disponível para o seu tipo de mensagem, você pode ter até dois botões exibidos abaixo do corpo do texto. Você pode criar e editar texto e cor personalizados para os botões. Também é possível adicionar um link de Termos de Serviço em formulários de captura de e-mail.

Se você optar por usar apenas um botão, ele se ajustará automaticamente para ocupar o espaço disponível na parte inferior da sua mensagem, em vez de deixar espaço para um botão adicional.

#### Escolhendo um botão principal {#choosing-a-primary-button}

Se você decidir formatar esses botões com suas próprias cores, recomendamos usar o Botão 2 para o resultado que você mais deseja.

Em outras palavras, se você quer que o usuário clique em um botão mais do que no outro, certifique-se de que ele seja o botão secundário. O botão secundário frequentemente demonstra melhor potencial de ser clicado, especialmente se tiver uma cor um pouco contrastante ou que se destaque do restante da mensagem. Isso é ainda mais evidente quando o botão principal se mistura mais visualmente com a mensagem.

![Botões principal e secundário em uma mensagem no app]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportamento ao clicar {#button-actions}

Quando seu cliente clica em um botão na sua mensagem no app, as seguintes ações estão disponíveis.

| Ação | Descrição |
|---|---|
| Redirecionar para URL da web | Abre uma página web não nativa. |
| [Deep link para o app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) | Faz deep link para uma tela existente no seu app. |
| Fechar mensagem | Fecha a mensagem ativa no momento. |
| Registrar evento personalizado | Escolha um [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events) para disparar. Pode ser usado para exibir outra mensagem no app ou disparar envio de mensagens adicionais. |
| Registrar atributo personalizado | Escolha um [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) para definir para o usuário atual. |
| Solicitar permissão de push | Exibe a solicitação nativa de permissão de push. Leia mais sobre [push priming]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), bem como [melhores práticas]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#best-practices) para preparar os usuários para push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamento ao clicar" }

Observação: as opções __Solicitar permissão de push__, __Registrar evento personalizado__ e __Registrar atributo personalizado__ requerem as seguintes versões mínimas do SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Para combinar múltiplas ações ou realizar ações adicionais do SDK não disponíveis no dashboard (como adicionar a um grupo de inscrições ou definir um tipo de inscrição de e-mail), você pode usar [deep links de Braze Actions]({{site.baseurl}}/developer_guide/braze_actions).

### Opções de dispositivos iOS {#ios-device-options}

Se desejar, você pode restringir sua mensagem no app para enviar apenas para dispositivos iOS. Para isso, clique em **Change** e selecione **Only send to iOS devices**.

### Fechamento da mensagem {#message-close}

Escolha entre as seguintes opções:

- **Dismiss Automatically:** Selecione quantos segundos a mensagem permanecerá na tela.
- **Wait for User Swipe or Touch:** Requer uma opção de dispensar ou fechar.

### Posição do slideup {#slide-up-position}

Essa configuração se aplica apenas ao tipo de mensagem slideup. Escolha entre fazer seu slideup aparecer **From Bottom of App Screen** ou **From Top of App Screen**.

### HTML e ativos {#html-and-assets}

Essa configuração se aplica apenas ao tipo de mensagem de código personalizado. Copie e cole HTML no espaço disponível e faça upload dos seus ativos usando um arquivo ZIP.

### Placeholder de entrada de captura de e-mail {#email-capture-input-placeholder}

Essa configuração se aplica apenas ao tipo de mensagem de formulário de captura de e-mail. Insira um texto personalizado que aparecerá como texto de placeholder no campo de entrada de e-mail. O padrão é "Enter your email address".

## Etapa 5: Estilize sua mensagem no app {#step-5-style-your-in-app-message}

A guia **Style** permite que você ajuste todos os aspectos visuais da sua mensagem. Faça upload de uma imagem ou badge, ou escolha um ícone de badge pré-projetado. Altere as cores do texto do cabeçalho e do corpo, botões e fundo selecionando de uma paleta ou inserindo um código hex, RGB ou HSB.

O conteúdo da guia **Style** varia com base nas opções de mensagem escolhidas na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

| Formatação | Entrada | Descrição |
|---|---|---|
| [Perfil de cor]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#reusable-color-profiles) | Aplicar a partir da galeria de modelos de mensagens no app. | Selecione **Apply Template** e escolha na galeria. Em seguida, selecione **Save**. |
| Alinhamento do texto | Esquerda, centro ou direita. | Disponível apenas para versões mais recentes do SDK da Braze. |
| Cabeçalho | Código de cor HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
| Texto | Código de cor HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
| Botões | Código de cor HEX. | As cores HEX desejadas serão exibidas. Você também poderá escolher a opacidade das cores. Você pode escolher cores para: o fundo do botão de fechar da mensagem, bem como o fundo, texto e borda de cada botão. |
| Borda do botão | Código de cor HEX. | Novo! Isso permitirá que você diferencie seus botões principal e secundário. Sugerimos contornar os botões com cores contrastantes. |
| Cor de fundo | Código de cor HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. Este é o fundo de toda a mensagem e será exibido claramente atrás do corpo do texto. |
| Sobreposição de tela | Código de cor HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. Disponível apenas para versões mais recentes do SDK da Braze. Este é o quadro ao redor de toda a mensagem. |
| Seta ou outra opção de fechar mensagem | Código de cor HEX. | A cor HEX desejada será exibida. Você também poderá escolher a opacidade da cor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 5: Estilize sua mensagem no app" }

Sempre [pré-visualize e teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) sua mensagem antes de enviar.

{% alert important %}
Alguns tipos de mensagem no app não possuem a opção de estilização além do upload de HTML personalizado (ou CSS ou JavaScript) e ativos usando um arquivo ZIP. [Modal web com CSS]({{site.baseurl}}/user_guide/channels/in_app_messages/customize#web-modal-css) permite que você faça upload ou escreva CSS personalizado para criar mensagens bonitas e totalmente estilizadas.
{% endalert %}

## Etapa 6: Configure definições adicionais (opcional) {#step-6-configure-additional-settings-optional}

### Pares chave-valor {#key-value-pairs}

Você pode adicionar [pares chave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) para enviar campos personalizados extras para os dispositivos dos usuários.

## Etapa 7: Construa o restante da sua campanha ou Canvas {#step-7-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construa o restante da sua campanha; consulte as seções a seguir para mais orientações sobre como usar melhor nossas ferramentas para criar mensagens no app.

### Escolha um gatilho {#choose-a-trigger}

Selecione a ação que você deseja que dispare sua mensagem, bem como os horários de início e término da sua campanha ou Canvas.

{% alert important %}
Observe que, se você pretende disparar sua mensagem no app com base em um evento personalizado, esse evento personalizado deve ser enviado usando o SDK.
{% endalert %}

![Campanha baseada em ação com a ação-gatilho definida como "Start Session".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

A entrega de mensagens no app é inteiramente baseada nos seguintes gatilhos de ação:

- Realizar uma compra
- Abrir o app ou página web
- Realizar um evento personalizado (funciona apenas com eventos enviados usando o SDK)
- Abrir uma mensagem push específica
- Agendar automaticamente campanhas para envio em um determinado horário com relação ao horário local de cada um dos seus usuários.
- As mensagens também podem ser configuradas para recorrer diariamente, semanalmente (opcionalmente em dias específicos) ou mensalmente.

Uma data e hora de início devem ser selecionadas; no entanto, uma data de término é opcional. Uma data de término impedirá que essa mensagem no app específica apareça nos dispositivos após a data/hora especificada.

Consulte nossa documentação para desenvolvedores sobre [disparo de eventos no servidor]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web) e [entrega local de mensagens no app]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery#local-in-app-messages).

#### Disparo online versus offline {#online-versus-offline-triggering}

Mensagens no app funcionam enviando a mensagem e os gatilhos para o dispositivo do usuário. Depois que as mensagens no app estão no dispositivo, elas aguardam para serem exibidas até que a condição de gatilho seja atendida. Se as mensagens no app já estiverem em cache no dispositivo do usuário, você pode até disparar mensagens no app offline sem conexão com a Braze (por exemplo, no modo avião).

{% alert important %}
Depois que uma mensagem no app for interrompida, pode haver alguns usuários que continuem a ver a mensagem se iniciaram uma sessão antes de a mensagem ser interrompida e, posteriormente, realizarem o evento de gatilho. Esses usuários serão contados como uma impressão única mesmo após a campanha ter sido interrompida.
{% endalert %}

### Escolha uma prioridade {#choose-a-priority}

Por fim, depois de selecionar a ação que disparará a mensagem no app, você também deve definir uma prioridade. Se duas mensagens forem disparadas pela mesma ação, mensagens de alta prioridade serão agendadas para aparecer nos dispositivos dos usuários antes de mensagens com prioridades mais baixas.

Você pode escolher entre as seguintes prioridades de mensagem:

- Alta prioridade (exibida antes de outras mensagens)
- Prioridade média (padrão)
- Baixa prioridade (exibida após outras mensagens)

As opções de alta, média e baixa prioridade para mensagens disparadas são agrupamentos, e como tal, múltiplas mensagens podem ter a mesma prioridade selecionada. Quando múltiplas mensagens compartilham a mesma prioridade, a mensagem criada ou atribuída mais recentemente tem precedência e é exibida primeiro:

- **Agrupamento de prioridade padrão:** Quando duas campanhas compartilham o mesmo gatilho e usam a prioridade padrão (média), a campanha criada por último recebe o gatilho.
- **Agrupamento de prioridade específica:** Quando múltiplas campanhas compartilham o mesmo gatilho e são atribuídas a um agrupamento de prioridade específico, a campanha atribuída mais recentemente a esse agrupamento recebe o gatilho.

Para definir prioridades dentro desses agrupamentos, clique em **Set Exact Priority**, e você pode arrastar e soltar campanhas para ordená-las com a prioridade correta.

![Um exemplo de como a prioridade é definida para uma campanha de mensagem no app e Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

### Escolha os usuários-alvo {#choose-users-to-target}

Em seguida, você deve [direcionar os usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) escolhendo Segments ou filtros para restringir seu público. Você recebe automaticamente um snapshot de como é a população aproximada desse Segment. Tenha em mente que a associação exata ao Segment é sempre calculada antes de a mensagem ser enviada.

{% alert note %}
Se houver uma postergação na etapa de mensagem no app, a associação ao Segment será avaliada após a postergação. Se o usuário for elegível, a mensagem no app será sincronizada na próxima sessão disponível.
{% endalert %}

#### Reavaliar elegibilidade da campanha e Liquid {#re-evaluate-campaign-eligibility-and-liquid}

Em alguns cenários, você pode querer reavaliar a elegibilidade de um usuário quando ele dispara uma mensagem no app para exibição. Exemplos incluem campanhas que direcionam um atributo personalizado que muda frequentemente ou mensagens que devem refletir quaisquer alterações de perfil de última hora.

![Caixa de seleção "Re-evaluate campaign eligibility before displaying" marcada.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Quando você seleciona **Re-evaluate campaign eligibility before displaying**, uma solicitação adicional à Braze será feita para confirmar que o usuário ainda é elegível para esta mensagem antes de enviá-la. Além disso, quaisquer variáveis [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) ou [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) serão processadas naquele momento antes de a mensagem ser exibida.

Isso evita que mensagens no app sejam enviadas a usuários em campanhas expiradas ou arquivadas. Se você não reavaliar a elegibilidade de um usuário, ele receberá a mensagem no app mesmo após a campanha ter expirado ou sido arquivada, porque a mensagem está no seu SDK e aguardando que os usuários a disparem.

{% alert note %}
Habilitar essa opção resultará em um leve atraso (< 100ms) entre o momento em que um usuário dispara uma mensagem no app e o momento em que a mensagem é exibida, devido à solicitação adicional de elegibilidade e processamento de template.
<br><br>
Não use essa opção para mensagens que podem ser disparadas enquanto o usuário está offline ou quando a reavaliação de elegibilidade e Liquid não é necessária.
{% endalert %}

#### Usar dados adicionados pela REST API em uma mensagem {#use-data-added-by-rest-api-in-a-message}

Dados de usuário que o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) adiciona na mesma sessão podem, às vezes, ser usados na mensagem no app desse usuário. Por exemplo, se um usuário está no público de uma mensagem no app que está aguardando um gatilho, inicia uma sessão e, nessa mesma sessão, a REST API atualiza seu perfil, esses novos dados podem aparecer na mensagem no app quando **Re-evaluate campaign eligibility before displaying** estiver selecionado. A Braze não processará o template da mensagem no app até que seja hora de renderizá-la.

Se um gatilho envia dados para a Braze e dispara a mensagem no app ao mesmo tempo, a mensagem não pode usar esses dados de perfil recém-atualizados, mesmo com uma postergação agendada. Use dois gatilhos separados: um para enviar os dados e outro para disparar a mensagem no app.

### Escolha eventos de conversão {#choose-conversion-events}

A Braze permite que você rastreie com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), após receberem uma campanha. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão será contada se o usuário realizar a ação especificada.

{% endtab %}
{% tab Canvas %}

Se ainda não o fez, conclua as seções restantes do seu componente de Canvas. Para mais detalhes sobre como construir o restante do seu Canvas, implementar testes multivariantes e seleção inteligente, e mais, consulte a etapa [Construa seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) da nossa documentação de Canvas.

Para informações sobre opções de mensagens no app específicas do Canvas, consulte [Mensagens no app no Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

{% endtab %}
{% endtabs %}

## Etapa 8: Revise e implante {#step-8-review-and-deploy}

Depois de terminar de construir a última parte da sua campanha ou Canvas, revise seus detalhes, [teste-a]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) e depois envie!

Em seguida, confira [Relatórios de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) para saber como você pode acessar os resultados das suas campanhas de envio de mensagens.

## Informações importantes {#things-to-know}

### Limites de campanhas ativas de mensagens no app {#active-in-app-message-campaign-limits}

A Braze valoriza confiabilidade e velocidade. Sugerimos que você envie apenas os dados necessários para a Braze e desative quaisquer campanhas que não agreguem mais valor à sua marca.

O processamento de campanhas de mensagens no app baseadas em ação que ainda estão em estado ativo, mas não estão mais enviando mensagens ou não são mais necessárias, desacelera o desempenho geral dos serviços da Braze para você e outros clientes. Esse tempo extra necessário para processar esses grandes números de campanhas sem atividades significa que quaisquer mensagens no app levarão mais tempo para aparecer nos dispositivos dos usuários finais, o que impacta a experiência do usuário final.

{% alert important %}
Você pode ter até 200 campanhas ativas de mensagens no app baseadas em ação por espaço de trabalho para otimizar a velocidade de entrega de mensagens e evitar timeouts. Isso não se aplica a Canvas.
{% endalert %}

A contagem de 200 inclui campanhas ativas de mensagens no app que ainda não atingiram o horário de término e aquelas que não possuem horário de término. Campanhas ativas de mensagens no app que já passaram do horário de término não serão contadas. O cliente médio da Braze tem um total de 26 campanhas ativas ao mesmo tempo — portanto, é improvável que essa limitação afete você.

### Avaliação de entrega no horário local {#local-time-delivery-evaluation}

Quando uma campanha de mensagem no app é agendada usando o fuso horário local do usuário, a avaliação dos horários de início e término da campanha é feita no próprio dispositivo.

Campanhas de mensagens no app são normalmente enviadas para o dispositivo do usuário quando a sessão do app inicia ou é atualizada. Nesse momento:

1. O SDK avalia se o usuário se qualifica para quaisquer mensagens no app baseadas em gatilho.
2. O dispositivo verifica se o evento de gatilho do usuário ocorreu dentro do horário de início e término da campanha (conforme definido pelo fuso horário local do usuário).
3. Se ambas as condições forem atendidas, a mensagem no app estará elegível para exibição.

#### Considerações {#considerations}

- Se um usuário disparar um evento (como um toque em botão) logo após a mensagem no app ser entregue, a mensagem pode não aparecer até a próxima atualização de sessão — assumindo que todos os critérios de elegibilidade ainda sejam atendidos.
- Semelhante a outros tipos de canal, campanhas de mensagens no app devem idealmente ser lançadas com 24 a 48 horas de antecedência. Esse intervalo dá aos usuários tempo suficiente para atender aos critérios de elegibilidade e iniciar uma sessão para que a mensagem seja avaliada e exibida.
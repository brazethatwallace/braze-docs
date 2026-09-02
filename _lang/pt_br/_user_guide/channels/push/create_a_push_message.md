---
nav_title: "Criar uma mensagem push"
article_title: "Criar uma mensagem push"
page_order: 1
page_type: tutorial
description: "Esta página de tutorial aborda os diferentes componentes envolvidos na criação de uma mensagem push, incluindo configuração, envio, direcionamento e mais."
channel: push
tool:
  - Campaigns




---

# Criar uma mensagem push {#create-a-push-message}

> As notificações por push são excelentes para chamadas à ação urgentes, bem como para reengajar usuários que não acessam o app há algum tempo. Campaigns de push bem-sucedidas direcionam o usuário diretamente ao conteúdo e demonstram o valor do seu app. Para ver exemplos de notificações por push, confira os [estudos de caso da Braze](https://www.braze.com/customers).

## Etapa 1: Escolha onde criar sua mensagem {#create-new-campaign-push}

{% alert tip %}
Não tem certeza se deve usar uma Campaign ou um Canvas? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas é melhor para jornadas de usuário com várias etapas.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Acesse **Envio de mensagens** > **Campaigns** e selecione **Criar Campaign**.
2. Para Campaigns direcionadas a múltiplos canais, selecione **Multicanal**. Caso contrário, selecione **Notificação por push**.
3. Dê à sua Campaign um nome claro e significativo.
4. Adicione [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) e [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) conforme necessário.

{% alert tip %}
Tags facilitam encontrar suas Campaigns e criar relatórios a partir delas. Por exemplo, ao usar o [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder), você pode filtrar por tags específicas.
{% endalert %}

{: start="5"}
5. Adicione e nomeie quantas variantes forem necessárias para sua Campaign. Você pode escolher diferentes plataformas, tipos de mensagem e layouts para cada variante adicionada. Para saber mais sobre esse assunto, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Se todas as mensagens da sua Campaign forem semelhantes ou tiverem o mesmo conteúdo, redija sua mensagem antes de adicionar variantes adicionais. Depois, você pode escolher **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## Etapa 2: Selecionar plataformas de push {#step-2-select-push-platforms}

Em seguida, escolha qual combinação de plataforma e dispositivo móvel deve receber o push. Use essa seleção para limitar a entrega de uma notificação por push a um conjunto específico de apps.

Existem algumas maneiras diferentes de fazer isso, dependendo das suas seleções anteriores:

| Seleção anterior | Opções |
| --- | --- |
| Campaign de notificação por push | Selecione uma ou mais plataformas e dispositivos. Se você optar por direcionar múltiplos dispositivos e plataformas, sua experiência de edição será otimizada para criar uma mensagem para todas as plataformas selecionadas. Consulte [Push para múltiplas plataformas]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push) para entender o que muda nessa experiência de edição. |
| Campaign multicanal | Selecione **Add Messaging Channel** para adicionar plataformas de push adicionais. Como as seleções de plataforma são específicas para cada variante, você pode testar o engajamento com mensagem por plataforma. |
| Canvas | Na sua etapa de Mensagem, selecione **+ Add more** para adicionar plataformas de push adicionais. Assim como em Campaigns multicanais, as seleções de plataforma são específicas para cada variante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Selecionar plataformas de push" }

## Etapa 3: Selecione o tipo de notificação (iOS e Android) {#step-3-select-notification-type-ios-and-android}

Se você está criando uma Campaign de push para múltiplas plataformas e selecionar Web e/ou Kindle, o tipo de notificação é automaticamente definido como **Push padrão** e não pode ser alterado.

![Tipo de notificação com Push padrão selecionado como exemplo.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Caso contrário, para iOS e Android, selecione o tipo de notificação:

- Push padrão
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) (compatível com Android + iOS)
- Imagem inline (somente Android)

Se você quiser incluir imagens na sua Campaign de push, consulte os guias a seguir sobre como criar uma notificação Rich para [iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications) ou [Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications).

## Etapa 4: Crie sua mensagem push {#step-4-compose-your-push-message}

Agora é hora de escrever sua mensagem push! A guia **Redigir** permite editar todos os aspectos do conteúdo e do comportamento da sua mensagem.

![Guia Redigir da criação de uma notificação por push.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

O conteúdo da guia **Redigir** varia de acordo com o tipo de notificação escolhido na etapa anterior, mas pode incluir qualquer uma das seguintes opções:

### Canal ou grupo de notificação (iOS e Android) {#notification-channel-or-group-ios-and-android}

Para saber mais sobre opções de notificação específicas por plataforma, consulte [Opções de notificação do iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options) ou [Opções de notificação do Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_options).

### Idioma {#language}

Adicione textos em vários idiomas usando o botão **Add Languages**. Recomendamos selecionar seus idiomas antes de escrever o conteúdo para que você possa preencher o texto no local adequado no Liquid. Para a lista completa de idiomas disponíveis, consulte [Idiomas compatíveis]({{site.baseurl}}/developer_guide/localization?tab=android).

Se você estiver adicionando texto em um idioma escrito da direita para a esquerda, a aparência final das mensagens depende muito de como os provedores de serviço as renderizam. Para práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas com a maior precisão possível, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### Título e corpo {#title-and-body}

{% tabs local %}
{% tab iOS %}
Comece a digitar na caixa de mensagem e observe uma prévia aparecer na caixa ao lado. As mensagens push devem ser formatadas em texto simples.

Adicione um título usando o campo **Title**. Para tornar seu push personalizado e direcionado, você pode incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid).
{% endtab %}

{% tab Android %}
Comece a digitar na caixa de mensagem e observe uma prévia aparecer na caixa ao lado. As mensagens push devem ser formatadas em texto simples.

Para tornar seu push personalizado e direcionado, você pode incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid).

{% alert important %}
**Não é possível** enviar uma mensagem push do Android sem um título&#8212;no entanto, você pode inserir um único espaço. Lembre-se de que, se sua mensagem contiver apenas um espaço, ela será enviada como uma notificação por push silenciosa. Para saber mais, consulte [Notificações por push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Precisa de ajuda para criar um texto incrível? Experimente usar o [Assistente de Copywriting com IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Insira o nome ou a descrição de um produto e a IA gerará um texto de marketing semelhante ao humano para uso nas suas mensagens.

![Botão Iniciar Assistente de Copywriting com IA, localizado no campo Corpo do criador de push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

### Imagem {#image}

Quando compatível, o ícone do seu app é adicionado automaticamente como a imagem da sua notificação por push. Você também tem a opção de enviar notificações Rich, que permitem mais personalização nas suas notificações por push adicionando conteúdo adicional além do texto.

Para orientações adicionais sobre o uso de imagens nas suas notificações por push, consulte os seguintes artigos:

- [Criar notificações Rich para iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications)
- [Criar notificações Rich para Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Comportamento ao clicar {#on-click-behavior}

Especifique o que acontece quando um usuário seleciona o corpo de uma notificação por push com **Comportamento ao clicar**. Por exemplo, você pode solicitar que os clientes abram seu aplicativo, redirecioná-los para uma URL da web específica ou até mesmo abrir uma página específica do seu aplicativo com um [deep link]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls).

Aqui, você também pode configurar botões de ação na sua notificação por push, como:

- Aceitar/Recusar
- Sim/Não
- Confirmar/Cancelar
- Mais

### Opções de envio {#sending-options}

Se um usuário tiver seu app instalado em vários dispositivos, por padrão, sua mensagem push é enviada para todos os dispositivos com um token por push válido atribuído. Se desejar, você pode selecionar **Dispositivo usado mais recentemente**.

![Caixa de seleção de opções de dispositivo para enviar este push apenas para o dispositivo usado mais recentemente pelo usuário.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Existem algumas nuances para essa configuração. Se essa opção for selecionada, a Braze limitará o envio múltiplo, exceto quando uma Campaign direcionar múltiplas plataformas, como iOS e Android. Se o usuário tiver seu app em um dispositivo iOS e em um dispositivo Android, ele receberá um push para ambas as plataformas. Se o dispositivo usado mais recentemente pelo usuário não estiver [habilitado para push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled), a mensagem não será enviada.

Por padrão, a Braze envia mensagens para todos os dispositivos de um usuário que possuam um token por push válido. Para iOS, você pode refinar ainda mais seu alcance escolhendo enviar notificações apenas para dispositivos iPad ou apenas para dispositivos iPhone e iPod.

Se desejar, você pode definir o destino do push como **Dispositivo usado mais recentemente**.

#### Dispositivo usado mais recentemente {#most-recently-used-device}

"Dispositivo usado mais recentemente" é um status técnico, não comportamental. Como a Braze envia para todos os dispositivos por padrão, mudar para essa configuração reduz significativamente seu alcance e depende inteiramente do status do único dispositivo com o token mais recente.

O dispositivo usado mais recentemente é determinado por qual dispositivo possui o token por push atualizado mais recentemente, e não por qual dispositivo teve a sessão mais recente.
* Se o token por push de um novo dispositivo for adicionado a um perfil de usuário por meio da API, esse dispositivo é imediatamente considerado o mais recentemente usado, mesmo que o usuário ainda não tenha iniciado uma sessão nele.
* Se o dispositivo usado mais recentemente por um usuário não estiver [habilitado para push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled), a mensagem não será enviada.

Envios múltiplos ainda podem ocorrer se uma Campaign direcionar plataformas diferentes, como iOS e Android. Se um usuário tiver o app em ambas, ele poderá receber um push para as duas plataformas.

Para iOS, você pode limitar ainda mais o envio de mensagens enviando notificações por push apenas para dispositivos iPad ou apenas para dispositivos iPhone e iPod.

## Etapa 5: Prévia e teste da mensagem (opcional) {#step-5-preview-and-test-your-message-optional}

O teste é sem dúvida uma das etapas mais importantes. Depois de finalizar sua mensagem push perfeita, teste-a antes de enviá-la. Selecione a guia **Teste** para escolher entre as opções de como testar sua mensagem push. Em **Destinatários de teste**, você pode selecionar um grupo de teste de conteúdo ou usuários individuais. Você também pode usar **Prévia da mensagem como usuário** para ter uma ideia de como sua mensagem pode ser visualizada no dispositivo móvel para um usuário aleatório, usuário existente, usuário personalizado ou usuário multilíngue.

Para saber mais, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=push).

## Etapa 6: Construa o restante da sua Campaign ou Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construa o restante da sua Campaign; veja as seções a seguir para mais detalhes sobre como usar melhor nossas ferramentas para criar notificações por push.

### Escolha o cronograma de entrega ou disparo {#choose-delivery-schedule-or-trigger}

Mensagens push podem ser entregues com base em um horário agendado, uma ação ou um disparo por API. Para saber mais, consulte [Agendando sua Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Para entrega baseada em ação, você também pode definir a duração da Campaign e o [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

Nesta etapa, você também pode especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) para receber a Campaign ou ativar regras de [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

### Escolha os usuários a serem direcionados {#choose-users-to-target}

Em seguida, você deve [direcionar usuários]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) escolhendo Segments ou filtros para refinar seu público. Você recebe automaticamente uma prévia de como é a população aproximada desse Segment. Estatísticas detalhadas do público para os canais direcionados pela sua Campaign estão disponíveis no rodapé. Para ver qual porcentagem da sua base de usuários está sendo direcionada e o valor do tempo de vida para este Segment, selecione **Show Additional Stats**.

{% multi_lang_include audience/target_audiences.md %}

{% details Por que minha métrica de Total de Usuários Contatáveis não corresponde à soma de todos os canais? %}

Quando você visualiza o Total de Usuários Contatáveis para seu público filtrado, pode notar que a soma das colunas individuais é menor do que o Total de Usuários Contatáveis. Essa diferença geralmente ocorre porque há vários usuários que se qualificam para o Segment ou filtros na Campaign, mas não são contatáveis por push (por exemplo, porque não possuem [tokens por push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#push-tokens) válidos ou ativos).

{% enddetails %}

![Tabela de estatísticas detalhadas do público para Usuários Contatáveis.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Lembre-se de que a composição exata do Segment é sempre calculada antes do envio da mensagem.

Você também pode optar por enviar sua Campaign apenas para usuários que possuem um [status de inscrição]({{site.baseurl}}/user_guide/channels/email/subscriptions) específico, como aqueles que estão inscritos e aceitaram receber push.

Opcionalmente, você também pode limitar a entrega a um número específico de usuários dentro do Segment ou permitir que os usuários recebam a mesma mensagem duas vezes em uma recorrência da Campaign.

#### Campaigns multicanal com e-mail e push {#multichannel-campaigns-with-email-and-push}

Para Campaigns multicanal direcionadas tanto a canais de e-mail quanto de push, você pode querer limitar sua Campaign para que apenas os usuários que aceitaram explicitamente recebam a mensagem (excluindo usuários inscritos ou não inscritos). Por exemplo, digamos que você tenha três usuários com diferentes status de aceitação:

{% multi_lang_include messaging/intelligent_channel_user_examples.md %}

Para fazer isso, em **Resumo do Público**, selecione enviar esta Campaign apenas para "usuários que aceitaram". Essa opção garantirá que apenas usuários que aceitaram receberão seu e-mail, e a Braze enviará push apenas para usuários que estão habilitados para push por padrão.

{% alert important %}
Com essa configuração, não inclua nenhum filtro na etapa **Públicos-alvo** que limite o público a um único canal (por exemplo, `Foreground Push Enabled = True` ou `Email Subscription = Opted-In`).
{% endalert %}

### Escolha os eventos de conversão {#choose-conversion-events}

A Braze permite rastrear com que frequência os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), após receberem uma Campaign. Você tem a opção de permitir uma janela de até 30 dias durante a qual uma conversão será contabilizada se o usuário realizar a ação especificada.

{% endtab %}

{% tab Canvas %}

Se ainda não o fez, complete as seções restantes do componente do seu Canvas. Para detalhes sobre como construir o restante do seu Canvas, incluindo testes multivariantes e [Otimizar com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai), consulte [Construir seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas).

{% endtab %}
{% endtabs %}

## Etapa 7: Revise e implante {#review-and-deploy-push}

Depois de terminar de construir a última parte da sua Campaign ou Canvas, revise seus detalhes. Para Campaigns, a página final apresenta um resumo da Campaign que você criou. Confirme todos os detalhes relevantes, certifique-se de que testou sua mensagem e então envie-a e observe os dados chegarem!

Em seguida, confira [Relatórios de push]({{site.baseurl}}/user_guide/channels/push/reporting) para saber como você pode acessar os resultados da sua Campaign de push. Para notificações por push, você poderá visualizar estatísticas sobre o número de mensagens enviadas, entregues, com bounce, abertas e abertas diretamente.

### Solução de problemas {#troubleshooting}

#### Comportamento ao clicar

Se você estiver usando o comportamento ao clicar padrão para a versão do seu SDK e selecionar uma notificação por push com uma URL da web que abre no app em vez de no navegador web, consulte os seguintes guias de integração para determinar o tratamento de notificações por push:

- [Swift]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#swift_step-2-enable-push-capabilities)
- [Android]({{site.baseurl}}/developer_guide/push_notifications#android_step-1-register-braze-firebase-messaging-service)

{% alert important %}
Você deve atribuir seu objeto delegate usando `center.delegate = self` de forma síncrona antes que seu app termine de inicializar, preferencialmente em `application:didFinishLaunchingWithOptions:`. Caso contrário, seu app pode perder notificações por push recebidas. Consulte a [documentação `UNUserNotificationCenterDelegate` da Apple](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) para saber mais.
{% endalert %}
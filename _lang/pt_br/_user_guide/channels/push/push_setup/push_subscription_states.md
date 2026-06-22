---
nav_title: "Estados de inscrição de push"
article_title: "Estados de inscrição de push"
page_order: 2
page_type: reference
description: "Este artigo de referência aborda os conceitos de ativação de push e estados de inscrição de push na Braze, incluindo as diferenças fundamentais de comportamento entre iOS, Android e web."
channel:
  - Push
---

# Ativação de push e inscrição de push {#push-enablement-and-push-subscription}

> Este artigo de referência aborda os conceitos de ativação de push e estados de inscrição de push na Braze, incluindo as diferenças fundamentais de comportamento entre iOS, Android e Web.

{% multi_lang_include push/subscription_states.md %}

## Onde o registro e o status de push aparecem {#where-push-registration-and-status-appear}

Você pode verificar o estado de inscrição de push, o registro e a ativação em três locais principais na Braze:

1. **[Perfis de usuário](#user-profiles-and-push-changelog)** na guia **Engagement**
2. **[Segmentação](#segmentation-and-push-filters)** no criador de segmentos
3. **[Analytics de Campaign e Canvas](#campaign-and-canvas-analytics)** na página de análise de dados de cada mensagem

### Perfis de usuário e changelog de push {#user-profiles-and-push-changelog}

No perfil de um usuário ([**Pesquisar usuários**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/) > selecione o usuário > guia **Engagement**), **Contact Settings** lista o estado de inscrição de push, **Push Registered For** (quais apps e plataformas a Braze pode usar para enviar push em primeiro plano para aquele perfil) e o **Push Changelog** para movimentações de token, erros e atualizações de registro. Para saber como interpretar **Push Registered For** e a autorização de primeiro plano versus segundo plano, consulte [Verificando o status de registro de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle/#checking-push-registration-status).

No iOS e Android, quando um dispositivo passa de autorização de push em primeiro plano para apenas segundo plano (por exemplo, depois que o usuário desativa notificações nas configurações do sistema e o SDK reporta a mudança), o changelog de push pode incluir uma entrada como "Push token was updated from foreground push enabled to foreground push disabled".

Depois de esperar novos dados do SDK (por exemplo, logo após uma sessão de teste), selecione **Refresh** no perfil do usuário se os valores parecerem desatualizados. Pode haver um pequeno atraso entre o envio dos dados pelo SDK e a atualização do perfil com o registro de push mais recente.

Para usuários que você adiciona a um [grupo interno]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/), selecione **Record User Events for group members** nas **Internal Group Settings** daquele grupo para que as solicitações do SDK apareçam no registro. Em seguida, abra o [Registro de usuários de eventos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log/) em **Settings** > **Event User Log**, encontre as solicitações do SDK do usuário e expanda a carga útil bruta. Você pode inspecionar campos como `remote_notification_enabled` ao validar se o dispositivo reporta notificações remotas como ativadas ou desativadas.

### Segmentação e filtros de push {#segmentation-and-push-filters}

No criador de segmentos, use filtros como **`Foreground Push Enabled`**, **`Foreground Push Enabled for App`**, **`Background or Foreground Push Enabled`** e filtros de inscrição de push para segmentar ou auditar usuários por preferência e autorização no nível do dispositivo. No iOS, como esses filtros são interpretados para um determinado usuário depende de ele ter concluído o prompt do SO, alterado configurações ou usar [autorização provisória](#provisional-push); consulte [Ações do usuário no iOS e status de push](#ios-user-actions-push-status) e [Outros cenários específicos de plataforma](#foreground-push-enabled).

### Analytics de Campaign e Canvas {#campaign-and-canvas-analytics}

Na página de análise de dados de uma **Campaign** ou **Canvas** de push, métricas como *Enviadas*, *Bounces* e *Aberturas* refletem a entrega e o engajamento daquele envio. Para cruzar esses números com perfis individuais, exporte os destinatários em **Campaign Details** ou **Canvas Details** usando **User Data** (CSV). Para etapas e permissões, consulte [Exportar dados de Campaign]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data/) e [Exportar dados de Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/). Se as contagens entre a análise de dados e uma exportação não coincidirem, consulte [Analytics de Campaign e Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/#campaign-and-canvas-analytics) na solução de problemas de exportação.

## Ações do usuário no iOS e status de push {#ios-user-actions-push-status}

A tabela a seguir mostra como diferentes ações do usuário afetam a ativação de push no iOS, o registro de push em primeiro ou segundo plano e o status de inscrição de push na Braze. Quando um usuário instala seu app e inicia a primeira sessão, o estado geralmente é o mostrado na primeira linha. Cada ação subsequente pode atualizar alguns desses valores, mas não outros.

| Ação do usuário | `Foreground Push Enabled` | `Foreground Push Enabled for App` | Tipo de registro de push | Status de inscrição de push |
| --- | --- | --- | --- | --- |
| O usuário instala o app e registra uma sessão | `false`* | Não atualizado | Segundo plano | `Subscribed` |
| O usuário recebe o prompt nativo de push do iOS e seleciona **Allow** | `true` | `true` | Primeiro plano | `Opted-In`** |
| O usuário recebe o prompt nativo de push do iOS e seleciona **Don't Allow** | `false` | Não atualizado | Segundo plano | Não atualizado |
| O usuário ativa push nas configurações do dispositivo e registra uma sessão | `true` | `true` | Primeiro plano | `Opted-In`** |
| O usuário desativa push nas configurações do dispositivo e registra uma sessão | `false` | `false` | Segundo plano | Não atualizado |
| O usuário exclui o app | Não atualizado | Atualizado quando o token de push é retirado | Atualizado quando o token de push é retirado | Não atualizado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Ações do usuário no iOS e status de push" }

<sup>* Se o app não usar push provisório, `Foreground Push Enabled` será `false` até que o usuário permita notificações por push. Se o app usar push provisório, `Foreground Push Enabled` será `true` no início da primeira sessão. Para saber mais, consulte [Autorização provisória e push silencioso](#provisional-push).</sup>

<sup>** A partir da [versão 7.5.0 do Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), a propriedade de configuração `optInWhenPushAuthorized` controla se o estado de inscrição de push é automaticamente definido como `Opted-In` quando a permissão de push é autorizada. Para saber mais, consulte [Atualizando estados de inscrição de push](#update-push-subscription-state).</sup>

## Permissão de push {#push-permission}

Todas as plataformas com push ativado — iOS, Web e Android — exigem opt-in explícito por meio de um prompt do sistema no nível do SO, com algumas pequenas diferenças descritas abaixo.

Como a decisão do usuário é final e você não pode perguntar novamente após uma recusa, usar mensagens no app de [push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/) é uma estratégia importante para aumentar suas taxas de opt-in.

**Prompts nativos de permissão de push do SO**

| Plataforma | Captura de tela | Descrição |
|--|--|--|
| iOS | ![Um prompt nativo de push do iOS perguntando "My App would like to send you notifications" com dois botões, "Don't Allow" e "Allow" na parte inferior da mensagem.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | Isso não se aplica ao solicitar permissão de [push provisório](#provisional-push). |
| Android | ![Uma mensagem de push do Android perguntando "Allow Kitchenerie to send you notifications?" com dois botões, "Allow" e "Don't allow" na parte inferior da mensagem.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Essa permissão de push foi introduzida no Android 13. Antes do Android 13, a permissão não era necessária para enviar push. |
| Web | ![Um prompt nativo de push do navegador web perguntando "Braze.com wants to show notification" com dois botões, "Block" e "Allow" na parte inferior da mensagem.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissão de push" }

### Android

Antes do Android 13, a permissão não era necessária para enviar notificações por push. No Android 12 e versões anteriores, todos os usuários são considerados `Subscribed` na primeira sessão, quando a Braze solicita automaticamente um token de push. Nesse ponto, o usuário está **com push ativado** com um token de push válido para aquele dispositivo e um estado de inscrição padrão de `Subscribed`.

A partir do [Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/), a permissão de push deve ser solicitada e concedida pelo usuário. Seu app pode solicitar manualmente a permissão ao usuário em momentos oportunos, mas, caso contrário, os usuários serão solicitados automaticamente quando seu app criar um [canal de notificação](https://developer.android.com/reference/android/app/NotificationChannel).

### iOS

![Uma notificação na central de notificações do sistema com uma mensagem na parte inferior perguntando "Keep receiving notifications from the Yachtr app?" com dois botões abaixo para "Keep" ou "Turn Off"]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Seu app pode solicitar push provisório ou push autorizado.

O push autorizado exige permissão explícita do usuário antes de enviar qualquer notificação, enquanto o [push provisório](https://www.braze.com/resources/articles/mastering-provisional-push) permite enviar notificações __silenciosamente__, diretamente para a central de notificações, sem som ou alerta.

#### Autorização provisória e push silencioso {#provisional-push}

Antes do iOS 12 (lançado em 2018), todos os usuários precisavam fazer opt-in explícito para receber notificações por push.

No iOS 12, a Apple introduziu a [autorização provisória](https://www.braze.com/resources/articles/mastering-provisional-push), permitindo que marcas enviem notificações por push silenciosas para a central de notificações dos usuários antes que eles façam opt-in explícito, dando a você a chance de demonstrar o valor das suas mensagens antecipadamente. Consulte [autorização provisória]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/#provisional-push-authentication--quiet-notifications) para saber mais.

### Web {#web}

Para Web, você deve solicitar opt-in explícito do usuário por meio do diálogo nativo de permissão do navegador.

Diferentemente do iOS e do Android, que permitem que seu app exiba o prompt de permissão a qualquer momento, alguns navegadores modernos só exibirão o prompt se acionado por um "gesto do usuário" (clique do mouse ou pressionamento de tecla). Se seu site tentar solicitar permissão de notificação por push no carregamento da página, provavelmente será ignorado ou silenciado pelo navegador.

Por isso, você deve solicitar permissão apenas quando o usuário clicar em algum lugar do seu site, e não aleatoriamente quando uma página carregar.

## Tokens de push {#push-tokens}

[Tokens de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle/) são identificadores anônimos únicos gerados pelo dispositivo do usuário e enviados à Braze para identificar para onde enviar a notificação de cada destinatário.

Existem duas formas de classificar um [token de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle/) que são essenciais para entender como uma notificação por push pode ser enviada aos seus usuários.

1. **Push em primeiro plano** oferece a capacidade de enviar notificações por push regulares e visíveis para o primeiro plano do dispositivo do usuário.
2. **Push em segundo plano** está disponível independentemente de um dispositivo específico ter feito opt-in para receber notificações por push daquela marca. O push em segundo plano permite que marcas enviem notificações por push silenciosas — notificações que intencionalmente não são exibidas — para dispositivos, a fim de dar suporte a funcionalidades essenciais como [rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Quando um perfil de usuário tem um token de push de primeiro plano válido associado a um app, a Braze considera o usuário como "registrado para push" naquele app. A Braze então fornece um filtro de segmentação específico, `Foreground Push Enabled for App,` para ajudar a identificar esses usuários.

{% alert note %}
O filtro `Foreground Push Enabled for App` considera apenas a presença de um token de push de primeiro plano e segundo plano válido para o app em questão. No entanto, o filtro mais genérico [`Foreground Push Enabled`](#foreground-push-enabled) segmenta usuários que ativaram explicitamente notificações por push para qualquer app no seu espaço de trabalho. Essa contagem inclui apenas push em primeiro plano e não inclui usuários que cancelaram a inscrição. Você pode saber mais sobre esses e outros filtros em [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).
{% endalert %}

### Múltiplos usuários em um dispositivo {#multiple-users-on-one-device}

Os tokens de push são específicos tanto para o dispositivo quanto para o app, então não é possível usar tokens de push para distinguir entre múltiplos usuários que estão usando o mesmo dispositivo.

Por exemplo, digamos que você tem dois usuários: Charlie e Kim. Se Charlie ativou notificações por push para seu app no telefone dele e Kim usa o telefone de Charlie para sair do perfil de Charlie e entrar no dela, o token de push será reatribuído ao perfil de Kim. O token de push permanecerá atribuído ao perfil de Kim naquele dispositivo até que ela saia e Charlie faça login novamente.

Um app ou site pode ter apenas uma inscrição de push por dispositivo. Então, quando um usuário sai de um dispositivo ou site e um novo usuário faz login, o token de push é reatribuído ao novo usuário. Isso é refletido no perfil do usuário, na seção **Contact Settings** da guia **Engagement**:

![Changelog do token de push na guia Engagement do perfil de um usuário, que lista quando o token de push foi movido para outro usuário e qual era o token.]({% image_buster /assets/img/push_token_changelog.png %})

Como não há uma forma de os provedores de push (APNs/FCM) distinguirem entre múltiplos usuários em um dispositivo, passamos o token de push para o último usuário que fez login para determinar qual usuário direcionar no dispositivo para push.

### Múltiplos dispositivos e um usuário {#multiple-devices-and-one-user}

O estado de inscrição de push é baseado no usuário e não é específico de nenhum app individual. O estado de inscrição de push é o valor que foi definido por último. Então, se um usuário fez opt-in para notificações por push, seu estado de inscrição de push será `Opted-In` em todos os dispositivos elegíveis. Se um usuário posteriormente cancelar explicitamente a inscrição de notificações por push por meio do seu aplicativo ou outros métodos que sua marca oferece, seu estado de inscrição de push será atualizado para `Unsubscribed` e nenhum dispositivo registrado para push poderá receber notificações por push.

## Filtro Foreground Push Enabled {#foreground-push-enabled}

`Foreground Push Enabled` é um filtro de segmentação na Braze que permite que profissionais de marketing identifiquem facilmente usuários que permitem que a Braze envie notificações por push e usuários que não expressaram preferências para não receber notificações por push.

O filtro `Foreground Push Enabled` leva em consideração o seguinte:
- A capacidade da Braze de enviar uma notificação por push (token de push de primeiro plano)
- A preferência geral do usuário de receber push em qualquer um dos seus dispositivos (estado de inscrição de push)

![Uma captura de tela do dashboard mostrando que um usuário está "Push Registered for Marketing (iOS)"]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Um usuário é considerado "com push ativado" ou "registrado para push" se tiver um token de push de primeiro plano ativo para um app dentro do seu espaço de trabalho, o que significa que o status de ativação de push é específico do app.

{% alert note %}
Para informações sobre como verificar o estado de registro de push, visite [status de registro de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle/#checking-push-registration-status)
{% endalert %}

## Encontrando informações de registro de push e changelog {#finding-push-registration-and-changelog-information}

No dashboard, você pode encontrar informações sobre registro de push e changelogs de push em:

- **Segmentação** – Filtre por estados de inscrição dos usuários, estado de ativação e estado de ativação em primeiro e segundo plano.
- **Analytics de Campaign** – Visualize estatísticas de push e feedback para uma única Campaign ou Canvas.
- **Perfil do usuário (guia Engagement)** – Visualize **Contact Settings** e o changelog de push para um usuário específico.

Ao revisar o estado de push ativado, **Push Registered for** indica para quais plataformas a Braze pode enviar push em primeiro plano para aquele usuário. No iOS e Android, se um usuário passou de push de primeiro plano ativado para push de segundo plano ativado (`remote_notification_enabled`), isso será documentado no changelog de push como "Push token was updated from foreground push enabled to foreground push disabled."

Se o usuário for adicionado como usuário teste, em **Console de desenvolvedor** > **Event User Log**, o perfil do usuário mostrará uma solicitação do SDK com `remote_notification_enabled` como `true` ou `false`. Pode ser necessário atualizar o perfil do usuário para visualizar as atualizações, pois há um pequeno atraso para que as atualizações do SDK cheguem ao perfil do usuário.

**Filtros de segmentação para estado de push no iOS:**

- **Push de primeiro plano e segundo plano desativado no iOS:** O usuário ainda não recebeu um prompt de push.
- **Push de segundo plano ativado no iOS:** O usuário recebeu o prompt de push e disse não, ou disse sim e depois desativou notificações por push nas configurações do dispositivo (refletido após o usuário ter uma sessão).
- **Push de primeiro plano ativado no iOS:** O usuário recebeu o prompt de push e está elegível para receber push em primeiro plano.

A análise de dados de Campaign refletirá as estatísticas de push de acordo com os detalhes acima. Você também pode baixar os perfis de usuários que entraram na Campaign ou Canvas para fazer referência cruzada com os perfis de usuários.

## Outros cenários específicos de plataforma {#other-platform-specific-scenarios}

{% tabs %}
{% tab Web %}

Quando um usuário aceita o prompt nativo de permissão de push, seu status de inscrição será alterado para `opted in`.

Para gerenciar inscrições, você pode usar o método de usuário [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) para criar uma página de configurações de preferências no seu site, após o que você pode filtrar usuários por status de descadastramento no dashboard.

Se um usuário desativar notificações no navegador, a próxima notificação por push enviada a esse usuário sofrerá bounce, e a Braze atualizará o token de push do usuário de acordo. Isso é usado para gerenciar a elegibilidade para os filtros de push ativado (`Background or Foreground Push Enabled`, `Foreground Push Enabled` e `Foreground Push Enabled for App`). O status de inscrição definido no perfil do usuário é uma configuração no nível do usuário e não muda quando um push sofre bounce.

### Erros 410 de token de push para Web {#410-web-push-token-errors}

Se você receber um erro `410: Gone`, isso pode ocorrer quando um usuário desativa notificações por push para a web nas configurações do SO do navegador, ou se está fazendo login como um usuário diferente no mesmo dispositivo, ou se o usuário não visitou o site há algum tempo.

Se você receber um erro `410: Endpoint Not Valid`, isso pode significar que o token de push para web (essencialmente a URL) expirou. Isso pode ocorrer se o usuário nunca mais visitar o site ou se o navegador invalidar o token. Também pode ocorrer periodicamente (geralmente a cada poucos meses), dependendo do navegador. Quando o usuário visitar o site novamente, se ainda tiver o navegador configurado como "Allow", a Braze coletará automaticamente um novo token para o dispositivo. Isso pressupõe que a [opção de inicialização `disablePushTokenMaintenance`](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions) não esteja sendo usada durante a inicialização do SDK.

{% alert note %}
Plataformas web não permitem push em segundo plano ou silencioso.
{% endalert %}
{% endtab %}
{% tab Android %}

Se um usuário com push de primeiro plano ativado desativar push nas configurações do SO, então no início da próxima sessão:
- A Braze o marca como push de primeiro plano desativado e não tenta mais enviar mensagens push.
- O filtro `Foreground Push Enabled for App (Android)` e o filtro de segmentação `Foreground Push Enabled` (assumindo que nenhum outro app no perfil do usuário tenha um token de push de primeiro plano válido) retornarão `false`.

Nesse cenário, como um token de push em segundo plano ainda existirá, você pode continuar enviando notificações por push em segundo plano (silenciosas) com o filtro de segmentação `Background or Foreground Push Enabled = true`.

Para Android, a Braze considerará um usuário com push desativado se:

- O usuário desinstalar o app do dispositivo.
- Uma mensagem push falhar na entrega devido a um bounce. Isso geralmente é causado por uma desinstalação, mas também pode ser devido a atualizações do app, nova versão do token de push ou formato.
- O registro de push falhar no Firebase Cloud Messaging (às vezes causado por conexões de rede ruins ou falha ao conectar ao FCM ou ao FCM retornar um token válido).
- O usuário bloquear notificações por push para o app nas configurações do dispositivo e, em seguida, registrar uma sessão.

{% alert note %}
Você só pode interceptar uma notificação por push do Android quando o app está em primeiro plano ou segundo plano (mas ainda em execução). Não é possível interceptar notificações quando o app está encerrado ou completamente fechado.
{% endalert %}

{% endtab %}
{% tab iOS %}

Independentemente de o usuário aceitar o prompt de opt-in de push em primeiro plano, você ainda poderá enviar push em segundo plano se tiver notificações remotas ativadas no Xcode e seu app chamar [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

Se seu app tiver autorização provisória ou o usuário tiver feito opt-in para push, ele receberá um token de push de primeiro plano, permitindo que você envie todos os tipos de push. Na Braze, consideramos um usuário no iOS que está com push de primeiro plano ativado como push ativado, seja explicitamente (nível do app) ou provisoriamente (nível do dispositivo).

Se um usuário recusar receber notificações por push no nível do SO, seu estado de inscrição de push será `Subscribed`, e seu perfil não mostrará que um token de push de primeiro plano foi registrado.

No cenário em que um usuário, que inicialmente fez opt-in no nível do SO, desativa notificações por push nas configurações do SO, no início da próxima sessão, o seguinte ocorrerá:
- A Braze o marca como push de primeiro plano desativado e não tenta mais enviar mensagens push.
- O filtro `Foreground Push Enabled for App (iOS)` e o filtro de segmentação `Foreground Push Enabled` (assumindo que nenhum outro app no perfil do usuário tenha um token de push de primeiro plano válido) retornarão `false`.

Nesse cenário, como um token de push em segundo plano ainda existirá, você pode continuar enviando notificações por push em segundo plano (silenciosas) com o filtro de segmentação `Background or Foreground Push Enabled = true`.

{% alert note %}
O iOS não permite que apps interceptem uma notificação por push antes de ela ser exibida. Isso significa que apps (e a Braze) não têm controle sobre se você pode exibir ou ocultar a notificação. Um usuário pode desativar notificações por push para um app nas configurações do dispositivo, mas isso é controlado pelo sistema operacional.
{% endalert %}

{% endtab %}
{% endtabs %}

## Práticas recomendadas {#best-practices}

Consulte nosso artigo dedicado sobre [Práticas recomendadas de push]({{site.baseurl}}/user_guide/channels/push/best_practices/) para orientações detalhadas sobre como otimizar o uso de push na Braze.
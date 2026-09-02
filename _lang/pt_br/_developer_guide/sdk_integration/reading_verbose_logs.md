---
page_order: 1.5
nav_title: Lendo logs verbosos
article_title: Lendo logs verbosos
description: "Aprenda a ler e interpretar a saída de logs verbosos do SDK or kit de desenvolvimento de software da Braze, incluindo entradas-chave para notificações por push, mensagens no app, Content Cards e deep links."
---

# Lendo logs verbosos {#reading-verbose-logs}

> Esta página explica como interpretar a saída de logs verbosos do SDK or kit de desenvolvimento de software da Braze. Para cada canal de envio de mensagens, você encontrará as entradas de log principais, o que elas significam e problemas comuns a serem observados.

Antes de começar, certifique-se de que você [ativou o registro verboso]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) e sabe como coletar logs na sua plataforma.

## Sessões {#sessions}

As sessões são a base da análise de dados e da entrega de mensagens da Braze. Muitos recursos de envio de mensagens, incluindo mensagens no app e Content Cards, dependem de uma sessão válida ser iniciada antes de poderem funcionar. Se as sessões não estiverem sendo registradas corretamente, investigue isso primeiro. Para saber mais sobre como ativar o rastreamento de sessão, consulte [Etapa 5: Ativar o rastreamento de sessão do usuário]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_step-5-enable-user-session-tracking).

### Principais entradas de log {#key-log-entries}

{% tabs %}
{% tab Swift %}

**Início da sessão:**

```
Started user session (id: <SESSION_ID>)
```

**Fim da sessão:**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**Início da sessão:**

Procure as seguintes entradas:

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

Filtre as solicitações de rede para o endpoint da Braze configurado (por exemplo, SDK or kit de desenvolvimento de software.iad-01.braze.com) para ver o evento de início de sessão (`ss`).

**Fim da sessão:**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### O que verificar {#what-to-check}

- Confirme que um log de início de sessão aparece quando o app é aberto.
- Se você não vir um início de sessão, verifique se o SDK or kit de desenvolvimento de software foi inicializado corretamente e se `openSession` (Android) está sendo chamado.
- No Android, confirme que uma solicitação de rede está sendo feita para o endpoint da Braze. Se você não vir isso, verifique a configuração da sua chave de API or interface de programação do aplicativo (API) e do endpoint.

## Notificações por push {#push-notifications}

Os logs de notificações por push ajudam a verificar se os tokens de dispositivo estão registrados, se as notificações estão sendo entregues e se os eventos de clique estão sendo rastreados.

### Registro de token {#token-registration}

Quando uma sessão é iniciada, o SDK or kit de desenvolvimento de software registra o token por push do dispositivo na Braze.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

Filtre as solicitações para o endpoint da Braze configurado (por exemplo, SDK or kit de desenvolvimento de software.iad-01.braze.com) e procure por `push_token` nos atributos do corpo da solicitação:

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

Confirme também que as informações do dispositivo incluem:

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

Procure pelo log de registro do FCM:

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

Verifique o seguinte:

- `com_braze_firebase_cloud_messaging_registration_enabled` está como `true`.
- O ID do remetente do FCM corresponde ao seu projeto do Firebase.

Um erro comum é `SENDER_ID_MISMATCH`, que significa que o ID do remetente configurado não corresponde ao seu projeto do Firebase.

{% endtab %}
{% endtabs %}

### O que verificar

- Se `push_token` estiver ausente no corpo da solicitação, o token não foi capturado. Verifique a configuração de push na configuração do seu app.
- Se `ios_push_auth` mostrar `denied` ou `provisional`, o usuário não concedeu permissão total de push.
- No Android, se aparecer `SENDER_ID_MISMATCH`, atualize o ID do remetente do FCM para que corresponda ao seu projeto do Firebase.

### Entrega e clique de push {#push-delivery-and-click}

Quando uma notificação por push é tocada, o SDK or kit de desenvolvimento de software registra os eventos de processamento e clique.

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

Seguido pelo evento de clique:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

Se o push contiver um deep link, você também verá:

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

Seguido pela carga útil do push e pelos logs de exibição. Para deep links, procure pelas entradas do Deep Link Delegate ou `UriAction`.

{% endtab %}
{% endtabs %}

### O que verificar

- Verifique se a carga útil do push contém o `title`, `body` e quaisquer deep links (`ab_uri`) esperados.
- Confirme que um evento `pushClick` é registrado após o toque.
- Se o evento de clique estiver ausente, verifique se o app delegate ou o handler de notificações está encaminhando corretamente os eventos de push para o SDK or kit de desenvolvimento de software da Braze.

## Mensagens no app {#in-app-messages}

Os registros de mensagens no app mostram o ciclo de vida completo: entrega a partir do servidor, disparo com base em eventos, exibição, registro de impressão e rastreamento de cliques.

### Entrega da mensagem {#message-delivery}

Quando um usuário inicia uma sessão e é elegível para uma mensagem no app, o SDK or kit de desenvolvimento de software recebe a carga útil da mensagem do servidor.

{% tabs %}
{% tab Swift %}

Filtre as respostas do seu endpoint da Braze configurado (por exemplo, SDK or kit de desenvolvimento de software.iad-01.braze.com) que contenham os dados da mensagem no app.

O corpo da resposta contém a carga útil da mensagem, incluindo:

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

Procure o registro de correspondência do evento-gatilho:

```
Triggering action: <CAMPAIGN_BSON_ID>
```

Isso confirma que a mensagem no app foi associada a um evento-gatilho.

{% endtab %}
{% endtabs %}

### Exibição e impressão da mensagem {#message-display-and-impression}

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

Seguido pelo registro de impressão:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### Eventos de clique e botão {#click-and-button-events}

Quando um usuário toca em um botão ou fecha a mensagem:

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

Se nenhuma outra mensagem disparada corresponder, você também verá:

```
No matching trigger for event.
```

Esse é o comportamento esperado quando nenhuma mensagem no app adicional está configurada para o evento.

{% endtab %}
{% tab Android %}

Filtre as requisições para o seu endpoint da Braze configurado (por exemplo, SDK or kit de desenvolvimento de software.iad-01.braze.com) e procure por eventos com o nome `sbc` (clique no botão) ou `si` (impressão) no corpo da requisição.

{% endtab %}
{% endtabs %}

### O que verificar

- Se a mensagem no app não for exibida, verifique se um início de sessão foi registrado primeiro.
- Filtre as respostas do seu endpoint da Braze configurado para confirmar que a carga útil da mensagem foi entregue.
- Se as impressões não estiverem sendo registradas, verifique se você não implementou um delegate `inAppMessageDisplay` personalizado que suprime o registro.
- Se "No matching trigger for event" aparecer, isso é normal e indica que nenhuma mensagem no app adicional está configurada para esse evento.

## Content Cards

Os logs de Content Cards ajudam você a verificar se os cartões estão sincronizados com o dispositivo, exibidos para o usuário e que as interações (impressões, cliques, dispensas) estão sendo rastreadas.

### Sincronização do cartão {#card-sync}

Os Content Cards são sincronizados no início da sessão e quando uma atualização manual é solicitada. Se nenhuma sessão for registrada, nenhum Content Card será exibido.

{% tabs %}
{% tab Swift %}

Filtre as respostas do seu endpoint da Braze configurado (por exemplo, SDK or kit de desenvolvimento de software.iad-01.braze.com) contendo os dados do cartão.

O corpo da resposta contém os dados do cartão, incluindo:

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

Campos principais:
- `v` (visualizado): `0` = não visualizado, `1` = visualizado
- `cl` (clicado): `0` = não clicado, `1` = clicado
- `p` (fixado): `0` = não fixado, `1` = fixado
- `tp` (tipo): `short_news`, `captioned_image`, `classic`, etc.

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

Seguido por uma solicitação POST para o seu endpoint da Braze configurado (por exemplo, SDK or kit de desenvolvimento de software.iad-01.braze.com) contendo informações do usuário e do dispositivo.

{% endtab %}
{% endtabs %}

### Impressões, cliques e dispensas {#impressions-clicks-and-dismissals}

{% tabs %}
{% tab Swift %}

**Impressão:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**Clique:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

Se o cartão tiver uma URL, você também verá:

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**Dispensa:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

Filtre as solicitações para o seu endpoint da Braze configurado (por exemplo, SDK or kit de desenvolvimento de software.iad-01.braze.com) e procure nomes de eventos no corpo da solicitação:
- `cci` — impressão de Content Card
- `ccc` — clique em Content Card
- `ccd` — Content Card dispensado

{% endtab %}
{% endtabs %}

### O que verificar

- **Nenhum cartão exibido**: Verifique se o início da sessão está registrado. Content Cards requerem uma sessão ativa para sincronizar.
- **Cartões ausentes para novos usuários**: Novos usuários em sua primeira sessão podem não ver Content Cards até a próxima sessão. Esse é um comportamento esperado.
- **Cartão excede o limite de tamanho**: Content Cards acima de 2 KB não são exibidos e a mensagem é abortada.
- **Cartão persiste após parar a Campaign**: Verifique se a sincronização foi concluída após a Campaign ser parada. Os Content Cards são removidos do dispositivo após uma sincronização bem-sucedida. Ao parar uma Campaign, certifique-se de que a opção de remover cartões ativos dos feeds dos usuários esteja selecionada.

## Deep links {#deep-links}

Os registros de deep links aparecem em notificações por push, mensagens no app e Content Cards. A estrutura do registro é consistente independentemente do canal de origem.

{% tabs %}
{% tab Swift %}

Quando o SDK or kit de desenvolvimento de software processa um deep link:

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

Onde `<SOURCE_CHANNEL>` é um dos seguintes: `notification`, `inAppMessage` ou `contentCard`.

{% endtab %}
{% tab Android %}

Para deep links, procure as entradas **Deep Link Delegate** ou **UriAction** no Logcat. Para testar a resolução de deep links de forma independente, execute o seguinte comando:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

Isso confirma se o deep link é resolvido corretamente fora do SDK or kit de desenvolvimento de software da Braze.

{% endtab %}
{% endtabs %}

### O que verificar

- Verifique se a URL do deep link corresponde ao que você configurou na Campaign.
- Se o deep link funciona a partir de um canal (por exemplo, push), mas não de outro (por exemplo, Content Cards), verifique se sua implementação de tratamento de deep links é compatível com todos os canais.
- No iOS, links universais exigem tratamento adicional. Se os links universais não estiverem funcionando a partir dos canais da Braze, verifique se o seu app implementa o protocolo `BrazeDelegate` para tratamento de URLs.
- No Android, verifique se o tratamento automático de deep links está desativado caso você use um handler personalizado. Caso contrário, o handler padrão pode entrar em conflito com a sua implementação.

## Identificação de usuários {#user-identification}

Quando um usuário é identificado com um `external_id`, o SDK or kit de desenvolvimento de software registra um evento de mudança de usuário.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

Informações importantes:
- Chame `changeUser` assim que o usuário fizer login — quanto antes, melhor.
- Se um usuário fizer logout, não há como chamar `changeUser` para revertê-lo a um usuário anônimo.
- Se você não quiser usuários anônimos, chame `changeUser` durante o início da sessão ou a inicialização do app.

{% endtab %}
{% tab Swift %}

Filtre as solicitações para o endpoint da Braze configurado (por exemplo, SDK or kit de desenvolvimento de software.iad-01.braze.com) e procure a identificação do usuário no corpo da solicitação:

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## Solicitações de rede {#network-requests}

Os logs detalhados incluem informações completas de solicitações e respostas HTTP para a comunicação do SDK or kit de desenvolvimento de software com os servidores da Braze. Eles são úteis para diagnosticar problemas de conectividade.

### Estrutura da solicitação {#request-structure}

Filtre as solicitações para o endpoint da Braze configurado (por exemplo, SDK or kit de desenvolvimento de software.iad-01.braze.com). A estrutura da solicitação inclui:

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### O que verificar

- **Chave de API or interface de programação do aplicativo (API)**: Verifique se `XBraze-ApiKey` corresponde à chave de API or interface de programação do aplicativo (API) do seu espaço de trabalho.
- **Endpoint**: Confirme se a URL da solicitação corresponde ao endpoint de SDK or kit de desenvolvimento de software or endpoint do SDK or kit de desenvolvimento de software configurado.
- **Tentativas de reenvio**: `XBraze-Req-Attempt` maior que 1 indica que o SDK or kit de desenvolvimento de software está reenviando uma solicitação que falhou, o que pode sinalizar problemas de conectividade.
- **Limite de frequência**: `XBraze-Req-Tokens-Remaining` mostra os tokens de solicitação restantes. Uma contagem baixa pode indicar que o SDK or kit de desenvolvimento de software está se aproximando dos limites de frequência.
- **Solicitações ausentes**: No Android, se você não visualizar uma solicitação para o endpoint da Braze após o início da sessão, verifique a configuração da chave de API or interface de programação do aplicativo (API) e do endpoint.

## Abreviações comuns de eventos {#common-event-abbreviations}

Nos payloads de log detalhados, a Braze usa nomes de eventos abreviados. Veja a referência:

| Abreviação | Evento |
|---|---|
| `ss` | Início da sessão |
| `se` | Fim da sessão |
| `si` | Impressão de mensagem no app |
| `sbc` | Clique no botão de mensagem no app |
| `cci` | Impressão de Content Card |
| `ccc` | Clique em Content Card |
| `ccd` | Content Card dispensado |
| `lr` | Local registrado |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abreviações comuns de eventos" }

## Solução de problemas {#troubleshooting}

### Geofences não sendo disparadas no Android SDK or kit de desenvolvimento de software 13.1.0–15.x {#geofences-not-triggering-on-android-sdk-131015x}

O Android SDK or kit de desenvolvimento de software da Braze nas versões 13.1.0 a 15.x apresentou uma regressão que podia impedir o registro de eventos de atualização de geofences. Em dispositivos com Android 10 ou anterior, as atualizações de local no início da sessão também podiam falhar. Faça upgrade para o Android SDK or kit de desenvolvimento de software 16.0.0 ou posterior. Para configuração do SDK or kit de desenvolvimento de software, consulte [Geofences]({{site.baseurl}}/developer_guide/geofences).

### Quando um usuário pode ter 0 sessões registradas no perfil? {#when-might-a-user-have-0-sessions-recorded-against-their-profile}

Um perfil de usuário pode mostrar 0 sessões quando você importa o usuário pela REST or transferir estado representacional API or interface de programação do aplicativo (API) ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)) ou por importação de CSV sem os campos **First session** ou **Last session**. As sessões são registradas quando os usuários interagem com o seu app por meio do SDK or kit de desenvolvimento de software. Para saber mais, consulte [Perfil de usuário com 0 sessões]({{site.baseurl}}/developer_guide/analytics/tracking_sessions#user-profile-has-0-sessions).

### Discrepâncias nos dados de usuários ao usar o SDK or kit de desenvolvimento de software e a REST or transferir estado representacional API or interface de programação do aplicativo (API) juntos {#user-data-discrepancies-when-using-the-sdk-and-rest-api-together}

Quando você usa o SDK or kit de desenvolvimento de software e a REST or transferir estado representacional API or interface de programação do aplicativo (API) ao mesmo tempo, condições de corrida podem causar discrepâncias nos dados. Depois de chamar `changeUser()`, permita que o SDK or kit de desenvolvimento de software envie os dados pendentes antes de fazer chamadas críticas à REST or transferir estado representacional API or interface de programação do aplicativo (API), evite agrupar atualizações sensíveis ao tempo e considere adicionar um pequeno atraso entre as requisições do SDK or kit de desenvolvimento de software e da API or interface de programação do aplicativo (API). Para entender o comportamento de `changeUser()`, consulte [Como o changeUser() funciona]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#how-changeuser-works).

### Dados não chegando à Braze {#data-not-reaching-braze}

Se os dados não estão chegando à Braze, confirme se o seu firewall permite tráfego de saída para os endpoints de API or interface de programação do aplicativo (API) da Braze e provedores de rede de distribuição de conteúdo (CDN). Execute um teste MTR e use o [Fastly Debug](https://www.fastly-debug.com/) enquanto o problema estiver ocorrendo. Para solução de problemas de conectividade e lista de permissões, consulte [Problemas de conectividade de rede da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/network_connectivity_issues).
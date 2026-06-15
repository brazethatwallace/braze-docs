---
page_order: 1.5
nav_title: Lendo logs verbosos
article_title: Lendo logs verbosos
description: "Aprenda a ler e interpretar a saída de logs verbosos do SDK da Braze, incluindo entradas-chave para notificações por push, mensagens no app, Content Cards e deep links."
---

# Lendo logs verbosos {#reading-verbose-logs}

> Esta página explica como interpretar a saída de logs verbosos do SDK da Braze. Para cada canal de envio de mensagens, você encontrará as entradas de log principais, o que elas significam e problemas comuns a serem observados.

Antes de começar, certifique-se de que você [ativou o registro verboso]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/) e sabe como coletar logs na sua plataforma.

## Sessões {#sessions}

As sessões são a base da análise de dados e da entrega de mensagens da Braze. Muitos recursos de envio de mensagens — incluindo mensagens no app e Content Cards — dependem de uma sessão válida ser iniciada antes que possam funcionar. Se as sessões não estiverem sendo registradas corretamente, investigue isso primeiro. Para saber mais sobre como ativar o rastreamento de sessões, veja [Etapa 5: Ativar o rastreamento de sessões do usuário]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_step-5-enable-user-session-tracking).

### Entradas de log principais {#key-log-entries}

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

Filtre as solicitações de rede para o seu endpoint da Braze configurado (por exemplo, sdk.iad-01.braze.com) para ver o evento de início da sessão (`ss`).

**Fim da sessão:**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### O que verificar {#what-to-check}

- Verifique se um log de início de sessão aparece quando o app é iniciado.
- Se você não vir um início de sessão, verifique se o SDK está devidamente inicializado e se `openSession` (Android) está sendo chamado.
- No Android, confirme se uma solicitação de rede está sendo feita para o endpoint da Braze. Se você não vir isso, verifique sua chave de API e a configuração do endpoint.

## Notificações por push {#push-notifications}

Os logs de notificação por push ajudam a verificar se os tokens dos dispositivos estão registrados, se as notificações são entregues e se os eventos de clique são rastreados.

### Registro de token {#token-registration}

Quando uma sessão começa, o SDK registra o token por push do dispositivo na Braze.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

Filtre as solicitações para o seu endpoint da Braze configurado (por exemplo, sdk.iad-01.braze.com) e procure por `push_token` nos atributos do corpo da solicitação:

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

Também confirme que as informações do dispositivo incluem:

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

Procure o log de registro do FCM:

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

Verifique o seguinte:

- `com_braze_firebase_cloud_messaging_registration_enabled` é `true`.
- O ID do remetente do FCM corresponde ao seu projeto Firebase.

Um erro comum é `SENDER_ID_MISMATCH`, que significa que o ID do remetente configurado não corresponde ao seu projeto Firebase.

{% endtab %}
{% endtabs %}

### O que verificar

- Se `push_token` estiver faltando no corpo da solicitação, o token não foi capturado. Verifique a configuração do push no seu app.
- Se `ios_push_auth` mostrar `denied` ou `provisional`, o usuário não concedeu permissão total para push.
- No Android, se você vir `SENDER_ID_MISMATCH`, atualize seu ID do remetente FCM para corresponder ao seu projeto Firebase.

### Entrega e clique do push {#push-delivery-and-click}

Quando uma notificação por push é tocada, o SDK registra o processamento e os eventos de clique.

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

Seguido pela carga útil do push e logs de exibição. Para deep links, procure as entradas Deep Link Delegate ou `UriAction`.

{% endtab %}
{% endtabs %}

### O que verificar

- Verifique se a carga útil do push contém os `title`, `body` esperados e quaisquer deep links (`ab_uri`).
- Confirme que um evento `pushClick` é registrado após o toque.
- Se o evento de clique estiver ausente, verifique se seu delegado de app ou manipulador de notificações está encaminhando corretamente os eventos de push para o SDK da Braze.

## Mensagens no app {#in-app-messages}

Os logs de mensagens no app mostram todo o ciclo de vida: entrega do servidor, acionamento com base em eventos, exibição, registro de impressão e rastreamento de cliques.

### Entrega da mensagem {#message-delivery}

Quando um usuário inicia uma sessão e é elegível para uma mensagem no app, o SDK recebe a carga útil da mensagem do servidor.

{% tabs %}
{% tab Swift %}

Filtre as respostas do seu endpoint da Braze configurado (por exemplo, sdk.iad-01.braze.com) contendo os dados da mensagem no app.

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

Procure o log do evento de gatilho correspondente:

```
Triggering action: <CAMPAIGN_BSON_ID>
```

Isso confirma que a mensagem no app foi correspondida a um evento de gatilho.

{% endtab %}
{% endtabs %}

### Exibição da mensagem e impressão {#message-display-and-impression}

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

Seguido pelo log de impressão:

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

Se não houver mais mensagens acionadas correspondentes, você também verá:

```
No matching trigger for event.
```

Esse é o comportamento esperado quando não há mensagens no app adicionais configuradas para o evento.

{% endtab %}
{% tab Android %}

Filtre as solicitações para seu endpoint da Braze configurado (por exemplo, sdk.iad-01.braze.com) e procure eventos com o nome `sbc` (clique no botão) ou `si` (impressão) no corpo da solicitação.

{% endtab %}
{% endtabs %}

### O que verificar

- Se a mensagem no app não for exibida, verifique se o início da sessão foi registrado primeiro.
- Filtre as respostas do seu endpoint da Braze configurado para confirmar que a carga útil da mensagem foi entregue.
- Se as impressões não estão sendo registradas, verifique se você não implementou um delegado `inAppMessageDisplay` personalizado que suprime o registro.
- Se "No matching trigger for event" aparecer, isso é normal e indica que nenhuma mensagem no app adicional está configurada para esse evento.

## Content Cards

Os logs de Content Cards ajudam você a verificar se os cartões estão sincronizados com o dispositivo, exibidos para o usuário e que as interações (impressões, cliques, dispensas) estão sendo rastreadas.

### Sincronização do cartão {#card-sync}

Os Content Cards são sincronizados no início da sessão e quando uma atualização manual é solicitada. Se nenhuma sessão for registrada, nenhum Content Card será exibido.

{% tabs %}
{% tab Swift %}

Filtre as respostas do seu endpoint da Braze configurado (por exemplo, sdk.iad-01.braze.com) contendo os dados do cartão.

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

Seguido por uma solicitação POST para o seu endpoint da Braze configurado (por exemplo, sdk.iad-01.braze.com) contendo informações do usuário e do dispositivo.

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

Filtre as solicitações para o seu endpoint da Braze configurado (por exemplo, sdk.iad-01.braze.com) e procure nomes de eventos no corpo da solicitação:
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

Os logs de deep link aparecem em notificações por push, mensagens no app e Content Cards. A estrutura do log é consistente, independentemente do canal de origem.

{% tabs %}
{% tab Swift %}

Quando o SDK processa um deep link:

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

Para deep links, procure as entradas **Deep Link Delegate** ou **UriAction** no Logcat. Para testar a resolução de deep link de forma independente, execute o seguinte comando:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

Isso confirma se o deep link resolve corretamente fora do SDK da Braze.

{% endtab %}
{% endtabs %}

### O que verificar

- Verifique se a URL do deep link corresponde ao que você configurou na Campaign.
- Se o deep link funcionar de um canal (por exemplo, push) mas não de outro (por exemplo, Content Cards), verifique se a sua implementação de tratamento de deep link suporta todos os canais.
- No iOS, links universais requerem tratamento adicional. Se os links universais não estiverem funcionando a partir dos canais da Braze, verifique se seu app implementa o protocolo `BrazeDelegate` para tratamento de URL.
- No Android, verifique se o tratamento automático de deep link está desativado se você usar um manipulador personalizado. Caso contrário, o manipulador padrão pode entrar em conflito com sua implementação.

## Identificação do usuário {#user-identification}

Quando um usuário é identificado com um `external_id`, o SDK registra um evento de mudança de usuário.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

Coisas importantes a saber:
- Chame `changeUser` assim que o usuário fizer login — quanto mais cedo, melhor.
- Se um usuário sair, não há como chamar `changeUser` para revertê-lo a um usuário anônimo.
- Se você não quiser usuários anônimos, chame `changeUser` durante o início da sessão ou a inicialização do app.

{% endtab %}
{% tab Swift %}

Filtre as solicitações para seu endpoint da Braze configurado (por exemplo, sdk.iad-01.braze.com) e procure a identificação do usuário no corpo da solicitação:

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## Solicitações de rede {#network-requests}

Os logs verbosos incluem todos os detalhes de solicitação e resposta HTTP para a comunicação do SDK com os servidores da Braze. Eles são úteis para diagnosticar problemas de conectividade.

### Estrutura da solicitação {#request-structure}

Filtre as solicitações para seu endpoint da Braze configurado (por exemplo, sdk.iad-01.braze.com). A estrutura da solicitação inclui:

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

- **Chave de API**: Verifique se `X-Braze-Api-Key` corresponde à chave de API do seu espaço de trabalho.
- **Endpoint**: Confirme se a URL da solicitação corresponde ao endpoint de SDK configurado.
- **Tentativas de reenvio**: `X-Braze-Req-Attempt` maior que 1 indica que o SDK está tentando novamente uma solicitação que falhou, o que pode sinalizar problemas de conectividade.
- **Limite de taxa**: `X-Braze-Req-Tokens-Remaining` mostra os tokens de solicitação restantes. Uma contagem baixa pode indicar que o SDK está se aproximando dos limites de taxa.
- **Solicitações ausentes**: No Android, se você não vir uma solicitação para o endpoint da Braze após o início da sessão, verifique sua chave de API e a configuração do endpoint.

## Abreviações comuns de eventos {#common-event-abbreviations}

Nas cargas úteis de logs verbosos, a Braze usa nomes de eventos abreviados. Aqui está uma referência:

| Abreviação | Evento |
|---|---|
| `ss` | Início da sessão |
| `se` | Fim da sessão |
| `si` | Impressão de mensagem no app |
| `sbc` | Clique no botão da mensagem no app |
| `cci` | Impressão de Content Card |
| `ccc` | Clique em Content Card |
| `ccd` | Content Card dispensado |
| `lr` | Local registrado |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Configurando notificações por push {#setting-up-push-notifications}

### Etapa 1: Conclua a configuração inicial {#step-1-complete-the-initial-setup}

{% tabs %}
{% tab Android %}
#### Etapa 1.1: Registre-se para push {#step-11-register-for-push}

Registre-se para push usando a API or interface de programação do aplicativo (API) Firebase Cloud Messaging (FCM) do Google. Para um passo a passo completo, consulte as etapas a seguir do [guia de integração de push nativo para Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/):

1. [Adicione o Firebase ao seu projeto]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-1-add-firebase-to-your-project).
2. [Adicione o Cloud Messaging às suas dependências]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-2-add-cloud-messaging-to-your-dependencies).
3. [Crie uma conta de serviço]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-3-create-a-service-account).
4. [Gere credenciais JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-generate-json-credentials).
5. [Faça upload das suas credenciais JSON para a Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-5-upload-your-json-credentials-to-braze).

#### Etapa 1.2: Obtenha seu Google Sender ID {#step-12-get-your-google-sender-id}

Primeiro, acesse o Firebase Console, abra seu projeto e selecione <i class="fa-solid fa-gear" aria-label="Configurações"></i>&nbsp;**Settings** > **Project settings**.

![O projeto Firebase com o menu "Settings" aberto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecione **Cloud Messaging** e, em **Firebase Cloud Messaging API or interface de programação do aplicativo (API) (V1)**, copie o **Sender ID** para a área de transferência.

![A página "Cloud Messaging" do projeto Firebase com o "Sender ID" destacado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### Etapa 1.3: Atualize seu `braze.xml` {#step-13-update-your-brazexml}

Adicione o seguinte ao seu arquivo `braze.xml`. Substitua `FIREBASE_SENDER_ID` pelo sender ID que você copiou anteriormente.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### Etapa 1.1: Faça upload dos certificados APNs {#step-11-upload-apns-certificates}

Gere um certificado do serviço de Notificações por Push da Apple (APN) e faça upload dele no dashboard da Braze. Para um passo a passo completo, consulte [Fazendo upload do seu certificado APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-upload-your-apns-certificate).

#### Etapa 1.2: Adicione suporte a notificações por push ao seu app {#step-12-add-push-notification-support-to-your-app}

Siga o [guia de integração nativa para iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

{% endtab %}
{% endtabs %}

### Etapa 2: Ouça eventos de notificação por push (opcional) {#step-2-listen-for-push-notification-events-optional}

Para ouvir eventos de notificação por push que a Braze detectou e tratou, chame `subscribeToPushNotificationEvents()` e passe um argumento para execução.

{% alert note %}
Os eventos de notificação por push da Braze estão disponíveis tanto no Android quanto no iOS. Devido a diferenças de plataforma, o iOS só detectará eventos de push da Braze quando um usuário tiver interagido com uma notificação.
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### Campos de eventos de notificação por push {#push-notification-event-fields}

{% alert note %}
Devido a limitações de plataforma no iOS, o SDK or kit de desenvolvimento de software da Braze só pode processar cargas úteis de push enquanto o app estiver em primeiro plano. Os listeners só serão disparados para o tipo de evento `push_opened` no iOS após o usuário ter interagido com uma notificação por push.
{% endalert %}

Para uma lista completa dos campos de notificação por push, consulte a tabela a seguir:

| Nome do campo | Tipo | Descrição |
| ------------------ | --------- | ----------- |
| `payloadType` | String | Especifica o tipo de carga útil da notificação. Os dois valores enviados pelo SDK or kit de desenvolvimento de software Flutter da Braze são `push_opened` e `push_received`. Apenas eventos `push_opened` são suportados no iOS. |
| `url` | String | Especifica a URL que foi aberta pela notificação. |
| `useWebview` | Boolean | Se `true`, a URL abre no app em um webview modal. Se `false`, a URL abre no navegador do dispositivo. |
| `title` | String | Representa o título da notificação. |
| `body` | String | Representa o corpo ou texto de conteúdo da notificação. |
| `summaryText` | String | Representa o texto de resumo da notificação. Isso é mapeado a partir de `subtitle` no iOS. |
| `badgeCount` | Number | Representa a contagem de badges da notificação. |
| `timestamp` | Number | Representa o momento em que a carga útil foi recebida pelo aplicativo. |
| `isSilent` | Boolean | Se `true`, a carga útil é recebida silenciosamente. Para saber mais sobre o envio de notificações por push silenciosas no Android, consulte [Notificações por push silenciosas no Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Para saber mais sobre o envio de notificações por push silenciosas no iOS, consulte [Notificações por push silenciosas no iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `isBrazeInternal` | Boolean | Será `true` se a carga útil da notificação foi enviada para um recurso interno do SDK or kit de desenvolvimento de software, como sincronização de Feature Flag ou Uninstall Tracking. A carga útil é recebida silenciosamente para o usuário. |
| `imageUrl` | String | Especifica a URL associada à imagem da notificação. |
| `brazeProperties` | Object | Representa as propriedades da Braze associadas à Campaign (pares chave-valor). |
| `ios` | Object | Representa campos específicos do iOS. |
| `android` | Object | Representa campos específicos do Android. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campos de eventos de notificação por push" }

### Etapa 3: Teste a exibição de notificações por push {#step-3-test-displaying-push-notifications}

Para testar sua integração após configurar as notificações por push na camada nativa:

1. Defina um usuário ativo no aplicativo Flutter. Para isso, inicialize seu plugin chamando `braze.changeUser('your-user-id')`.
2. Acesse **Campaigns** e crie uma nova Campaign de notificação por push. Escolha as plataformas que você deseja testar.
3. Componha sua notificação de teste e vá para a guia **Test**. Adicione o mesmo `user-id` como usuário teste e clique em **Send Test**.
4. Você deverá receber a notificação no seu dispositivo em breve. Pode ser necessário verificar a central de notificações ou atualizar as configurações caso ela não seja exibida.

{% alert tip %}
A partir do Xcode 14, você pode testar notificações por push remotas em um simulador iOS.
{% endalert %}

### Etapa 4: Adicione deep links (Android) {#step-4-add-deep-links-android}

{% alert warning %}
No Android, `com_braze_handle_push_deep_links_automatically` tem o valor padrão `false`. Com o padrão, tocar em uma notificação por push ainda envia um evento `push_opened` para o seu listener Dart, mas o SDK or kit de desenvolvimento de software nativo não traz o app para o primeiro plano nem abre o destino do deep link automaticamente. Se o seu app não abrir quando uma notificação for tocada, essa flag é a causa mais provável.
{% endalert %}

Para permitir que a Braze abra automaticamente seu app e quaisquer deep links quando uma notificação por push for tocada, defina `com_braze_handle_push_deep_links_automatically` como `true` no seu `braze.xml`:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Essa flag também pode ser definida por meio da [configuração em tempo de execução]({{site.baseurl}}/developer_guide/sdk_integration#android_runtime-configuration) no seu código Android nativo:

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

Se você quiser tratar deep links de forma personalizada, use o listener `subscribeToPushNotificationEvents()` descrito na Etapa 2 para rotear o campo `url` do evento `push_opened` por conta própria. Para saber mais, consulte [Deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=flutter).
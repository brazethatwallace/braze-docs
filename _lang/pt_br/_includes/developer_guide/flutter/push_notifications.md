{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Configuração de notificações por push {#setting-up-push-notifications}

### Etapa 1: Concluir a configuração inicial {#step-1-complete-the-initial-setup}

{% tabs %}
{% tab Android %}
#### Etapa 1.1: Registre-se para push {#step-11-register-for-push}

Registre-se para push usando a API Firebase Cloud Messaging (FCM) do Google. Para obter um passo a passo completo, consulte as etapas a seguir do [guia de integração de push do Android nativo]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/):

1. [Adicione o Firebase ao seu projeto]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Adicione o Cloud Messaging às suas dependências]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Crie uma conta de serviço]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Gere credenciais JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Faça upload das suas credenciais JSON para a Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

#### Etapa 1.2: Obtenha seu Sender ID do Google {#step-12-get-your-google-sender-id}

Primeiro, acesse o Firebase Console, abra seu projeto e selecione <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![O projeto Firebase com o menu "Settings" aberto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecione **Cloud Messaging** e, em seguida, em **Firebase Cloud Messaging API (V1)**, copie o **Sender ID** para a área de transferência.

![A página "Cloud Messaging" do projeto Firebase com o "Sender ID" destacado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### Etapa 1.3: Atualize seu `braze.xml` {#step-13-update-your-brazexml}

Adicione o seguinte ao seu arquivo `braze.xml`. Substitua `FIREBASE_SENDER_ID` pelo Sender ID que você copiou anteriormente.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### Etapa 1.1: Fazer upload de certificados APNs {#step-11-upload-apns-certificates}

Gere um certificado do serviço de Notificações por Push da Apple (APNs) e faça upload dele no dashboard da Braze. Para obter um passo a passo completo, consulte [Como fazer upload do seu certificado de APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

#### Etapa 1.2: Adicione suporte a notificações por push ao app {#step-12-add-push-notification-support-to-your-app}

Siga o [guia de integração nativa do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

{% endtab %}
{% endtabs %}

### Etapa 2: Ouça os eventos de notificação por push (opcional) {#step-2-listen-for-push-notification-events-optional}

Para ouvir os eventos de notificação por push que a Braze detectou e tratou, chame `subscribeToPushNotificationEvents()` e passe um argumento a ser executado.

{% alert note %}
Os eventos de notificação por push da Braze estão disponíveis tanto no Android quanto no iOS. Devido às diferenças de plataforma, o iOS só detectará eventos push da Braze quando um usuário interagir com uma notificação.
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

##### Campos de eventos de notificação por push {#push-notification-event-fields}

{% alert note %}
Devido às limitações da plataforma no iOS, o SDK da Braze só pode processar cargas úteis push enquanto o app estiver em primeiro plano. Os ouvintes só serão disparados para o tipo de evento `push_opened` no iOS depois que um usuário interagir com um push.
{% endalert %}

Para obter uma lista completa dos campos de notificação por push, consulte a tabela abaixo:

| Nome do campo | Tipo | Descrição |
| ------------------ | --------- | ----------- |
| `payloadType`     | String    | Especifica o tipo de carga útil da notificação. Os dois valores enviados pelo Braze Flutter SDK são `push_opened` e `push_received`. Somente os eventos `push_opened` são compatíveis com o iOS. |
| `url`              | String    | Especifica a URL que foi aberta pela notificação. |
| `useWebview`      | Booleano   | Se for `true`, a URL será aberta no app em uma visualização modal da web. Se `false`, a URL será aberta no navegador do dispositivo. |
| `title`            | String    | Representa o título da notificação. |
| `body`             | String    | Representa o corpo ou o texto do conteúdo da notificação. |
| `summaryText`     | String    | Representa o texto resumido da notificação. Isso é mapeado a partir de `subtitle` no iOS. |
| `badgeCount`      | Número   | Representa a contagem de emblemas da notificação. |
| `timestamp`        | Número | Representa a hora em que a carga útil foi recebida pelo aplicativo. |
| `isSilent`        | Booleano   | Se `true`, a carga útil é recebida silenciosamente. Para obter detalhes sobre o envio de notificações por push silenciosas no Android, consulte [Notificações por push silenciosas no Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Para obter detalhes sobre o envio de notificações por push silenciosas no iOS, consulte [Notificações por push silenciosas no iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `isBrazeInternal`| Booleano   | Será `true` se uma carga útil de notificação tiver sido enviada para um recurso interno do SDK, como sincronização de Feature Flag ou rastreamento de desinstalação. A carga útil é recebida silenciosamente para o usuário. |
| `imageUrl`        | String    | Especifica a URL associada à imagem da notificação. |
| `brazeProperties` | Objeto    | Representa as propriedades da Braze associadas à campanha (pares chave-valor). |
| `ios`              | Objeto    | Representa campos específicos do iOS. |
| `android`          | Objeto    | Representa campos específicos do Android. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push notification event fields" }

### Etapa 3: Teste a exibição de notificações por push {#step-3-test-displaying-push-notifications}

Para testar sua integração depois de configurar as notificações por push na camada nativa:

1. Defina um usuário ativo no aplicativo Flutter. Para fazer isso, inicialize seu plug-in chamando `braze.changeUser('your-user-id')`.
2. Acesse **Campaigns** e crie uma nova campanha de notificação por push. Escolha as plataformas que você gostaria de testar.
3. Crie sua notificação de teste e vá para a guia **Test**. Adicione o mesmo `user-id` que o usuário teste e clique em **Send Test**.
4. Você deverá receber a notificação em seu dispositivo em breve. Talvez seja necessário verificar a central de notificações ou atualizar as configurações se ela não for exibida.

{% alert tip %}
A partir do Xcode 14, você pode testar notificações por push remotas em um simulador de iOS.
{% endalert %}
{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Configuração da notificação por push {#setting-up-push-notification}

### Etapa 1: Configurar a plataforma {#step-1-set-up-the-platform}

{% tabs %}
{% tab Android %}
#### Etapa 1.1: Ativar Firebase {#step-11-enable-firebase}

Para começar, siga a documentação de configuração do [Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
Integrar o Firebase Unity SDK or kit de desenvolvimento de software pode fazer com que seu `AndroidManifest.xml` seja substituído. Se isso ocorrer, certifique-se de reverter para o original.
{% endalert %}

#### Etapa 1.2: Defina suas credenciais do Firebase {#step-12-set-your-firebase-credentials}

Você precisa inserir sua chave de servidor do Firebase e o ID do remetente no dashboard da Braze. Para fazer isso, registre-se no [console de desenvolvedores do Firebase](https://console.firebase.google.com/) e selecione seu projeto Firebase. Em seguida, selecione **Cloud Messaging** em **Settings** e copie a Server Key e o Sender ID:<br>![Configurações de Cloud Messaging no console do Firebase mostrando a Server Key e o Sender ID.]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

Na Braze, selecione seu app Android na página de **App Settings** em **Manage Settings**. Em seguida, insira sua chave de servidor do Firebase no campo **Firebase Cloud Messaging Server Key** e o ID do remetente do Firebase no campo **Firebase Cloud Messaging Sender** ID.

![Configurações do app Android na Braze com os campos de chave de servidor e ID do remetente do Firebase Cloud Messaging.]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### Etapa 1.1: Verificar o método de integração {#step-11-verify-integration-method}

A Braze fornece uma solução Unity nativa para automatizar as integrações push do iOS. Se, em vez disso, você quiser configurar e gerenciar sua integração manualmente, consulte [Swift: Notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

Caso contrário, continue para a próxima etapa.

{% alert note %}
Nossa solução de notificação por push automática aproveita o recurso de autorização provisória do iOS 12 e não está disponível para uso com o pop-up nativo de prompt de push.
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### Etapa 1.1: Ativar ADM {#step-11-enable-adm}

1. Crie uma conta no [Portal do desenvolvedor de apps e jogos da Amazon](https://developer.amazon.com/public), caso ainda não tenha feito isso.
2. Obtenha [as credenciais do OAuth (Client ID e Client Secret) e uma chave de API or interface de programação do aplicativo (API) do ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Ative **Automatic ADM Registration Enabled** na janela de configuração do Unity Braze.
  - Como alternativa, é possível adicionar a seguinte linha ao arquivo `res/values/braze.xml` para ativar o registro do ADM:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### Etapa 2: Configurar notificações por push {#step-2-configure-push-notifications}

{% tabs %}
{% tab Android %}
#### Etapa 2.1: Configurar as definições de push {#unity_step-21-configure-push-settings}

O SDK or kit de desenvolvimento de software da Braze pode lidar automaticamente com o registro de push nos servidores do Firebase Cloud Messaging para que os dispositivos recebam notificações por push. No Unity, ative **Automate Unity Android Integration** e, em seguida, defina as seguintes configurações de **Push Notification**.

| Configuração | Descrição |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Automatic Firebase Cloud Messaging Registration Enabled | Instrui o SDK or kit de desenvolvimento de software da Braze a recuperar e enviar automaticamente um token por push FCM para um dispositivo. |
| Firebase Cloud Messaging Sender ID | O Sender ID do seu console do Firebase. |
| Handle Push Deeplinks Automatically | Se o SDK or kit de desenvolvimento de software deve lidar com a abertura de deep links ou abrir o app quando notificações por push são clicadas. |
| Small Notification Icon Drawable | Referência de recurso drawable do Android para o ícone pequeno exibido quando uma notificação por push chega. Insira a referência completa incluindo o prefixo `@drawable/` (por exemplo, `@drawable/hourglass_icon`). A integração automatizada grava esse valor no `braze.xml` conforme inserido. Se você deixar em branco, a notificação usará o ícone do aplicativo como ícone pequeno. |
| Large Notification Icon Drawable | Ícone grande opcional para notificações. Use o mesmo formato `@drawable/` do ícone pequeno (por exemplo, `@drawable/my_large_icon`). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2.1: Configure push settings" }

{% alert note %}
**Small Notification Icon Drawable** e **Large Notification Icon Drawable** aparecem em **Push Configuration** em **Braze > Braze Configuration**. Ambos os valores são gravados no `braze.xml` conforme você os insere. Inclua o prefixo `@drawable/` você mesmo — a integração Unity da Braze não o adiciona automaticamente (por exemplo, `<drawable name="com_braze_push_small_notification_icon">@drawable/hourglass_icon</drawable>`).
{% endalert %}
{% endtab %}

{% tab Swift %}
#### Etapa 2.1: Faça upload do seu token de APNs {#step-21-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### Etapa 2.2: Ativar o push automático {#step-22-enable-automatic-push}

Abra as definições de configuração da Braze no Unity Editor navegando até **Braze > Braze Configuration**.

Marque **Integrate Push With Braze** para registrar automaticamente os usuários para notificações por push, passar tokens por push para a Braze, rastrear análise de dados para aberturas de push e aproveitar nosso tratamento padrão de notificações por push.

#### Etapa 2.3: Ativar o push em segundo plano (opcional) {#step-23-enable-background-push-optional}

Marque **Enable Background Push** se quiser ativar o `background mode` para notificações por push. Isso permite que o sistema desperte seu aplicativo do estado `suspended` quando chegar uma notificação por push, permitindo que seu aplicativo baixe conteúdo em resposta às notificações por push. É necessário marcar essa opção para nossa funcionalidade de rastreamento de desinstalação.

![O editor Unity mostra as opções de configuração da Braze. Nesse editor, as opções "Automate Unity iOS integration", "Integrate push with Braze" e "Enable background push" estão ativadas.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### Etapa 2.4: Desativar o registro automático (opcional) {#step-24-disable-automatic-registration-optional}

Os usuários que ainda não tiverem aceitado as notificações por push serão automaticamente autorizados a receber push ao abrir o aplicativo. Para desativar esse recurso e registrar manualmente os usuários para push, marque **Disable Automatic Push Registration**.

- Se **Disable Provisional Authorization** não estiver marcada no iOS 12 ou posterior, o usuário será autorizado provisoriamente (silenciosamente) a receber quiet push. Se estiver marcada, o usuário verá o prompt de push nativo.
- Se precisar configurar exatamente quando o prompt é mostrado em tempo de execução, desative o registro automático no editor de configuração da Braze e use `AppboyBinding.PromptUserForPushPermissions()`.

![O editor Unity mostra as opções de configuração da Braze. Nesse editor, as opções "Automate Unity iOS integration", "integrate push with Braze" e "disable automatic push registration" estão ativadas.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### Etapa 2.1: Atualize `AndroidManifest.xml` {#unity_step-21-update-androidmanifestxml}

Se o seu app não tiver um `AndroidManifest.xml`, você poderá usar o seguinte como modelo. Caso contrário, se você já tiver um `AndroidManifest.xml`, confira se alguma das seções a seguir está faltando e adicione-a ao seu `AndroidManifest.xml` existente.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon"
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity"
      android:label="@string/app_name"
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### Etapa 2.2: Armazene sua chave de API or interface de programação do aplicativo (API) do ADM {#step-22-store-your-adm-api-key}

Primeiro, [gere uma chave de API or interface de programação do aplicativo (API) do ADM para o seu app](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials), salve a chave em um arquivo chamado `api_key.txt` e adicione-o ao diretório [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) do projeto.

{% alert important %}
A Amazon não reconhecerá sua chave se `api_key.txt` contiver caracteres de espaço em branco, como uma quebra de linha à direita.
{% endalert %}

Em seguida, em seu arquivo `mainTemplate.gradle`, adicione o seguinte:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### Etapa 2.3: Adicionar o JAR do ADM {#step-23-add-adm-jar}

O arquivo JAR do ADM necessário pode ser colocado em qualquer lugar do seu projeto, de acordo com a [documentação do JAR do Unity](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

#### Etapa 2.4: Adicionar o Client Secret e o Client ID ao dashboard da Braze {#step-24-add-client-secret-and-client-id-to-your-braze-dashboard}

Por fim, você deve adicionar o Client Secret e o Client ID obtidos na [Etapa 1](#unity_step-1-enable-adm) à página de **Manage Settings** do dashboard da Braze.

![Página de configurações do app Fire OS na Braze com os campos de Client ID e Client Secret do ADM.]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### Etapa 3: Definir ouvintes de push {#step-3-set-push-listeners}

{% tabs %}
{% tab Android %}
#### Etapa 3.1: Ativar o ouvinte de push recebido {#step-31-enable-push-received-listener}

O ouvinte de push recebido é acionado quando um usuário recebe uma notificação por push. Para enviar a carga útil do push para o Unity, defina o nome do seu objeto de jogo e o método de retorno de chamada do ouvinte de push recebido em **Set Push Received Listener**.

#### Etapa 3.2: Ativar o ouvinte de push aberto {#step-32-enable-push-opened-listener}

O ouvinte de push aberto é acionado quando um usuário lança o app clicando em uma notificação por push. Para enviar a carga útil do push para o Unity, defina o nome do seu objeto de jogo e o método de retorno de chamada do ouvinte de push aberto em **Set Push Opened Listener**.

#### Etapa 3.3: Ativar o ouvinte de push excluído {#step-33-enable-push-deleted-listener}

O ouvinte de push excluído é acionado quando um usuário desliza ou descarta uma notificação por push. Para enviar a carga útil do push para o Unity, defina o nome do seu objeto de jogo e o método de retorno de chamada do ouvinte de push excluído em **Set Push Deleted Listener**.

#### Exemplo de ouvinte de push {#push-listener-example}

O exemplo a seguir implementa o objeto de jogo `BrazeCallback` usando um método de retorno de chamada chamado `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback` e `PushNotificationDeletedCallback`, respectivamente.

![Este gráfico de exemplo de implementação mostra as opções de configuração da Braze mencionadas nas seções anteriores e um trecho de código C#.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);
#endif
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);
#endif
  }

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);
#endif
  }
}
```
{% endtab %}

{% tab Swift %}
#### Etapa 3.1: Ativar o ouvinte de push recebido

O ouvinte de push recebido é acionado quando um usuário recebe uma notificação por push enquanto usa ativamente o aplicativo (por exemplo, quando o app está em primeiro plano). Defina o ouvinte de push recebido no editor de configuração da Braze. Se você precisar configurar o ouvinte do objeto de jogo em tempo de execução, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.PUSH_RECEIVED`.

![O editor Unity mostra as opções de configuração da Braze. Nesse editor, a opção "Set Push Received Listener" é expandida, e o "Game Object Name" (AppBoyCallback) e o "Callback Method Name" (PushNotificationReceivedCallback) são fornecidos.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### Etapa 3.2: Ativar o ouvinte de push aberto

O ouvinte de push aberto é acionado quando um usuário lança o app clicando em uma notificação por push. Para enviar a carga útil do push para o Unity, defina o nome do seu objeto de jogo e o método de retorno de chamada do ouvinte de push aberto na opção **Set Push Opened Listener**:

![O editor Unity mostra as opções de configuração da Braze. Nesse editor, a opção "Set Push Opened Listener" é expandida, e o "Game Object Name" (AppBoyCallback) e o "Callback Method Name" (PushNotificationOpenedCallback) são fornecidos.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Se você precisar configurar o ouvinte do objeto de jogo em tempo de execução, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.PUSH_OPENED`.

#### Exemplo de ouvinte de push

O exemplo a seguir implementa o objeto de jogo `AppboyCallback` usando um nome de método de retorno de chamada `PushNotificationReceivedCallback` e `PushNotificationOpenedCallback`, respectivamente.

![Este gráfico de exemplo de implementação mostra as opções de configuração da Braze mencionadas nas seções anteriores e um trecho de código C#.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);
#endif
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);
#endif
  }
}
```
{% endtab %}

{% tab Amazon Device Messaging %}
Ao atualizar o `AndroidManifest.xml` na [etapa anterior](#unity_step-21-update-androidmanifestxml), os ouvintes de push foram configurados automaticamente quando você adicionou as seguintes linhas. Portanto, não é necessária nenhuma configuração adicional.

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
Para saber mais sobre os ouvintes de push do ADM, consulte [Amazon: Integrar o Amazon Device Messaging](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html).
{% endalert %}
{% endtab %}
{% endtabs %}

## Configurações opcionais {#optional-configurations}

{% tabs %}
{% tab Android %}
### Deep linking para recursos in-app {#deep-linking-to-in-app-resources}

Embora a Braze possa lidar com deep links padrão (como URLs de sites, URIs do Android, etc.) por padrão, a criação de deep links personalizados requer uma configuração adicional do Manifesto.

Para obter orientações de configuração, visite [Deep Linking to In-App Resources](https://developer.android.com/training/app-links/deep-linking).

#### Adição de ícones de notificação por push da Braze {#adding-braze-push-notification-icons}

{% alert important %}
Não adicione imagens de ícones de notificação em `Assets/Plugins/Android/res`. O Unity [descontinuou o fornecimento de recursos Android nesse caminho](https://support.unity.com/hc/en-us/articles/115005875443-Providing-Android-resources-in-Assets-Plugins-Android-res-is-deprecated), o que pode gerar avisos de build ou erros de validação. Empacote seus drawables de ícone em um [plug-in Android Archive (AAR)](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) ou em um projeto de biblioteca Android para que eles sejam mesclados nos recursos do app compilado como qualquer outro drawable.
{% endalert %}

Para adicionar ícones de push ao seu projeto, crie um plug-in AAR ou uma biblioteca Android que contenha os arquivos de imagem do ícone em `res/drawable*` (ou pastas específicas por densidade) e, em seguida, referencie cada ícone em **Braze > Braze Configuration** usando o nome completo do recurso `@drawable/` (consulte a [Etapa 2.1: Configurar as definições de push](#unity_step-21-configure-push-settings)). Para as etapas de empacotamento e importação do Unity, consulte [Android Library Projects and Android Archive plug-ins](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).

Para regras de arte do ícone pequeno (somente alfa, sem cor), consulte [Notificações por push para Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android), Etapa 2: Adequar ícones pequenos às diretrizes de design.
{% endtab %}

{% tab Swift %}
#### Retorno de chamada do token por push {#push-token-callback}

Para receber uma cópia dos tokens de dispositivos da Braze do sistema operacional, defina um delegate usando `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.
{% endtab %}

{% tab Amazon Device Messaging %}
No momento, não há configurações opcionais para o ADM.
{% endtab %}
{% endtabs %}
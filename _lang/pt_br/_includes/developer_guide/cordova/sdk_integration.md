## Integrando o SDK Cordova {#integrating-the-cordova-sdk}

### Pré-requisitos {#prerequisites}

Antes de começar, verifique se o seu ambiente é compatível com a [versão mais recente do SDK Cordova da Braze](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements).

### Etapa 1: Adicione o SDK ao seu projeto {#step-1-add-the-sdk-to-your-project}

{% alert warning %}
Adicione o SDK Cordova da Braze apenas utilizando os métodos a seguir. Não tente instalar por outros métodos, pois isso pode resultar em uma falha de segurança.
{% endalert %}

Se você está no Cordova 6 ou posterior, pode adicionar o SDK diretamente do GitHub. Alternativamente, você pode baixar um ZIP do [repositório no GitHub](https://github.com/braze-inc/braze-cordova-sdk) e adicionar o SDK manualmente.

{% tabs local %}
{% tab geofence desativado %}
Se você não pretende usar coleta de localização e geofences, use a Branch `master` do GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab geofence ativado %}
Se você pretende usar coleta de localização e geofences, use a `geofence-branch` do GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Você pode alternar entre `master` e `geofence-branch` a qualquer momento repetindo esta etapa.
{% endalert %}

### Etapa 2: Configure seu projeto {#step-2-configure-your-project}

Em seguida, adicione as seguintes preferências ao elemento `platform` no arquivo `config.xml` do seu projeto.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Substitua os seguintes valores:

| Valor                 | Descrição                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `BRAZE_API_KEY`       | Sua [chave da API REST da Braze]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab#rest-api-keys).                 |
| `CUSTOM_API_ENDPOINT` | Um endpoint de API personalizado. Esse endpoint é usado para direcionar os dados da sua instância da Braze para o grupo de apps correto no seu dashboard da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Configure seu projeto" }

O elemento `platform` no seu arquivo `config.xml` deve ser semelhante ao seguinte:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Sintaxe específica por plataforma {#platform-specific-syntax}

A seção a seguir aborda a sintaxe específica por plataforma ao usar o Cordova com iOS ou Android.

### Inteiros {#integers}

{% tabs %}
{% tab ios %}
As preferências de inteiros são lidas como representações de string, como no exemplo a seguir:

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
Devido à forma como o framework Cordova 8.0.0+ lida com preferências, as preferências exclusivamente inteiras (como IDs de remetente) devem ser definidas como strings com o prefixo `str_`, como no exemplo a seguir:

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### Booleanos {#booleans}

{% tabs %}
{% tab ios %}
As preferências booleanas são lidas pelo SDK usando as palavras-chave `YES` e `NO` como representações de string, como no exemplo a seguir:

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
As preferências booleanas são lidas pelo SDK usando as palavras-chave `true` e `false` como representações de string, como no exemplo a seguir:

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Configurações opcionais {#optional}

Você pode adicionar qualquer uma das seguintes preferências ao elemento `platform` no arquivo `config.xml` do seu projeto:

{% tabs %}
{% tab ios %}
| Método                                            | Descrição                                                                                                                                                                                                                                           |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key`                                     | Define a chave de API para seu aplicativo.                                                                                                                                                                                                                |
| `ios_api_endpoint`                                | Define o [endpoint de SDK]({{site.baseurl}}/api/basics#endpoints) para seu aplicativo.                                                                                                                                                                 |
| `ios_disable_automatic_push_registration`         | Define se o registro automático de push deve ser desativado.                                                                                                                                                                                          |
| `ios_disable_automatic_push_handling`             | Define se o tratamento automático de push deve ser desativado.                                                                                                                                                                                              |
| `ios_enable_idfa_automatic_collection`            | Define se o SDK da Braze deve coletar automaticamente as informações do IDFA. Para saber mais, consulte [a documentação do método IDFA da Braze](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection`                      | Define se a coleta automática de localização está ativada (se o usuário permitir). O `geofence-branch`                                                                                                                                                |
| `geofences_enabled`                               | Define se os geofences estão ativados.                                                                                                                                                                                                                   |
| `ios_session_timeout`                             | Define o tempo limite da sessão da Braze para seu aplicativo em segundos. O padrão é 10 segundos.                                                                                                                                                               |
| `sdk_authentication_enabled`                      | Define se deve ativar o recurso de [autenticação do SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).                                                                                              |
| `display_foreground_push_notifications`           | Define se as notificações por push devem ser exibidas enquanto o aplicativo está em primeiro plano.                                                                                                                                                       |
| `ios_disable_un_authorization_option_provisional` | Define se `UNAuthorizationOptionProvisional` deve ser desativado.                                                                                                                                                                                   |
| `trigger_action_minimum_time_interval_seconds`    | Define o intervalo mínimo de tempo em segundos entre os acionamentos. O padrão é 30 segundos.                                                                                                                                                                   |
| `ios_push_app_group`                              | Define o ID do grupo de apps para extensões de push no iOS.                                                                                                                                                                                                        |
| `ios_forward_universal_links`                     | Define se o SDK reconhece automaticamente e encaminha links universais para os métodos do sistema. Necessário para que deep links de notificações por push funcionem no iOS. O padrão é desativado.                                                                |
| `ios_log_level`                                   | Define o nível mínimo de registro para `Braze.Configuration.Logger`.                                                                                                                                                                                      |
| `ios_use_uuid_as_device_id`                       | Define se um UUID gerado aleatoriamente deve ser usado como o ID do dispositivo.                                                                                                                                                                                    |
| `ios_flush_interval_seconds`                      | Define o intervalo em segundos entre os envios automáticos de dados. O padrão é 10 segundos.                                                                                                                                                                  |
| `ios_use_automatic_request_policy`                | Define se a política de solicitação para `Braze.Configuration.Api` deve ser automática ou manual.                                                                                                                                                          |
| `should_opt_in_when_push_authorized`              | Define se o estado de inscrição de notificações de um usuário deve ser automaticamente definido como `optedIn` quando as permissões de push forem autorizadas.                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurações opcionais" }

{% alert tip %}
Para mais informações, acesse [GitHub: Plugin Braze iOS Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| Método                                                            | Descrição                                                                                                                                                                                   |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key`                                                 | Define a chave de API para seu aplicativo.                                                                                                                                                        |
| `android_api_endpoint`                                            | Define o [endpoint de SDK]({{site.baseurl}}/api/basics#endpoints) para seu aplicativo.                                                                                                         |
| `android_small_notification_icon`                                 | Define o ícone pequeno da notificação.                                                                                                                                                             |
| `android_large_notification_icon`                                 | Define o ícone grande da notificação.                                                                                                                                                             |
| `android_notification_accent_color`                               | Define a cor de destaque da notificação usando uma representação hexadecimal.                                                                                                                        |
| `android_default_session_timeout`                                 | Define o tempo limite da sessão da Braze para seu aplicativo em segundos. O padrão é 10 segundos.                                                                                                       |
| `android_handle_push_deep_links_automatically`                    | Define se o SDK da Braze lida automaticamente com deep links de push. Necessário para que os deep links de notificações por push funcionem no Android. O padrão é desativado.                                   |
| `android_log_level`                                               | Define o nível de registro para seu aplicativo. O nível de registro padrão é 4 e registrará minimamente as informações. Para ativar o registro detalhado para depuração, use o nível de registro 2.                                    |
| `firebase_cloud_messaging_registration_enabled`                   | Define se deve usar o Firebase Cloud Messaging para notificações por push.                                                                                                                          |
| `android_fcm_sender_id`                                           | Define o ID do remetente do Firebase Cloud Messaging.                                                                                                                                                  |
| `enable_location_collection`                                      | Define se a coleta automática de localização está ativada (se o usuário permitir).                                                                                                              |
| `geofences_enabled`                                               | Define se os geofences estão ativados.                                                                                                                                                           |
| `android_disable_auto_session_tracking`                           | Desativa o rastreamento automático de sessões pelo plugin Cordova do Android. Para saber mais, veja [Desativando o rastreamento automático de sessão](#cordova_disable-automatic-session-tracking). |
| `sdk_authentication_enabled`                                      | Define se deve ativar o recurso de [autenticação do SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).                                      |
| `trigger_action_minimum_time_interval_seconds`                    | Define o intervalo mínimo de tempo em segundos entre os acionamentos. O padrão é 30 segundos.                                                                                                           |
| `is_session_start_based_timeout_enabled`                          | Define se o comportamento do tempo limite da sessão deve ser baseado em eventos de início ou fim da sessão.                                                                                          |
| `default_notification_channel_name`                               | Define o nome visível para o usuário conforme visto via `NotificationChannel.getName` para o `NotificationChannel` padrão da Braze.                                                                              |
| `default_notification_channel_description`                        | Define a descrição visível para o usuário conforme visto via `NotificationChannel.getDescription` para o `NotificationChannel` padrão da Braze.                                                                |
| `does_push_story_dismiss_on_click`                                | Define se uma story por push é automaticamente descartada quando clicada.                                                                                                                            |
| `is_fallback_firebase_messaging_service_enabled`                  | Define se o uso de um fallback do Firebase Cloud Messaging Service está ativado.                                                                                                               |
| `fallback_firebase_messaging_service_classpath`                   | Define o classpath para o fallback do Firebase Cloud Messaging Service.                                                                                                                         |
| `is_content_cards_unread_visual_indicator_enabled`                | Define se a barra de indicação visual de não lidos dos Content Cards está ativada.                                                                                                                       |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Define se o SDK da Braze registrará automaticamente tokens em `com.google.firebase.messaging.FirebaseMessagingService.onNewToken`.                                                         |
| `is_push_deep_link_back_stack_activity_enabled`                   | Define se a Braze adicionará uma atividade à pilha de atividades ao seguir automaticamente deep links para push.                                                                                   |
| `push_deep_link_back_stack_activity_class_name`                   | Define a atividade que a Braze adicionará à pilha de atividades ao seguir automaticamente deep links para push.                                                                                     |
| `should_opt_in_when_push_authorized`                              | Define se a Braze deve automaticamente aceitar o opt-in do usuário quando o push é autorizado.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurações opcionais" }

{% alert tip %}
Para mais informações, acesse [GitHub: Plugin Braze Android Cordova](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt).
{% endalert %}
{% endtab %}
{% endtabs %}

A seguir, veja um exemplo de arquivo `config.xml` com configurações adicionais:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO"/"YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO"/"YES" />
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES"/"NO" />
    <preference name="com.braze.enable_location_collection" value="NO"/"YES" />
    <preference name="com.braze.geofences_enabled" value="NO"/"YES" />
    <preference name="com.braze.ios_session_timeout" value="5" />
    <preference name="com.braze.sdk_authentication_enabled" value="YES"/"NO" />
    <preference name="com.braze.display_foreground_push_notifications" value="YES"/"NO" />
    <preference name="com.braze.ios_disable_un_authorization_option_provisional" value="NO"/"YES" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" />
    <preference name="com.braze.ios_push_app_group" value="PUSH_APP_GROUP_ID" />
    <preference name="com.braze.ios_forward_universal_links" value="YES"/"NO" />
    <preference name="com.braze.ios_log_level" value="2" />
    <preference name="com.braze.ios_use_uuid_as_device_id" value="YES"/"NO" />
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_use_automatic_request_policy" value="YES"/"NO" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES"/"NO" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.braze.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.braze.android_log_level" value="str_LOG_LEVEL_INTEGER" />
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.braze.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.braze.enable_location_collection" value="true"/"false" />
    <preference name="com.braze.geofences_enabled" value="true"/"false" />
    <preference name="com.braze.android_disable_auto_session_tracking" value="true"/"false" />
    <preference name="com.braze.sdk_authentication_enabled" value="true"/"false" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="str_MINIMUM_INTERVAL_INTEGER" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false"/"true" />
    <preference name="com.braze.default_notification_channel_name" value="DEFAULT_NAME" />
    <preference name="com.braze.default_notification_channel_description" value="DEFAULT_DESCRIPTION" />
    <preference name="com.braze.does_push_story_dismiss_on_click" value="true"/"false" />
    <preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true"/"false" />
    <preference name="com.braze.fallback_firebase_messaging_service_classpath" value="FALLBACK_FIREBASE_MESSAGING_CLASSPATH" />
    <preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true"/"false" />
    <preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true"/"false" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true"/"false" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="DEEPLINK_BACKSTACK_ACTIVITY_CLASS_NAME" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true"/"false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Desativando o rastreamento automático de sessão (apenas Android) {#disable-automatic-session-tracking}

Por padrão, o plugin do Android Cordova rastreia automaticamente as sessões. Para desativar o rastreamento automático de sessão, adicione a seguinte preferência ao elemento `platform` no arquivo `config.xml` do seu projeto:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Para começar a rastrear as sessões novamente, chame `BrazePlugin.startSessionTracking()`. Lembre-se de que somente as sessões iniciadas após o próximo `Activity.onStart()` serão rastreadas.

## Configurando canais de notificação para notificações heads-up (somente Android) {#configuring-notification-channels-for-heads-up-notifications-android-only}

No Android 8.0 (nível de API 26) e versões posteriores, o comportamento das notificações é controlado por meio de canais de notificação. Para exibir notificações heads-up — alertas que aparecem brevemente no topo da tela enquanto o usuário está usando o dispositivo — você deve criar um canal de notificação com `NotificationManager.IMPORTANCE_HIGH` no código do seu aplicativo Android.

Embora o SDK do Cordova permita definir o nome e a descrição padrão do canal de notificação por meio das preferências do `config.xml` (`default_notification_channel_name` e `default_notification_channel_description`), o nível de importância deve ser configurado programaticamente no seu código nativo Android.

### Exemplo: Criando um canal de notificação de alta importância {#example-creating-a-high-importance-notification-channel}

Adicione o seguinte código ao método `onCreate()` da classe `Application` do seu aplicativo Android:

{% subtabs local %}
{% subtab Kotlin %}
```kotlin
import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.os.Build

override fun onCreate() {
    super.onCreate()

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        val channelId = "high_priority_channel"
        val channelName = "High Priority Notifications"
        val importance = NotificationManager.IMPORTANCE_HIGH

        val channel = NotificationChannel(channelId, channelName, importance).apply {
            description = "Notifications that require immediate attention"
        }

        val notificationManager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        notificationManager.createNotificationChannel(channel)
    }
}
```
{% endsubtab %}

{% subtab Java %}
```java
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Context;
import android.os.Build;

@Override
public void onCreate() {
    super.onCreate();

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        String channelId = "high_priority_channel";
        String channelName = "High Priority Notifications";
        int importance = NotificationManager.IMPORTANCE_HIGH;

        NotificationChannel channel = new NotificationChannel(channelId, channelName, importance);
        channel.setDescription("Notifications that require immediate attention");

        NotificationManager notificationManager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        notificationManager.createNotificationChannel(channel);
    }
}
```
{% endsubtab %}
{% endsubtabs %}

Após criar o canal no seu código Android, use o ID do canal ao enviar notificações por push pelo dashboard da Braze. Para saber mais sobre canais de notificação, consulte [Canais de notificação do Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels).

## Solução de problemas em builds iOS após o upgrade do plugin {#troubleshooting-ios-builds-after-upgrading-the-plugin}

O SDK da Braze para Cordova 9.0.0 e posteriores utilizam o Swift SDK 9.0.0 ou posterior. A partir do Swift SDK 8.0.0, esse SDK nativo é compilado com **Xcode 15.2**. Se o build do iOS falhar após o upgrade do plugin Cordova para 9.0.0 ou posterior, atualize o Xcode para a versão 15.2 ou mais recente e confirme que ele corresponde ao [changelog do Swift SDK]({{site.baseurl}}/developer_guide/changelogs/?sdktab=swift) para a versão nativa do iOS que seu plugin utiliza.
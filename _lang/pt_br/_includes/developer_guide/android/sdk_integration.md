## Integrando o SDK para Android {#integrating-the-android-sdk}

### Etapa 1: Atualize a configuração do seu Gradle build {#step-1-update-your-gradle-build-configuration}

No repositório de configuração do seu projeto (por exemplo, `settings.gradle`, `settings.gradle.kts` ou `build.gradle` de nível superior), adicione [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) à sua lista de repositórios. Essa sintaxe é a mesma para Groovy e Kotlin DSL.

```groovy
repositories {
  mavenCentral()
}
```

Em seguida, adicione a Braze às suas dependências. Nos exemplos a seguir, substitua `SDK_VERSION` pela versão atual do seu SDK da Braze para Android. Para a lista completa de versões, consulte os [Changelogs]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

{% alert note %}
- Para Kotlin DSL (`build.gradle.kts`), use a sintaxe `implementation("...")`.
- Para Groovy (`build.gradle`), use a sintaxe `implementation '...'`.
- Para [catálogos de versão](https://developer.android.com/build/migrate-to-catalogs), adicione entradas ao seu arquivo `gradle/libs.versions.toml` e faça referência a elas usando os accessors gerados.
{% endalert %}

{% tabs local %}
{% tab base only %}
Se você não pretende usar componentes de UI da Braze, adicione o seguinte às suas dependências.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-base:SDK_VERSION") // (Required) Adds dependencies for the base Braze SDK.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
No seu arquivo `gradle/libs.versions.toml`:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-base = { group = "com.braze", name = "android-sdk-base", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

Em seguida, no seu arquivo `build.gradle` ou `build.gradle.kts`, adicione as seguintes dependências. Essa sintaxe é a mesma para Groovy e Kotlin DSL.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.base) // (Required) Adds dependencies for the base Braze SDK.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab with ui components %}
Se você pretende usar componentes de UI da Braze, adicione o seguinte às suas dependências.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-ui:SDK_VERSION") // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
No seu arquivo `gradle/libs.versions.toml`:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-ui = { group = "com.braze", name = "android-sdk-ui", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

Em seguida, no seu arquivo `build.gradle` ou `build.gradle.kts`, adicione as seguintes dependências. Essa sintaxe é a mesma para Groovy e Kotlin DSL.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.ui) // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etapa 2: Configure seu `braze.xml` {#step-2-configure-your-brazexml}

{% alert note %}
A partir de dezembro de 2019, endpoints personalizados não são mais fornecidos. Se você já possui um endpoint personalizado pré-existente, pode continuar usando-o. Para saber mais, consulte nossa <a href="{{site.baseurl}}/api/basics/#endpoints">lista de endpoints disponíveis</a>.
{% endalert %}

Crie um arquivo `braze.xml` na pasta `res/values` do seu projeto. Se você está em um cluster de dados específico ou possui um endpoint personalizado pré-existente, também precisa especificar o endpoint no seu arquivo `braze.xml`.

O conteúdo desse arquivo deve se parecer com o trecho de código a seguir. Substitua `YOUR_APP_IDENTIFIER_API_KEY` pelo identificador encontrado na página **Manage Settings** do dashboard da Braze. Faça login em [dashboard.braze.com](https://dashboard.braze.com) para encontrar o [endereço do seu cluster]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints).

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Etapa 3: Adicione permissões ao `AndroidManifest.xml` {#step-3-add-permissions-to-androidmanifestxml}

Em seguida, adicione as seguintes permissões ao seu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Com o lançamento do Android M, o Android mudou de um modelo de permissões em tempo de instalação para um modelo de permissões em tempo de execução. No entanto, ambas as permissões são permissões normais e são concedidas automaticamente se listadas no manifesto do app. Para saber mais, acesse a [documentação de permissões](https://developer.android.com/training/permissions/index.html) do Android.
{% endalert %}

### Etapa 4: Ative a inicialização atrasada (opcional) {#step-4-enable-delayed-initialization-optional}

Para usar a inicialização atrasada, a versão mínima do SDK da Braze é necessária:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
Enquanto a inicialização atrasada estiver ativada, todas as conexões de rede serão canceladas, impedindo que o SDK envie dados para os servidores da Braze.
{% endalert %}

#### Etapa 4.1: Atualize seu `braze.xml` {#step-41-update-your-brazexml}

A inicialização atrasada está desativada por padrão. Para ativá-la, use uma das seguintes opções:

{% tabs %}
{% tab Arquivo Braze XML %}
No arquivo `braze.xml` do seu projeto, defina `com_braze_enable_delayed_initialization` como `true`.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab Em tempo de execução %}
Para ativar a inicialização atrasada em tempo de execução, use o seguinte método.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert note %}
Quando a inicialização atrasada está ativada e uma notificação por push contém uma ação de deep link, o deep link não é resolvido.
{% endalert %}

#### Etapa 4.2: Configure a análise de dados de push (opcional) {#step-42-configure-push-analytics-optional}

Quando a inicialização atrasada está ativada, a análise de dados de push é enfileirada por padrão. No entanto, você pode optar por [enfileirar explicitamente](#explicitly-queue-push-analytics) ou [descartar](#drop-push-analytics) a análise de dados de push.

##### Enfileirar explicitamente {#explicitly-queue-push-analytics}

Para enfileirar explicitamente a análise de dados de push, escolha uma das seguintes opções:

{% tabs %}
{% tab Arquivo Braze XML %}
No seu arquivo `braze.xml`, defina `com_braze_delayed_initialization_analytics_behavior` como `QUEUE`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab Em tempo de execução %}
Adicione `QUEUE` ao seu método [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html):

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### Descartar {#drop-push-analytics}

Para descartar a análise de dados de push, escolha uma das seguintes opções:

{% tabs %}
{% tab Arquivo Braze XML %}
No seu arquivo `braze.xml`, defina `com_braze_delayed_initialization_analytics_behavior` como `DROP`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab Em tempo de execução %}
Adicione `DROP` ao método [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html):

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Etapa 4.3: Inicialize o SDK manualmente {#step-43-manually-initialize-the-sdk}

Após o período de atraso escolhido, use o método [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) para inicializar o SDK manualmente.

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### Etapa 5: Ative o rastreamento de sessão do usuário {#step-5-enable-user-session-tracking}

Ao ativar o rastreamento de sessão do usuário, as chamadas para `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html) e o registro do `InAppMessageManager` podem ser tratados automaticamente.

Para registrar retornos de chamada do ciclo de vida da atividade, adicione o seguinte código ao método `onCreate()` da sua classe `Application`.

{% tabs local %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

Para a lista de parâmetros disponíveis, consulte [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## Testando o rastreamento de sessões {#testing-session-tracking}

{% alert tip %}
Você também pode usar o [depurador do SDK]({{site.baseurl}}/developer_guide/debugging) para diagnosticar problemas do SDK.
{% endalert %}

Se você tiver problemas durante os testes, ative o [registro detalhado](#android_enabling-logs) e use o logcat para detectar chamadas `openSession` e `closeSession` ausentes nas suas atividades.

1. Na Braze, acesse **Overview**, selecione seu app e, no menu suspenso **Display Data For**, escolha **Today**.
    ![A página "Overview" na Braze, com o campo "Display Data For" definido como "Today".]({% image_buster /assets/img_archive/android_sessions.png %})
2. Abra seu app e atualize o dashboard da Braze. Verifique se suas métricas aumentaram em 1.
3. Navegue pelo seu app e verifique se apenas uma sessão foi registrada na Braze.
4. Envie o app para segundo plano por pelo menos 10 segundos e depois traga-o de volta para o primeiro plano. Verifique se uma nova sessão foi registrada.

## Configurações opcionais {#optional-configurations}

### Configuração em tempo de execução {#runtime-configuration}

Para definir suas opções da Braze no código em vez do arquivo `braze.xml`, use a [configuração em tempo de execução](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Se um valor existir em ambos os locais, o valor em tempo de execução será utilizado. Depois que todas as configurações obrigatórias forem fornecidas em tempo de execução, você pode excluir seu arquivo `braze.xml`.

No exemplo a seguir, um [objeto builder](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) é criado e depois passado para [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Note que apenas algumas das opções disponíveis em tempo de execução são exibidas&#8212;consulte nosso [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) para a lista completa.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Procurando outro exemplo? Confira nosso [app de exemplo Hello Braze](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java).
{% endalert %}

### Google Advertising ID

O [Google Advertising ID (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) é um ID opcional, anônimo, único e redefinível, específico do usuário, fornecido pelo Google Play Services para fins de publicidade. O GAID permite que os usuários redefinam seu identificador, desativem anúncios baseados em interesses em apps do Google Play, e oferece aos desenvolvedores um sistema simples e padronizado para continuar a monetizar seus apps.

O Google Advertising ID não é coletado automaticamente pelo SDK da Braze e deve ser definido manualmente por meio do método [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).

{% tabs local %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
O Google exige que o Advertising ID seja coletado em uma thread que não seja a de UI.
{% endalert %}


### Monitoramento de localização {#location-tracking}

Para ativar a coleta de localização da Braze, defina `com_braze_enable_location_collection` como `true` no seu arquivo `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
A partir da versão 3.6.0 do SDK Android da Braze, a coleta de localização está desativada por padrão.
{% endalert %}

### Registro de logs {#logging}

Por padrão, o nível de log do SDK Android da Braze é definido como `INFO`. Você pode [suprimir esses logs](#android_suppressing-logs) ou [definir um nível de log diferente](#android_enabling-logs), como `VERBOSE`, `DEBUG` ou `WARN`.

#### Ativando logs {#enabling-logs}

Para ajudar a solucionar problemas no seu app ou reduzir o tempo de resposta com o suporte da Braze, você pode ativar logs detalhados para o SDK. Ao enviar logs detalhados para o suporte da Braze, certifique-se de que eles comecem assim que você iniciar seu app e terminem bem depois de o problema ocorrer. Para uma visão geral centralizada, consulte [Registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Para aprender como interpretar a saída de logs, consulte [Leitura de logs detalhados]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

Lembre-se de que logs detalhados são destinados apenas ao seu ambiente de desenvolvimento, então você deve desativá-los antes de publicar seu app.

{% alert important %}
Ative logs detalhados antes de qualquer outra chamada em `Application.onCreate()` para garantir que seus logs sejam o mais completos possível.
{% endalert %}

{% tabs local %}
{% tab Application %}
Para ativar logs diretamente no seu app, adicione o seguinte ao método `onCreate()` da sua aplicação, antes de qualquer outro método.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

Substitua `MIN_LOG_LEVEL` pela **Constante** do nível de log que você deseja definir como seu nível mínimo de log. Quaisquer logs em um nível `>=` ao `MIN_LOG_LEVEL` definido serão encaminhados para o método [`Log`](https://developer.android.com/reference/android/util/Log) padrão do Android. Quaisquer logs `<` ao `MIN_LOG_LEVEL` definido serão descartados.

| Constante   | Valor          | Descrição                                                                 |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra as mensagens mais detalhadas para depuração e desenvolvimento.   |
| `DEBUG`     | 3              | Registra mensagens descritivas para depuração e desenvolvimento.          |
| `INFO`      | 4              | Registra mensagens informativas para destaques gerais.                    |
| `WARN`      | 5              | Registra mensagens de alerta para identificar situações potencialmente prejudiciais. |
| `ERROR`     | 6              | Registra mensagens de erro para indicar falhas ou problemas graves no app. |
| `ASSERT`    | 7              | Registra mensagens de asserção quando condições são falsas durante o desenvolvimento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ativando logs" }

Por exemplo, o código a seguir encaminhará os níveis de log `2`, `3`, `4`, `5`, `6` e `7` para o método `Log`.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab xml %}
Para ativar logs no `braze.xml`, adicione o seguinte ao seu arquivo:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Substitua `MIN_LOG_LEVEL` pelo **Valor** do nível de log que você deseja definir como seu nível mínimo de log. Quaisquer logs em um nível `>=` ao `MIN_LOG_LEVEL` definido serão encaminhados para o método [`Log`](https://developer.android.com/reference/android/util/Log) padrão do Android. Quaisquer logs `<` ao `MIN_LOG_LEVEL` definido serão descartados.

| Constante   | Valor          | Descrição                                                                 |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra as mensagens mais detalhadas para depuração e desenvolvimento.   |
| `DEBUG`     | 3              | Registra mensagens descritivas para depuração e desenvolvimento.          |
| `INFO`      | 4              | Registra mensagens informativas para destaques gerais.                    |
| `WARN`      | 5              | Registra mensagens de alerta para identificar situações potencialmente prejudiciais. |
| `ERROR`     | 6              | Registra mensagens de erro para indicar falhas ou problemas graves no app. |
| `ASSERT`    | 7              | Registra mensagens de asserção quando condições são falsas durante o desenvolvimento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ativando logs" }

Por exemplo, o código a seguir encaminhará os níveis de log `2`, `3`, `4`, `5`, `6` e `7` para o método `Log`.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### Verificando logs detalhados {#verifying-verbose-logs}

Para verificar se seus logs estão definidos como `VERBOSE`, confira se `V/Braze` aparece em algum lugar nos seus logs. Se aparecer, os logs detalhados foram ativados com sucesso. Por exemplo:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### Suprimindo logs {#suppressing-logs}

Para suprimir todos os logs do SDK Android da Braze, defina o nível de log como `BrazeLogger.SUPPRESS` no método `onCreate()` da sua aplicação, _antes_ de qualquer outro método.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### Múltiplas chaves de API {#multiple-api-keys}

O caso de uso mais comum para múltiplas chaves de API é separar chaves de API para variantes de build de depuração e de release.

Para alternar facilmente entre múltiplas chaves de API em seus builds, recomendamos criar um arquivo `braze.xml` separado para cada [variante de build](https://developer.android.com/studio/build/build-variants.html) relevante. Uma variante de build é uma combinação de tipo de build e flavor de produto. Por padrão, novos projetos Android são configurados com [tipos de build `debug` e `release`](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) e sem flavors de produto.

Para cada variante de build relevante, crie um novo `braze.xml` no diretório `src/<build variant name>/res/values/`. Quando a variante de build for compilada, ela utilizará a nova chave de API.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
Para saber como configurar a chave de API no seu código, consulte [Configuração em tempo de execução]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#runtime-configuration).
{% endalert %}

### TalkBack exclusivo para mensagens no app {#exclusive-in-app-message-talkback}

Em conformidade com as [diretrizes de acessibilidade do Android](https://developer.android.com/guide/topics/ui/accessibility), o SDK Android da Braze oferece o Android TalkBack por padrão. Para garantir que apenas o conteúdo das mensagens no app seja lido em voz alta — sem incluir outros elementos da tela, como a barra de título do app ou a navegação — você pode ativar o modo exclusivo para o TalkBack.

Para ativar o modo exclusivo para mensagens no app:

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8 e ProGuard {#r8-and-proguard}

A configuração de [redução de código](https://developer.android.com/build/shrink-code) é incluída automaticamente na sua integração com a Braze.

Apps clientes que ofuscam o código da Braze devem armazenar os arquivos de mapeamento de release para que a Braze possa interpretar rastreamentos de pilha. Se você quiser manter todo o código da Braze, adicione o seguinte ao seu arquivo ProGuard:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

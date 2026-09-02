## Sobre o SDK or kit de desenvolvimento de software do Unity da Braze {#about-the-unity-braze-sdk}

Para obter uma lista completa de tipos, funções, variáveis e muito mais, consulte o [Arquivo de declaração do Unity](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs). Além disso, se você já tiver integrado o Unity manualmente para iOS, poderá [mudar para uma integração automatizada](#unity_automated-integration).

## Integração do SDK or kit de desenvolvimento de software do Unity {#integrating-the-unity-sdk}

### Pré-requisitos {#prerequisites}

Antes de começar, verifique se seu ambiente é compatível com a [versão mais recente do Braze Unity SDK or kit de desenvolvimento de software](https://github.com/braze-inc/braze-unity-sdk/releases).

### Etapa 1: Escolha seu pacote Braze Unity {#step-1-choose-your-braze-unity-package}

{% tabs %}
{% tab Android %}
O [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) da Braze agrupa bindings nativos para as plataformas Android e iOS, juntamente com uma interface C#.

Há vários pacotes do Braze Unity disponíveis para baixar na [página de lançamentos do Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases):

- `Appboy.unitypackage`
    - Esse pacote reúne os SDKs da Braze para Android e iOS e a dependência [SDWebImage](https://github.com/SDWebImage/SDWebImage) para o SDK or kit de desenvolvimento de software do iOS, que é necessária para o funcionamento adequado dos recursos de mensagem no app e Content Cards da Braze no iOS. O framework SDWebImage é usado para baixar e exibir imagens, inclusive GIFs. Se você pretende utilizar toda a funcionalidade da Braze, baixe e importe esse pacote.
- `Appboy-nodeps.unitypackage`
    - Esse pacote é semelhante ao `Appboy.unitypackage`, exceto pelo fato de que o framework [SDWebImage](https://github.com/SDWebImage/SDWebImage) não está presente. Esse pacote é útil se você não quiser que o framework SDWebImage esteja presente no seu app para iOS.

{% alert note %}
A partir do Unity 2.6.0, o artefato agrupado do Braze Android SDK or kit de desenvolvimento de software requer dependências do [AndroidX](https://developer.android.com/jetpack/androidx). Se você estava usando um `jetified unitypackage`, faça a transição com segurança para o `unitypackage` correspondente.

Se os builds do Android falharem com "This project uses AndroidX dependencies, but the 'android.useAndroidX' property is not enabled", ative o [Custom Gradle Properties Template](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) nas suas configurações de publicação do Unity. Em seguida, abra `Assets/Plugins/Android/gradleTemplate.properties` e defina `android.useAndroidX=true`. Para um modelo funcional, consulte o [app de amostra do Braze Unity](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples) e seu arquivo [`gradleTemplate.properties`](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/gradleTemplate.properties).
{% endalert %}
{% endtab %}

{% tab Swift %}
O [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) da Braze agrupa bindings nativos para as plataformas Android e iOS, juntamente com uma interface C#.

O pacote Braze Unity está disponível para download na [página de lançamentos do Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases) com duas opções de integração:

1. Apenas `Appboy.unitypackage`
  - Este pacote inclui os SDKs da Braze para Android e iOS sem nenhuma outra dependência. Com este método de integração, os recursos de mensagem no app e Content Cards da Braze não funcionarão corretamente no iOS. Se você pretende utilizar a funcionalidade completa da Braze sem código personalizado, use a opção abaixo.
  - Para usar essa opção de integração, *desmarque* a opção `Import SDWebImage dependency` na interface do Unity em "Braze Configuration".
2. `Appboy.unitypackage` com `SDWebImage`
  - Essa opção de integração agrupa os SDKs da Braze para Android e iOS e a dependência [SDWebImage](https://github.com/SDWebImage/SDWebImage) para o SDK or kit de desenvolvimento de software do iOS, que é necessária para o funcionamento adequado da mensagem no app e dos recursos de Content Cards da Braze no iOS. O framework `SDWebImage` é usado para baixar e exibir imagens, inclusive GIFs. Se você pretende utilizar toda a funcionalidade da Braze, baixe e importe esse pacote.
  - Para importar automaticamente o `SDWebImage`, *marque* a opção `Import SDWebImage dependency` na interface do Unity em "Braze Configuration".

{% alert note %}
Para verificar se você precisa da dependência [SDWebImage](https://github.com/SDWebImage/SDWebImage) para seu projeto iOS, visite a [documentação de mensagem no app do iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).
{% endalert %}
{% endtab %}
{% endtabs %}

### Etapa 2: Importar o pacote {#step-2-import-the-package}

{% tabs %}
{% tab Android %}
No Unity Editor, importe o pacote em seu projeto Unity navegando até **Assets > Import Package > Custom Package**. Em seguida, clique em **Import**.

Como alternativa, siga as instruções de [importação de pacotes de ativos do Unity](https://docs.unity3d.com/Manual/AssetPackages.html) para obter mais detalhes sobre a importação de pacotes personalizados do Unity.

{% alert note %}
Para importar apenas o plug-in para iOS ou Android, desmarque o subdiretório `Plugins/Android` ou `Plugins/iOS` ao importar o `.unitypackage` da Braze.
{% endalert %}
{% endtab %}

{% tab Swift %}
No Unity Editor, importe o pacote em seu projeto Unity navegando até **Assets > Import Package > Custom Package**. Em seguida, clique em **Import**.

Como alternativa, siga as instruções de [importação de pacotes de ativos do Unity](https://docs.unity3d.com/Manual/AssetPackages.html) para obter mais detalhes sobre a importação de pacotes personalizados do Unity.

{% alert note %}
Para importar apenas o plug-in para iOS ou Android, desmarque o subdiretório `Plugins/Android` ou `Plugins/iOS` ao importar o `.unitypackage` da Braze.
{% endalert %}
{% endtab %}
{% endtabs %}

### Etapa 3: Configurar o SDK or kit de desenvolvimento de software {#step-3-configure-the-sdk}

{% tabs %}
{% tab Android %}
#### Etapa 3.1: Configurar o `AndroidManifest.xml` {#step-31-configure-androidmanifestxml}

Configure o [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) para que o SDK or kit de desenvolvimento de software da Braze funcione. Se o seu app não tiver um `AndroidManifest.xml`, você poderá usar o modelo a seguir. Caso contrário, se você já tiver um `AndroidManifest.xml`, confira se falta alguma das seções a seguir e adicione-as ao seu `AndroidManifest.xml` existente.

1. Acesse o diretório `Assets/Plugins/Android/` e abra o arquivo `AndroidManifest.xml`. Esse é o [local padrão no Unity Editor](https://docs.unity3d.com/Manual/android-manifest.html).
2. No seu `AndroidManifest.xml`, adicione as permissões e atividades necessárias do modelo a seguir.
3. Quando terminar, o seu `AndroidManifest.xml` deverá conter apenas uma Activity com `"android.intent.category.LAUNCHER"` presente.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon"
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity"
      android:theme="@style/UnityThemeSelector"
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

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

{% alert important %}
Todas as classes de Activity registradas no seu arquivo `AndroidManifest.xml` devem ser totalmente integradas ao Braze Android SDK or kit de desenvolvimento de software, caso contrário, a análise de dados não será coletada. Se você adicionar sua própria classe Activity, certifique-se de [estender o player do Braze Unity](#unity_extend-unity-player) para evitar isso.
{% endalert %}

#### Etapa 3.2: Atualize o `AndroidManifest.xml` com o nome do seu pacote {#step-32-update-androidmanifestxml-with-your-package-name}

Para encontrar o nome do pacote, clique em **File > Build Settings > Player Settings > guia Android**.

![Guia Android das configurações do Unity Player mostrando o nome do pacote da aplicação.]({% image_buster /assets/img_archive/UnityPackageName.png %})

No seu `AndroidManifest.xml`, todas as instâncias de `REPLACE_WITH_YOUR_PACKAGE_NAME` devem ser substituídas pelo `Package Name` da etapa anterior.

#### Etapa 3.3: Adicionar dependências do Gradle {#step-33-add-gradle-dependencies}

Para adicionar dependências do Gradle ao seu projeto Unity, primeiro ative a opção ["Custom Main Gradle Template"](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) nas suas configurações de publicação. Isso criará um arquivo Gradle modelo que será usado pelo seu projeto. Um arquivo Gradle lida com as dependências e outras configurações de projeto durante o build. Para saber mais, consulte o [mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle) do app de amostra do Braze Unity.

As seguintes dependências são necessárias:

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

Você também pode definir essas dependências usando o [External Dependency Manager](https://github.com/googlesamples/unity-jar-resolver).

#### Etapa 3.4: Automatize a integração do Unity com o Android {#step-34-automate-the-unity-android-integration}

A Braze oferece uma solução nativa do Unity para automatizar a integração do Unity com o Android.

1. No Unity Editor, abra as configurações da Braze navegando até **Braze > Braze Configuration**.
2. Marque a caixa **Automate Unity Android Integration**.
3. No campo **Braze API or interface de programação do aplicativo (API) Key**, insira a chave de API or interface de programação do aplicativo (API) do seu app encontrada em **Manage Settings** no dashboard da Braze.

{% alert note %}
Essa integração automática não deve ser usada com um arquivo `braze.xml` criado manualmente, pois os valores de configuração podem entrar em conflito durante o build do projeto. Se precisar de um `braze.xml` manual, desative a integração automática.
{% endalert %}
{% endtab %}

{% tab Swift %}
#### Etapa 3.1: Defina sua chave de API or interface de programação do aplicativo (API) {#step-31-set-your-api-key}

A Braze oferece uma solução nativa do Unity para automatizar a integração do Unity com o iOS. Essa solução modifica o projeto do Xcode usando o [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) do Unity e cria subclasses do `UnityAppController` usando a macro `IMPL_APP_CONTROLLER_SUBCLASS`.

1. No Unity Editor, abra as configurações da Braze navegando até **Braze > Braze Configuration**.
2. Marque a opção **Automate Unity iOS Integration**.
3. No campo **Braze API or interface de programação do aplicativo (API) Key**, insira a chave de API or interface de programação do aplicativo (API) do seu app encontrada em **Manage Settings**.

![Janela de configuração da Braze no Unity com os campos Automate Unity iOS Integration e Braze API or interface de programação do aplicativo (API) Key.]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

Se o seu app já estiver usando outra subclasse `UnityAppController`, será necessário mesclar a implementação da sua subclasse com `AppboyAppDelegate.mm`.
{% endtab %}
{% endtabs %}

## Personalização do pacote Unity {#customizing-the-unity-package}

### Etapa 1: Clonar o repositório {#step-1-clone-the-repository}

No seu terminal, clone o [repositório do Braze Unity SDK or kit de desenvolvimento de software no GitHub](https://github.com/braze-inc/braze-unity-sdk) e, em seguida, navegue até essa pasta:

{% tabs local %}
{% tab MacOS %}
```bash
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd ~/PATH/TO/DIRECTORY/braze-unity-sdk
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd C:\PATH\TO\DIRECTORY\braze-unity-sdk
```
{% endtab %}
{% endtabs %}

### Etapa 2: Exportar pacote do repositório {#step-2-export-package-from-repository}

Primeiro, inicie o Unity e mantenha-o em execução em segundo plano. Em seguida, na raiz do repositório, execute o seguinte comando para exportar o pacote para `braze-unity-sdk/unity-package/`.

{% tabs local %}
{% tab MacOS %}
```bash
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -nographics -projectPath "$(pwd)" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
"%UNITY_PATH%" -batchmode -nographics -projectPath "%PROJECT_ROOT%" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Se você tiver algum problema após executar esses comandos, consulte [Unity: argumentos de linha de comando](https://docs.unity3d.com/2017.2/Documentation/Manual/CommandLineArguments.html).
{% endalert %}

### Etapa 3: Importar pacote no Unity {#step-3-import-package-into-unity}

1. No Unity, importe o pacote desejado para seu projeto Unity navegando até **Assets** > **Import Package** > **Custom Package**.
2. Se houver algum arquivo que você não queira importar, desmarque-o agora.
3. Personalize o pacote Unity exportado, localizado em `Assets/Editor/Build.cs`.

## Mudar para uma integração automatizada (somente Swift) {#automated-integration}

Para aproveitar a integração automatizada do iOS oferecida no SDK or kit de desenvolvimento de software do Braze Unity, siga estas etapas para fazer a transição de uma integração manual para uma automatizada.

1. Remova todo o código relacionado à Braze da subclasse `UnityAppController` do seu projeto do Xcode.
2. Remova as bibliotecas da Braze para iOS do seu projeto Unity ou Xcode (como `Appboy_iOS_SDK.framework` e `SDWebImage.framework`).
3. Importe o pacote Braze Unity no seu projeto novamente. Para obter um passo a passo completo, consulte [Etapa 2: Importar o pacote](#unity_step-2-import-the-package).
4. Defina sua chave de API or interface de programação do aplicativo (API) novamente. Para obter um passo a passo completo, consulte [Etapa 3.1: Defina sua chave de API or interface de programação do aplicativo (API)](#unity_step-31-set-your-api-key).

## Configurações opcionais {#optional-configurations}

### Registro detalhado {#verbose-logging}

Para ativar o registro detalhado no Unity Editor, faça o seguinte:

1. Abra as configurações da Braze navegando até **Braze** > **Braze Configuration**.
2. Clique no menu suspenso **Show Braze Android Settings**.
3. No campo **SDK or kit de desenvolvimento de software Log Level**, insira o valor "0".

### Compatibilidade com o Prime 31 {#prime-31-compatibility}

Para usar o plug-in Braze Unity com os plug-ins Prime31, edite o `AndroidManifest.xml` do seu projeto para usar as classes Activity compatíveis com o Prime31. Altere todas as referências de
`com.braze.unity.BrazeUnityPlayerActivity` para `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

### Amazon Device Messaging (ADM)

A Braze oferece suporte à integração do [ADM push](https://developer.amazon.com/public/apis/engage/device-messaging) em apps Unity. Se quiser integrar o ADM push, crie um arquivo chamado `api_key.txt` contendo sua chave de API or interface de programação do aplicativo (API) do ADM e coloque-o na pasta `Plugins/Android/assets/`. Para saber mais sobre a integração do ADM com a Braze, acesse nossas [instruções de integração push do ADM]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=unity).

### Ampliação do player Braze Unity (somente Android) {#extend-unity-player}

O arquivo de exemplo `AndroidManifest.xml` fornecido tem uma classe Activity registrada, [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). Essa classe é integrada ao SDK or kit de desenvolvimento de software da Braze e estende o `UnityPlayerActivity` com manipulação de sessão, registro de mensagens no app, registro de análise de dados de notificações por push e muito mais. Para saber mais sobre como estender a classe `UnityPlayerActivity`, consulte a documentação do [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html).

Se estiver criando seu próprio `UnityPlayerActivity` personalizado em uma biblioteca ou projeto de plug-in, será necessário estender nosso `BrazeUnityPlayerActivity` para integrar sua funcionalidade personalizada à Braze. Antes de começar a trabalhar na extensão do `BrazeUnityPlayerActivity`, siga nossas instruções para integrar a Braze no seu projeto Unity.

1. Adicione o Braze Android SDK or kit de desenvolvimento de software como uma dependência da sua biblioteca ou projeto de plug-in, conforme descrito nas [instruções de integração do Braze Android SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).
2. Integre nosso Unity `.aar`, que contém nossa funcionalidade específica do Unity, ao seu projeto de biblioteca Android que está sendo desenvolvido para o Unity. O `appboy-unity.aar` está disponível no nosso [repositório público](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android). Depois que nossa biblioteca Unity for integrada com sucesso, modifique seu `UnityPlayerActivity` para estender o `BrazeUnityPlayerActivity`.
3. Exporte sua biblioteca ou projeto de plug-in e coloque-o em `/<your-project>/Assets/Plugins/Android` normalmente. Não inclua nenhum código-fonte da Braze na sua biblioteca ou plug-in, pois eles já estarão presentes em `/<your-project>/Assets/Plugins/Android`.
4. Edite o `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` para especificar a subclasse `BrazeUnityPlayerActivity` como a atividade principal.

Agora, você poderá empacotar um `.apk` pelo Unity IDE totalmente integrado à Braze e que contenha sua funcionalidade personalizada do `UnityPlayerActivity`.

## Solução de problemas {#troubleshooting}

### Erro: "File could not be read" {#error-file-could-not-be-read}

Erros semelhantes aos seguintes podem ser ignorados com segurança. O software da Apple usa uma extensão PNG proprietária chamada CgBI, que o Unity não reconhece. Esses erros não afetarão seu build do iOS nem a exibição adequada das imagens associadas no pacote da Braze.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```

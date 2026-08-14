---
nav_title: Integração com o Baidu
article_title: Integração de notificações por push do Baidu para Android
platform: Android
permalink: /baidu_integration/
description: "Este artigo mostra como configurar uma integração do Baidu com o Android."
hidden: true
excerpt_separator: ""
---
# Integração com o Baidu {#baidu-integration}
{% alert warning %}
A integração de push do Baidu com a Braze foi descontinuada em 24 de março de 2022.

* **24 de março de 2022:** Não é mais possível criar novos apps do Baidu no dashboard da Braze.
* **15 de setembro de 2022:** Não é mais possível criar novas mensagens push do Baidu. Mensagens existentes e a coleta de dados não são afetadas.
* **15 de janeiro de 2023:** A Braze não envia mais mensagens nem coleta dados de apps do Baidu.
{% endalert %}

A Braze pode enviar notificações por push para dispositivos Android usando o [Baidu Cloud Push]({% image_buster /assets/img_archive/baidu_app_console.png %}). Note que o uso do Baidu Cloud Push não exige que você distribua seus apps por meio da Baidu App Store.

## Etapa 1: Criar uma conta no Baidu {#step-1-create-a-baidu-account}

Para criar uma conta no Baidu, visite o [Portal do Baidu](https://www.baidu.com/) e clique em **登录** (Login) para abrir uma caixa de diálogo que permitirá fazer login ou criar uma nova conta.

![Portal do Baidu]({% image_buster /assets/img_archive/baidu_portal.png %})

Para criar uma nova conta, na parte inferior da caixa de diálogo de login, clique em **立即注册** (nova conta).

![Caixa de diálogo de login do Baidu]({% image_buster /assets/img_archive/baidu_login_dialog.png %}){: style="max-width:70%;"}

Insira seu nome de usuário, número de telefone e senha na página de criação de conta. Em seguida, clique no botão para receber o código de verificação. Você receberá uma mensagem SMS do Baidu contendo um código de verificação. Por fim, aceite o contrato de licença e clique em **注册** (criar conta) para se registrar. Se essas etapas de configuração falharem, tente se registrar pelo login do Baidu Cloud conforme descrito neste [artigo sobre login](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/).

![Página de inscrição do Baidu]({% image_buster /assets/img_archive/baidu_signup.png %}){: style="max-width:80%;"}

## Etapa 2: Registrar-se como desenvolvedor Baidu {#step-2-register-as-a-baidu-developer}

Em seguida, você deve se registrar como desenvolvedor Baidu. Primeiro, acesse o [portal de desenvolvedores Baidu](http://developer.baidu.com/) e escolha **注册** (criar nova conta de desenvolvedor) para iniciar o registro.

![Portal de desenvolvedores Baidu]({% image_buster /assets/img_archive/baidu_dev_portal.png %})

Na página de registro, escolha o tipo de conta (个人 para pessoal, 公司 para empresa) e o tipo de desenvolvedor (desenvolvedor já vem pré-selecionado e é a opção correta para a maioria dos casos). Insira seu nome, uma breve descrição e o número de telefone com o código do país entre parênteses (por exemplo, (1)xxxxxxxxxx). Clique em **发送验证码** (enviar código de verificação) e insira o código de verificação na linha seguinte. Os dois campos seguintes, website do desenvolvedor e logo do desenvolvedor, são opcionais. Aceite o contrato de licença e clique em **提交** (enviar) para concluir o envio. Agora você tem uma conta de desenvolvedor Baidu.

![Página de registro de desenvolvedor Baidu]({% image_buster /assets/img_archive/baidu_dev_reg.png %})

## Etapa 3: Registre seu aplicativo no Baidu {#step-3-register-your-application-with-baidu}

Para registrar seu aplicativo no Baidu, visite o [portal de projetos do Baidu](http://developer.baidu.com/console#app/project) e clique em **创建工程** (criar projeto).

![Portal de projetos do Baidu]({% image_buster /assets/img_archive/baidu_project.png %})

Na página seguinte, insira o nome do seu aplicativo. As duas caixas de seleção a seguir servem para ativar serviços adicionais do Baidu. Na maioria dos casos, elas devem ser deixadas em branco.

![Campo de nome do aplicativo no Baidu]({% image_buster /assets/img_archive/baidu_app_name.png %})

Após configurar seu aplicativo, você será direcionado a um console que exibe informações sobre o app, incluindo a chave de API. Em seguida, navegue até **云推送** (cloud push) na barra lateral. Na página seguinte, clique em **推送设置** (configurar push).

![Console do aplicativo no Baidu exibindo informações da API]({% image_buster /assets/img_archive/baidu_app_console.png %})

![Página de cloud push do Baidu]({% image_buster /assets/img_archive/baidu_continue.png %})

Na página seguinte, insira o nome do pacote do seu app (por exemplo, `com.braze.sample`) e especifique se deseja armazenar mensagens em cache e, em caso afirmativo, por quanto tempo (em horas). Isso indica ao Baidu por quanto tempo ele deve continuar tentando enviar mensagens para usuários offline. Clique em **保存设置** (salvar configurações) para salvar.

![Página de configuração de cloud push do Baidu]({% image_buster /assets/img_archive/baidu_configure_cloud.png %})

## Etapa 4: Adicionar o Baidu ao seu aplicativo {#step-4-add-baidu-to-your-application}

Acesse o [portal do SDK de push do Baidu](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk) e baixe a versão mais recente do Baidu Cloud Push Android SDK.

![Portal do SDK de push do Baidu]({% image_buster /assets/img_archive/baidu_sdk.png %})

Dentro do SDK, você encontrará o jar do serviço de push e as bibliotecas nativas específicas de cada plataforma. Integre-as ao seu projeto. Certifique-se de que seu app tenha como alvo a versão mais recente do SDK atualmente suportada pelo Baidu. Esta documentação está atualizada para a versão `4.6.2.38` do Baidu Cloud Push Android SDK.

Adicione as seguintes permissões obrigatórias do Baidu ao `AndroidManifest.xml` do seu aplicativo.

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

A biblioteca do Baidu contém broadcast receivers que tratam as mensagens push recebidas. Declare os receivers internos do Baidu no `AndroidManifest.xml` do seu aplicativo, dentro do elemento `<application>`.

```xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>
```

Você também precisará criar um broadcast receiver que escute as mensagens push e notificações recebidas. Declare seu receiver no `AndroidManifest.xml` do seu aplicativo, dentro do elemento `<application>`. Esse receiver precisará estender `com.baidu.android.pushservice.PushMessageReceiver` e implementar métodos que recebam atualizações de eventos do serviço de push do Baidu.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

No método `onCreate()` da sua activity principal, adicione a linha a seguir, que registrará seu aplicativo no Baidu e começará a escutar mensagens push recebidas. Substitua "Your-API-Key" pela chave de API do Baidu do seu projeto.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

Por fim, você precisará registrar seus usuários na Braze. No método `onBind()` do broadcast receiver do Baidu que você criou nesta etapa, envie o `channelId` para a Braze usando `Braze.registerAppboyPushMessages(channelId)`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## Etapa 5: Registrando aberturas de push {#step-5-registering-push-opens}

O Baidu oferece suporte ao envio de pares chave-valor extras com mensagens push em formato JSON. O método `public void onNotificationClicked(Context context, String title, String description, String customContentString)` do seu broadcast receiver será chamado sempre que um usuário clicar em uma mensagem push recebida. O parâmetro `customContentString` contém os extras em formato JSON. Todas as mensagens da Braze conterão os dois pares chave-valor a seguir:

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

Sempre que `onNotificationClicked` for chamado pelo seu receiver Baidu, o receiver deve enviar um [Intent](http://developer.android.com/reference/android/content/Intent.html) para o seu aplicativo contendo `customContentString`. Seu aplicativo registrará o clique na Braze usando o `customContentString`.

O código de exemplo a seguir passa `customContentString` para a Braze e registra um clique:

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## Etapa 6: Extras {#step-6-extras}

Além das chaves reservadas usadas pela Braze, o parâmetro `customContentString` também contém todos os pares chave-valor personalizados definidos pelo usuário. Para extrair seus pares chave-valor, envolva `customContentString` em um JSONObject e recupere seus extras:

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## Etapa 7: Configurar as chaves do Baidu {#step-7-set-up-baidu-keys}

Você precisa inserir sua chave de API do Baidu e sua chave secreta do Baidu no dashboard da Braze. Ambas as chaves estão disponíveis no console de aplicativos do Baidu.

Na página **Manage Settings**, selecione seu app Android China e insira sua chave de API do Baidu e sua chave secreta do Baidu na seção de notificações por push.

![Chave de API do Baidu]({% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"){: style="max-width:80%;"}

## Recursos adicionais {#additional-resources}

- [Portal do Baidu](https://www.baidu.com/)
- [Portal do desenvolvedor Baidu](http://developer.baidu.com/)
- [Portal de projetos Baidu](http://developer.baidu.com/console#app/project)
- [Portal do SDK de push do Baidu](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)
- [Documentação de integração do Baidu](http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview)
---
nav_title: Integre o SDK
article_title: Integre o SDK da Braze
description: "Aprenda como integrar o SDK da Braze."
page_order: 2.0
---

# ![Logotipo da Braze]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Integre o SDK da Braze {#braze-logo-image_buster-assetsbraze_primary_icon_blacksvg-stylefloatrightwidth120pxborder0-classnoimgborderintegrate-the-braze-sdk}

> Aprenda como integrar o SDK da Braze. Cada SDK é hospedado em seu próprio repositório público no GitHub, que inclui apps de exemplo totalmente compiláveis que você pode usar para testar os recursos da Braze ou implementar junto com suas próprias aplicações. Para saber mais, veja [Referências, repositórios e apps de exemplo]({{site.baseurl}}/developer_guide/references). Para mais informações gerais sobre o SDK, veja [Introdução: Visão geral da integração]({{site.baseurl}}/developer_guide/getting_started/integration_overview).

Para conteúdo espelhado do README do SDK na documentação, veja [Guias de repositório]({{site.baseurl}}/developer_guide/sdk_repository_guides).

{% alert tip %}
Após integrar o SDK, você pode ativar a [autenticação do SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication) para adicionar uma camada adicional de segurança, impedindo solicitações não autorizadas ao SDK. A autenticação do SDK está disponível para Web, Android, Swift, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin) e Expo.
{% endalert %}

{% alert note %}
Se a inicialização do SDK falhar com erros de confiança de certificado HTTPS (por exemplo, `SSLHandshakeException` com `Trust anchor for certification path not found`), consulte [Solução de problemas de erros de confiança de certificado do SDK]({{site.baseurl}}/developer_guide/sdk_integration/troubleshooting_certificate_errors).
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/sdk_integration.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/sdk_integration.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/sdk_integration.md %}
{% endsdktab %}

{% sdktab React Native %}
{% multi_lang_include developer_guide/react_native/sdk_integration.md %}
{% endsdktab %}

{% sdktab roku %}
## Integrando o Roku SDK {#integrating-the-roku-sdk}

### Etapa 1: Adicionar arquivos {#step-1-add-files}

Os arquivos do SDK da Braze podem ser encontrados no diretório `sdk_files` no [repositório do Braze Roku SDK](https://github.com/braze-inc/braze-roku-sdk).

1. Adicione `BrazeSDK.brs` ao seu app no diretório `source`.
2. Adicione `BrazeTask.brs` e `BrazeTask.xml` ao seu app no diretório `components`.

### Etapa 2: Adicionar referências {#step-2-add-references}

Adicione uma referência ao `BrazeSDK.brs` na sua cena principal usando o seguinte elemento `script`:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Etapa 3: Configurar {#step-3-configure}

Em `main.brs`, defina a configuração da Braze no nó global:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Você pode encontrar seu [endpoint de SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) e chave de API no dashboard da Braze.

### Etapa 4: Inicializar a Braze {#step-4-initialize-braze}

Inicialize a instância da Braze:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configurações opcionais {#optional-configurations}

### Registro de logs {#logging}

Para depurar sua integração com a Braze, você pode visualizar o console de depuração do Roku para os logs da Braze. Consulte [Depuração de código](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) da Roku Developers para saber mais.

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/sdk_integration.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}

{% sdktab chatgpt apps %}
{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}
{% endsdktab %}

{% sdktab vega %}
{% multi_lang_include developer_guide/vega/sdk_integration.md %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
Ao realizar QA na sua integração de SDK, use o [Depurador do SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sem ativar o registro detalhado no seu app.
{% endalert %}
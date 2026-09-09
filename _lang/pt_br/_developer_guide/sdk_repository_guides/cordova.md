---
nav_title: Cordova SDK
article_title: Guia do repositório do Cordova SDK
page_order: 5
description: "Referência do README do Cordova SDK da Braze espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do Cordova SDK {#cordova-sdk-repository-guide}

## Sobre o SDK Cordova da Braze {#about-the-braze-cordova-sdk}

O SDK Cordova da Braze ajuda você a integrar os recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze no seu app.

Para começar, consulte os seguintes recursos:

- [Guia do Usuário da Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova)

## Requisitos mínimos de versão {#minimum-version-requirements}

A tabela a seguir lista as versões mínimas compatíveis com o SDK Cordova da Braze.

| Plugin Braze | Cordova Android | Cordova iOS |
| ------------ | --------------- | ----------- |
| 10.0.0+      | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+      | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos mínimos de versão" }

Este SDK também herda os requisitos dos SDKs nativos da Braze subjacentes. Certifique-se de também seguir as informações de compatibilidade de versão definidas em [braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk) e [braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).

## Instalando o SDK {#installing-the-sdk}

{% alert important %}
Adicione o SDK Cordova da Braze usando apenas os métodos a seguir. Usar outros métodos pode introduzir riscos de segurança.
{% endalert %}
``` text
# To use the base SDK functionality, install using the `master` branch.

cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To use location collection and geofences in addition to the base SDK functionality, install using `geofence-branch`.
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

## Executando o app de exemplo {#running-the-sample-application}
``` text
cordova plugin remove cordova-plugin-braze
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To run android
cordova run android

# To run iOS
cordova run ios
```
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-cordova-sdk](https://github.com/braze-inc/braze-cordova-sdk).
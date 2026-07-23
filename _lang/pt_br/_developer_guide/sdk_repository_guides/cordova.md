---
nav_title: Cordova SDK
article_title: Guia do repositório do Cordova SDK
page_order: 5
description: "Referência do README do Cordova SDK da Braze espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do Cordova SDK {#cordova-sdk-repository-guide}

## Sobre o SDK Cordova da Braze {#about-the-braze-cordova-sdk}

O SDK Cordova da Braze ajuda você a integrar recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze ao seu app.

Para começar, consulte os seguintes recursos:

- [Guia do Usuário da Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova)

## Requisitos mínimos de versão {#minimum-version-requirements}

| Plugin Braze | Cordova Android | Cordova iOS |
| ------------ | --------------- | ----------- |
| 10.0.0+      | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+      | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos mínimos de versão" }

Esse SDK também herda os requisitos dos SDKs nativos da Braze subjacentes. Certifique-se de também seguir os seguintes requisitos dos SDKs nativos:
* [Requisitos do SDK Android](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
* [Requisitos do SDK SWIFT](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

## Instalando o SDK {#installing-the-sdk}
{% alert warning %}
Adicione o SDK Cordova da Braze apenas usando os métodos abaixo. Não tente instalar usando outros métodos, pois isso pode levar a uma falha de segurança.
{% endalert %}
``` text
# To use the base SDK functionality, install using the `master` branch.

cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To use location collection and geofences in addition to the base SDK functionality, install using `geofence-branch`.
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

## Executando o aplicativo de exemplo {#running-the-sample-application}
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
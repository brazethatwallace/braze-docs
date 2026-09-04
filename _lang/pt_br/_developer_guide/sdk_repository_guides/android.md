---
nav_title: Android SDK
article_title: Guia do repositório do Android SDK
page_order: 2
description: "Referência do README do Android SDK da Braze espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do Android SDK {#android-sdk-repository-guide}

## Sobre o SDK Android da Braze {#about-the-braze-android-sdk}

O SDK Android da Braze ajuda você a integrar os recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze ao seu aplicativo.

Para começar, consulte os seguintes recursos:

- [Guia do usuário da Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guia do desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android)

## Início rápido {#quickstart}

Os snippets a seguir mostram a configuração mínima necessária para adicionar o SDK da Braze para Android ao seu app.

``` groovy
// build.gradle

// ...
repositories {
  mavenCentral()
}
// ...
dependencies {
  `implementation 'com.braze:android-sdk-ui:43.1.+'`
  `implementation 'com.braze:android-sdk-location:43.1.+'`
}
// ...
```

``` xml
<!-- res/values/braze.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

``` kotlin
Braze.getInstance(context).changeUser("Jane Doe");
```

Para saber mais sobre opções avançadas de integração, consulte o [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android).

## Suporte de versão {#version-support}

{% alert important %}
O SDK Android da Braze declara um `minSdkVersion` de API 21+, o que permite que o SDK seja compilado em apps que suportam a partir da API 21. Embora o SDK compile para essas versões, a Braze não oferece suporte formal para versões de API abaixo de 25, e o SDK pode não funcionar conforme o esperado em dispositivos que executam essas versões.

Se o seu app suporta essas versões, faça o seguinte:

- Valide que sua integração do SDK funciona conforme o esperado em dispositivos físicos (não apenas emuladores) para essas versões de API.
- Se você não conseguir validar o comportamento esperado, deve chamar [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) ou pular a inicialização do SDK nessas versões. Caso contrário, você pode causar efeitos colaterais indesejados ou desempenho degradado nos dispositivos dos seus usuários.
{% endalert %}
A tabela a seguir lista as versões mínimas suportadas para ferramentas usadas pelo SDK Android da Braze.

Ferramenta | Versão mínima suportada
:----|:----
minSdk|5.0+ / API 21+ (Lollipop e superior)
targetSdk|37
Kotlin|`org.jetbrains.kotlin:kotlin-stdlib:2.2.20`
Firebase Cloud Messaging|25.1.1
Font Awesome|4.3.0

## Módulos {#modules}

A tabela a seguir descreve cada módulo no SDK da Braze para Android.

Módulo | Descrição
:----|:----
`android-sdk-base`|A biblioteca base de análise de dados do SDK da Braze.
`android-sdk-ui`|A biblioteca de interface do usuário do SDK da Braze para mensagens no app, push, Content Cards e banners.
`android-sdk-location`|A biblioteca de localização do SDK da Braze para locais e geofences.
`android-sdk-jetpack-compose`|A biblioteca do SDK da Braze para suporte ao Jetpack Compose.
`droidboy`|Um app de exemplo que demonstra como usar a Braze em profundidade.
`android-sdk-unity`|Uma biblioteca que permite integrações do SDK da Braze no Unity.
`samples`|Uma pasta que contém apps de exemplo para diversas opções de integração.

## Contato {#contact}

Para dúvidas, entre em contato com o suporte técnico da Braze.
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk).
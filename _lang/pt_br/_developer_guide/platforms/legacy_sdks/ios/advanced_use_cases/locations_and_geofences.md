---
nav_title: Localizações e geofences
article_title: Localizações e geofences para iOS
platform: iOS
page_order: 6
description: "Este artigo de referência explica como implementar localizações e geofences no seu app para iOS."
tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Localizações e geofences {#locations-and-geofences}

Para oferecer suporte a geofences no iOS:

1. Sua integração deve suportar notificações por push em segundo plano.
2. [É preciso ativar]({{site.baseurl}}/developer_guide/geofences?sdktab=swift) as geofences da Braze pelo SDK or kit de desenvolvimento de software, seja implicitamente (com a ativação da coleta de localização) ou explicitamente (com a ativação da coleta de geofence). Elas não estão ativadas por padrão.

{% alert important %}
A partir do iOS 14, as geofences não funcionam de forma confiável para os usuários que optam por conceder permissão de localização aproximada.
{% endalert %}

## Etapa 1: Ativar push em segundo plano {#step-1-enable-background-push}

Para utilizar totalmente nossa estratégia de sincronização de geofences, você deve ter o [push em segundo plano]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications#use-silent-push-notifications-to-trigger-background-work) ativado, além de concluir a integração padrão de push.

## Etapa 2: Ativar geofences {#step-2-enable-geofences}

Por padrão, as geofences são ativadas com base na ativação ou não da coleta automática de localização. Você pode ativar geofences usando o arquivo `Info.plist`. Adicione o dicionário `Braze` ao seu arquivo `Info.plist`. Dentro do dicionário `Braze`, adicione a subentrada booleana `EnableGeofences` e defina o valor como `YES`. Observe que, antes do Braze iOS SDK or kit de desenvolvimento de software v4.0.2, a chave de dicionário `Appboy` deve ser usada no lugar de `Braze`.

Você também pode ativar geofences no momento da inicialização do app usando o método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). No dicionário `appboyOptions`, defina `ABKEnableGeofencesKey` como `YES`. Por exemplo:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## Etapa 3: Verificar o push em segundo plano da Braze {#step-3-check-for-braze-background-push}

A Braze sincroniza geofences com os dispositivos usando notificações por push em segundo plano. Siga o artigo de [personalização do iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push) para garantir que seu aplicativo não execute nenhuma ação indesejada ao receber notificações de sincronização de geofences da Braze.

## Etapa 4: Adicionar NSLocationAlwaysUsageDescription ao seu Info.plist {#step-4-add-nslocationalwaysusagedescription-to-your-infoplist}

Adicione as chaves `NSLocationAlwaysUsageDescription` e `NSLocationAlwaysAndWhenInUseUsageDescription` ao seu `info.plist` com um valor `String` que contenha uma descrição do motivo pelo qual seu aplicativo precisa rastrear a localização. Ambas as chaves são exigidas pelo iOS 11 ou posterior.
Essa descrição será exibida quando o prompt de localização do sistema solicitar autorização e deve explicar claramente os benefícios do monitoramento de localização para seus usuários.

## Etapa 5: Solicitar autorização do usuário {#step-5-request-authorization-from-the-user}

O recurso de geofences só funciona quando a autorização de localização `Always` é concedida.

Para solicitar a autorização de localização `Always`, use o seguinte código:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## Etapa 6: Ativar geofences no dashboard {#step-6-enable-geofences-on-the-dashboard}

O iOS permite que apenas até 20 geofences sejam armazenadas para um determinado app. O uso de localizações consumirá alguns desses 20 slots de geofence disponíveis. Para evitar interrupções acidentais ou indesejadas em outras funcionalidades relacionadas a geofences no seu app, as geofences de localização devem ser ativadas para apps individuais no dashboard.

Para que as localizações funcionem corretamente, você também deve confirmar que seu app não está usando todos os slots de geofence disponíveis.

### Ativar geofences na página de localizações: {#enable-geofences-from-the-locations-page}

![As opções de geofence na página de localizações da Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Ativar geofences na página de configurações: {#enable-geofences-from-the-settings-page}

![A caixa de seleção de geofence localizada nas páginas de configurações da Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Desativando solicitações automáticas de geofences {#disabling-automatic-geofence-requests}

A partir da versão 3.21.3 do SDK or kit de desenvolvimento de software para iOS, você pode desativar a solicitação automática de geofences. Para isso, utilize o arquivo `Info.plist`. Adicione o dicionário `Braze` ao seu arquivo `Info.plist`. Dentro do dicionário `Braze`, adicione a subentrada booleana `DisableAutomaticGeofenceRequests` e defina o valor como `YES`.

Você também pode desativar as solicitações automáticas de geofences no momento da inicialização do app por meio do método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). No dicionário `appboyOptions`, defina `ABKDisableAutomaticGeofenceRequestsKey` como `YES`. Por exemplo:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

Se você optar por usar essa opção, será necessário solicitar geofences manualmente para que o recurso funcione.

## Solicitação manual de geofences {#manually-requesting-geofences}

Quando o SDK or kit de desenvolvimento de software da Braze solicita geofences para monitorar a partir do backend, ele informa a localização atual do usuário e recebe geofences consideradas otimamente relevantes com base na localização informada. Há um limite de frequência de uma atualização de geofence por sessão.

Para controlar a localização que o SDK or kit de desenvolvimento de software informa para fins de receber as geofences mais relevantes, a partir da versão 3.21.3 do SDK or kit de desenvolvimento de software para iOS, você pode solicitar geofences manualmente fornecendo a latitude e a longitude de um local. É recomendável desativar as solicitações automáticas de geofence ao usar esse método. Para isso, use o seguinte código:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}
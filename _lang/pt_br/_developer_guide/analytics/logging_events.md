---
nav_title: Registrar eventos personalizados
article_title: Registrar eventos personalizados
page_order: 3.1
description: "Aprenda como registrar eventos personalizados por meio do SDK da Braze."
---

# Registrar eventos personalizados {#log-custom-events}

> Aprenda como registrar eventos personalizados por meio do SDK da Braze.

{% alert note %}
Para wrapper SDKs não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

Para eventos recomendados de eCommerce, consulte [Registrar eventos de eCommerce]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events).

## Registrando um evento personalizado {#logging-a-custom-event}

Para registrar um evento personalizado, use o seguinte método de registro de eventos.

{% tabs %}
{% tab web %}
Para uma implementação padrão do SDK para web, você pode usar o seguinte método:

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Se preferir usar o Google Tag Manager, você pode usar o tipo de tag **Custom Event** para chamar o [método `logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) e enviar eventos personalizados para a Braze, incluindo opcionalmente propriedades de evento personalizado. Para fazer isso:

1. Insira o **Event Name** usando uma variável ou digitando o nome de um evento.
2. Use o botão **Add Row** para adicionar propriedades de evento.

![Caixa de diálogo mostrando as configurações da tag de ação da Braze. As configurações incluem "tag type" (evento personalizado), "event name" (clique no botão) e "event properties".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
Para Android nativo, você pode usar o seguinte método:

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab cordova %}
Use o método do plugin Cordova da Braze:

```javascript
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");
```

A API `logCustomEvent` aceita:
- `eventName` (string obrigatória): Use até 255 caracteres. Não inicie o nome com `$`. Use caracteres alfanuméricos e pontuação.
- `eventProperties` (objeto opcional): Adicione pares chave-valor para metadados do evento. Use chaves de até 255 caracteres e não inicie as chaves com `$`.

Para valores de propriedade, use `string` (até 255 caracteres), `numeric`, `boolean`, arrays ou objetos JSON aninhados.

Para detalhes de implementação, consulte o código-fonte do SDK Cordova da Braze:
- [Método `logCustomEvent` em `www/BrazePlugin.js` (linhas 138-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L138-L140)
- [JSDoc em `www/BrazePlugin.js` (linhas 128-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Handler Android em `src/android/BrazePlugin.kt` (linhas 108-115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [Handler iOS em `src/ios/BrazePlugin.m` (linhas 308-313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
- [Declaração do método iOS em `src/ios/BrazePlugin.h` (linha 24)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.h#L24)
{% endtab %}

{% tab infillion %}
Se você integrou os [Infillion Beacons](https://infillion.com/software/beacons/) ao seu app Android, pode opcionalmente usar `visit.getPlace()` para registrar eventos específicos de localização. `requestImmediateDataFlush` garante que seu evento será registrado mesmo se o app estiver em segundo plano.

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}
{% endtabs %}

## Adicionando propriedades de metadados {#adding-metadata-properties}

Ao registrar um evento personalizado, você tem a opção de adicionar metadados sobre esse evento personalizado passando um objeto de propriedades junto com o evento. As propriedades são definidas como pares de chave-valor. As chaves são strings e os valores podem ser `string`, `numeric`, `boolean`, objetos [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp), arrays ou objetos JSON aninhados.

Para adicionar propriedades de metadados, use o seguinte método de registro de eventos.

{% tabs %}
{% tab web %}
```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can",
  pass: false,
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(
  name: "YOUR-EVENT-NAME",
  properties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
                       properties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab cordova %}
Registre eventos personalizados com um objeto de propriedades:

```javascript
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);
```

Você também pode passar propriedades inline:

```javascript
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
  "key": "value",
  "amount": 42,
});
```

O app de exemplo oficial do Cordova inclui propriedades de string, numéricas, booleanas, arrays e objetos aninhados:
- [`sample-project/www/js/index.js` (linhas 230-251)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/sample-project/www/js/index.js#L230-L251)

Trecho do projeto de exemplo:

```javascript
var properties = {};
properties["One"] = "That's the Way of the World";
properties["Two"] = "After the Love Has Gone";
properties["Three"] = "Can't Hide Love";
BrazePlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
BrazePlugin.logCustomEvent("cordovaCustomEventWithoutProperties");
BrazePlugin.logCustomEvent("cordovaCustomEventWithFloatProperties", {
  "Cart Value": 4.95,
  "Cart Item Name": "Spicy Chicken Bites 5 pack"
});
BrazePlugin.logCustomEvent("cordovaCustomEventWithNestedProperties", {
  "array key": [1, "2", false],
  "object key": {
    "k1": "1",
    "k2": 2,
    "k3": false,
  },
  "deep key": {
    "key": [1, "2", true]
  }
});
```

Para detalhes sobre a API e a ponte nativa, consulte:
- [`www/BrazePlugin.js` JSDoc (linhas 128-140)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [Handler Android em `src/android/BrazePlugin.kt` (linhas 108-115)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [Handler iOS em `src/ios/BrazePlugin.m` (linhas 308-313)](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
{% endtab %}

{% tab React Native %}
```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}
{% endtabs %}

{% alert important %}
As chaves `time` e `event_name` são reservadas e não podem ser usadas como propriedades de eventos personalizados.
{% endalert %}

## Práticas recomendadas {#best-practices}

Existem três verificações importantes a realizar para que as propriedades de eventos personalizados sejam registradas conforme esperado:

* [Verificar quais eventos são registrados](#verify-events)
* [Verificar o registro](#verify-log)
* [Verificar os valores](#verify-values)

Várias propriedades podem ser registradas cada vez que um evento personalizado é registrado.

### Verificar eventos {#verify-events}

Confirme com seus desenvolvedores quais propriedades de eventos estão sendo rastreadas. Lembre-se de que todas as propriedades de eventos diferenciam maiúsculas de minúsculas. Para mais informações sobre o rastreamento de eventos personalizados, confira estes artigos de acordo com a sua plataforma:

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
* [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)

### Verificar o registro {#verify-log}

Para confirmar que as propriedades de eventos estão sendo rastreadas com sucesso, você pode visualizar todas as propriedades de eventos na página **Custom Events**.

1. Acesse **Data Settings** > **Custom Events**.
2. Localize seu evento personalizado na lista.
3. Para o seu evento, selecione **Manage Properties** para visualizar os nomes das propriedades associadas ao evento.

### Verificar os valores {#verify-values}

Depois de [adicionar seu usuário como usuário teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), siga estas etapas para verificar seus valores:

1. Execute o evento personalizado no app.
2. Aguarde aproximadamente 10 segundos para que os dados sejam enviados.
3. Atualize o [registro de usuários de eventos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) para visualizar o evento personalizado e o valor da propriedade de evento que foi transmitido com ele.

## Solução de problemas para eventos personalizados {#troubleshooting-custom-events}

Use estes cenários para solucionar problemas de registro de eventos personalizados em diferentes SDKs.

### Verificando o disparo do evento personalizado {#verifying-the-custom-event-trigger}

Se um evento personalizado não aparece, a ação rastreada no seu app pode não corresponder à ação que você está testando.

- Confirme com sua equipe de desenvolvimento qual ação do app dispara o evento personalizado.
- Verifique se há caminhos de código descontinuados após atualizações do SDK, como referências a `appboy` em vez de `braze`.

### Eventos personalizados registrados em um perfil anônimo {#custom-events-are-logged-to-an-anonymous-profile}

Se você não identificar um usuário antes de registrar um evento personalizado, a Braze pode associar esse evento a um perfil anônimo.

- Chame `changeUser()` antes de executar o evento personalizado para que a Braze registre o evento em um perfil de usuário identificado.
- Teste com um usuário teste identificado e depois consulte o [registro de usuários de eventos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log).

### Verificando a configuração de registro de eventos personalizados {#verifying-custom-event-logging-setup}

Se os eventos personalizados não estão aparecendo como esperado, confirme que sua equipe de desenvolvimento implementou o registro de eventos personalizados para a ação correta do app.

- Peça à sua equipe de desenvolvimento que verifique se o evento está sendo registrado corretamente e disparado a partir da ação de usuário esperada.
- Quando sua equipe abrir um ticket de suporte com o suporte da Braze, inclua [logs detalhados]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) e snippets de código relevantes.
- Se o seu app usa SWIFT ou Android, sua equipe de desenvolvimento pode usar os [pré-requisitos do debugger do SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging#prerequisites) para ajudar a gerar logs detalhados.
- Se sua equipe de desenvolvimento não conseguir identificar o problema, abra um [ticket de suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).
---
nav_title: Definir atributos personalizados
article_title: Definir atributos personalizados para iOS
platform: iOS
page_order: 3
description: "Este artigo de referência mostra como definir atributos personalizados no seu aplicativo iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Definir atributos personalizados para iOS {#set-custom-attributes-for-ios}

A Braze fornece métodos para atribuir atributos aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com esses atributos no dashboard.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [melhores práticas]({{site.baseurl}}/developer_guide/analytics), bem como nossas notas sobre [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

## Atribuindo atributos de usuário padrão {#assigning-default-user-attributes}

Para atribuir atributos de usuário, você precisa definir o campo apropriado no objeto compartilhado `ABKUser`.

A seguir, um exemplo de como definir o atributo de nome:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].user.firstName = @"first_name";
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.firstName = "first_name"
```

{% endtab %}
{% endtabs %}

Os seguintes atributos devem ser definidos no objeto `ABKUser`:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `userID`
- `gender`

## Atribuindo atributos personalizados ao usuário {#assigning-custom-user-attributes}

Além dos atributos de usuário padrão, a Braze também permite que você defina atributos personalizados usando vários tipos diferentes de dados. Consulte nossa documentação de [coleta de dados de usuários]({{site.baseurl}}/developer_guide/analytics) para saber mais sobre as opções de segmentação que cada um desses atributos oferece.

### Atributo personalizado com valor da string {#custom-attribute-with-a-string-value}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andStringValue:"your_attribute_value"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andStringValue: "your_attribute_value")
```

{% endtab %}
{% endtabs %}

### Atributo personalizado com valor inteiro {#custom-attribute-with-an-integer-value}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andIntegerValue: yourIntegerValue)
```

{% endtab %}
{% endtabs %}

### Atributo personalizado com valor double {#custom-attribute-with-a-double-value}

A Braze trata valores `float` e `double` da mesma forma em nosso banco de dados.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDoubleValue: yourDoubleValue)
```

{% endtab %}
{% endtabs %}

### Atributo personalizado com valor booleano {#custom-attribute-with-a-boolean-value}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andBOOLValue: yourBoolValue)
```

{% endtab %}
{% endtabs %}

### Atributo personalizado com valor de data {#custom-attribute-with-a-date-value}

As datas enviadas à Braze com esse método devem estar no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (por exemplo, `2013-07-16T19:20:30+01:00`) ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (`2016-12-14T13:32:31.601-0800`).

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDateValue:yourDateValue)
```

{% endtab %}
{% endtabs %}

### Atributo personalizado com valor de array {#custom-attribute-with-an-array-value}

O número máximo de elementos em um array é 500 por padrão. Você pode atualizar o número máximo de arrays no dashboard da Braze, em **Data Settings** > **Custom Attributes**. Arrays que excedem o número máximo de elementos serão truncados para conter o número máximo de elementos.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Setting a custom attribute with an array value
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[[Appboy sharedInstance].user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
Appboy.sharedInstance()?.user.setCustomAttributeArrayWithKey("array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
Appboy.sharedInstance()?.user.addToCustomAttributeArrayWithKey("array_name", value: "value3")
// Removing a value from an array type custom attribute
Appboy.sharedInstance()?.user.removeFromCustomAttributeArrayWithKey("array_name", value: "value2")
```

{% endtab %}
{% endtabs %}

### Removendo a definição de um atributo personalizado {#unsetting-a-custom-attribute}

Os atributos personalizados também podem ter sua definição removida usando o seguinte método:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.unsetCustomAttributeWithKey("your_attribute_key")
```

{% endtab %}
{% endtabs %}

### Incrementando/decrementando atributos personalizados {#incrementingdecrementing-custom-attributes}

Este código é um exemplo de incremento de atributo personalizado. Você pode incrementar o valor de um atributo personalizado por qualquer valor inteiro ou long, positivo ou negativo:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.incrementCustomUserAttribute("your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% endtabs %}

### Definindo um atributo personalizado via REST or transferir estado representacional API or interface de programação do aplicativo (API) {#setting-a-custom-attribute-via-the-rest-api}

Você também pode usar nossa REST or transferir estado representacional API or interface de programação do aplicativo (API) para definir atributos de usuário. Consulte a [documentação da API or interface de programação do aplicativo (API) de usuários]({{site.baseurl}}/api/endpoints/user_data) para mais detalhes.

### Limites de valor de atributos personalizados {#custom-attribute-value-limits}

Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.

#### Informações adicionais {#additional-information}

- Mais detalhes podem ser encontrados no [arquivo `ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
- Consulte a [documentação do `ABKUser`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html) para saber mais.

## Configurando inscrições de usuários {#setting-up-user-subscriptions}

Para configurar uma inscrição para seus usuários (e-mail ou push), chame as funções `setEmailNotificationSubscriptionType` ou `setPushNotificationSubscriptionType`, respectivamente. Ambas as funções recebem o tipo enum `ABKNotificationSubscriptionType` como argumento. Esse tipo possui três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `ABKOptedin` | Inscrito e com aceitação explícita |
| `ABKSubscribed` | Inscrito, mas sem aceitação explícita |
| `ABKUnsubscribed` | Inscrição cancelada e/ou recusa explícita |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurando inscrições de usuários" }

Usuários que concedem permissão para um app enviar notificações por push têm o status padrão `ABKOptedin`, pois o iOS exige uma aceitação explícita.

Os usuários serão definidos automaticamente como `ABKSubscribed` ao receberem um endereço de e-mail válido. No entanto, recomendamos que você estabeleça um processo de aceitação explícita e defina esse valor como `OptedIn` ao receber o consentimento explícito do usuário. Consulte [Gerenciamento de inscrições de usuários]({{site.baseurl}}/user_guide/channels/email/subscriptions) para mais detalhes.

### Configurando inscrições de e-mail {#setting-email-subscriptions}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setEmailNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setEmailNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### Configurando inscrições de notificações por push {#setting-push-notification-subscriptions}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].user setPushNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setPushNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

Consulte [Gerenciamento de inscrições de usuários]({{site.baseurl}}/user_guide/channels/email/subscriptions) para mais detalhes.
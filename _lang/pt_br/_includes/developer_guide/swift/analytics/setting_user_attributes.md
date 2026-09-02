{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Atributos padrão do usuário {#default-user-attributes}

### Atributos suportados {#supported-attributes}

Os seguintes atributos devem ser definidos no objeto `Braze.User`:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

### Definindo atributos padrão {#setting-default-attributes}

Para definir um atributo padrão do usuário, defina o campo apropriado no objeto compartilhado `Braze.User`. A seguir, um exemplo de como definir o atributo de nome:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
```

{% endtab %}
{% endtabs %}

### Removendo atributos padrão {#unsetting-default-attributes}

Para remover um atributo padrão do usuário, passe `nil` para o método relevante.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: nil)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:nil];
```

{% endtab %}
{% endtabs %}

## Atributos personalizados do usuário {#custom-user-attributes}

Além dos atributos padrão do usuário, a Braze também permite que você defina atributos personalizados usando vários tipos de dados diferentes. Para saber mais sobre as opções de segmentação de cada atributo, consulte [Coleta de dados do usuário]({{site.baseurl}}/developer_guide/analytics).

{% alert important %}
Os valores dos atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados. Para saber mais, consulte [`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class).
{% endalert %}

### Definindo atributos personalizados {#setting-custom-attributes}

{% tabs local %}
{% tab string %}
Para definir um atributo personalizado com um valor de `string`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab integer %}
Para definir um atributo personalizado com um valor de `integer`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab floating-points %}
A Braze trata valores `float` e `double` da mesma forma em nosso banco de dados. Para definir um atributo personalizado com um valor double:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab boolean %}
Para definir um atributo personalizado com um valor `boolean`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab date %}
Para definir um atributo personalizado com um valor de `date`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab array %}
O número padrão e máximo de elementos em um array é 500. Você pode atualizar o número máximo de arrays no dashboard da Braze, em **Data Settings** > **Custom Attributes**. Arrays que excederem o número máximo de elementos serão truncados para conter o número máximo de elementos.

Para definir um atributo personalizado com um valor de `array`:

{% subtabs %}
{% subtab swift %}
```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Incrementando ou decrementando atributos personalizados {#incrementing-or-decrementing-custom-attributes}

Este código é um exemplo de incremento de atributo personalizado. Você pode incrementar o valor de um atributo personalizado por qualquer valor `integer` ou `long`:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### Removendo atributos personalizados {#unsetting-custom-attributes}

{% tabs %}
{% tab swift %}
Para remover um atributo personalizado, passe a chave do atributo relevante para o método `unsetCustomAttribute`.

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objective-c %}
Para remover um atributo personalizado, passe a chave do atributo relevante para o método `unsetCustomAttributeWithKey`.

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Aninhando atributos personalizados {#nesting-custom-attributes}

Você também pode aninhar propriedades dentro de atributos personalizados. No exemplo a seguir, um objeto `favorite_book` com propriedades aninhadas é definido como um atributo personalizado no perfil de usuário. Para saber mais, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

{% tabs %}
{% tab swift %}
```swift
let favoriteBook: [String: Any?] = [
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)
```
{% endtab %}

{% tab objective-c %}
```objc
NSDictionary *favoriteBook = @{
  @"title": @"The Hobbit",
  @"author": @"J.R.R. Tolkien",
  @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];
```
{% endtab %}
{% endtabs %}

### Usando a REST API {#using-the-rest-api}

Você também pode usar nossa REST API para definir ou remover atributos do usuário. Para saber mais, consulte [Endpoints de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Definindo inscrições do usuário {#setting-user-subscriptions}

Para configurar uma inscrição para seus usuários (e-mail ou push), chame as funções `set(emailSubscriptionState:)` ou `set(pushNotificationSubscriptionState:)`, respectivamente. Ambas as funções recebem o tipo enum `Braze.User.SubscriptionState` como argumento. Esse tipo possui três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `optedIn` | Inscrito e com aceitação explícita |
| `subscribed` | Inscrito, mas sem aceitação explícita |
| `unsubscribed` | Cancelou a inscrição e/ou recusou explicitamente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definindo inscrições do usuário" }

Usuários que concedem permissão para um app enviar notificações por push recebem, por padrão, o status `optedIn`, pois o iOS exige uma aceitação explícita.

Usuários serão definidos automaticamente como `subscribed` ao receberem um endereço de e-mail válido; no entanto, recomendamos que você estabeleça um processo de aceitação explícita e defina esse valor como `optedIn` ao receber o consentimento explícito do seu usuário. Consulte [Gerenciamento de inscrições de usuários]({{site.baseurl}}/user_guide/channels/email/subscriptions) para mais detalhes.

### Definindo inscrições de e-mail {#setting-email-subscriptions}

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### Definindo inscrições de notificação por push {#setting-push-notification-subscriptions}

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Consulte [Gerenciamento de inscrições de usuários]({{site.baseurl}}/user_guide/channels/email/subscriptions) para mais detalhes.
{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Atributos predeterminados del usuario {#default-user-attributes}

### Atributos admitidos {#supported-attributes}

Los siguientes atributos deben establecerse en el objeto `Braze.User`:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

### Configuración de atributos predeterminados {#setting-default-attributes}

Para establecer un atributo predeterminado del usuario, configura el campo correspondiente en el objeto compartido `Braze.User`. A continuación se muestra un ejemplo de cómo establecer el atributo de nombre:

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

### Desactivar atributos predeterminados {#unsetting-default-attributes}

Para desactivar un atributo predeterminado del usuario, pasa `nil` al método correspondiente.

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

## Atributos personalizados del usuario {#custom-user-attributes}

Además de los atributos predeterminados del usuario, Braze también te permite definir atributos personalizados utilizando distintos tipos de datos. Para más información sobre las opciones de segmentación de cada atributo, consulta [Recopilación de datos de usuario]({{site.baseurl}}/developer_guide/analytics).

{% alert important %}
Los valores de los atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán. Para más información, consulta [`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class).
{% endalert %}

### Configuración de atributos personalizados {#setting-custom-attributes}

{% tabs local %}
{% tab string %}
Para establecer un atributo personalizado con un valor `string`:

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
Para establecer un atributo personalizado con un valor `integer`:

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
Braze trata los valores `float` y `double` de la misma manera en nuestra base de datos. Para establecer un atributo personalizado con un valor double:

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
Para establecer un atributo personalizado con un valor `boolean`:

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
Para establecer un atributo personalizado con un valor `date`:

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
La cantidad predeterminada y máxima de elementos en un array es de 500. Puedes actualizar la cantidad máxima de arrays en el panel de Braze, en **Data Settings** > **Custom Attributes**. Los arrays que superen la cantidad máxima de elementos se truncarán para contener la cantidad máxima de elementos.

Para establecer un atributo personalizado con un valor `array`:

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

### Incrementar o decrementar atributos personalizados {#incrementing-or-decrementing-custom-attributes}

Este código es un ejemplo de un atributo personalizado que se incrementa. Puedes incrementar el valor de un atributo personalizado con cualquier valor `integer` o `long`:

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

### Desactivar atributos personalizados {#unsetting-custom-attributes}

{% tabs %}
{% tab swift %}
Para desactivar un atributo personalizado, pasa la clave del atributo correspondiente al método `unsetCustomAttribute`.

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objective-c %}
Para desactivar un atributo personalizado, pasa la clave del atributo correspondiente al método `unsetCustomAttributeWithKey`.

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Anidar atributos personalizados {#nesting-custom-attributes}

También puedes anidar propiedades dentro de los atributos personalizados. En el siguiente ejemplo, se establece un objeto `favorite_book` con propiedades anidadas como atributo personalizado en el perfil de usuario. Para más detalles, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

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

### Uso de la REST or transferencia de estado representacional API {#using-the-rest-api}

También puedes utilizar nuestra REST or transferencia de estado representacional API para establecer o desactivar atributos de usuario. Para más información, consulta [Endpoints de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Configuración de suscripciones de usuario {#setting-user-subscriptions}

Para configurar una suscripción para tus usuarios (ya sea correo electrónico o push), llama a las funciones `set(emailSubscriptionState:)` o `set(pushNotificationSubscriptionState:)`, respectivamente. Ambas funciones toman el tipo enumeración `Braze.User.SubscriptionState` como argumento. Este tipo tiene tres estados diferentes:

| Estado de suscripción | Definición |
| ------------------- | ---------- |
| `optedIn` | Suscrito y con adhesión voluntaria explícita |
| `subscribed` | Suscrito, pero sin adhesión voluntaria explícita |
| `unsubscribed` | Dado de baja o con exclusión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración de suscripciones de usuario" }

Los usuarios que otorgan permiso a una aplicación para enviarles notificaciones push tienen de forma predeterminada el estado `optedIn`, ya que iOS requiere una adhesión voluntaria explícita.

Los usuarios se establecerán en `subscribed` automáticamente cuando se reciba una dirección de correo electrónico válida; sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícito y configures este valor en `optedIn` cuando recibas el consentimiento explícito de tu usuario. Consulta [Gestionar suscripciones de usuario]({{site.baseurl}}/user_guide/channels/email/subscriptions) para más detalles.

### Configuración de suscripciones de correo electrónico {#setting-email-subscriptions}

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

### Configuración de suscripciones de notificaciones push {#setting-push-notification-subscriptions}

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

Consulta [Gestionar suscripciones de usuario]({{site.baseurl}}/user_guide/channels/email/subscriptions) para más detalles.
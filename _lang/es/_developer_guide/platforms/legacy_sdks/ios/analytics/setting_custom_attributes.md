---
nav_title: Establecer atributos personalizados
article_title: Establecer atributos personalizados para iOS
platform: iOS
page_order: 3
description: "Este artículo de referencia muestra cómo establecer atributos personalizados en tu aplicación iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Establecer atributos personalizados para iOS {#set-custom-attributes-for-ios}

Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el panel.

Antes de la implementación, asegúrate de revisar los ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [mejores prácticas]({{site.baseurl}}/developer_guide/analytics), así como nuestras notas sobre [las convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).

## Asignar atributos predeterminados al usuario {#assigning-default-user-attributes}

Para asignar atributos de usuario, necesitas establecer el campo apropiado en el objeto compartido `ABKUser`.

El siguiente es un ejemplo de cómo establecer el atributo de nombre:

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

Los siguientes atributos deben establecerse en el objeto `ABKUser`:

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

## Asignar atributos personalizados al usuario {#assigning-custom-user-attributes}

Más allá de los atributos de usuario predeterminados, Braze también te permite definir atributos personalizados utilizando varios tipos de datos diferentes. Consulta nuestra [recopilación de datos de usuario]({{site.baseurl}}/developer_guide/analytics) para obtener más información sobre las opciones de segmentación que te ofrecerá cada uno de estos atributos.

### Atributo personalizado con un valor de cadena {#custom-attribute-with-a-string-value}

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

### Atributo personalizado con un valor entero {#custom-attribute-with-an-integer-value}

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

### Atributo personalizado con un valor double {#custom-attribute-with-a-double-value}

Braze trata los valores `float` y `double` de la misma manera dentro de nuestra base de datos.

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

### Atributo personalizado con un valor booleano {#custom-attribute-with-a-boolean-value}

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

### Atributo personalizado con un valor de fecha {#custom-attribute-with-a-date-value}

Las fechas enviadas a Braze con este método deben estar en formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (por ejemplo, `2013-07-16T19:20:30+01:00`) o en el formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (`2016-12-14T13:32:31.601-0800`).

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

### Atributo personalizado con un valor de matriz {#custom-attribute-with-an-array-value}

La cantidad predeterminada y máxima de elementos en una matriz es de 500. Puedes actualizar la cantidad máxima de matrices en el panel de Braze, en **Configuración de datos** > **Atributos personalizados**. Las matrices que excedan la cantidad máxima de elementos se truncarán para contener la cantidad máxima de elementos.


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

### Desestablecer un atributo personalizado {#unsetting-a-custom-attribute}

Los atributos personalizados también se pueden desestablecer utilizando el siguiente método:

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

### Incrementar/decrementar atributos personalizados {#incrementingdecrementing-custom-attributes}

Este código es un ejemplo de un atributo personalizado que se incrementa. Puedes incrementar el valor de un atributo personalizado con cualquier valor entero o long, positivo o negativo:

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

### Establecer un atributo personalizado a través de la REST or transferencia de estado representacional API {#setting-a-custom-attribute-via-the-rest-api}

También puedes utilizar nuestra REST or transferencia de estado representacional API para establecer atributos de usuario. Consulta la [documentación de la API de usuario]({{site.baseurl}}/api/endpoints/user_data) para obtener más detalles.

### Límites de valores de atributos personalizados {#custom-attribute-value-limits}

Los valores de los atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán.

#### Información adicional {#additional-information}

- Puedes encontrar más detalles en el [archivo `ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
- Consulta la [documentación de `ABKUser`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html) para obtener más información.

## Configurar las suscripciones de usuario {#setting-up-user-subscriptions}

Para configurar una suscripción para tus usuarios (ya sea de correo electrónico o push), llama a las funciones `setEmailNotificationSubscriptionType` o `setPushNotificationSubscriptionType`, respectivamente. Ambas funciones toman el tipo de enumeración `ABKNotificationSubscriptionType` como argumento. Este tipo tiene tres estados diferentes:

| Estado de suscripción | Definición |
| ------------------- | ---------- |
| `ABKOptedin` | Suscrito y con adhesión voluntaria explícita |
| `ABKSubscribed` | Suscrito, pero sin adhesión voluntaria explícita |
| `ABKUnsubscribed` | Cancelada la suscripción o exclusión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurar las suscripciones de usuario" }

Los usuarios que conceden permiso a una aplicación para enviarles notificaciones push tienen de forma predeterminada el estado `ABKOptedin`, ya que iOS requiere una adhesión voluntaria explícita.

Los usuarios se establecerán automáticamente como `ABKSubscribed` tras la recepción de una dirección de correo electrónico válida; sin embargo, te recomendamos que establezcas un proceso de adhesión voluntaria explícito y configures este valor como `OptedIn` cuando recibas el consentimiento explícito de tu usuario. Consulta [Gestión de suscripciones de usuario]({{site.baseurl}}/user_guide/channels/email/subscriptions) para más detalles.

### Configurar las suscripciones de correo electrónico {#setting-email-subscriptions}

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

### Configurar las suscripciones de notificaciones push {#setting-push-notification-subscriptions}

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

Consulta [Gestión de suscripciones de usuario]({{site.baseurl}}/user_guide/channels/email/subscriptions) para más detalles.
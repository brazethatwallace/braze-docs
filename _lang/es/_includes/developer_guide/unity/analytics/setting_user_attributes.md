{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Atributos predeterminados del usuario {#default-user-attributes}

### Métodos predefinidos {#predefined-methods}

Braze proporciona métodos predefinidos para establecer los siguientes atributos de usuario utilizando el objeto `BrazeBinding`. Para más información, consulta el [archivo de declaración de Braze Unity](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs).

- Nombre
- Apellido
- Correo electrónico del usuario
- Género
- Fecha de nacimiento
- País del usuario
- Ciudad de origen del usuario
- Suscripción de correo electrónico del usuario
- Suscripción push del usuario
- Número de teléfono del usuario

### Configuración de atributos predeterminados {#setting-default-attributes}

Para establecer un atributo predeterminado, llama al método correspondiente en el objeto `BrazeBinding`.

{% tabs local %}
{% tab First name %}
```csharp
BrazeBinding.SetUserFirstName("first name");
```
{% endtab %}
{% tab Last name %}
```csharp
BrazeBinding.SetUserLastName("last name");
```
{% endtab %}
{% tab Email %}
```csharp
BrazeBinding.SetUserEmail("user@example.com");
```
{% endtab %}
{% tab Gender %}
```csharp
BrazeBinding.SetUserGender(Appboy.Models.Gender);
```
{% endtab %}
{% tab Birth date %}
```csharp
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```
{% endtab %}
{% tab Country %}
```csharp
BrazeBinding.SetUserCountry("country name");
```
{% endtab %}
{% tab Home city %}
```csharp
BrazeBinding.SetUserHomeCity("city name");
```
{% endtab %}
{% tab Email subscription %}
```csharp
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Push subscription %}
```csharp
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Phone number %}
```csharp
BrazeBinding.SetUserPhoneNumber("phone number");
```
{% endtab %}
{% endtabs %}

### Desactivar atributos predeterminados {#unsetting-default-attributes}

Para desactivar un atributo predeterminado del usuario, pasa `null` al método correspondiente.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## Atributos personalizados del usuario {#custom-user-attributes}

Además de los atributos predeterminados del usuario, Braze también te permite definir atributos personalizados utilizando distintos tipos de datos. Para obtener más información sobre las opciones de segmentación de cada atributo, consulta [Recopilación de datos de usuario]({{site.baseurl}}/developer_guide/analytics).

### Establecer atributos personalizados {#setting-custom-attributes}

Para establecer un atributo personalizado, utiliza el método correspondiente para el tipo de atributo:

{% tabs %}
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab Integer %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```
{% endtab %}

{% tab Float %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom float attribute key", 'float value');
```

{% endtab %}

{% tab Double %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double value');
```

{% endtab %}

{% tab Boolean %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```
{% endtab %}

{% tab Date %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
Las fechas pasadas a Braze deben estar en formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (como `2013-07-16T19:20:30+01:00`) o en el formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (como `2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}

{% tab Array %}

```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}

{% tab Nested objects %}

Puedes establecer atributos personalizados que contengan objetos anidados (disponible en Unity SDK or kit de desarrollo de software 5.1.0 y versiones posteriores). Para obtener más información, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).
Los siguientes ejemplos muestran cómo establecer un atributo de objeto anidado, fusionar actualizaciones en un objeto existente y establecer una matriz de objetos anidados.

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>));
```

Para actualizar un objeto anidado existente, utiliza el parámetro merge:

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>), merge(bool));
```

También puedes establecer una matriz de objetos anidados:

```csharp
AppboyBinding.SetCustomUserAttribute("custom object array attribute key", list(List<Dictionary<string, object>>));
```

{% endtab %}
{% endtabs %}

{% alert important %}
Los valores de los atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán.
{% endalert %}

### Desactivar atributos personalizados {#unsetting-custom-attributes}

Para desactivar un atributo personalizado, pasa la clave del atributo correspondiente al método `UnsetCustomUserAttribute`.

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Uso de la REST or transferencia de estado representacional API {#using-the-rest-api}

También puedes utilizar nuestra REST or transferencia de estado representacional API para establecer o desactivar atributos de usuario. Para obtener más información, consulta [Endpoints de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Configuración de suscripciones de usuario {#setting-user-subscriptions}

Para configurar una suscripción de correo electrónico o push para tus usuarios, llama a una de las siguientes funciones.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Ambas funciones toman `Appboy.Models.AppboyNotificationSubscriptionType` como argumento, que tiene tres estados diferentes:

| Estado de suscripción | Definición |
| ------------------- | ---------- |
| `OPTED_IN` | Suscrito y con adhesión voluntaria explícita |
| `SUBSCRIBED` | Suscrito, pero sin adhesión voluntaria explícita |
| `UNSUBSCRIBED` | Dado de baja o con exclusión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración de suscripciones de usuario" }

{% alert note %}
Windows no requiere una adhesión voluntaria explícita para enviar notificaciones push a los usuarios. Cuando un usuario se registra para push, se establece como `SUBSCRIBED` en lugar de `OPTED_IN` de forma predeterminada. Para obtener más información, consulta nuestra documentación sobre [implementación de suscripciones y adhesiones voluntarias explícitas]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions).
{% endalert %}

| Tipo de suscripción | Descripción |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType` | Los usuarios se establecerán como `SUBSCRIBED` automáticamente al recibir una dirección de correo electrónico válida. Sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícita y configures este valor como `OPTED_IN` cuando recibas el consentimiento explícito de tu usuario. Visita nuestro documento sobre [Cambiar las suscripciones de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions) para obtener más detalles. |
| `PushNotificationSubscriptionType` | Los usuarios se establecerán como `SUBSCRIBED` automáticamente tras un registro push válido. Sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícita y configures este valor como `OPTED_IN` cuando recibas el consentimiento explícito de tu usuario. Visita nuestro documento sobre [Cambiar las suscripciones de usuario]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions) para obtener más detalles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración de suscripciones de usuario" }

{% alert note %}
Estos tipos se encuentran en `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### Configuración de suscripciones de correo electrónico {#setting-email-subscriptions}

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Configuración de suscripciones de notificaciones push {#setting-push-notification-subscriptions}

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

---
nav_title: Establecer atributos personalizados
article_title: Establecer atributos personalizados para Windows Universal
platform: Windows Universal
page_order: 3
description: "En este artículo de referencia se explica cómo establecer atributos personalizados en la plataforma Windows Universal."
hidden: true
---

# Establecer atributos personalizados {#set-custom-attributes}
{% multi_lang_include archive/windows_deprecation.md %}

Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el dashboard.

Antes de la implementación, asegúrate de revisar los ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [mejores prácticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

Se pueden asignar atributos de usuario al `IAppboyUser` actual. Para obtener una referencia al `IAppboyUser` actual, llama a `Appboy.SharedInstance.AppboyUser`

## Asignar atributos predeterminados al usuario {#assigning-default-user-attributes}

Los siguientes atributos deben definirse como propiedades de `IAppboyUser`:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**Ejemplo de implementación**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## Asignar atributos personalizados al usuario {#assigning-custom-user-attributes}

Más allá de los atributos de usuario predeterminados, Braze también te permite definir atributos personalizados utilizando varios tipos de datos diferentes. Para más información sobre las opciones de segmentación y cómo te afectará cada uno de estos atributos, consulta nuestras [mejores prácticas]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes).

### Configuración de valores de atributos personalizados {#setting-custom-attribute-values}

{% tabs %}
{% tab Boolean %}
```csharp
bool SetCustomAttribute(STRING_KEY, BOOL_VALUE);
```
{% endtab %}
{% tab Integer %}
```csharp
bool SetCustomAttribute(STRING_KEY, INT_VALUE);
```
{% endtab %}
{% tab Double or Float %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze trata los valores FLOAT y DOUBLE exactamente igual dentro de su base de datos.
{% endtab %}
{% tab String %}
```csharp
bool SetCustomAttribute(STRING_KEY, "STRING_VALUE");
```
{% endtab %}
{% tab Long %}
```csharp
bool SetCustomAttribute(STRING_KEY, LONG_VALUE);
```
{% endtab %}
{% tab Date %}
```csharp
bool SetCustomAttribute(STRING_KEY, "DATE_VALUE");
```
>  Las fechas transmitidas a Braze deben estar en el formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601), p. ej., `2013-07-16T19:20:30+01:00` o en el formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`, p. ej., `2016-12-14T13:32:31.601-0800`
{% endtab %}
{% tab Array %}
```csharp
// Setting a custom attribute with an array value
Appboy.SharedInstance.EventLogger.SetCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Adding to a custom attribute with an array value
Appboy.SharedInstance.EventLogger.AddToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Removing a value from an array type custom attribute
Appboy.SharedInstance.EventLogger.RemoveFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```
{% endtab %}
{% endtabs %}

### Aumentar/disminuir atributos personalizados {#incrementingdecrementing-custom-attributes}

Este código es un ejemplo de un atributo personalizado que se incrementa. Puedes incrementar el valor de un atributo personalizado en cualquier valor entero positivo o negativo.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### Desactivar un atributo personalizado {#unsetting-a-custom-attribute}

Los atributos personalizados también se pueden desactivar utilizando el siguiente método:

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### Configuración de un atributo personalizado a través de la REST API {#setting-a-custom-attribute-via-the-rest-api}

También puedes utilizar nuestra REST API para establecer atributos de usuario. Consulta la documentación de [la API de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para más detalles.

### Límites del valor del atributo personalizado {#custom-attribute-value-limits}

Los valores de atributos personalizados tienen una longitud máxima de 255 caracteres; los valores más largos se truncarán.

## Gestión de los estados de suscripción a las notificaciones {#managing-notification-subscription-statuses}

Para configurar una suscripción para tus usuarios (ya sea por correo electrónico o push), puedes establecer los siguientes estados de suscripción como propiedades de `IAppboyUser`. Los estados de suscripción en Braze tienen tres estados diferentes, tanto para correo electrónico como para push:

| Estado de la suscripción | Definición |
| ------------------- | ---------- |
| `OptedIn` | Suscrito y con adhesión voluntaria explícita |
| `Subscribed` | Suscrito, pero sin adhesión voluntaria explícita |
| `UnSubscribed` | No suscrito y/o con exclusión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Managing notification subscription statuses" }

- `EmailNotificationSubscriptionType`
  - Los usuarios se configurarán en `Subscribed` automáticamente al recibir una dirección de correo electrónico válida; sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícito y configures este valor en `OptedIn` al recibir el consentimiento explícito de tu usuario.
- `PushNotificationSubscriptionType`
  - Los usuarios se establecerán en `Subscribed` automáticamente tras un registro push válido; sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícito y establezcas este valor en `OptedIn` tras recibir el consentimiento explícito de tu usuario.

>  Estos tipos se incluyen en `AppboyPlatform.PCL.Models.NotificationSubscriptionType`. Visita [Gestionar las suscripciones de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) para más detalles.
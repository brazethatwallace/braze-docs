---
nav_title: Definir atributos personalizados
article_title: Definir atributos personalizados para o Windows Universal
platform: Windows Universal
page_order: 3
description: "Este artigo de referência mostra como definir atributos personalizados na plataforma Windows Universal."
hidden: true
---

# Definir atributos personalizados {#set-custom-attributes}
{% multi_lang_include archive/windows_deprecation.md %}

A Braze fornece métodos para atribuir atributos aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com esses atributos no dashboard.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [melhores práticas]({{site.baseurl}}/developer_guide/analytics#best-practices).

Os atributos do usuário podem ser atribuídos ao `IAppboyUser` atual. Para obter uma referência ao `IAppboyUser` atual, chame `Appboy.SharedInstance.AppboyUser`

## Atribuindo atributos de usuário padrão {#assigning-default-user-attributes}

Os seguintes atributos devem ser definidos como propriedades de `IAppboyUser`:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**Exemplo de implementação**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## Atribuindo atributos personalizados ao usuário {#assigning-custom-user-attributes}

Além dos atributos de usuário padrão, a Braze também permite que você defina atributos personalizados usando vários tipos de dados diferentes. Para saber mais sobre as opções de segmentação e como cada um desses atributos afetará você, consulte nossas [Melhores práticas]({{site.baseurl}}/hidden/archive_docs/windows_universal/analytics/setting_user_ids#user-id-integration-best-practices-and-notes).

### Definindo valores de atributos personalizados {#setting-custom-attribute-values}

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
A Braze trata os valores FLOAT e DOUBLE exatamente da mesma forma em nosso banco de dados.
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
>  As datas enviadas para a Braze devem estar no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601), por exemplo `2013-07-16T19:20:30+01:00`, ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`, por exemplo `2016-12-14T13:32:31.601-0800`
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

### Incrementando/decrementando atributos personalizados {#incrementingdecrementing-custom-attributes}

Este código é um exemplo de incremento de atributo personalizado. Você pode incrementar o valor de um atributo personalizado por qualquer valor inteiro positivo ou negativo.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### Removendo um atributo personalizado {#unsetting-a-custom-attribute}

Atributos personalizados também podem ser removidos usando o seguinte método:

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### Definindo um atributo personalizado via REST API {#setting-a-custom-attribute-via-the-rest-api}

Você também pode usar nossa REST API para definir atributos de usuário. Consulte a documentação da [API de usuários]({{site.baseurl}}/api/endpoints/user_data) para mais detalhes.

### Limites de valores de atributos personalizados {#custom-attribute-value-limits}

Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.

## Gerenciando status de inscrição de notificações {#managing-notification-subscription-statuses}

Para configurar uma inscrição para seus usuários (e-mail ou push), você pode definir os seguintes status de inscrição como propriedades de `IAppboyUser`. Os status de inscrição na Braze possuem três estados diferentes tanto para e-mail quanto para push:

| Status de inscrição | Definição |
| ------------------- | ---------- |
| `OptedIn` | Inscrito e com aceitação explícita |
| `Subscribed` | Inscrito, mas sem aceitação explícita |
| `UnSubscribed` | Inscrição cancelada e/ou com recusa explícita |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gerenciando status de inscrição de notificações" }

- `EmailNotificationSubscriptionType`
  - Os usuários serão definidos como `Subscribed` automaticamente ao receber um endereço de e-mail válido. No entanto, recomendamos que você estabeleça um processo explícito de aceitação e defina esse valor como `OptedIn` após receber o consentimento explícito do seu usuário.
- `PushNotificationSubscriptionType`
  - Os usuários serão definidos como `Subscribed` automaticamente ao realizar um registro de push válido. No entanto, recomendamos que você estabeleça um processo explícito de aceitação e defina esse valor como `OptedIn` após receber o consentimento explícito do seu usuário.

>  Esses tipos pertencem a `AppboyPlatform.PCL.Models.NotificationSubscriptionType`. Acesse [Gerenciando inscrições de usuários]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) para saber mais.
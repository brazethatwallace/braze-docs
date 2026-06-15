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

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [melhores práticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

Os atributos do usuário podem ser atribuídos ao `IAppboyUser` atual. Para obter uma referência ao `IAppboyUser` atual, chame `Appboy.SharedInstance.AppboyUser`

## Atribuindo atributos de usuário padrão {#assigning-default-user-attributes}

Os seguintes atributos devem ser definidos como propriedades do `IAppboyUser`:

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

Além dos atributos de usuário padrão, a Braze também permite que você defina atributos personalizados usando vários tipos diferentes de dados. Para saber mais sobre as opções de segmentação e como cada um desses atributos afetará você, consulte nossas [melhores práticas]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes).

### Definindo valores de atributo personalizado {#setting-custom-attribute-values}

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

Este código é um exemplo de um atributo personalizado sendo incrementado. Você pode incrementar o valor de um atributo personalizado por qualquer valor inteiro positivo ou negativo.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### Removendo um atributo personalizado {#unsetting-a-custom-attribute}

Atributos personalizados também podem ser removidos usando o seguinte método:

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### Definindo um atributo personalizado via REST API {#setting-a-custom-attribute-via-the-rest-api}

Você também pode usar nossa REST API para definir atributos de usuário. Consulte a documentação da [API de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para obter detalhes.

### Limites de valor de atributo personalizado {#custom-attribute-value-limits}

Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.

## Gerenciamento do status de inscrição de notificações {#managing-notification-subscription-statuses}

Para configurar uma inscrição para seus usuários (seja e-mail ou push), você pode definir os seguintes status de inscrição como propriedades do `IAppboyUser`. Os status de inscrição na Braze têm três estados diferentes para e-mail e push:

| Status de inscrição | Definição |
| ------------------- | ---------- |
| `OptedIn` | Inscrito e com aceitação explícita |
| `Subscribed` | Inscrito, mas sem aceitação explícita |
| `UnSubscribed` | Cancelamento da inscrição e/ou recusa explícita |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Managing notification subscription statuses" }

- `EmailNotificationSubscriptionType`
  - Os usuários serão configurados para `Subscribed` automaticamente após o recebimento de um endereço de e-mail válido. No entanto, sugerimos que você estabeleça um processo de aceitação explícita e defina este valor para `OptedIn` após o recebimento do consentimento explícito do seu usuário.
- `PushNotificationSubscriptionType`
  - Os usuários serão configurados para `Subscribed` automaticamente após o registro válido de push. No entanto, sugerimos que você estabeleça um processo de aceitação explícita e defina este valor para `OptedIn` após o recebimento do consentimento explícito do seu usuário.

>  Esses tipos se enquadram em `AppboyPlatform.PCL.Models.NotificationSubscriptionType`. Para saber mais, consulte [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).
{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Atributos padrão do usuário {#default-user-attributes}

### Métodos predefinidos {#predefined-methods}

A Braze fornece métodos predefinidos para definir os seguintes atributos de usuário usando o objeto `BrazeBinding`. Para saber mais, consulte o [arquivo de declaração do Braze Unity](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs).

- Nome
- Sobrenome
- E-mail do usuário
- Gênero
- Data de nascimento
- País do usuário
- Cidade de origem do usuário
- Inscrição de e-mail do usuário
- Inscrição push do usuário
- Número de telefone do usuário

### Definindo atributos padrão {#setting-default-attributes}

Para definir um atributo padrão, chame o método relevante no objeto `BrazeBinding`.

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
BrazeBinding.SetUserEmail("email@email.com");
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

### Removendo atributos padrão {#unsetting-default-attributes}

Para remover a definição de um atributo de usuário padrão, passe `null` para o método relevante.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## Atributos personalizados do usuário {#custom-user-attributes}

Além dos atributos de usuário padrão, a Braze também permite definir atributos personalizados usando vários tipos de dados diferentes. Para saber mais sobre as opções de segmentação de cada atributo, consulte [Coleta de dados de usuários]({{site.baseurl}}/developer_guide/analytics/).

### Definindo atributos personalizados {#setting-custom-attributes}

Para definir um atributo personalizado, use o método correspondente ao tipo do atributo:

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
As datas passadas para a Braze devem estar no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (como `2013-07-16T19:20:30+01:00`) ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (como `2016-12-14T13:32:31.601-0800`).
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
{% endtabs %}

{% alert important %}
Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.
{% endalert %}

### Removendo atributos personalizados {#unsetting-custom-attributes}

Para remover a definição de um atributo personalizado, passe a chave do atributo relevante para o método `UnsetCustomUserAttribute`.

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Usando a REST API {#using-the-rest-api}

Também é possível usar nossa REST API para definir ou remover atributos de usuário. Para saber mais, consulte [Endpoints de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuração de inscrições de usuários {#setting-user-subscriptions}

Para configurar uma inscrição de e-mail ou push para seus usuários, chame uma das seguintes funções.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Ambas as funções recebem `Appboy.Models.AppboyNotificationSubscriptionType` como argumento, que possui três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `OPTED_IN` | Inscrito e com opt-in explícito |
| `SUBSCRIBED` | Inscrito, mas sem opt-in explícito |
| `UNSUBSCRIBED` | Cancelou a inscrição e/ou fez opt-out explícito |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuração de inscrições de usuários" }

{% alert note %}
O Windows não exige opt-in explícito para enviar notificações por push aos usuários. Quando um usuário é registrado para push, ele é definido como `SUBSCRIBED` em vez de `OPTED_IN` por padrão. Para saber mais, consulte nossa documentação sobre [implementação de inscrições e opt-ins explícitos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).
{% endalert %}

| Tipo de inscrição                        | Descrição |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | Os usuários serão definidos como `SUBSCRIBED` automaticamente ao receberem um endereço de e-mail válido. No entanto, recomendamos que você estabeleça um processo de opt-in explícito e defina esse valor como `OPTED_IN` após receber o consentimento explícito do usuário. Consulte nosso documento [Alterando inscrições de usuários]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) para mais detalhes. |
| `PushNotificationSubscriptionType`       | Os usuários serão definidos como `SUBSCRIBED` automaticamente mediante registro push válido. No entanto, recomendamos que você estabeleça um processo de opt-in explícito e defina esse valor como `OPTED_IN` após receber o consentimento explícito do usuário. Consulte nosso documento [Alterando inscrições de usuários]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) para mais detalhes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuração de inscrições de usuários" }

{% alert note %}
Esses tipos pertencem a `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### Configuração de inscrições de e-mail {#setting-email-subscriptions}

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Configuração de inscrições de notificação por push {#setting-push-notification-subscriptions}

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

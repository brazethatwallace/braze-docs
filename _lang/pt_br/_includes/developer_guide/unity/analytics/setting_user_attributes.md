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
- Cidade natal do usuário
- Inscrição de e-mail do usuário
- Inscrição de push do usuário
- Número de telefone do usuário

### Definindo atributos padrão {#setting-default-attributes}

Para definir um atributo padrão, chame o método relevante no objeto `BrazeBinding`.

{% tabs local %}
{% tab Nome %}
```csharp
BrazeBinding.SetUserFirstName("first name");
```
{% endtab %}
{% tab Sobrenome %}
```csharp
BrazeBinding.SetUserLastName("last name");
```
{% endtab %}
{% tab E-mail %}
```csharp
BrazeBinding.SetUserEmail("user@example.com");
```
{% endtab %}
{% tab Gênero %}
```csharp
BrazeBinding.SetUserGender(Appboy.Models.Gender);
```
{% endtab %}
{% tab Data de nascimento %}
```csharp
BrazeBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");
```
{% endtab %}
{% tab País %}
```csharp
BrazeBinding.SetUserCountry("country name");
```
{% endtab %}
{% tab Cidade natal %}
```csharp
BrazeBinding.SetUserHomeCity("city name");
```
{% endtab %}
{% tab Inscrição de e-mail %}
```csharp
BrazeBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Inscrição de push %}
```csharp
BrazeBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);
```
{% endtab %}
{% tab Número de telefone %}
```csharp
BrazeBinding.SetUserPhoneNumber("phone number");
```
{% endtab %}
{% endtabs %}

### Removendo atributos padrão {#unsetting-default-attributes}

Para remover um atributo padrão do usuário, passe `null` para o método relevante.

```csharp
BrazeBinding.SetUserFirstName(null);
```

## Atributos personalizados do usuário {#custom-user-attributes}

Além dos atributos padrão do usuário, a Braze também permite que você defina atributos personalizados usando vários tipos de dados diferentes. Para saber mais sobre as opções de segmentação de cada atributo, consulte [Coleta de dados do usuário]({{site.baseurl}}/developer_guide/analytics).

### Definindo atributos personalizados {#setting-custom-attributes}

Para definir um atributo personalizado, use o método correspondente ao tipo de atributo:

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
As datas enviadas para a Braze devem estar no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (como `2013-07-16T19:20:30+01:00`) ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (como `2016-12-14T13:32:31.601-0800`).
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

Você pode definir atributos personalizados contendo objetos aninhados (disponível no Unity SDK or kit de desenvolvimento de software 5.1.0 e posterior). Para saber mais, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).
Os exemplos a seguir mostram como definir um atributo de objeto aninhado, mesclar atualizações em um objeto existente e definir um vetor de objetos aninhados.

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>));
```

Para atualizar um objeto aninhado existente, use o parâmetro merge:

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>), merge(bool));
```

Você também pode definir um vetor de objetos aninhados:

```csharp
AppboyBinding.SetCustomUserAttribute("custom object array attribute key", list(List<Dictionary<string, object>>));
```

{% endtab %}
{% endtabs %}

{% alert important %}
Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.
{% endalert %}

### Removendo atributos personalizados {#unsetting-custom-attributes}

Para remover um atributo personalizado, passe a chave do atributo relevante para o método `UnsetCustomUserAttribute`.

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Usando a REST or transferir estado representacional API or interface de programação do aplicativo (API) {#using-the-rest-api}

Você também pode usar nossa REST or transferir estado representacional API or interface de programação do aplicativo (API) para definir ou remover atributos de usuário. Para saber mais, consulte [Endpoints de dados do usuário]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Definindo inscrições do usuário {#setting-user-subscriptions}

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
| `OPTED_IN` | Inscrito e com aceitação explícita |
| `SUBSCRIBED` | Inscrito, mas sem aceitação explícita |
| `UNSUBSCRIBED` | Cancelou a inscrição e/ou recusou explicitamente |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definindo inscrições do usuário" }

{% alert note %}
Não é necessária uma aceitação explícita no Windows para enviar notificações por push aos usuários. Quando um usuário é registrado para push, ele é definido como `SUBSCRIBED` em vez de `OPTED_IN` por padrão. Para saber mais, confira nossa documentação sobre [implementação de inscrições e aceitação explícita]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions).
{% endalert %}

| Tipo de inscrição                        | Descrição |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | Os usuários serão definidos como `SUBSCRIBED` automaticamente ao receberem um endereço de e-mail válido. No entanto, recomendamos que você estabeleça um processo de aceitação explícita e defina esse valor como `OPTED_IN` ao receber o consentimento explícito do seu usuário. Acesse nosso documento [Alterando inscrições de usuários]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions) para mais detalhes. |
| `PushNotificationSubscriptionType`       | Os usuários serão definidos como `SUBSCRIBED` automaticamente ao realizarem um registro de push válido. No entanto, recomendamos que você estabeleça um processo de aceitação explícita e defina esse valor como `OPTED_IN` ao receber o consentimento explícito do seu usuário. Acesse nosso documento [Alterando inscrições de usuários]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions) para mais detalhes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definindo inscrições do usuário" }

{% alert note %}
Esses tipos estão dentro de `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### Definindo inscrições de e-mail {#setting-email-subscriptions}

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Definindo inscrições de notificação por push {#setting-push-notification-subscriptions}

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Atributos padrão do usuário {#default-user-attributes}

### Métodos predefinidos {#predefined-methods}

A Braze fornece métodos predefinidos para definir os seguintes atributos de usuário usando o objeto `m.Braze`.

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

### Definindo atributos padrão {#setting-default-attributes}

Para definir um atributo padrão, chame o método relevante no objeto `m.Braze`.

{% tabs local %}
{% tab First name %}
```brightscript
m.Braze.setFirstName("Alex")
```
{% endtab %}
{% tab Last name %}
```brightscript
m.Braze.setLastName("Smith")
```
{% endtab %}
{% tab Email %}
```brightscript
m.Braze.setEmail("alex@example.com")
```
{% endtab %}
{% tab Gender %}
```brightscript
m.Braze.setGender("m") ' Accepts: "m", "f", "o", "n", "u", "p"
```
{% endtab %}
{% tab Birth date %}
```brightscript
m.Braze.setDateOfBirth(1990, 5, 15) ' Year, month, day
```
{% endtab %}
{% tab Country %}
```brightscript
m.Braze.setCountry("United States")
```
{% endtab %}
{% tab Language %}
```brightscript
m.Braze.setLanguage("en")
```
{% endtab %}
{% tab Home city %}
```brightscript
m.Braze.setHomeCity("New York")
```
{% endtab %}
{% tab Phone number %}
```brightscript
m.Braze.setPhoneNumber("+1234567890")
```
{% endtab %}
{% endtabs %}

## Atributos personalizados do usuário {#custom-user-attributes}

Além dos atributos de usuário padrão, a Braze também permite que você defina atributos personalizados usando vários tipos de dados diferentes.

### Definindo atributos personalizados {#settings-custom-attributes}

{% tabs %}
{% tab String %}
Para definir um atributo personalizado com um valor `string`:

```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}

{% tab Integer %}
Para definir um atributo personalizado com um valor `integer`:

```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}

{% tab Floating-points %}
A Braze trata os valores `float` e `double` exatamente da mesma forma. Para definir um atributo personalizado com qualquer um dos valores:

```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
{% endtab %}

{% tab Boolean %}
Para definir um atributo personalizado com um valor `boolean`:

```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}

{% tab Date %}
Para definir um atributo personalizado com um valor `date`:

```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}

{% tab Array %}
Para definir um atributo personalizado com um valor `array`:

```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

{% alert important %}
Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.
{% endalert %}

### Incrementando e decrementando atributos personalizados {#incrementing-and-decrementing-custom-attributes}

Este código é um exemplo de incremento de atributo personalizado. Você pode incrementar o valor de um atributo personalizado por qualquer valor inteiro positivo ou negativo.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Removendo atributos personalizados {#unsetting-custom-attributes}

Para remover um atributo personalizado, passe a chave do atributo relevante para o método `unsetCustomAttribute`.

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Usando a REST API {#using-the-rest-api}

Você também pode usar nossa REST API para definir ou remover atributos de usuário. Para saber mais, consulte [Endpoints de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configurando inscrições de e-mail {#setting-email-subscriptions}

Você pode definir os seguintes status de inscrição de e-mail para seus usuários de forma programática por meio do SDK.

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `OptedIn` | Inscrito e com opt-in explícito |
| `Subscribed` | Inscrito, mas sem opt-in explícito |
| `UnSubscribed` | Cancelou a inscrição e/ou fez opt-out explícito |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Esses tipos se enquadram em `BrazeConstants().SUBSCRIPTION_STATES`.
{% endalert %}

O método para definir o status da inscrição de e-mail é `setEmailSubscriptionState()`. Os usuários serão definidos como `Subscribed` automaticamente após o recebimento de um endereço de e-mail válido; no entanto, sugerimos que você estabeleça um processo de opt-in explícito e defina esse valor como `OptedIn` após o recebimento do consentimento explícito do usuário. Para saber mais, acesse [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

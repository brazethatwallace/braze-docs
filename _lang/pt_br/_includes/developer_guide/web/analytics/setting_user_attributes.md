{% multi_lang_include developer_guide/prerequisites/web.md %}

## Atributos padrão do usuário {#default-user-attributes}

### Métodos predefinidos {#predefined-methods}

A Braze fornece métodos predefinidos para definir os seguintes atributos de usuário na classe [`User`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html):

- Nome
- Sobrenome
- Idioma
- País
- Data de nascimento
- E-mail
- Gênero
- Cidade
- Número de telefone

### Definindo atributos padrão {#setting-default-attributes}

{% tabs %}
{% tab usando métodos %}
Para definir um atributo padrão para um usuário, chame o método `getUser()` na sua instância do Braze para obter uma referência ao usuário atual do seu app. Em seguida, você pode chamar métodos para definir um atributo de usuário.

{% subtabs local %}
{% subtab Nome %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Gênero %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Data de nascimento %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Google Tag Manager %}
Ao usar o Google Tag Manager, os atributos padrão do usuário (como o nome do usuário) devem ser registrados da mesma forma que os atributos personalizados de usuário. Certifique-se de que os valores que você está passando para atributos padrão correspondam ao formato esperado especificado na documentação da classe [`User`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Por exemplo, o atributo de gênero pode aceitar qualquer um dos seguintes valores: `"m" | "f" | "o" | "u" | "n" | "p"`. Portanto, para definir o gênero de um usuário como feminino, crie uma tag HTML personalizada com o seguinte conteúdo:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Removendo atributos padrão {#unsetting-default-attributes}

Você pode remover ou desfazer um atributo de usuário pelo código do seu app, por uma solicitação da REST API ou por uma etapa [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) do Canvas. Para atributos de array e booleanos, use `null`. Para outros tipos de dados, use uma string vazia (`""`).

Para remover um atributo padrão de usuário com o Web SDK, passe `null` para o método correspondente. Por exemplo:

{% tabs local %}
{% tab Nome %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Gênero %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Data de nascimento %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Atributos personalizados do usuário {#custom-user-attributes}

### Definindo atributos personalizados {#setting-custom-attributes}

{% tabs %}
{% tab using methods %}
Além dos métodos de atributos padrão do usuário, você também pode definir [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attribute-data-types) para seus usuários. Para especificações completas dos métodos, consulte [nosso JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
Para definir um atributo personalizado com um valor de `string`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
Para definir um atributo personalizado com um valor de `integer`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

{% endsubtab %}
{% subtab Date %}
Para definir um atributo personalizado com um valor de `date`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```

{% endsubtab %}
{% subtab Array %}

O número padrão e máximo de elementos em uma matriz é 500. Você pode atualizar o número máximo de elementos no dashboard da Braze, em **Data Settings** > **Custom Attributes**. Matrizes que excedam o número máximo de elementos serão truncadas para conter o número máximo de elementos.


Para definir um atributo personalizado com um valor de `array`:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
As datas passadas para a Braze com este método devem ser objetos JavaScript Date.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
As chaves e os valores de atributos personalizados podem ter no máximo 255 caracteres. Para saber mais sobre valores válidos de atributos personalizados, consulte a [documentação de referência](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab google tag manager %}
Atributos personalizados do usuário não estão disponíveis devido a uma limitação na linguagem de script do Google Tag Manager. Para registrar atributos personalizados, crie uma tag HTML personalizada com o seguinte conteúdo:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
O modelo GTM não oferece suporte para propriedades aninhadas em eventos ou compras. Você pode usar o HTML anterior para registrar quaisquer eventos ou compras que exijam propriedades aninhadas.
{% endalert %}
{% endtab %}
{% endtabs %}

### Removendo atributos personalizados {#unsetting-custom-attributes}

Para remover um atributo personalizado, passe `null` para o método correspondente.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Aninhando atributos personalizados {#nesting-custom-attributes}

Você também pode aninhar propriedades dentro de atributos personalizados. No exemplo a seguir, um objeto `favorite_book` com propriedades aninhadas é definido como um atributo personalizado no perfil de usuário. Para saber mais, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### Usando a REST API {#using-the-rest-api}

Você também pode usar nossa REST API para definir ou remover atributos do usuário. Para saber mais, consulte [Endpoints de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Definindo inscrições do usuário {#setting-user-subscriptions}

Para configurar uma inscrição para seus usuários (e-mail ou push), chame as funções `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`, respectivamente. Ambas as funções recebem o tipo `enum` `braze.User.NotificationSubscriptionTypes` como argumento. Esse tipo possui três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Inscrito e com aceitação explícita |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Inscrito, mas sem aceitação explícita |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Inscrição cancelada e/ou recusa explícita |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definindo inscrições do usuário" }

Quando um usuário é registrado para push, o navegador exige que ele escolha permitir ou bloquear as notificações. Se ele optar por permitir push, será definido como `OPTED_IN` por padrão.

Acesse [Gerenciando inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions) para saber mais sobre a implementação de inscrições e aceitações explícitas.

### Cancelando a inscrição de um usuário de e-mail {#unsubscribing-a-user-from-email}

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Cancelando a inscrição de um usuário de push {#unsubscribing-a-user-from-push}

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

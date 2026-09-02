{% multi_lang_include developer_guide/prerequisites/android.md %}

## Atributos padrão do usuário {#default-user-attributes}

### Métodos predefinidos {#predefined-methods}

A Braze fornece métodos predefinidos para definir os seguintes atributos de usuário na classe [`BrazeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html). Para especificações dos métodos, consulte [nosso KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/index.html).

- Nome
- Sobrenome
- País
- Idioma
- Data de nascimento
- E-mail
- Gênero
- Cidade
- Número de telefone

{% alert note %}
Todos os valores de string, como nome, sobrenome, país e cidade natal, estão limitados a 255 caracteres.
{% endalert %}

### Definindo atributos padrão {#setting-default-attributes}

Para definir um atributo padrão para um usuário, chame o método `getCurrentUser()` na sua instância do Braze para obter uma referência ao usuário atual do seu app. Em seguida, você pode chamar métodos para definir um atributo de usuário.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName("first_name");
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName("first_name")
}
```

{% endtab %}
{% endtabs %}

### Removendo atributos padrão {#unsetting-default-attributes}

Para remover um atributo de usuário, passe `null` para o método relevante.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setFirstName(null);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setFirstName(null)
}
```

{% endtab %}
{% endtabs %}

## Atributos personalizados do usuário {#custom-user-attributes}

Além dos atributos de usuário padrão, a Braze também permite que você defina atributos personalizados usando vários tipos de dados diferentes. Para saber mais sobre as opções de segmentação de cada atributo, consulte [Coleta de dados de usuários]({{site.baseurl}}/developer_guide/analytics).

### Definindo atributos personalizados {#setting-custom-attributes}

{% tabs local %}
{% tab String %}
Para definir um atributo personalizado com um valor de `string`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value");
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", "your_attribute_value")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Integers %}
Para definir um atributo personalizado com um valor de `int`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE);

    // Integer attributes may also be incremented using code like the following:
    brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE);
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_INT_VALUE)

  // Integer attributes may also be incremented using code like the following:
  brazeUser.incrementCustomUserAttribute("your_attribute_key", YOUR_INCREMENT_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}

Para definir um atributo personalizado com um valor inteiro `long`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_LONG_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Floating-points %}
Para definir um atributo personalizado com um valor de `float`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_FLOAT_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}

Para definir um atributo personalizado com um valor de `double`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DOUBLE_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Boolean %}
Para definir um atributo personalizado com um valor de `boolean`:

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_BOOLEAN_VALUE)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Date %}
{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE);
    // This method will assign the current time to a custom attribute at the time the method is called:
    brazeUser.setCustomUserAttributeToNow("your_attribute_key");
    // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
    brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setCustomUserAttribute("your_attribute_key", YOUR_DATE_VALUE)
  // This method will assign the current time to a custom attribute at the time the method is called:
  brazeUser.setCustomUserAttributeToNow("your_attribute_key")
  // This method will assign the date specified by SECONDS_FROM_EPOCH to a custom attribute:
  brazeUser.setCustomUserAttributeToSecondsFromEpoch("your_attribute_key", SECONDS_FROM_EPOCH)
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
As datas enviadas à Braze com este método devem estar no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (por exemplo, `2013-07-16T19:20:30+01:00`) ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (por exemplo, `2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}
{% tab Array %}

O número máximo de elementos em um array é 500 por padrão. Você pode atualizar o número máximo de arrays no dashboard da Braze, em **Data Settings** > **Custom Attributes**. Arrays que excedem o número máximo de elementos são truncados para conter o número máximo de elementos. Para saber mais sobre arrays de atributos personalizados e seu comportamento, consulte [Arrays]({{site.baseurl}}/developer_guide/analytics#arrays).

{% subtabs global %}
{% subtab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    // Setting a custom attribute with an array value
    brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray);
    // Adding to a custom attribute with an array value
    brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add");
    // Removing a value from an array type custom attribute
    brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove");
  }
});
```
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  // Setting a custom attribute with an array value
  brazeUser.setCustomAttributeArray("your_attribute_key", testSetArray)
  // Adding to a custom attribute with an array value
  brazeUser.addToCustomAttributeArray("your_attribute_key", "value_to_add")
  // Removing a value from an array type custom attribute
  brazeUser.removeFromCustomAttributeArray("your_attribute_key", "value_to_remove")
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Removendo atributos personalizados {#unsetting-custom-attributes}

Para remover um atributo personalizado, passe a chave do atributo relevante para o método `unsetCustomUserAttribute`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.unsetCustomUserAttribute("your_attribute_key");
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.unsetCustomUserAttribute("your_attribute_key")
}
```

{% endtab %}
{% endtabs %}

### Atributos personalizados aninhados {#nesting-custom-attributes}

Você também pode aninhar propriedades dentro de atributos personalizados. No exemplo a seguir, um objeto `favorite_book` com propriedades aninhadas é definido como um atributo personalizado no perfil de usuário. Para saber mais, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

{% tabs %}
{% tab JAVA %}
```java
JSONObject favoriteBook = new JSONObject();
try {
  favoriteBook.put("title", "The Hobbit");
  favoriteBook.put("author", "J.R.R. Tolkien");
  favoriteBook.put("publishing_date", "1937");
} catch (JSONException e) {
  e.printStackTrace();
}

braze.getCurrentUser(user -> {
  user.setCustomUserAttribute("favorite_book", favoriteBook);
  return null;
});
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
val favoriteBook = JSONObject()
  .put("title", "The Hobbit")
  .put("author", "J.R.R. Tolkien")
  .put("publishing_date", "1937")

braze.getCurrentUser { user ->
  user.setCustomUserAttribute("favorite_book", favoriteBook)
}
```
{% endtab %}
{% endtabs %}

### Usando a REST or transferir estado representacional API or interface de programação do aplicativo (API) {#using-the-rest-api}

Você também pode usar nossa REST or transferir estado representacional API or interface de programação do aplicativo (API) para definir ou remover atributos de usuário. Para saber mais, consulte [Endpoints de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).

## Definindo inscrições de usuários {#setting-user-subscriptions}

Para configurar uma inscrição para seus usuários (e-mail ou push), chame as funções `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`, respectivamente. Ambas as funções aceitam o tipo enum `NotificationSubscriptionType` como argumento. Esse tipo possui três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `OPTED_IN` | Inscrito e com aceitação explícita |
| `SUBSCRIBED` | Inscrito, mas sem aceitação explícita |
| `UNSUBSCRIBED` | Desinscrito e/ou com cancelamento de inscrição explícito |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definindo inscrições de usuários" }

{% alert important %}
O Android não exige aceitação explícita para enviar notificações por push aos usuários. Quando um usuário é registrado para push, ele é definido como `SUBSCRIBED` em vez de `OPTED_IN` por padrão. Consulte [gerenciamento de inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions) para saber mais sobre a implementação de inscrições e aceitações explícitas.
{% endalert %}

### Definindo inscrições de e-mail {#setting-email-subscriptions}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setEmailNotificationSubscriptionType(emailNotificationSubscriptionType)
}
```

{% endtab %}
{% endtabs %}

### Definindo inscrição de notificações por push {#setting-push-notification-subscription}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setPushNotificationSubscriptionType(pushNotificationSubscriptionType)
}
```

{% endtab %}
{% endtabs %}
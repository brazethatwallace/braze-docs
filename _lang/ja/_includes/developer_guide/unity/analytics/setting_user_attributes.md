{% multi_lang_include developer_guide/prerequisites/unity.md %}

## デフォルトのユーザー属性 {#default-user-attributes}

### 定義済みメソッド {#predefined-methods}

Brazeは、`BrazeBinding`オブジェクトを使用して以下のユーザー属性を設定するための定義済みメソッドを提供しています。詳細については、[Braze Unity宣言ファイル](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)を参照してください。

- 名
- 姓
- ユーザーメール
- 性別
- 生年月日
- ユーザーの国
- ユーザーの市区町村
- ユーザーのメール購読
- ユーザーのプッシュ購読
- ユーザーの電話番号

### デフォルト属性の設定 {#setting-default-attributes}

デフォルト属性を設定するには、`BrazeBinding`オブジェクトの関連メソッドを呼び出します。

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

### デフォルト属性の解除 {#unsetting-default-attributes}

デフォルトのユーザー属性を解除するには、該当するメソッドに`null`を渡します。

```csharp
BrazeBinding.SetUserFirstName(null);
```

## カスタムユーザー属性 {#custom-user-attributes}

デフォルトのユーザー属性に加え、Brazeではいくつかのデータタイプを使用してカスタム属性を定義することもできます。各属性のセグメンテーションオプションの詳細については、[ユーザーデータ収集]({{site.baseurl}}/developer_guide/analytics)を参照してください。

### カスタム属性の設定 {#setting-custom-attributes}

カスタム属性を設定するには、属性タイプに対応するメソッドを使用します。

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
Brazeに渡される日付は、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)形式（`2013-07-16T19:20:30+01:00` など）または `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式（`2016-12-14T13:32:31.601-0800` など）である必要があります。
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

{% tab ネストされたオブジェクト %}

ネストされたオブジェクトを含むカスタム属性を設定できます（Unity SDK 5.1.0以降で利用可能）。詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)を参照してください。
以下の例では、ネストされたオブジェクト属性の設定、既存のオブジェクトへの更新のマージ、およびネストされたオブジェクトの配列の設定方法を示しています。

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>));
```

既存のネストされたオブジェクトを更新するには、mergeパラメーターを使用します。

```csharp
AppboyBinding.SetCustomUserAttribute("custom object attribute key", dictionary(Dictionary<string, object>), merge(bool));
```

ネストされたオブジェクトの配列を設定することもできます。

```csharp
AppboyBinding.SetCustomUserAttribute("custom object array attribute key", list(List<Dictionary<string, object>>));
```

{% endtab %}
{% endtabs %}

{% alert important %}
カスタム属性の値は最大255文字に制限されています。それを超える値は切り捨てられます。
{% endalert %}

### カスタム属性の解除 {#unsetting-custom-attributes}

カスタム属性を解除するには、関連する属性キーを `UnsetCustomUserAttribute` メソッドに渡します。

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### REST APIの使用 {#using-the-rest-api}

REST APIを使用してユーザー属性を設定または解除することもできます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data)を参照してください。

## ユーザーの購読を設定する {#setting-user-subscriptions}

ユーザーのメールまたはプッシュの購読を設定するには、以下のいずれかの関数を呼び出します。

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

両方の関数は引数として`Appboy.Models.AppboyNotificationSubscriptionType`を取り、3つの異なるステータスがあります。

| 購読ステータス | 定義 |
| ------------------- | ---------- |
| `OPTED_IN` | 購読済みで、明示的にオプトインしている |
| `SUBSCRIBED` | 購読済みだが、明示的にはオプトインしていない |
| `UNSUBSCRIBED` | 購読解除済み、および/または明示的にオプトアウトしている |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーの購読設定" }

{% alert note %}
Windowsでは、ユーザーにプッシュ通知を送信するために明示的なオプトインは必要ありません。ユーザーがプッシュに登録されると、デフォルトでは`OPTED_IN`ではなく`SUBSCRIBED`に設定されます。詳しくは、[購読と明示的なオプトインの実装]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions)に関するドキュメントをご覧ください。
{% endalert %}

| 購読タイプ | 説明 |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType` | 有効なメールアドレスを受信すると、ユーザーは自動的に`SUBSCRIBED`に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を`OPTED_IN`に設定することをお勧めします。詳しくは、[ユーザーの購読の変更]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions)のドキュメントをご覧ください。 |
| `PushNotificationSubscriptionType` | 有効なプッシュ登録が行われると、ユーザーは自動的に`SUBSCRIBED`に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を`OPTED_IN`に設定することをお勧めします。詳しくは、[ユーザーの購読の変更]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions)のドキュメントをご覧ください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーの購読設定" }

{% alert note %}
これらのタイプは`Appboy.Models.AppboyNotificationSubscriptionType`に属します。
{% endalert %}

### メール購読の設定 {#setting-email-subscriptions}

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### プッシュ通知購読の設定 {#setting-push-notification-subscriptions}

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

{% multi_lang_include developer_guide/prerequisites/unity.md %}

## デフォルトのユーザー属性 {#default-user-attributes}

### 定義済みメソッド {#predefined-methods}

Brazeは、`BrazeBinding`オブジェクトを使用して以下のユーザー属性を設定するための定義済みメソッドを提供しています。詳しくは[Braze Unity宣言ファイル](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)を参照してください。

- 名
- 姓
- ユーザーのメールアドレス
- 性別
- 生年月日
- ユーザーの国
- ユーザーの市区町村
- ユーザーのメールサブスクリプション
- ユーザーのプッシュサブスクリプション
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

デフォルトのユーザー属性を解除するには、関連するメソッドに`null`を渡します。

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
Brazeに渡される日付は、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)形式（`2013-07-16T19:20:30+01:00`など）か、`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式（`2016-12-14T13:32:31.601-0800`など）でなければなりません。
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
カスタム属性値の最大長は255文字です。これより長い値は切り捨てられます。
{% endalert %}

### カスタム属性の解除 {#unsetting-custom-attributes}

カスタム属性を解除するには、`UnsetCustomUserAttribute`メソッドに関連する属性キーを渡します。

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### REST APIの使用 {#using-the-rest-api}

REST APIを使用して、ユーザー属性を設定または解除することもできます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data)を参照してください。

## ユーザーサブスクリプションの設定 {#setting-user-subscriptions}

ユーザーのメールまたはプッシュサブスクリプションを設定するには、以下のいずれかの関数を呼び出します。

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

どちらの関数も引数として`Appboy.Models.AppboyNotificationSubscriptionType`を取り、3つの異なるステータスがあります。

| サブスクリプションステータス | 定義 |
| ------------------- | ---------- |
| `OPTED_IN` | 購読中、かつ明示的にオプトイン済み |
| `SUBSCRIBED` | 購読中、ただし明示的にオプトインしていない |
| `UNSUBSCRIBED` | 配信停止済み、または明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーサブスクリプションの設定" }

{% alert note %}
Windowsでは、ユーザーにプッシュ通知を送る際に明示的なオプトインは必要ありません。ユーザーがプッシュ登録されると、デフォルトで`OPTED_IN`ではなく`SUBSCRIBED`に設定されます。詳細については、[サブスクリプションと明示的なオプトインの実装]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions)に関するドキュメントを参照してください。
{% endalert %}

| サブスクリプションタイプ | 説明 |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType` | 有効なメールアドレスを受信すると、ユーザーは自動的に`SUBSCRIBED`に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を受け取った時点でこの値を`OPTED_IN`に設定することをお勧めします。詳細については、[ユーザーサブスクリプションの変更]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions)のドキュメントを参照してください。 |
| `PushNotificationSubscriptionType` | 有効なプッシュ登録時に、ユーザーは自動的に`SUBSCRIBED`に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を受け取った時点でこの値を`OPTED_IN`に設定することをお勧めします。詳細については、[ユーザーサブスクリプションの変更]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions#changing-subscriptions)のドキュメントを参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーサブスクリプションの設定" }

{% alert note %}
これらのタイプは`Appboy.Models.AppboyNotificationSubscriptionType`に属します。
{% endalert %}

### メールサブスクリプションの設定 {#setting-email-subscriptions}

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### プッシュ通知サブスクリプションの設定 {#setting-push-notification-subscriptions}

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

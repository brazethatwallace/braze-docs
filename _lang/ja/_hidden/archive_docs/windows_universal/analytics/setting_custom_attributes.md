---
nav_title: カスタム属性を設定する
article_title: Windows Universalのカスタム属性を設定する
platform: Windows Universal
page_order: 3
description: "このリファレンス記事では、Windows Universalプラットフォームでカスタム属性を設定する方法について説明します。"
hidden: true
---

# カスタム属性を設定する {#set-custom-attributes}
{% multi_lang_include archive/windows_deprecation.md %}

Brazeには、ユーザーに属性を割り当てるメソッドが用意されています。ダッシュボードでこれらの属性に基づき、ユーザーをフィルターおよびセグメント化できます。

実装前に、カスタムイベント、カスタム属性、および購入イベントが提供するセグメンテーションオプションの例を[ベストプラクティス]({{site.baseurl}}/developer_guide/analytics#best-practices)で確認してください。

ユーザー属性は、現在の`IAppboyUser`に割り当てることができます。現在の`IAppboyUser`への参照を取得するには、`Appboy.SharedInstance.AppboyUser`を呼び出します。

## デフォルトユーザー属性の割り当て {#assigning-default-user-attributes}

以下の属性は、`IAppboyUser`のプロパティとして定義する必要があります。

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**実装例**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## カスタムユーザー属性の割り当て {#assigning-custom-user-attributes}

デフォルトのユーザー属性だけでなく、Brazeではさまざまなデータタイプを使用してカスタム属性を定義することもできます。セグメンテーションオプションの詳細と、これらの各属性がどのように影響するかについては、[ベストプラクティス]({{site.baseurl}}/hidden/archive_docs/windows_universal/analytics/setting_user_ids#user-id-integration-best-practices-and-notes)を参照してください。

### カスタム属性値の設定 {#setting-custom-attribute-values}

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
Brazeでは、データベース内でFLOATとDOUBLEの値をまったく同じように扱います。
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
>  Brazeに渡される日付は、[ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)形式（例：`2013-07-16T19:20:30+01:00`）、または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式（例：`2016-12-14T13:32:31.601-0800`）でなければなりません。
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

### カスタム属性の増減 {#incrementingdecrementing-custom-attributes}

このコードは、カスタム属性をインクリメントする例です。カスタム属性の値は、任意の正または負の整数値でインクリメントできます。

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### カスタム属性の設定解除 {#unsetting-a-custom-attribute}

カスタム属性は、次のメソッドを使用して設定を解除することもできます。

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### REST APIを使用したカスタム属性の設定 {#setting-a-custom-attribute-via-the-rest-api}

REST APIを使用してユーザー属性を設定することもできます。詳細については、[ユーザーAPI]({{site.baseurl}}/api/endpoints/user_data)のドキュメントを参照してください。

### カスタム属性値の制限 {#custom-attribute-value-limits}

カスタム属性値の最大長は255文字です。それより長い値は切り捨てられます。

## 通知購読ステータスの管理 {#managing-notification-subscription-statuses}

ユーザーの購読（メールまたはプッシュ）を設定するには、`IAppboyUser`のプロパティとして以下の購読ステータスを設定します。Brazeの購読ステータスには、メールとプッシュの両方に対して3つの状態があります。

| 購読ステータス | 定義 |
| ------------------- | ---------- |
| `OptedIn` | 購読中、かつ明示的にオプトイン済み |
| `Subscribed` | 購読中、ただし明示的にはオプトインしていない |
| `UnSubscribed` | 購読解除済み、および/または明示的にオプトアウト済み |
{: .reset-td-br-1 .reset-td-br-2 aria-label="通知購読ステータスの管理" }

- `EmailNotificationSubscriptionType`
  - 有効なメールアドレスを受信すると、ユーザーは自動的に`Subscribed`に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を`OptedIn`に設定することをお勧めします。
- `PushNotificationSubscriptionType`
  - 有効なプッシュ登録が行われると、ユーザーは自動的に`Subscribed`に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を`OptedIn`に設定することをお勧めします。

>  これらのタイプは`AppboyPlatform.PCL.Models.NotificationSubscriptionType`に含まれます。詳細については、[ユーザー購読の管理]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)を参照してください。
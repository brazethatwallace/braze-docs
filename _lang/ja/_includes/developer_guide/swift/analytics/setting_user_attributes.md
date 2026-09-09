{% multi_lang_include developer_guide/prerequisites/swift.md %}

## デフォルトのユーザー属性 {#default-user-attributes}

### サポートされている属性 {#supported-attributes}

以下の属性は`Braze.User`オブジェクトに設定する必要があります。

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

### デフォルト属性の設定 {#setting-default-attributes}

デフォルトのユーザー属性を設定するには、共有の`Braze.User`オブジェクトの適切なフィールドを設定します。以下は、名の属性を設定する例です。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
```

{% endtab %}
{% endtabs %}

### デフォルト属性の解除 {#unsetting-default-attributes}

デフォルトのユーザー属性を解除するには、関連するメソッドに`nil`を渡します。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: nil)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:nil];
```

{% endtab %}
{% endtabs %}

## カスタムユーザー属性 {#custom-user-attributes}

デフォルトのユーザー属性に加え、Brazeではいくつかのデータタイプを使用してカスタム属性を定義することもできます。各属性のセグメンテーションオプションの詳細については、[ユーザーデータ収集]({{site.baseurl}}/developer_guide/analytics)を参照してください。

{% alert important %}
カスタム属性の値の最大長は255文字です。これを超える値は切り捨てられます。詳細については、[`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class)を参照してください。
{% endalert %}

### カスタム属性の設定 {#setting-custom-attributes}

{% tabs local %}
{% tab string %}
`string`値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab integer %}
`integer`値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab floating-points %}
Brazeはデータベース内で`float`と`double`の値を同じように扱います。double値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab boolean %}
`boolean`値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab date %}
`date`値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab array %}
配列内の要素のデフォルトおよび最大数は500です。最大数はBrazeダッシュボードの**データ設定** > **カスタム属性**から更新できます。最大要素数を超える配列は、最大要素数に切り捨てられます。

`array`値でカスタム属性を設定するには：

{% subtabs %}
{% subtab swift %}
```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### カスタム属性のインクリメントまたはデクリメント {#incrementing-or-decrementing-custom-attributes}

このコードはカスタム属性をインクリメントする例です。カスタム属性の値は、任意の`integer`または`long`値でインクリメントできます。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### カスタム属性の解除 {#unsetting-custom-attributes}

{% tabs %}
{% tab swift %}
カスタム属性を解除するには、関連する属性キーを`unsetCustomAttribute`メソッドに渡します。

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objective-c %}
カスタム属性を解除するには、関連する属性キーを`unsetCustomAttributeWithKey`メソッドに渡します。

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### カスタム属性の階層化 {#nesting-custom-attributes}

カスタム属性内にプロパティを階層化することもできます。以下の例では、階層化されたプロパティを持つ`favorite_book`オブジェクトをユーザープロファイルのカスタム属性として設定しています。詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)を参照してください。

{% tabs %}
{% tab swift %}
```swift
let favoriteBook: [String: Any?] = [
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)
```
{% endtab %}

{% tab objective-c %}
```objc
NSDictionary *favoriteBook = @{
  @"title": @"The Hobbit",
  @"author": @"J.R.R. Tolkien",
  @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];
```
{% endtab %}
{% endtabs %}

### REST APIの使用 {#using-the-rest-api}

REST APIを使用してユーザー属性を設定または解除することもできます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data)を参照してください。

## ユーザーの購読を設定する {#setting-user-subscriptions}

ユーザーの購読（メールまたはプッシュ）を設定するには、それぞれ関数`set(emailSubscriptionState:)`または`set(pushNotificationSubscriptionState:)`を呼び出します。これらの関数はどちらも列挙型`Braze.User.SubscriptionState`を引数として受け取ります。この型には3つの異なる状態があります。

| 購読ステータス | 定義 |
| ------------------- | ---------- |
| `optedIn` | 購読済み、かつ明示的にオプトイン済み |
| `subscribed` | 購読済み、ただし明示的にオプトインしていない |
| `unsubscribed` | 購読解除済み、または明示的にオプトアウト済み |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザーの購読を設定する" }

アプリにプッシュ通知の送信を許可したユーザーは、iOSでは明示的なオプトインが必要なため、デフォルトで`optedIn`のステータスに設定されます。

ユーザーは有効なメールアドレスを受信すると自動的に`subscribed`に設定されます。ただし、明示的なオプトインプロセスを確立し、ユーザーから明示的な同意を受けた時点でこの値を`optedIn`に設定することを推奨します。詳細については、[ユーザーの購読を管理する]({{site.baseurl}}/user_guide/channels/email/subscriptions)を参照してください。

### メール購読の設定 {#setting-email-subscriptions}

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### プッシュ通知購読の設定 {#setting-push-notification-subscriptions}

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

詳細については、[ユーザーの購読を管理する]({{site.baseurl}}/user_guide/channels/email/subscriptions)を参照してください。
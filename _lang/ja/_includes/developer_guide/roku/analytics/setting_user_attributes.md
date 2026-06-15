{% multi_lang_include developer_guide/prerequisites/roku.md %}

## デフォルトのユーザー属性 {#default-user-attributes}

### 定義済みメソッド {#predefined-methods}

Brazeは、`m.Braze`オブジェクトを使用して以下のユーザー属性を設定するための定義済みメソッドを提供しています。

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

### デフォルト属性の設定 {#setting-default-attributes}

デフォルト属性を設定するには、`m.Braze`オブジェクトの関連メソッドを呼び出します。

{% tabs local %}
{% tab First name %}
```brightscript
m.Braze.setFirstName("Alex")
```
{% endtab %}
{% tab Last name %}
`````````brightscript
m.Braze.setLastName("Smith")
```
{% endtab %}
{% tab Email %}
`````````brightscript
m.Braze.setEmail("alex@example.com")
```
{% endtab %}
{% tab Gender %}
`````````brightscript
m.Braze.setGender("m") ' Accepts: "m", "f", "o", "n", "u", "p"
```
{% endtab %}
{% tab Birth date %}
`````````brightscript
m.Braze.setDateOfBirth(1990, 5, 15) ' Year, month, day
```
{% endtab %}
{% tab Country %}
`````````brightscript
m.Braze.setCountry("United States")
```
{% endtab %}
{% tab Language %}
`````````brightscript
m.Braze.setLanguage("en")
```
{% endtab %}
{% tab Home city %}
`````````brightscript
m.Braze.setHomeCity("New York")
```
{% endtab %}
{% tab Phone number %}
`````````brightscript
m.Braze.setPhoneNumber("+1234567890")
```
{% endtab %}
{% endtabs %}

## カスタムユーザー属性 {#custom-user-attributes}

デフォルトのユーザー属性に加え、Brazeではいくつかのデータタイプを使用してカスタム属性を定義することもできます。

### カスタム属性の設定 {#settings-custom-attributes}

{% tabs %}
{% tab String %}
`string`値でカスタム属性を設定するには：

`````````brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}

{% tab Integer %}
`integer`値でカスタム属性を設定するには：

`````````brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}

{% tab Floating-points %}
Brazeは、`float`と`double`の値をまったく同じように扱います。いずれかの値でカスタム属性を設定するには：

`````````brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
{% endtab %}

{% tab Boolean %}
`boolean`値でカスタム属性を設定するには：

`````````brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}

{% tab Date %}
`date`値でカスタム属性を設定するには：

`````````brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}

{% tab Array %}
`array`値でカスタム属性を設定するには：

`````````brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

{% alert important %}
カスタム属性値の最大長は255文字です。これより長い値は切り捨てられます。
{% endalert %}

### カスタム属性のインクリメントとデクリメント {#incrementing-and-decrementing-custom-attributes}

このコードは、カスタム属性のインクリメントの例です。カスタム属性の値は、正または負の整数値でインクリメントできます。

`````````brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### カスタム属性の設定解除 {#unsetting-custom-attributes}

カスタム属性を解除するには、`unsetCustomAttribute`メソッドに関連する属性キーを渡します。

`````````brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### REST APIの使用 {#using-the-rest-api}

REST APIを使用して、ユーザー属性を設定または解除することもできます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を参照してください。

## メールサブスクリプションの設定 {#setting-email-subscriptions}

SDKから、ユーザーに対して以下のメールのサブスクリプションステータスをプログラムで設定できます。

| サブスクリプションのステータス | 定義 |
| ------------------- | ---------- |
| `OptedIn` | 購読中、かつ明示的にオプトイン済み |
| `Subscribed` | 購読中、ただし明示的にオプトインしていない |
| `UnSubscribed` | 配信停止済みまたは明示的にオプトアウト済み、あるいはその両方 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="メールサブスクリプションの設定" }

{% alert note %}
これらのタイプは`BrazeConstants().SUBSCRIPTION_STATES`に属します。
{% endalert %}

メールのサブスクリプションステータスを設定するメソッドは`setEmailSubscriptionState()`です。ユーザーは、有効なメールアドレスを受信すると自動的に`Subscribed`に設定されます。ただし、明示的なオプトインのプロセスを確立し、ユーザーから明示的な同意を得た時点でこの値を`OptedIn`に設定することをお勧めします。詳細については、[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions)を参照してください。

`````````brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

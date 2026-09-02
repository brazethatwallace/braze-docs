{% multi_lang_include developer_guide/prerequisites/web.md %}

## デフォルトのユーザー属性 {#default-user-attributes}

### 定義済みメソッド {#predefined-methods}

Brazeは、[`User`クラス](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)内で以下のユーザー属性を設定するための定義済みメソッドを提供しています。

- 名
- 姓
- 言語
- 国
- 生年月日
- メール
- 性別
- 市区町村
- 電話番号

### デフォルト属性の設定 {#setting-default-attributes}

{% tabs %}
{% tab メソッドを使用 %}
ユーザーのデフォルト属性を設定するには、Brazeインスタンスで`getUser()`メソッドを呼び出し、アプリの現在のユーザーへの参照を取得します。その後、ユーザー属性を設定するメソッドを呼び出すことができます。

{% subtabs local %}
{% subtab 名 %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab 性別 %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab 生年月日 %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Google Tag Manager %}
Google Tag Managerを使用する場合、標準ユーザー属性（ユーザーの名など）はカスタムユーザー属性と同じ方法で記録する必要があります。標準属性に渡す値が、[Userクラス](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)のドキュメントで指定されている期待されるフォーマットと一致していることを確認してください。

たとえば、性別属性は値として`"m" | "f" | "o" | "u" | "n" | "p"`のいずれかを受け付けます。そのため、ユーザーの性別を女性に設定するには、以下の内容でカスタムHTMLタグを作成します。

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### デフォルト属性の解除 {#unsetting-default-attributes}

ユーザー属性は、アプリコード、REST APIリクエスト、または[ユーザー更新]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)キャンバスステップを通じて削除または解除できます。配列およびブール属性には`null`を使用します。その他のデータタイプには空文字列（`""`）を使用します。

Web SDKでデフォルトのユーザー属性を解除するには、関連するメソッドに`null`を渡します。例：

{% tabs local %}
{% tab 名 %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab 性別 %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab 生年月日 %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## カスタムユーザー属性 {#custom-user-attributes}

### カスタム属性の設定 {#setting-custom-attributes}

{% tabs %}
{% tab メソッドを使用する %}
デフォルトのユーザー属性メソッドに加えて、ユーザーに[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attribute-data-types)を設定することもできます。メソッドの完全な仕様については、[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)を参照してください。

{% subtabs local %}
{% subtab String %}
`string` 値でカスタム属性を設定するには:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
`integer` 値でカスタム属性を設定するには:

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
`date` 値でカスタム属性を設定するには:

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

配列内の要素のデフォルトおよび最大数は500です。最大数はBrazeダッシュボードの**データ設定** > **カスタム属性**で更新できます。最大要素数を超える配列は、最大要素数に切り詰められます。


`array` 値でカスタム属性を設定するには:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
Brazeに渡される日付は、JavaScriptのDateオブジェクトでなければなりません。
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
カスタム属性のキーと値は最大255文字です。有効なカスタム属性値の詳細については、[リファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)を参照してください。
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
Google Tag Managerのスクリプト言語の制限により、カスタムユーザー属性は利用できません。カスタム属性を記録するには、以下の内容でカスタムHTMLタグを作成してください:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
GTMテンプレートは、イベントや購入のネストされたプロパティをサポートしていません。ネストされたプロパティが必要なイベントや購入を記録するには、上記のHTMLを使用してください。
{% endalert %}
{% endtab %}
{% endtabs %}

### カスタム属性の解除 {#unsetting-custom-attributes}

カスタム属性を解除するには、関連するメソッドに`null`を渡します。

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### カスタム属性のネスト {#nesting-custom-attributes}

カスタム属性内にプロパティをネストすることもできます。以下の例では、ネストされたプロパティを持つ`favorite_book`オブジェクトがユーザープロファイルのカスタム属性として設定されています。詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)を参照してください。

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### REST APIの使用 {#using-the-rest-api}

REST APIを使用してユーザー属性を設定または解除することもできます。詳細については、[ユーザーデータエンドポイント]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data)を参照してください。

## ユーザー購読の設定 {#setting-user-subscriptions}

ユーザーの購読（メールまたはプッシュ）を設定するには、それぞれ`setEmailNotificationSubscriptionType()`または`setPushNotificationSubscriptionType()`関数を呼び出します。両方の関数は、引数として`enum`型の`braze.User.NotificationSubscriptionTypes`を受け取ります。この型には3つの異なるステータスがあります。

| 購読ステータス | 定義 |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | 購読済みで、明示的にオプトイン済み |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | 購読済みだが、明示的にはオプトインしていない |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | 購読解除済み、かつ/または明示的にオプトアウト済み |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー購読の設定" }

ユーザーがプッシュに登録されると、ブラウザは通知を許可するかブロックするかの選択を求めます。ユーザーがプッシュを許可した場合、デフォルトで`OPTED_IN`に設定されます。

購読や明示的なオプトインの実装について詳しくは、[ユーザー購読の管理]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#managing-user-subscriptions)を参照してください。

### ユーザーのメール購読を解除する {#unsubscribing-a-user-from-email}

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### ユーザーのプッシュ購読を解除する {#unsubscribing-a-user-from-push}

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

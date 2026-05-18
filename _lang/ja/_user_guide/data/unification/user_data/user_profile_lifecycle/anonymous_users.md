---
nav_title: 匿名ユーザー
article_title: 匿名ユーザー
page_order: 0
page_type: reference
description: "この記事では、匿名ユーザーとユーザーエイリアスの概要を示し、その重要性と、メッセージで活用できる方法について説明します。"

---

# 匿名ユーザー {#anonymous-users}

> ゲスト訪問者のように、ログインせずにWebサイトやアプリケーションにアクセスするユーザーは、匿名ユーザーとして認識されます。これらのユーザーには`external_ids`はありません。`external_ids`はBraze APIを使用してユーザープロファイルを更新するために使用されますが、匿名ユーザーにも[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points/)が割り当てられており、セグメントでターゲットにすることができます。

匿名ユーザーがWebサイトまたはアプリケーションにアクセスすると、Braze SDKはそれらを作成し、「匿名」ユーザープロファイルに割り当てます。ユーザーがブラウズする間、SDKは使用状況情報やデバイス情報など、匿名ユーザープロファイルのデータを自動的にキャプチャします（カスタム属性やカスタムイベントを設定している場合はそれらも含みます）。

キャプチャされた匿名ユーザーに対して、以下のことが可能です。

- ユーザーがログインする前にメッセージを送信する
- ログイン前にユーザーのプロファイルを収集し、関連データを見逃さないようにする
- ユーザーがプロファイルの一部しか完成していない場合に、メッセージでプロファイルの完成を促す
- ユーザーがログインした際にプロファイルを完成させ、他のプラットフォームでのメッセージングをキャンセルできるようにする（例えば、ユーザーがすでにアプリで注文済みの場合に「初回アプリ注文で送料無料」メッセージを送信しないなど）
- 離脱の意思を示しているユーザーに対して、プロファイルの作成やカートの精算、その他のアクションを促してエンゲージメントを図る

## 仕組み {#how-it-works}

{% multi_lang_include anonymous_users/about_anonymous_users.md section='user_guide' %}

## ユーザーエイリアスの割り当て {#assigning-user-aliases}

{% multi_lang_include anonymous_users/about_user_aliases.md section='user_guide' %}

## 匿名ユーザーのマージ {#merging-anonymous-users}

匿名ユーザープロファイルは、他のユーザープロファイルと同じ電話番号またはメールアドレスを持つ重複である場合があります。重複の1つが識別済みのユーザープロファイルである可能性もあります。これらの重複は、[POST: Merge Usersエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)を使用するか、Brazeプラットフォームのマージツール（[ルールベースのマージ]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#rules-based-merging)など）を使用して、1つのユーザープロファイルに統合できます。

## 匿名ユーザーの検索 {#looking-up-an-anonymous-user}

匿名ユーザーには`external_id`がないため、デバイスIDを使用して特定のプロファイルを検索できます。以下の手順では、Web SDK統合で現在のユーザーのデバイスIDを取得する方法を示します。

1. ブラウザの開発者ツールを開きます（例えば、Chromeの場合、Macでは**Command + Option + J**、Windowsでは**Ctrl + Shift + I**を押します）。
2. **Console**タブで、以下を実行します。

```javascript
console.log(braze.getDeviceId());
```

{:start="3"}
3. Brazeダッシュボードで、[ユーザー検索]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/)を使用して、返されたデバイスIDを検索します。

## ユースケース {#use-cases}

### セグメントで匿名ユーザーをターゲットにする {#target-anonymous-users-in-your-segment}

匿名ユーザーには`external_id`がないため、セグメンテーションフィルター**外部ユーザーIDが空白**を使用して一括でターゲットにできます。さらに精度を高めるために、ターゲットにしたい匿名ユーザーにカスタム属性を追加し、それでフィルタリングすることもできます。

例えば、各匿名ユーザープロファイルにカスタム属性「is_lead_profile」を割り当てるとします。次のフィルターの一方または両方を使用して、これらのプロファイルをターゲットにできます。

- **外部ユーザーIDが空白である**
- 「is_lead_profile」が**真である**

![外部ユーザーIDが空白で、「is_lead_profile」カスタム属性が真のセグメントフィルター。]({% image_buster /assets/img/getting_started/anonymous_users.png %})

### 匿名ユーザーからのチェックアウトデータのキャプチャ {#capture-checkout-data-from-an-anonymous-user}

匿名ユーザー（またはゲスト訪問者）のチェックアウトデータをキャプチャするには、チェックアウトプロセス中にユーザーエイリアスプロファイルを作成します。匿名ユーザーがWebキャプチャフォームを使用してチェックアウトする際に、API呼び出しをトリガーしてユーザーエイリアスプロファイルを作成し、購入イベントをログに記録します。作成したユーザープロファイルは、Braze APIを使用して更新できます。

Webキャプチャフォームが送信されたときに生成されるペイロードの例を以下に示します。

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}
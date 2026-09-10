---
nav_title: コンテンツカード
article_title: コンテンツカード
page_order: 2
page_type: landing
description: "コンテンツカードを使用して、アプリやWebサイトに直接埋め込まれたダイナミックなリッチコンテンツのストリームをユーザーに送信できます。"
channel:
  - content cards
search_rank: 5
---

# コンテンツカード {#content-cards}

> コンテンツカードを使用すると、ユーザーが愛用するアプリ内で、エクスペリエンスを中断することなく、高度にターゲティングされたダイナミックなリッチコンテンツのストリームを顧客に送信できます。コンテンツカードはアプリやWebサイトに直接埋め込まれるため、メッセージ受信トレイやカスタムインターフェイスを作成して、メールやプッシュ通知などの他のチャネルのリーチを拡大できます。

## 前提条件 {#prerequisites}

Content Cardsの利用可能性は、お使いのBrazeパッケージによって異なります。開始するには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。

Content Cardsを使用する前に、アプリまたはWebサイトに[Braze SDK]({{site.baseurl}}/developer_guide/content_cards)を統合する必要があります。追加の設定は不要です。独自のUIを構築する場合は、[Content Cardsカスタマイズガイド]({{site.baseurl}}/developer_guide/content_cards/customizing_cards)を参照してください。

## Content Cardsを使用するメリット {#benefits-of-using-content-cards}

Content Cardsを使用することと、開発者にアプリ内にコンテンツを直接組み込んでもらうことを比較した場合のメリットをご紹介します。

- **セグメンテーションとパーソナライゼーションが容易:** ユーザーデータはBrazeに保存されるため、オーディエンスの定義やContent Cardsを使用したメッセージのパーソナライズが簡単に行えます。
- **一元化されたレポート:** Content Cardsの分析はBrazeで追跡されるため、すべてのキャンペーンのインサイトを1か所で確認できます。
- **一貫したカスタマージャーニー:** Content CardsをBrazeの他のチャネルと組み合わせて、一貫した顧客体験を実現できます。よくあるユースケースとして、プッシュ通知を送信した後、プッシュに反応しなかったユーザーのためにその通知をアプリ内のContent Cardsとして保存する方法があります。コンテンツが開発者によってアプリに直接組み込まれている場合、そのコンテンツは残りのメッセージングから切り離されてしまいます。
- **オプトインが不要:** アプリ内メッセージと同様に、Content Cardsはユーザーからのオプトインや許可を必要としません。ただし、アプリ内メッセージは許可不要で一時的なものですが、Content Cardsは許可不要で永続的です。つまり、アプリ内メッセージとContent Cardsを組み合わせたメッセージング戦略は、優れたバランスを実現します。
- **メッセージング体験をより細かくコントロール:** Content Cardsの初期設定には開発者の協力が必要ですが、その後はメッセージ、受信者、タイミングなどをBrazeダッシュボードから直接コントロールできます。

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Content Cardsの数字で見る効果 {#content-cards-by-the-numbers}

BrazeでContent Cardsを構築すると、アプリやWebサイトを大幅に改修することなく、メッセージングの更新や効果の測定が可能です。Brazeの調査によるハイライトは以下のとおりです。

- Content Cardsは、72時間以内の売上向上においてメールより**38倍**効果的です。[^1]
- ロイヤルティ登録キャンペーンでContent Cardsを使用すると、コンバージョンが**5倍**向上します。[^1]
- プッシュ通知、In-App Messages、Content Cardsを組み合わせたアウトリーチは、プッシュ通知のみの場合と比較して**6.9倍**多くのセッションを促進します。[^2]
- メール、In-App Messages、Content Cardsを組み合わせたアウトリーチは、メールのみの場合と比較して平均ユーザーライフタイムが**3.6倍**長くなります。[^2]

## ユースケース {#use-cases}

Content Cardsの一般的なユースケースについては、このセクションを参照してください。

{% alert tip %}
さらにインスピレーションを得るには、紹介プログラム、新製品の発売、サブスクリプションの更新など、20以上のカスタマイズ可能なキャンペーンを含む[Content Cardsインスピレーションガイド](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide)を参照してください。
{% endalert %}

{% tabs %}
{% tab オンボーディングと次のステップ %}

新しいユーザーがアプリやWebサイトを探索する際に、戦略的に配置されたContent Cardsを使用して、提供するサービスの価値やメリットを紹介しましょう。ホームページのContent Cardsで他のコミュニケーションチャネルへのオプトインを促し、Content Cardsを活用した専用のオンボーディングタブに未完了のオンボーディングタスクを保存しましょう。ユーザーが目的のタスクを完了したら、カードを削除することも忘れないでください。

![Content Cardsのオンボーディングユースケースの例]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab イベント参加 %}

ユーザーのホームページの上部にContent Cardsを表示し、位置情報ターゲティングを使用して潜在的なユーザーにリーチすることで、イベントへの参加を促しましょう。ブランドとの過去のアクティビティを活用したパーソナライズされたメッセージングで、関連する実際のイベントにユーザーを招待すると、ユーザーに特別感を与えることができます。

![Content Cardsのイベント参加ユースケースの例]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab レコメンデーション %}

ユーザーの行動や好みに関するデータを活用して、ホームページや受信トレイのContent Cardsから関連コンテンツをリアルタイムで表示し、ユーザーを製品提案に引き戻しましょう。

![Content Cardsのレコメンデーションユースケースの例]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab セールとプロモーション %}

Content Cardsを活用して、プロモーションメッセージや未受領のオファーをホームページや専用のプロモーション受信トレイに直接表示しましょう。各顧客の過去の購入履歴に基づいた関連コンテンツを取り込み、注目を集めるパーソナライズされたプロモーションを提供しましょう。

![Content Cardsのセールとプロモーションユースケースの例]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### その他のユースケース {#other-use-cases}

これらの主要なユースケース以外にも、顧客はContent Cardsをさまざまな方法で活用しています。Content Cardsの強みはその柔軟性にあります。ここに表示されていないユースケースが必要な場合は、[キーと値のペア]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)を設定して、アプリやWebサイトにペイロードを送信できます。

アプリやWebサイトでContent Cardsの配置を実装する方法の概要については、[カスタムContent Cardsの作成]({{site.baseurl}}/developer_guide/content_cards/creating_cards)を参照してください。

## 次のステップ {#next-steps}

{% article_tiles %}
- name: Content Cardsの作成
  link: /docs/user_guide/channels/content_cards/create_a_content_card
- name: クリエイティブの詳細
  link: /docs/user_guide/channels/content_cards/creative_details
{% endarticle_tiles %}

[^1]: [カスタマーリテンションキャンペーンを最大限に活用するための8つのヒント](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [レポート：クロスチャネルマーケティングの違い](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)
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

コンテンツカードの利用可否は、ご利用のBrazeパッケージによって異なります。開始するには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。

コンテンツカードを使用するには、[Braze SDK]({{site.baseurl}}/developer_guide/content_cards)をアプリまたはWebサイトに統合する必要があります。追加のセットアップは不要です。独自のUIを構築する場合は、[コンテンツカードカスタマイズガイド]({{site.baseurl}}/developer_guide/content_cards/customizing_cards)を参照してください。

## コンテンツカードを使用するメリット {#benefits-of-using-content-cards}

開発者にアプリ内にコンテンツを直接構築してもらう場合と比較した、コンテンツカードを使用するメリットをいくつかご紹介します。

- **セグメンテーションとパーソナライゼーションが容易:** ユーザーデータはBrazeに保存されるため、オーディエンスの定義やContent Cardsによるメッセージのパーソナライズが簡単に行えます。
- **一元化されたレポート:** コンテンツカードの分析はBrazeで追跡されるため、すべてのキャンペーンのインサイトを一箇所で確認できます。
- **一貫性のあるカスタマージャーニー:** Content CardsをBrazeの他のチャネルと組み合わせて、一貫したカスタマーエクスペリエンスを作成できます。よくあるユースケースとして、プッシュ通知を送信した後、プッシュに反応しなかったユーザー向けにその通知をアプリ内のContent Cardとして保存する方法があります。コンテンツが開発者によってアプリ内に直接構築されている場合、そのコンテンツは他のメッセージングから分離されてしまいます。
- **オプトインが不要:** In-App Messagesと同様に、Content Cardsはユーザーからのオプトインや権限を必要としません。ただし、In-App Messagesは権限不要で一時的であるのに対し、Content Cardsは権限不要で永続的です。つまり、In-App MessagesとContent Cardsを組み合わせたメッセージング戦略は、優れたバランスを実現します。
- **メッセージングエクスペリエンスをより細かくコントロール:** Content Cardsの初期セットアップには開発者の協力が必要ですが、その後はメッセージ、受信者、タイミングなどをBrazeダッシュボードから直接コントロールできます。

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## コンテンツカードの数値実績 {#content-cards-by-the-numbers}

BrazeでContent Cardsを構築すると、アプリやWebサイトを大幅に改修することなく、メッセージングの更新と効果測定が可能です。Brazeの調査によるハイライトは以下のとおりです。

- Content Cardsは、72時間の時間枠で売上を向上させる効果がメールの**38倍**です。[^1]
- ロイヤルティ登録キャンペーンでContent Cardsを使用すると、コンバージョンが**5倍**向上します。[^1]
- プッシュ通知、In-App Messages、Content Cardsを通じたアウトリーチは、プッシュ単独と比較してセッション数が**6.9倍**増加します。[^2]
- メール、In-App Messages、Content Cardsを通じたアウトリーチは、メール単独と比較して平均ユーザーライフタイムが**3.6倍**長くなります。[^2]

[^1]: [顧客維持キャンペーンを最大限に活用するための8つのヒント](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [レポート：クロスチャネルマーケティングの違い](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)

## ユースケース {#use-cases}

コンテンツカードの一般的なユースケースについては、このセクションを参照してください。

{% alert tip %}
さらにインスピレーションを得るには、[コンテンツカードインスピレーションガイド](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide)を参照してください。紹介プログラム、新製品の発売、サブスクリプションの更新など、20以上のカスタマイズ可能なキャンペーンが含まれています。
{% endalert %}

{% tabs %}
{% tab オンボーディングと次のステップ %}

新規ユーザーがアプリやWebサイトを探索する際に、戦略的に配置されたコンテンツカードで提供する価値やメリットを案内しましょう。ホームページのコンテンツカードで他のコミュニケーションチャネルへのオプトインを促し、コンテンツカードを活用した専用のオンボーディングタブに未完了のオンボーディングタスクを保存しましょう。ユーザーが目的のタスクを完了したら、カードを削除することを忘れないでください！

![コンテンツカードのオンボーディングユースケースの例。]({% image_buster /assets/img_archive/cc_usecase_onboarding.png %})

{% endtab %}
{% tab イベント参加 %}

ユーザーのホームページの上部にコンテンツカードを表示して、イベント参加を促しましょう。ロケーションターゲティングを使用して、潜在的なユーザーがいる場所にリーチします。関連する実際のイベントにユーザーを招待することで、特にブランドとの過去のアクティビティを活用したパーソナライズされたメッセージングにより、ユーザーに特別感を与えることができます。

![コンテンツカードのイベント参加ユースケースの例。]({% image_buster /assets/img_archive/cc_usecase_event.png %})

{% endtab %}
{% tab おすすめ %}

ユーザーの動作や好みに関するデータを活用して、ホームページや受信トレイのコンテンツカードから関連コンテンツをリアルタイムで表示し、ユーザーを製品に引き戻しましょう。

![コンテンツカードのおすすめユースケースの例。]({% image_buster /assets/img_archive/cc_usecase_recommendation.png %})

{% endtab %}
{% tab セールとプロモーション %}

コンテンツカードを活用して、プロモーションメッセージや未使用のオファーをホームページや専用のプロモーション受信トレイに直接表示しましょう。各顧客の過去の購入履歴に基づいて関連コンテンツを取り込み、注目を集めるパーソナライズされたプロモーションを配信します。

![コンテンツカードのセールとプロモーションユースケースの例。]({% image_buster /assets/img_archive/cc_usecase_promo.png %})

{% endtab %}
{% endtabs %}

### その他のユースケース {#other-use-cases}

これらの主要なユースケース以外にも、顧客はコンテンツカードをさまざまな方法で活用しています。コンテンツカードの強みはその柔軟性にあります。ここに表示されていないユースケースがある場合は、[キーと値のペア]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)を設定して、ペイロードをアプリやWebサイトに送信できます。

アプリやWebサイトにコンテンツカードの配置を実装する方法の概要については、[カスタムコンテンツカードの作成]({{site.baseurl}}/developer_guide/content_cards/creating_cards)を参照してください。

## 次のステップ {#next-steps}

- [コンテンツカードの作成]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card)
- [クリエイティブの詳細]({{site.baseurl}}/user_guide/channels/content_cards/creative_details)
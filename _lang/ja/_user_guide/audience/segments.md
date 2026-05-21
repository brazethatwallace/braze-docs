---
nav_title: セグメント
article_title: セグメント
page_order: 3
layout: dev_guide
guide_top_header: "セグメント"
guide_top_text: "オーディエンスのセグメンテーションは戦略的マーケティングの鍵です。過剰なターゲティング、ユーザーへの不要な干渉、顧客との潜在的なつながりの見逃しを防ぐことができます。以下の記事を参照して、オーディエンスをセグメント化およびフィルタリングし、あなた（そしてユーザー）にとって最大の効果を得る方法を学びましょう。"
descriptions: "オーディエンスのセグメンテーションは戦略的マーケティングの鍵です。過剰なターゲティング、ユーザーへの不要な干渉、顧客との潜在的なつながりの見逃しを防ぐことができます。このランディングページで、オーディエンスをセグメント化およびフィルタリングし、あなた（そしてユーザー）にとって最大の効果を得る方法を学びましょう。"
search_rank: 4
tool: Segments
page_type: landing
description: "このランディングページでは、ダッシュボードのキャンペーンにおけるセグメンテーションに関する記事を掲載しています。セグメントの設定方法、フィルター、ファネル、インサイト、エクステンションなどの情報をご覧いただけます。"

guide_featured_title: "セクション記事"
guide_featured_list:
  - name: セグメントを作成する
    link: /docs/user_guide/audience/segments/creating_a_segment
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: セグメントを管理する
    link: /docs/user_guide/audience/segments/managing_segments
    image: /assets/img/braze_icons/edit-05.svg
  - name: セグメンテーションフィルター
    link: /docs/user_guide/audience/segments/segmentation_filters
    image: /assets/img/braze_icons/flag-02.svg
  - name: セグメントデータ
    link: /docs/user_guide/audience/segments/segment_data
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: セグメントエクステンション
    link: /docs/user_guide/audience/segments/segment_extension
    image: /assets/img/braze_icons/users-01.svg
  - name: セグメントインサイト
    link: /docs/user_guide/audience/segments/segment_insights
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "その他の記事"
guide_menu_list:
  - name: ロケーションターゲティング
    link: /docs/user_guide/audience/segments/location_targeting
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: 正規表現
    link: /docs/user_guide/audience/segments/regex
    image: /assets/img/braze_icons/search-sm.svg
  - name: セグメントサイズを測定する
    link: /docs/user_guide/audience/segments/measuring_segment_size
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: "ユースケース：階層化カスタム属性でセグメント化する"
    link: /docs/user_guide/audience/segments/segment_with_nested_custom_attributes
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: トラブルシューティング
    link: /docs/user_guide/audience/segments/troubleshooting
    image: /assets/img/braze_icons/annotation-question.svg

---

## Braze セグメントについて {#about-braze-segments}

Brazeでは、セグメントはユーザー属性、ユーザーの動作、カスタムイベントなど、定義した特定の条件に一致するユーザーのダイナミックなグループです。セグメントを他のセグメント内にネストし、追加機能を適用することで条件を細かく設定でき、オーディエンスの範囲を絞り込んで、適切なユーザーに高度にパーソナライズされた魅力的なコンテンツを送信できます。

ユーザーをターゲットにするためのセグメントはいくつでも作成できます。セグメント機能とセグメンテーションフィルターのさまざまな組み合わせを試して、ユーザーデータを活用するクリエイティブな方法を発見し、ユーザーに関連性の高いメッセージを送信してエンゲージメントを向上させる新しい方法を見つけましょう。

以下のユースケースで、Braze セグメントがユーザーのターゲティングにどのように役立つかの一部をご覧ください。

### ユースケース {#use-cases}

- **ウェルカムメッセージ:** 新規ユーザーをセグメント化して、アプリを紹介するオンボーディングメールやアプリ内メッセージを送信できます。
- **ロイヤルティ報酬:** 購入頻度、メンバーシップ記念日、その他のマイルストーンに基づいてユーザーをセグメント化し、最もロイヤルティの高いユーザーに限定オファーや報酬を送信できます。
- **行動トリガー:** カートの放棄などのユーザーアクションに基づいてユーザーをセグメント化し、アプリ内メッセージやプッシュ通知をトリガーできます。
- **商品のおすすめ:** 特定の商品を購入したユーザーをセグメント化し、補完的な商品やより上位の商品のおすすめを送信できます。
- **ABテスト:** 異なるメッセージ、件名、コンテンツのABテスト用にユーザーをセグメント化し、特定の年齢、性別、その他の属性を持つユーザーに最も響くものを判断できます。

#### セグメントエクステンションのユースケース {#segment-extension-use-cases}

[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)を使用して、ユーザープロファイルの全期間にわたって保存されたカスタムイベントや購入行動に基づいてユーザーをターゲットにすることで、セグメントをさらに絞り込むことができます。

- **過去の購入:** 過去2年間に特定の商品の特定の色を少なくとも2回購入したかどうかでユーザーをセグメント化できます。
- **イベントとメッセージのインタラクション:** 過去30日間に購入を行い、かつ特定のアプリ内メッセージとインタラクションしたかどうかでユーザーをセグメント化できます。
- **データのクエリ:**
  - **Snowflakeへのクエリ:** [SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/)を使用してSnowflakeにクエリを実行し、Brazeと外部ソース（CRMやデータウェアハウスなど）のデータを組み合わせてユーザーをセグメント化できます。
  - **データウェアハウスからの同期:** [CDIセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/)を使用して、データウェアハウスやファイルストレージシステムからBrazeに直接同期されたデータでユーザーをセグメント化できます。
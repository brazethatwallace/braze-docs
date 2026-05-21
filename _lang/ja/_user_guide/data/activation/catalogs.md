---
nav_title: カタログ
article_title: カタログ
page_order: 3
layout: dev_guide

guide_top_header: "カタログ"
guide_top_text: "カタログは、Liquidを通してカスタム属性やカスタムイベントプロパティにアクセスするのと同様に、インポートしたCSVファイルやAPIエンドポイントからデータにアクセスしてメッセージを充実させます。"

description: "このランディングページはカタログのホームです。カタログとフィルターセットを使用して、Braze キャンペーンで非ユーザーデータを活用し、パーソナライズ済みメッセージを送信できます。"

guide_featured_title: "セクション記事"
guide_featured_list:
- name: カタログを作成する
  link: /docs/user_guide/data/activation/catalogs/create
  image: /assets/img/braze_icons/users-01.svg
- name: カタログの使用
  link: /docs/user_guide/data/activation/catalogs/use
  image: /assets/img/braze_icons/users-01.svg
- name: 再入荷通知
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: 価格低下通知
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: セレクション
  link: /docs/user_guide/data/activation/catalogs/selections
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "その他の記事"
guide_menu_list:
- name: カタログAPIエンドポイント
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg
- name: ドラッグ＆ドロップ製品ブロック
  link: /docs/dnd_product_blocks/
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## カタログのユースケース {#catalog-use-cases}

カタログには、あらゆるタイプのデータを取り込むことができます。通常、データは製品、割引、プロモーション、イベントなど、提供するアイテムに関するメタデータです。このデータを使用して関連性の高いメッセージングでユーザーをターゲットにする方法について、以下のユースケースをご覧ください。

### 小売業とeコマース {#retail-and-ecommerce}

- **季節のプロモーション:** 季節の商品コレクションをインポートし、現在のトレンドを反映したメッセージをパーソナライズします。
- **ローカライズされたメッセージ:** 実店舗の住所、営業時間、サービスをインポートし、ユーザーの所在地に基づいて通知をパーソナライズします。
- **再入荷通知:** 在庫数量を含む製品情報をインポートし、[再入荷通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/)とBrazeのカスタムイベントを使用して、製品が再入荷したことをユーザーに通知するキャンペーンまたはキャンバスをトリガーします。
- **価格低下通知:** 商品価格を含む製品情報をインポートし、[価格低下通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/)とBrazeのカスタムイベントを使用して、商品の価格が下がったことをユーザーに通知するキャンバスをトリガーします。

### エンターテイメント {#entertainment}

- **サブスクリプションプラン:** サブスクリプションプランをインポートし、ユーザーの利用パターンや最もよく消費するコンテンツの種類に基づいてアドオンをプロモーションします。
- **今後のイベント:** 近日開催予定のイベントリストとその場所、対象年齢をインポートし、対象エリア内にいる該当年齢のユーザーにパーソナライズされた通知を送信します。
- **メディアの好み:** 映画や番組の情報をインポートし、ユーザーのお気に入りタイトルやよく視聴するジャンルに基づいてコンテンツをおすすめします。

### 旅行とホスピタリティ {#travel-and-hospitality}

- **旅行先:** 旅行先とその人気アトラクション、レストラン、アクティビティをインポートし、ユーザーの過去の旅行に基づいてパーソナライズされたおすすめを提供します。
- **宿泊施設:** ホテルの施設情報とそのアメニティ、客室タイプ、料金をインポートし、ユーザーが選択した好みに基づいてプロモーションを送信します。
- **移動手段:** 航空券、鉄道、レンタカーなどの移動手段に関するお得な情報やプロモーションをインポートし、ユーザーの最近の検索履歴に基づいて送信します。
- **食事の好み:** 食事メニューの情報をインポートし、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)を使用して、最近閲覧した食品カテゴリに基づき、特定の食事の好みを持つユーザーにパーソナライズされたメッセージを送信します。

## カタログとLiquidの連携の仕組み {#how-catalogs-and-liquid-work-together}

カタログはデータ保存機能です。パーソナライゼーションのためにメッセージ内で参照できる大規模なデータセットが含まれています。実際にデータを参照するには、テンプレート言語として[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)を使用します。つまり、カタログはデータが保管されているストレージであり、Liquidはストレージから関連データを取得するための言語です。

Liquidを使用してカタログ情報を取得する方法の例については、[カタログを作成する]({{site.baseurl}}/user_guide/data/activation/catalogs/create#additional-use-cases/)の追加のユースケースを参照してください。

## データ保存の制限 {#data-storage-limitations}

カタログのデータストレージは、カタログアイテムのサイズに基づいて制限されます。これは、アップロードしたCSVファイルのサイズとは異なる場合があります。

カタログの無料バージョンの場合、許可されるストレージ容量は最大100&nbsp;MBです。ストレージが100&nbsp;MBを超えない限り、アイテム数は無制限です。

Catalogs Proの場合、ストレージサイズのオプションは5&nbsp;GB、10&nbsp;GB、15&nbsp;GB、または50&nbsp;GBです。なお、無料版のストレージ（100&nbsp;MB）はこれらの各プランに含まれています。

カタログストレージのアップグレードが必要な場合は、Brazeアカウントマネージャーにお問い合わせください。プランの詳細と利用資格については、[カタログストレージ]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers)を参照してください。
---
nav_title: "フルスクリーン"
article_title: フルスクリーンアプリ内メッセージ
description: "このリファレンス記事では、フルスクリーンアプリ内メッセージのメッセージおよびデザイン要件について説明します。"
page_type: reference
page_order: 1
channel:
  - in-app messages
tool:
  - Media

---

# フルスクリーンアプリ内メッセージ {#fullscreen-in-app-messages}

> フルスクリーンメッセージは、デバイスの画面全体を占有します。このメッセージタイプは、必須のアプリ更新など、ユーザーの注意を確実に引きたい場合に最適です。

このメッセージタイプは、[ドラッグ＆ドロップ]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)と[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)の両方で利用できます。

{% tabs %}
{% tab 縦向き %}

![縦向きで並べて表示された2つのフルスクリーンアプリ内メッセージ。画像とテキストの推奨事項が記載されています。詳細は以下のセクションを参照してください。]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab 横向き %}

![横向きで並べて表示された2つのフルスクリーンアプリ内メッセージ。画像とテキストの推奨事項が記載されています。詳細は以下のセクションを参照してください。]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## 画像 {#images}

フルスクリーンアプリ内メッセージは、デバイスの高さ全体を埋め、必要に応じて水平方向（左右）にトリミングされます。画像とテキストのフルスクリーンメッセージは、デバイスの高さの50%を占めます。すべてのフルスクリーンアプリ内メッセージは、「ノッチ」付きデバイスのステータスバーも埋めます。

{% multi_lang_include in-app_messages/image_requirements.md %}

{% alert tip %} 自信を持ってアセットを作成しましょう！アプリ内メッセージの画像テンプレートとセーフゾーンオーバーレイは、あらゆるサイズのデバイスに対応するよう設計されています。[デザインテンプレートZIPをダウンロード]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### 縦向き {#portrait}

| レイアウト | アセットサイズ | 備考 |
|--- | --- | --- |
| 画像とテキスト | 6:5のアスペクト比<br> 高解像度 1200 x 1000&nbsp;px<br> 最小 600 x 500&nbsp;px | すべての辺でトリミングが発生する可能性がありますが、画像は常にビューポートの上部50%を埋めます |
| 画像のみ | 3:5のアスペクト比<br> 高解像度 1200 x 2000&nbsp;px<br> 最小 600 x 1000&nbsp;px | 縦長のデバイスでは主要な辺と右端でトリミングが発生する可能性があります |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="縦向き" }

### 横向き {#landscape}

| レイアウト | アセットサイズ | 備考 |
|--- | --- | --- |
| 画像とテキスト | 10:3のアスペクト比<br> 高解像度 2000 x 600px<br> 最小 1000 x 300&nbsp;px | すべての辺でトリミングが発生する可能性がありますが、画像は常にビューポートの上部50%を埋めます |
| 画像のみ | 5:3のアスペクト比<br> 高解像度 2000 x 1200px<br> 最小 1000 x 600&nbsp;px | 縦長のデバイスでは主要な辺と右端でトリミングが発生する可能性があります |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="横向き" }

### 画像セーフゾーン {#image-safe-zone}

Brazeプラットフォームでフルスクリーンアプリ内メッセージをプレビューする際、画像セーフゾーンを有効にすると、さまざまなデバイスで表示した際にトリミングされない安全な領域を確認できます。プレビューペインで画像セーフゾーンをテストするだけでなく、いつものように[メッセージをテスト]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)することをお勧めします。

![Brazeでアプリ内メッセージをプレビューしている画面。「Show Image Safe Zone」が有効になっています。画像セーフゾーンは、画像のどの部分がトリミングされずに安全に表示されるかを視覚化するオーバーレイです。]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## 大画面 {#larger-screens}

タブレットやデスクトップブラウザでは、フルスクリーンアプリ内メッセージは以下のスクリーンショットのようにアプリ画面の中央に表示されます。

{% tabs %}
{% tab 縦向き %}

![大画面で縦向きに表示されたフルスクリーンアプリ内メッセージ。メッセージは画面中央に配置された大きなモーダルとして表示されます。]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab 横向き %}

![大画面で横向きに表示されたフルスクリーンアプリ内メッセージ。メッセージは画面中央に配置された大きなモーダルとして表示されます。]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}
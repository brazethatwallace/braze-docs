---
nav_title: "アプリ内メッセージ"
article_title: "アプリ内メッセージ"
page_order: 5
page_type: landing
alias: /in-app_messages/
description: "Brazeのさまざまなレイアウトやパーソナライゼーションツールを使用して、カスタマイズされたアプリ内メッセージでユーザーをエンゲージし、ユーザー体験を向上させましょう。"
channel:
  - in-app messages
search_rank: 5
---

# アプリ内メッセージ {#in-app-messages}

> アプリ内メッセージを使用すると、プッシュ通知でユーザーの日常を中断することなく、コンテンツを届けることができます。カスタマイズされたアプリ内メッセージはユーザー体験を向上させ、オーディエンスがアプリから最大限の価値を得られるようにします。さまざまなレイアウトやカスタマイズツールから選択でき、アプリ内メッセージはこれまで以上にユーザーをエンゲージします。

## 前提条件 {#prerequisites}

アプリ内メッセージを送信するには、アプリまたはWebサイトに[Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)を統合する必要があります。追加のセットアップは不要です。

SDKの最小バージョンおよび機能固有の要件については、以下を参照してください。
- [ドラッグ＆ドロップエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
- [メッセージタイプ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/)

## ユースケース {#use-cases}

アプリ内メッセージが提供するリッチなコンテンツを活用して、さまざまなユースケースでこのチャネルを利用できます。

| ユースケース | 説明 |
| --- | --- |
| プッシュプライミング | リッチなアプリ内メッセージを使用した[プッシュプライミング]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/)キャンペーンを実行し、アプリやサイトのプッシュ通知をオプトインするメリットを顧客に示し、プッシュ許可を付与するプロンプトを表示します。
| セールとプロモーション | モーダルアプリ内メッセージを使用して、静的なプロモーションコードやオファーを含む視覚的に魅力的なメディアで顧客を迎えます。通常であれば購入やコンバージョンに至らなかったユーザーにインセンティブを与えます。 |
| 機能の採用促進 | アプリの他の部分を使用したり、サービスを活用したりするよう顧客に促します。 |
| 高度にパーソナライズされたキャンペーン | 顧客がアプリやサイトに入ったときに最初に目にするものとしてアプリ内メッセージを配置します。[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)などのBrazeパーソナライゼーション機能を追加して、ユーザーにアクションを促し、アウトリーチをより効果的にします。
{: .reset-td-br-1 .reset-td-br-2 aria-label="Use cases" }

その他に検討すべきユースケースには以下があります。

- 新しいアプリ機能
- アプリ管理
- レビュー
- アプリのアップグレードまたは更新
- プレゼントや懸賞

## 標準メッセージタイプ {#standard-message-types}

以下のタブでは、標準的なアプリ内メッセージタイプ（スライドアップ、モーダル、フルスクリーンアプリ内メッセージ）をユーザーが開いたときの表示を確認できます。

{% tabs %}
{% tab スライドアップ %}

スライドアップメッセージは通常、アプリ画面の上部または下部に表示されます（メッセージ作成時に設定できます）。利用規約、Cookie、その他の情報スニペットについてユーザーに通知するのに最適です。

![アプリ画面の下部からスライドアップするアプリ内メッセージ。スライドアップにはアイコン画像と短いメッセージが含まれています。]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab モーダル %}

モーダルはデバイス画面の中央に表示され、バックグラウンドのアプリから目立つようにスクリーンオーバーレイが付きます。セールやプレゼントを活用するようユーザーにさりげなく提案するのに最適です。

![アプリとWebサイトの中央にダイアログとして表示されるモーダルアプリ内メッセージ。モーダルには画像、ヘッダー、メッセージ本文、2つのボタンが含まれています。]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab フルスクリーン %}

フルスクリーンメッセージはその名の通り、デバイスの画面全体を占有します！このメッセージタイプは、必須のアプリ更新など、ユーザーの注意を確実に引きたい場合に最適です。

![アプリ画面全体を占有するフルスクリーンアプリ内メッセージ。フルスクリーンメッセージには大きな画像、ヘッダー、メッセージ本文、2つのボタンが含まれています。]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

これらのデフォルトメッセージテンプレートに加えて、カスタムHTMLアプリ内メッセージ、CSSを使用したWebモーダル、またはWebメールキャプチャフォームを使用して、メッセージングをさらにカスタマイズすることもできます。詳細については、[カスタマイズ]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/)を参照してください。

表示時のテンプレート配信が**中止**ログにどのように影響するかについては、[アプリ内メッセージFAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq/)を参照してください。

## 次のステップ {#next-steps}

- [ドラッグ＆ドロップエディターでアプリ内メッセージを作成する]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)
- [従来のエディターでアプリ内メッセージを作成する]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}
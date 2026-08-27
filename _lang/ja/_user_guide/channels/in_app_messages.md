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

> アプリ内メッセージは、プッシュ通知でユーザーを中断することなく、アプリやWebサイト内でコンテンツを配信します。カスタマイズされたアプリ内メッセージは、レイアウト、パーソナライゼーション、ターゲティングツールを通じてユーザー体験を向上させ、オーディエンスがプロダクトからより多くの価値を得られるようにします。このハブでは、メッセージタイプ、ドラッグ＆ドロップエディター、前提条件、オンボーディングやプロモーションなどの一般的なユースケースについて説明します。最初のアプリ内メッセージを作成する前に[Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)を統合し、キャンペーンに合わせて標準またはカスタムレイアウトを選択してください。

## 前提条件 {#prerequisites}

アプリ内メッセージを送信するには、アプリまたはWebサイトに[Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)を統合する必要があります。追加の設定は不要です。

最小SDKバージョンおよび機能固有の要件については、以下を参照してください。
- [ドラッグ＆ドロップエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [メッセージタイプ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)

## ユースケース {#use-cases}

アプリ内メッセージが提供するリッチなコンテンツにより、このチャネルをさまざまなユースケースに活用できます。

| ユースケース | 説明 |
| --- | --- |
| プッシュプライミング | リッチなアプリ内メッセージを使用して[プッシュプライミング]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)キャンペーンを実施し、アプリやサイトのプッシュ通知をオプトインするメリットを顧客に示し、プッシュ許可を付与するプロンプトを表示します。
| セールとプロモーション | モーダルアプリ内メッセージを使用して、静的なプロモーションコードやオファーを含む視覚的に魅力的なメディアで顧客を迎えます。通常では購入やコンバージョンに至らない場面で、行動を促すインセンティブを提供します。 |
| 機能の導入促進 | アプリの他の機能を使用したり、サービスを活用したりするよう顧客に働きかけます。 |
| 高度にパーソナライズされたキャンペーン | 顧客がアプリやサイトを開いたときに最初に表示されるものとしてアプリ内メッセージを配置します。[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)などのBrazeパーソナライゼーション機能を追加して、ユーザーにアクションを促し、アウトリーチの効果を高めます。
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

その他に検討すべきユースケースには以下があります。

- アプリの新機能
- アプリ管理
- レビュー
- アプリのアップグレードまたは更新
- プレゼントや懸賞

## 標準メッセージタイプ {#standard-message-types}

以下のタブでは、標準的なアプリ内メッセージタイプ（スライドアップ、モーダル、フルスクリーンのアプリ内メッセージ）がユーザーに表示される様子を示しています。

{% tabs %}
{% tab スライドアップ %}

スライドアップメッセージは通常、アプリ画面の上部または下部に表示されます（メッセージ作成時に設定できます）。新しい利用規約、Cookie、その他の情報をユーザーに通知するのに最適です。

![アプリ画面の下部からスライドアップするアプリ内メッセージ。アイコン画像と短いメッセージが含まれています。]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab モーダル %}

モーダルはデバイス画面の中央に表示され、バックグラウンドのアプリから目立つようにスクリーンオーバーレイが付きます。セールやキャンペーンの活用をユーザーにしっかりと促すのに最適です。

![アプリやWebサイトの中央にダイアログとして表示されるモーダルアプリ内メッセージ。画像、ヘッダー、メッセージ本文、2つのボタンが含まれています。]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab フルスクリーン %}

フルスクリーンメッセージはその名の通り、デバイスの画面全体を占有します。必須のアプリ更新など、ユーザーの注意を確実に引きたい場合に最適なメッセージタイプです。

![アプリ画面全体を占めるフルスクリーンアプリ内メッセージ。大きな画像、ヘッダー、メッセージ本文、2つのボタンが含まれています。]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

これらのデフォルトメッセージテンプレートに加えて、カスタムHTMLアプリ内メッセージ、CSSを使用したWebモーダル、またはWebメールキャプチャフォームを使用して、メッセージングをさらにカスタマイズすることもできます。詳細については、[カスタマイズ]({{site.baseurl}}/user_guide/channels/in_app_messages/customize)を参照してください。

テンプレート化された配信が表示時に**中止**ログにどのように影響するかについては、[アプリ内メッセージ FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)を参照してください。

## 次のステップ {#next-steps}

- [ドラッグ＆ドロップエディターでアプリ内メッセージを作成する]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [従来のエディターでアプリ内メッセージを作成する]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}
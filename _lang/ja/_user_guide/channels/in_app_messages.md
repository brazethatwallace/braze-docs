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

アプリ内メッセージが提供する豊富なコンテンツレベルにより、このチャネルをさまざまなユースケースに活用できます。

| ユースケース | 説明 |
| --- | --- |
| プッシュプライミング | リッチなアプリ内メッセージを使用して[プッシュプライミング]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)キャンペーンを実行し、アプリやサイトのプッシュ通知をオプトインするメリットを顧客に示し、プッシュ許可を付与するプロンプトを提示します。
| セールとプロモーション | モーダルアプリ内メッセージを使用して、静的なプロモーションコードやオファーを含む視覚的に魅力的なメディアで顧客を迎えます。通常であれば行わなかったであろう購入やコンバージョンを促進します。 |
| 機能の採用促進 | アプリの他の部分を使用したり、サービスを活用したりするよう顧客に働きかけます。 |
| 高度にパーソナライズされたキャンペーン | アプリやサイトに入った顧客が最初に目にするものとしてアプリ内メッセージを配置します。[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)などのBrazeパーソナライゼーション機能を追加して、ユーザーにアクションを促し、アウトリーチをより効果的にします。
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

検討すべきその他のユースケースには以下があります。

- 新しいアプリ機能
- アプリ管理
- レビュー
- アプリのアップグレードまたは更新
- プレゼントや懸賞

## 標準メッセージタイプ {#standard-message-types}

以下のタブでは、標準的なアプリ内メッセージタイプ（スライドアップ、モーダル、フルスクリーンのアプリ内メッセージ）がユーザーにどのように表示されるかを確認できます。

{% tabs %}
{% tab スライドアップ %}

スライドアップメッセージは通常、アプリ画面の上部または下部に表示されます（メッセージ作成時に設定できます）。新しい利用規約、Cookie、その他の簡単な情報をユーザーに通知するのに最適です。

![アプリ画面の下部からスライドアップするアプリ内メッセージ。スライドアップにはアイコン画像と簡単なメッセージが含まれています。]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab モーダル %}

モーダルはデバイス画面の中央に表示され、画面オーバーレイによってバックグラウンドのアプリから目立つようになっています。セールやプレゼント企画をユーザーに積極的に案内したい場合に最適です。

![アプリとWebサイトの中央にダイアログとして表示されるモーダルアプリ内メッセージ。モーダルには画像、ヘッダー、メッセージ本文、2つのボタンが含まれています。]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab フルスクリーン %}

フルスクリーンメッセージは、その名の通りデバイスの画面全体を占有します！このメッセージタイプは、必須のアプリアップデートなど、ユーザーの注意を確実に引きたい場合に最適です。

![アプリ画面全体を占有するフルスクリーンアプリ内メッセージ。フルスクリーンメッセージには大きな画像、ヘッダー、メッセージ本文、2つのボタンが含まれています。]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

これらのデフォルトメッセージテンプレートに加えて、カスタムHTMLアプリ内メッセージ、CSSを使用したWebモーダル、またはWebメールキャプチャフォームを使用して、メッセージングをさらにカスタマイズすることもできます。詳細については、[カスタマイズ]({{site.baseurl}}/user_guide/channels/in_app_messages/customize)を参照してください。

表示時のテンプレート配信が**中止**ログにどのように影響するかについては、[アプリ内メッセージ FAQ]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)を参照してください。

## 次のステップ {#next-steps}

{% article_tiles %}
- name: ドラッグ＆ドロップエディターでアプリ内メッセージを作成する
  link: /docs/user_guide/channels/in_app_messages/drag_and_drop
- name: 従来のエディターでアプリ内メッセージを作成する
  link: /docs/user_guide/channels/in_app_messages/traditional
{% endarticle_tiles %}

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}
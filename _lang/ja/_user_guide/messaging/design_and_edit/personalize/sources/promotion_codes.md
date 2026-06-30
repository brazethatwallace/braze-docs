---
nav_title: プロモーションコード
article_title: プロモーションコード
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "プロモーションコードリストについて学び、CampaignやCanvasesに追加する方法を確認しましょう。"
---

# プロモーションコード {#promotion-codes}

> プロモーションコードリストについて学び、CampaignやCanvasesに追加する方法を確認しましょう。

## プロモーションコードについて {#about-promotion-codes}

プロモーションコードを使用すると、メッセージにユニークで期間限定の値を挿入して、コンバージョンを促進できます。各リストには最大2,000万件のコードを保持でき、各コードは最大6か月間有効です。

Brazeがプロモーションコード付きのメッセージを送信する際、コードはメッセージが送信される前に差し引かれます。コードの一貫性、ユニーク性、再利用防止を確保するために：

- メッセージの送信に失敗した場合でも、コードは消費されます。
- マルチチャネル送信では、同じコードがすべてのチャネルに適用されます。
- 条件付きLiquidを使用する場合、1つの分岐のみが表示される場合でも、参照されるすべてのリストからコードが差し引かれます。
- キャンバスステップに入る、または再入する場合、新しいコードが消費されます。

同じリストから複数のスニペットを1つのメッセージに配置した場合、Brazeはすべてのスニペットに同じコードを適用します。コードが不足しないように、使用予定数よりも多くのコードをアップロードすることをお勧めします。

{% tabs local %}
{% tab 例 %}
プロモーションコードは、郵便局のクーポンのようなものと考えてください。窓口係があなたの手紙のためにクーポンの束から1枚を取り出すと、たとえ手紙が届かなくても、そのクーポンはなくなります。

例えば、以下の条件付きLiquidでは、各ユーザーが1つの分岐しか見ない場合でも、両方のリスト（`vip-deal`と`regular-deal`）からコードが差し引かれます：

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
プロモーションコードは、アプリ内メッセージCampaignでは早期アクセス機能として利用可能ですが、Canvasのアプリ内メッセージでは送信できません。
{% endalert %}

## 次のステップ {#next-steps}

次のステップをお探しですか？こちらから始めましょう：

- [プロモーションコードリストの作成]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create)
- [プロモーションコードの使用]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#using-promotion-codes)
- [プロモーションコードの使用状況の確認]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#viewing-promotion-code-usage)

## よくある質問 {#frequently-asked-questions}

### プロモーションコードはどのメッセージングチャネルで使用できますか？ {#which-messaging-channels-can-i-use-with-promotion-codes}

プロモーションコードは、メール、モバイルプッシュ、Webプッシュ、Content Cards、Webhook、SMS、WhatsAppでサポートされています。アプリ内メッセージCampaignでは、早期アクセス機能としてプロモーションコードをサポートしています。BrazeのトランザクションメールCampaignおよびCanvasのアプリ内メッセージでは、プロモーションコードはサポートされていません。

### テスト送信やシード送信は使用量にカウントされますか？ {#do-test-and-seed-sends-count-towards-usage}

デフォルトでは、テスト送信およびシードグループのメール送信は、ユーザーごと、テスト送信ごとにプロモーションコードを使用します。ただし、テスト中にプロモーションコードを使用しないように動作を更新するには、Brazeアカウントマネージャーにお問い合わせください。

### 複数のメッセージングチャネルが同じプロモーションコードスニペットを使用する場合はどうなりますか？ {#what-happens-when-multiple-messaging-channels-use-the-same-promotion-code-snippet}

特定のユーザーが複数のチャネルを通じてコードを受け取る資格がある場合、各チャネルを通じて同じコードを受け取ります。受信したチャネル数に関係なく、使用されるプロモーションコードは1つだけです。

### 1つのメッセージ内で同じプロモーションコードリストを参照する複数のLiquidスニペットを使用できますか？ {#can-i-use-multiple-liquid-snippets-to-reference-the-same-promotion-code-list-in-one-message}

はい。Brazeはメッセージ内のそのスニペットのすべてのインスタンスに同じプロモーションコードを適用し、ユーザーが受け取るユニークコードは1つだけになります。

### プロモーションコードリストが期限切れまたは空の場合はどうなりますか？ {#what-happens-when-a-promotion-code-list-is-expired-or-empty}

期限切れのコードは6か月後に削除されます。

空または期限切れのリストからのプロモーションコードを含むはずだったメッセージは、キャンセルされます。

メッセージに条件付きでプロモーションコードを挿入するLiquidロジックが含まれている場合、プロモーションコードを含むはずだった場合にのみメッセージがキャンセルされます。プロモーションコードを含むはずでなかった場合、メッセージは通常どおり送信されます。

### 間違ったプロモーションコードをアップロードした場合、更新できますか？ {#if-i-uploaded-the-wrong-promotion-codes-can-i-update-them}

間違ったコードをアップロードした場合、以下の2つの方法で解決できます：

- **リスト全体を非推奨にする：** 現在のリストをすべてのCampaign、Canvases、またはテンプレートでの使用を停止します。次に、正しいコードを新しいリストにアップロードし、すべてのメッセージを新しいリストを使用するように切り替えます。
- **間違ったコードを使い切る：** 間違ったリストからプレースホルダーユーザーにコードを送信するCampaignを作成し、間違ったコードがすべて使用されるまで実行します。その後、間違ったコードを除外して、正しいコードを同じリストに再アップロードします。

リストの更新に関する一般的なガイダンスについては、[プロモーションコードリストの更新]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#updating-a-promotion-code-list)を参照してください。

### Brazeはどのユーザーがどのプロモーションコードを受け取ったか、または利用したかを追跡しますか？ {#does-braze-track-which-users-received-or-redeemed-which-promotion-codes}

メッセージでプロモーションコードが使用されると、Brazeはそのコードを消費済みとしてマークし、再送信されないようにして、リストの残数を更新します。Brazeは送信済みコードのレポートを保持したり、各コードを受け取った特定のユーザーを追跡したり、コードが利用されたかどうかを追跡したりすることはありません。

コードをユーザーに関連付けたり、利用状況を自分で追跡したりする必要がある場合は、以下の方法があります：

- ユーザーの更新ステップを通じて、プロモーションコードをユーザープロファイルに保存します。詳細については、[プロモーションコードをユーザープロファイルに保存する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile)を参照してください。
- `message_extras` Liquidタグを使用して、プロモーションコードの値をCurrentsに送信します。詳細については、[プロモーションコード情報をCurrentsに送信する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras#sending-promotion-code-information-to-currents)を参照してください。

### プロモーションコードをユーザープロファイルに保存して、将来のメッセージで使用できますか？ {#can-i-save-a-promotion-code-to-a-users-profile-for-future-messages}

はい。ユーザーの更新ステップを通じて、プロモーションコードをユーザープロファイルに保存できます。詳細については、[プロモーションコードをユーザープロファイルに保存する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile)を参照してください。
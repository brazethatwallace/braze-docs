---
nav_title: プロモーションコード
article_title: プロモーションコード
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "プロモーションコードリストについて学び、キャンペーンやキャンバスに追加する方法を確認しましょう。"
---

# プロモーションコード {#promotion-codes}

> プロモーションコードリストについて学び、キャンペーンやキャンバスに追加する方法を確認しましょう。

## プロモーションコードについて {#about-promotion-codes}

プロモーションコードを使用すると、メッセージにユニークで有効期限付きの値を挿入してコンバージョンを促進できます。各リストには最大2,000万個のコードを保持でき、各コードは最長6か月間有効です。

Brazeがプロモーションコード付きのメッセージを送信する際、コードはメッセージが送信される前に差し引かれます。コードの一貫性、ユニーク性、再利用防止を確保するために、以下の点にご注意ください。

- メッセージの送信に失敗した場合でも、コードは消費されます。
- マルチチャネル送信では、すべてのチャネルで同じコードが適用されます。
- 条件付きLiquidを使用する場合、1つの分岐のみが表示される場合でも、参照されたすべてのリストからコードが差し引かれます。
- キャンバスステップへの入場または再入場時に新しいコードが消費されます。

1つのメッセージ内で同じリストから複数のスニペットを配置した場合、Brazeはすべてのスニペットに同じコードを適用します。コード不足を避けるため、使用予定数よりも多くのコードをアップロードすることをお勧めします。

{% tabs local %}
{% tab 例 %}
プロモーションコードは、郵便局のクーポンのようなものと考えてください。窓口担当者が手紙用にクーポンの束から1枚取り出すと、たとえ手紙が届かなくても、そのクーポンはなくなります。

たとえば、以下の条件付きLiquidでは、各ユーザーに1つの分岐のみが表示される場合でも、両方のリスト（`vip-deal`と`regular-deal`）からコードが差し引かれます。

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
プロモーションコードは、アプリ内メッセージキャンペーンで早期アクセス機能として利用できますが、キャンバスのアプリ内メッセージでは送信できません。
{% endalert %}

## 次のステップ {#next-steps}

次のステップをお探しですか？ここから始めましょう：

{% article_tiles %}
- name: プロモーションコードリストの作成
  link: /docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create
- name: プロモーションコードの使用
  link: /docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#using-promotion-codes
- name: プロモーションコードの使用状況の確認
  link: /docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#viewing-promotion-code-usage
{% endarticle_tiles %}

## よくある質問 {#frequently-asked-questions}

### プロモーションコードで使用できるメッセージングチャネルは何ですか？ {#which-messaging-channels-can-i-use-with-promotion-codes}

プロモーションコードは、メール、モバイルプッシュ、Webプッシュ、Content Cards、Webhook、SMS、WhatsAppでサポートされています。アプリ内メッセージキャンペーンでは、プロモーションコードは早期アクセス機能としてサポートされています。Brazeトランザクションメールキャンペーンおよびキャンバス内のアプリ内メッセージでは、プロモーションコードはサポートされていません。

### テスト送信とシード送信は使用量にカウントされますか？ {#do-test-and-seed-sends-count-towards-usage}

デフォルトでは、テスト送信とシードグループのメール送信は、ユーザーごと、テスト送信ごとにプロモーションコードを使用します。ただし、テスト中にプロモーションコードを使用しないようにこの動作を変更するには、Brazeアカウントマネージャーにお問い合わせください。

### 複数のメッセージングチャネルが同じプロモーションコードスニペットを使用するとどうなりますか？ {#what-happens-when-multiple-messaging-channels-use-the-same-promotion-code-snippet}

特定のユーザーが複数のチャネルを通じてコードを受け取る対象となっている場合、各チャネルで同じコードが送信されます。受信チャネル数に関係なく、使用されるプロモーションコードは1つだけです。

### 1つのメッセージで同じプロモーションコードリストを参照するために、複数のLiquidスニペットを使用できますか？ {#can-i-use-multiple-liquid-snippets-to-reference-the-same-promotion-code-list-in-one-message}

はい。Brazeはメッセージ内のそのスニペットのすべてのインスタンスに同じプロモーションコードを適用し、ユーザーが受け取るユニークなコードは1つだけになります。

### プロモーションコードリストが期限切れまたは空の場合はどうなりますか？ {#what-happens-when-a-promotion-code-list-is-expired-or-empty}

期限切れのコードは6か月後に削除されます。

空または期限切れのリストからプロモーションコードを含むべきメッセージは、キャンセルされます。

メッセージにプロモーションコードを条件付きで挿入するLiquidロジックが含まれている場合、プロモーションコードを含むべきメッセージのみがキャンセルされます。プロモーションコードを含むべきでないメッセージは、通常どおり送信されます。

### 間違ったプロモーションコードをアップロードしてしまった場合、更新できますか？ {#if-i-uploaded-the-wrong-promotion-codes-can-i-update-them}

間違ったコードをアップロードした場合、解決するには2つのオプションがあります。

- **リスト全体を廃止する:** 現在のリストをすべてのキャンペーン、キャンバス、またはテンプレートで使用を停止します。次に、正しいコードを新しいリストにアップロードし、すべてのメッセージを新しいリストに切り替えます。
- **間違ったコードを使い切る:** プレースホルダーユーザーに間違ったリストからコードを送信するキャンペーンを作成し、すべての間違ったコードが使用されるまで続けます。その後、間違ったコードを除外して、同じリストに正しいコードを再アップロードします。

リストの更新に関する一般的なガイダンスについては、[プロモーションコードリストの更新]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#updating-a-promotion-code-list)を参照してください。

### Brazeはどのユーザーがどのプロモーションコードを受け取ったか、または使用したかを追跡しますか？ {#does-braze-track-which-users-received-or-redeemed-which-promotion-codes}

メッセージがプロモーションコードを使用すると、Brazeはそのコードを消費済みとしてマークし、再送信されないようにしてリストの残数を更新します。Brazeは、送信済みコードのレポートの維持、各コードを受け取った特定のユーザーの追跡、またはコードが利用されたかどうかの追跡は行いません。

コードをユーザーに関連付けたり、利用状況を自分で追跡したりする必要がある場合は、以下の方法があります。

- ユーザーの更新ステップを使用して、プロモーションコードをユーザープロファイルに保存します。詳細については、[プロモーションコードをユーザープロファイルに保存する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile)を参照してください。
- `message_extras` Liquidタグを使用して、プロモーションコードの値をCurrentsに送信します。詳細については、[プロモーションコード情報をCurrentsに送信する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras#sending-promotion-code-information-to-currents)を参照してください。

### プロモーションコードを将来のメッセージ用にユーザーのプロファイルに保存できますか？ {#can-i-save-a-promotion-code-to-a-users-profile-for-future-messages}

はい。ユーザーの更新ステップを使用して、プロモーションコードをユーザーのプロファイルに保存できます。詳細については、[プロモーションコードをユーザープロファイルに保存する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile)を参照してください。
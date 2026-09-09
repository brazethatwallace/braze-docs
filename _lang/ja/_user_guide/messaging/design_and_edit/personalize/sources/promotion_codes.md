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

プロモーションコードを使用すると、メッセージにユニークで期間限定の値を挿入してコンバージョンを促進できます。各リストには最大2,000万件のコードを保持でき、各コードの有効期限は最大6か月です。

Brazeがプロモーションコード付きのメッセージを送信する際、メッセージの送信前にコードが差し引かれます。コードの一貫性、一意性、再利用防止を確保するために、以下の点に注意してください。

- 送信に失敗したメッセージでもコードは消費されます。
- マルチチャネル送信では、すべてのチャネルで同じコードが適用されます。
- 条件付きLiquidの場合、1つの分岐のみが表示される場合でも、参照されているすべてのリストからコードが差し引かれます。
- キャンバスステップへの進入または再進入により、新しいコードが消費されます。

1つのメッセージに同じリストから複数のスニペットを配置した場合、Brazeはすべてのスニペットに同じコードを適用します。コードの不足を避けるために、使用予定数より多めにコードをアップロードしてください。

{% tabs local %}
{% tab 例 %}
プロモーションコードは、郵便局のクーポンのようなものです。窓口の担当者があなたの手紙のためにクーポンの束から1枚を取り出すと、手紙が届かなかったとしても、そのクーポンは使われたことになります。

たとえば、以下の条件付きLiquidでは、各ユーザーが1つの分岐のみを見る場合でも、両方のリスト（`vip-deal`と`regular-deal`）からコードが差し引かれます。

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
プロモーションコードはアプリ内メッセージキャンペーンで利用できますが、キャンバスのアプリ内メッセージでは送信できません。
{% endalert %}

## 次のステップ {#next-steps}

次のステップをお探しですか？こちらからご覧ください。

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

プロモーションコードは、メール、モバイルプッシュ、Webプッシュ、Content Cards、Webhook、SMS、WhatsAppに対応しています。アプリ内メッセージキャンペーンでは、プロモーションコードは早期アクセス機能としてサポートされています。Brazeトランザクションメールキャンペーンおよびキャンバスのアプリ内メッセージでは、プロモーションコードはサポートされていません。

### テスト送信およびシード送信は使用量にカウントされますか？ {#do-test-and-seed-sends-count-towards-usage}

デフォルトでは、テスト送信とシードグループのメール送信は、ユーザーごと、テスト送信ごとにプロモーションコードを使用します。ただし、テスト中にプロモーションコードを使用しないようにするには、Brazeアカウントマネージャーに連絡してこの動作を更新できます。

### 複数のメッセージングチャネルで同じプロモーションコードスニペットを使用するとどうなりますか？ {#what-happens-when-multiple-messaging-channels-use-the-same-promotion-code-snippet}

特定のユーザーが複数のチャネルを通じてコードを受け取る資格がある場合、各チャネルで同じコードが送信されます。受信したチャネル数に関係なく、使用されるプロモーションコードは1つだけです。

### 1つのメッセージで同じプロモーションコードリストを参照する複数のLiquidスニペットを使用できますか？ {#can-i-use-multiple-liquid-snippets-to-reference-the-same-promotion-code-list-in-one-message}

はい。Brazeはメッセージ内のそのスニペットのすべてのインスタンスに同じプロモーションコードを適用し、ユーザーが受け取るユニークなコードは1つだけになります。

### プロモーションコードリストが期限切れまたは空の場合はどうなりますか？ {#what-happens-when-a-promotion-code-list-is-expired-or-empty}

期限切れのコードは6か月後に削除されます。

空または期限切れのリストからプロモーションコードを含むべきメッセージの場合、そのメッセージはキャンセルされます。

メッセージにプロモーションコードを条件付きで挿入するLiquidロジックが含まれている場合、メッセージがキャンセルされるのはプロモーションコードを含むべきだった場合のみです。プロモーションコードを含むべきでなかった場合、メッセージは通常どおり送信されます。

### 間違ったプロモーションコードをアップロードした場合、更新できますか？ {#if-i-uploaded-the-wrong-promotion-codes-can-i-update-them}

間違ったコードをアップロードした場合、解決する方法は2つあります。

- **リスト全体を廃止する：**現在のリストをすべてのキャンペーン、キャンバス、またはテンプレートでの使用を停止します。次に、正しいコードを新しいリストにアップロードし、すべてのメッセージを新しいリストに切り替えます。
- **間違ったコードを使い切る：**プレースホルダーユーザーに間違ったリストからコードを送信するキャンペーンを作成し、すべての間違ったコードが使用されるまで送信します。その後、間違ったコードを除外して、正しいコードを同じリストに再アップロードします。

リストの更新に関する一般的なガイダンスについては、[プロモーションコードリストの更新]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#updating-a-promotion-code-list)を参照してください。

### Brazeはどのユーザーがどのプロモーションコードを受け取ったか、または利用したかを追跡しますか？ {#does-braze-track-which-users-received-or-redeemed-which-promotion-codes}

メッセージがプロモーションコードを使用すると、Brazeはそのコードを消費済みとしてマークし、再送信できないようにし、リストの残りの数を更新します。Brazeは送信済みコードのレポートを保持せず、どのユーザーがどのコードを受け取ったかの追跡や、コードが利用されたかどうかの追跡も行いません。

コードをユーザーに関連付けたり、利用状況を自分で追跡する必要がある場合は、以下の方法があります。

- ユーザー更新ステップを通じてプロモーションコードをユーザープロファイルに保存します。詳細については、[プロモーションコードをユーザープロファイルに保存する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile)を参照してください。
- `message_extras` Liquidタグを使用して、プロモーションコードの値をCurrentsに送信します。詳細については、[プロモーションコード情報をCurrentsに送信する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras#sending-promotion-code-information-to-currents)を参照してください。

### プロモーションコードを将来のメッセージのためにユーザーのプロファイルに保存できますか？ {#can-i-save-a-promotion-code-to-a-users-profile-for-future-messages}

はい。ユーザー更新ステップを通じてプロモーションコードをユーザーのプロファイルに保存できます。詳細については、[プロモーションコードをユーザープロファイルに保存する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile)を参照してください。
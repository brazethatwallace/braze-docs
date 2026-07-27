---
nav_title: ドラッグ＆ドロップメールユーザー設定センター
article_title: ドラッグ＆ドロップメールユーザー設定センター
alias: "/dnd_preference_center/"
description: "このリファレンスページでは、ドラッグ＆ドロップエディターを使用してメールユーザー設定センターを作成する方法について説明します。"
page_order: 2
---

# ドラッグ＆ドロップでメールユーザー設定センターを作成する {#create-an-email-preference-center-with-drag-and-drop}

> ドラッグ＆ドロップエディターを使用すると、ユーザー設定センターを作成・カスタマイズして、どのユーザーがどの種類のコミュニケーションを受信するかを管理できます。ワークスペースごとに最大100個のユーザー設定センターを作成できます。

既存のドラッグ＆ドロップユーザー設定センターは、**オーディエンス** > **メールユーザー設定センター**から管理できます。

- ユーザー設定センターの名前やコンテンツを変更するには、ダッシュボードからユーザー設定センターを開きます。
- ドラッグ＆ドロップユーザー設定センターはダッシュボードから削除できません。削除するには、まずメールキャンペーンまたはキャンバスステップからLiquidタグを削除してから、[Brazeサポート]({{site.baseurl}}/support_contact)にお問い合わせください。
- 削除されたユーザー設定センターが以前送信されたメッセージで使用されていた場合、配信済みのメールでは機能しなくなります。
{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## ステップ1：メールユーザー設定センターを作成する {#step-1-create-an-email-preference-center}

**オーディエンス** > **メールユーザー設定センター**に移動して、ユーザー設定センターを作成します。ここには、カスタムユーザー設定センターの一覧が表示されます。**新規作成**を選択して新しいユーザー設定センターを作成するか、既存のユーザー設定センターの名前を選択して変更を加えます。

## ステップ2：メールユーザー設定センターに名前を付ける {#step-2-name-the-email-preference-center}

ユーザー設定センターの名前には、英数字、ダッシュ、またはアンダースコアのみを使用できます。指定した名前によって、生成されるLiquidタグの構文が決まります。

このLiquidタグは、任意の送信メールキャンペーンまたはキャンバスステップに含めることができ、ユーザーをユーザー設定センターに誘導します。

## ステップ3：ユーザー設定センターに購読グループを追加する {#step-3-add-subscription-groups-to-the-preference-center}

**Launch Editor** を選択して、ドラッグ＆ドロップエディターでユーザー設定センターのデザインを開始します。

### 利用可能な購読グループを定義する {#define-available-subscription-groups}

ユーザー設定センターに表示する購読グループを決定するには、**+ Add subscription groups** ボタンを選択して、目的の購読グループを選択できるモーダルを起動します。選択後、**Add Subscription Groups** ボタンを選択して、ユーザー設定センターに追加します。

スマートブロックを選択してブロックプロパティを調整することで、選択した購読グループをさらに設定できます。

- 購読グループの順序を調整する
- 追加の購読グループを追加または削除する
- 説明を含める
- **Subscribe to all** チェックボックスを追加または削除する。これにより、ユーザーはこのブロックに表示されているすべての購読グループに購読されます
- **Unsubscribe from all** チェックボックスを追加または削除する。これにより、ユーザーはこのブロックに表示されているすべての購読グループから購読解除されます

テンプレートの下部にある **Unsubscribe from all** ボタンは削除できず、ユーザーのメール受信を[グローバルに購読解除]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)します。

## ステップ4: ドラッグ＆ドロップエディターを使用してユーザー設定センターをカスタマイズする {#step-4-customize-the-preference-center-using-the-drag-and-drop-editor}

### 共通スタイルを設定する {#set-common-styles}

**共通スタイル**タブから、ユーザー設定センター内のすべての関連ブロックに適用されるスタイルを設定できます。このセクションで設定されたスタイルは、特定のブロックでオーバーライドしない限り、メッセージ全体で使用されます。デザインを効率的に行うために、ブロックレベルでスタイルをカスタマイズする前に、ページレベルのスタイルを設定することをお勧めします。

![テキスト、ボタン、リンクの共通スタイル設定の例。]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
共通スタイルに戻るには、個々のブロックプロパティの「X」ボタンを選択します。次に、メッセージコンテナ、メッセージの「X」ボタン、またはエディターの背景を選択します。
{% endalert %}

## ドラッグ＆ドロップのユーザー設定センターコンポーネント {#drag-and-drop-preference-center-components}

ドラッグ＆ドロップエディターは、ユーザー設定センターの作成を迅速かつ簡単にするために、行とブロックという2つの主要コンポーネントを使用します。すべてのブロックは行の中に配置する必要があります。

{% tabs %}
{% tab 行 %}

行は、セルを使用してメッセージのセクションの水平方向の構成を定義する構造単位です。

![メッセージで使用する行のタイプを選択するオプション。]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

行を選択すると、「列のカスタマイズ」セクションから必要な列数を追加または削除して、異なるコンテンツ要素を横に並べて配置できます。また、スライドして既存の列のサイズを調整することもできます。

![背景色、ボーダースタイル、ボーダーの角丸、パディングなど、列のプロパティをカスタマイズするオプション。]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

ベストプラクティスとして、行内のブロックをフォーマットする前に、行と列のプロパティをフォーマットしてください。間隔や配置はさまざまな場所で調整できるため、基盤から始めることで、作業を進めながら編集しやすくなります。

{% endtab %}
{% tab ブロック %}

ブロックは、メッセージで使用できるさまざまなタイプのコンテンツを表します。既存の行セグメント内にドラッグすると、セルの幅に自動的に調整されます。

![タイトル、段落、ボタン、画像、スペーサーなどのブロックを選択するオプション。]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

各ブロックには、パディングの細かいコントロールなど、独自の設定があります。右側のパネルは、選択したコンテンツ要素のスタイリングパネルに自動的に切り替わります。詳細については、[エディターブロック（ユーザー設定センター）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=preference%20center)を参照してください。

ユーザー設定センターでカスタムコードブロックを使用している場合、ユーザーに配信される際にカスタムコード内でインラインフレームが生成されないことがあります。

{% alert note %}
リンクを含むContent Blocksは、ドラッグ＆ドロップのユーザー設定センターでは使用できません。Content Blocks内のリンクはクリックできません。
{% endalert %}

{% endtab %}
{% endtabs %}

## ステップ5：確認ページをカスタマイズする {#step-5-customize-your-confirmation-page}

次に、**確認ページ**を選択して確認ページをカスタマイズします。このページは、ユーザーがユーザー設定センターを使用して設定を更新した後に表示されます。[共通スタイルの設定](#set-common-styles)および[ドラッグ＆ドロップのユーザー設定センターコンポーネント](#drag-and-drop-preference-center-components)と同じスタイリング機能がこのページにも適用されます。

![ユーザーの設定が更新されたことを伝える確認ページの例。]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## ステップ6：ユーザー設定センターをプレビューして公開する {#step-6-preview-and-launch-your-preference-center}

エディター内の**プレビュー**タブを選択すると、ユーザー設定センターをプレビューできます。プレビューでは、ユーザー設定センターと確認ページの両方が表示されます。

ただし、テスト機能は無効になっています。また、ユーザー設定センターのLiquidタグを含むキャンペーンやキャンバスステップのテスト送信では、有効なリンクが生成されません。このプレビューでは購読の変更を保存することはできず、ページの見た目を確認するためだけのものです。設定の保存をテストするには、[ユーザー設定センターのテスト](#testing-preference-centers)を参照してください。ユーザー設定センターの編集が完了したら、**Done**ボタンを選択してエディターを閉じることができます。

**Save as Draft**を選択すると、後でこのユーザー設定センターに戻ることができます。準備ができたら、**Launch Preference Center**を選択してください。

ユーザー設定センターを公開する際、名前の確認を求められます。公開後は名前を編集できないためです。名前を確認すると、ユーザー設定センターが公開され、使用可能な状態になります。

## ユーザー設定センターの使用 {#use-the-preference-center}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

メールにユーザー設定センターへのリンクを配置するには、**Copy Liquid** アイコンを選択して、目的のユーザー設定センターのLiquidタグをコピーします。

![ユーザー設定センターの行にあるCopy Liquidオプション。]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

[購読解除URL]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer#adding-a-custom-unsubscribe-link)を挿入する場合と同様に、メール内の目的の場所にLiquidタグを追加します。

{% multi_lang_include preference_center/testing.md %}

## よくある質問 {#frequently-asked-questions}

### テスト送信でユーザー設定センターが機能しないのはなぜですか？ {#why-doesnt-my-preference-center-work-in-a-test-send}

ユーザー設定センターのリンクには、ライブ送信のコンテキストが必要です。テスト送信では有効なユーザー設定センターのURLが生成されず、ページが読み込まれると**設定を保存**ボタンが無効になります。これは想定された動作です。エンドツーエンドのテストを行うには、キャンペーンまたはキャンバスステップをテストユーザーまたは小規模な内部セグメントに送信してください。詳細については、[ユーザー設定センターのテスト](#testing-preference-centers)を参照してください。

## エラーの処理 {#handle-errors}

ユーザーがユーザー設定センターで**保存**を選択した際にエラーが発生すると、以下のデフォルトのエラーメッセージが表示されます。このメッセージはエディターでカスタマイズやスタイル変更を行うことはできません。ただし、これらのページではエラーメッセージのローカライゼーションは引き続きサポートされています。

![「設定の保存中に問題が発生しました。もう一度お試しください。」というエラーメッセージ]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}
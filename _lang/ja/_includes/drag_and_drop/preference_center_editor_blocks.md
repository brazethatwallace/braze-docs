## ユーザー設定センターエディターのブロック {#preference-center-editor-blocks}

ドラッグ＆ドロップのユーザー設定センターエディターで、**Build**セクションからブロックを行にドラッグします。各ブロックには独自の設定があり、右側のパネルは選択した要素のプロパティまたはスタイリングに切り替わります。

ブロックを編集する前に、購読グループを追加し、購読**スマートブロック**を設定してください（以下のセクションを参照）。完全な設定フローについては、[ドラッグ＆ドロップでメールのユーザー設定センターを作成する]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center)を参照してください。

### タイトルと段落 {#title-and-paragraph}

リッチテキストオプションを使用して、見出しまたは本文コピーを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### ボタン {#button}

クリック可能なボタンを追加します（例：**Save**やナビゲーション）。

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### 画像 {#image}

[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)またはURLから画像を表示します。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### スペーサー {#spacer}

ブロック間に垂直方向のスペースを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### 購読グループ（スマートブロック） {#subscription-groups-smart-block}

購読グループ、オプションの**すべてを購読**／**すべての購読を解除**コントロール、および説明を一覧表示するテンプレートブロックを追加します。ユーザー設定センターのワークフローでグループを追加した後に設定してください。

[購読グループを追加]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-3-add-subscription-groups-to-the-preference-center)した後、エディターのキャンバス上でスマートブロックを選択して以下を行います。

- 購読グループの並べ替え
- グループの追加または削除
- 説明の追加または削除
- そのブロック内のグループに対する**すべてを購読**と**すべての購読を解除**の切り替え

デフォルトテンプレートの下部にある**すべての購読を解除**コントロールは必須であり、メールからの[グローバル購読解除]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)を実行します。

## 知っておくべきこと {#things-to-know}

- **共通スタイル：** 個々のブロックを調整する前に、**Common Styles**でページ全体のデフォルトを設定できます。詳細については、[ドラッグ＆ドロップエディターを使用してユーザー設定センターをカスタマイズする]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-4-customize-the-preference-center-using-the-drag-and-drop-editor)を参照してください。
- **確認ページ：** エディターの上部で**Confirmation Page**に切り替えると、同じブロックタイプを使用して保存後のエクスペリエンスをスタイリングできます。
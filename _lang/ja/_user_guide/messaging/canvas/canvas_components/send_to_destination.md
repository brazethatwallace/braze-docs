---
nav_title: 送信先へ送信
article_title: 送信先へ送信
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "この参照記事では、送信先へ送信コンポーネントと、Canvasでの使用方法について説明します。"
tool: Canvas
---

# 送信先へ送信ステップ {#send-to-destination-step}

> 送信先へ送信ステップを使用すると、あるCanvasから別のCanvasにユーザーを送信できます。例えば、プロモーションオファーのメッセージングを共有するCanvasを接続できます。

## 仕組み {#how-it-works}

![新しいCanvasにユーザーを送信するための送信先へ送信ステップ。]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

送信先へ送信ステップを含む現在のCanvasがソースです。ステップ内で、送信先のCanvasを選択できます。ソースCanvasのユーザーは、送信先Canvasのエントリ条件とオーディエンス条件を満たす必要があります。例えば、2つのCanvasがあるとします。

- **ソース:** Canvas 1、ユーザーをCanvas 2に送信する送信先へ送信ステップを含む
- **送信先:** Canvas 2、アイテムを注文したユーザーをエントリさせるエントリ条件を持つ

このステップにより、Canvas 1のユーザーをCanvas 2に送信できます。Canvas 1のユーザーが送信先へ送信ステップに入ると、Canvas 2のエントリ条件とオーディエンス条件に基づいて評価され、Canvasに入る資格があるかどうかが判断されます。この場合、アイテムを注文したユーザーはCanvas 2に入ることができ、Canvas 1のジャーニーも引き続き進みます。アイテムを注文していないユーザーは、Canvas 1のジャーニーのみを続けます。

### エントリの動作 {#entry-behavior}

送信先へ送信ステップは、ユーザーがこのステップに到達するとすぐに送信先Canvasにエントリさせます。このステップは、送信先Canvasへの1回限りのエントリポイントとして機能します。送信先Canvasのエントリ条件とオーディエンス条件を満たすユーザーは、そのCanvasジャーニーを開始します。その時点で条件を満たさないユーザーは送信先Canvasにエントリせず、ソースCanvasを続行します。

送信先Canvasがスケジュールされたエントリスケジュールを使用している場合、送信先へ送信ステップはそのエントリスケジュールをバイパスします。また、送信先Canvasの**エントリコントロール**で**Canvasがスケジュールされるたびに**に設定されている場合、[**エントリ数の制限**]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#selecting-entry-controls)もバイパスします。このステップから送信されたユーザーは、次のスケジュールされた評価時間枠を待ちません。送信先Canvasのエントリ条件とオーディエンス条件を満たしている場合、送信先へ送信ステップに到達した時点で評価され、エントリします。

送信先Canvasがアクションベースのエントリを使用している場合、送信先へ送信ステップは、ユーザーがそのCanvasに入るために設定されたエントリアクションを実行する要件をバイパスします。

## 送信先へ送信ステップを作成する {#create-a-send-to-destination-step}

### ステップ 1: ステップを追加する {#step-1-add-a-step}

サイドバーから**Send to Destination**コンポーネントをドラッグ＆ドロップするか、ステップの下部にある <i class="fas fa-plus-circle"></i> プラスボタンを選択して**Send to Destination**を選択します。

### ステップ 2: 送信先を選択する {#step-2-choose-your-destination}

ドロップダウンを選択するか、**Destination**フィールドにCanvas名を入力します。次に、**Done**を選択します。

![「Feature Adoption」という名前のCanvasから「New Canvas」にユーザーを送信するように設定された送信先へ送信ステップ。]({% image_buster /assets/img/send_to_destination2.png %})

### ステップ 3: 送信先をプレビューする {#step-3-preview-your-destination}

**Preview destination**を選択すると、ユーザーの送信先Canvasをプレビューできます。

このCanvasステップを設定した後、[ユーザーパスをプレビュー]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths/)して、ユーザーが現在のCanvasの次のステップに進むかどうか、また送信先Canvasにも進むかどうかを確認できます。

## よくある質問 {#frequently-asked-questions}

### 送信先を下書きのCanvasに設定できますか？ {#can-i-set-the-destination-to-a-draft-canvas}

はい。送信先のCanvasは下書きまたはアイドルステータスにすることができます。

### コンテキスト変数は保持されますか？ {#are-context-variables-preserved}

はい。ソースCanvasの[コンテキスト]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)は常に送信先Canvasに渡されます。

### APIやユーザーの更新のワークアラウンドの代わりに、送信先へ送信ステップを使用してCanvasを接続できますか？ {#can-i-use-the-send-to-destination-step-to-connect-canvases-instead-of-using-api-or-user-update-workarounds}

はい。ユーザーを別のCanvasジャーニーに直接移動させる場合、送信先へ送信ステップでCanvasを接続できます。

ユーザーが送信先Canvasの条件を満たしている限り、Canvas間でユーザーを移動させるためだけに、別途ユーザーの更新ステップ、APIトリガー、またはwebhookを使用する必要はありません。

### ユーザーは送信先Canvasの最初から入りますか？ {#do-users-enter-at-the-start-of-the-destination-canvas}

資格のあるユーザーは、送信先Canvasの最初のステップにすぐにエントリします。送信先Canvasの次のスケジュールされたエントリ時間を待つことはありません。送信先Canvas内の特定のキャンバスステップにリンクすることはできません。

### 送信先へ送信ステップは、スケジュールされた送信先Canvasのエントリスケジュールを尊重しますか？ {#does-the-send-to-destination-step-respect-a-scheduled-destination-canvas-entry-schedule}

いいえ。送信先Canvasがスケジュールされたエントリタイプを使用している場合、送信先へ送信ステップから送信されたユーザーは、次のスケジュールされた評価時間枠を待ちません。ユーザーが送信先Canvasのエントリ条件とオーディエンス条件を満たしている場合、送信先へ送信ステップに到達した時点で評価され、エントリします。

### 送信先へ送信ステップの進行動作はどのように機能しますか？ {#how-does-advancement-behavior-work-for-send-to-destination-steps}

送信先へ送信ステップに入ったユーザーは、ソースCanvasに追加のステップがある場合、ユーザージャーニーを続行します。ユーザーが送信先Canvasのエントリルールも満たしている場合、そのCanvasに入り、そのジャーニーを開始できます。
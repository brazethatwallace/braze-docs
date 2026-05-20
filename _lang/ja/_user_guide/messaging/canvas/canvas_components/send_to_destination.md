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

> 送信先へ送信ステップを使用すると、あるCanvasから別のCanvasにユーザーを送信できます。例えば、プロモーションオファーのメッセージングを共有する2つのCanvasがある場合、送信先へ送信を使用してこれらのCanvasを接続できます。

## 仕組み {#how-it-works}

![新しいCanvasにユーザーを送信するための送信先へ送信ステップ。]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

送信先へ送信ステップを含む現在のCanvasがソースです。ステップ内で、送信先のCanvasを選択できます。ソースCanvasからの受信ユーザーは、送信先Canvasのエントリルールに従う必要があります。例えば、2つのCanvasがあるとします。

- **ソース:** Canvas 1、ユーザーをCanvas 2に送信する送信先へ送信ステップを含む
- **送信先:** Canvas 2、アイテムを注文したユーザーをエントリさせるエントリ条件を持つ

このステップにより、Canvas 1のユーザーをCanvas 2に送信できます。Canvas 1のユーザーが送信先へ送信ステップに入ると、Canvas 2のエントリルールによって評価され、Canvasに入る資格があるかどうかが判断されます。この場合、アイテムを注文したユーザーはCanvas 2に入ることができ、Canvas 1のジャーニーも引き続き進みます。アイテムを注文していないユーザーは、Canvas 1のジャーニーのみを続けます。

## 送信先へ送信ステップを作成する {#create-a-send-to-destination-step}

### ステップ 1: ステップを追加する {#step-1-add-a-step}

サイドバーから**Send to Destination**コンポーネントをドラッグ＆ドロップするか、ステップの下部にある <i class="fas fa-plus-circle"></i> プラスボタンを選択して**Send to Destination**を選択します。

### ステップ 2: 送信先を選択する {#step-2-choose-your-destination}

ドロップダウンを選択するか、**Destination**フィールドにCanvas名を入力します。次に、**Done**を選択します。

![「Feature Adoption」という名前のCanvasから「New Canvas」にユーザーを送信するように設定された送信先へ送信ステップ。]({% image_buster /assets/img/send_to_destination2.png %})

### ステップ 3: 送信先をプレビューする {#step-3-preview-your-destination}

**Preview destination**を選択すると、送信先Canvasのエントリ条件を満たすユーザーのジャーニーを確認できます。

このCanvasステップを設定した後、[ユーザーパスをプレビュー]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths/)して、ユーザーが現在のCanvasの次のステップに進むかどうか、また送信先Canvasにも進むかどうかを確認できます。

## よくある質問 {#frequently-asked-questions}

### 送信先を下書きのCanvasに設定できますか？ {#can-i-set-the-destination-to-a-draft-canvas}

はい。送信先のCanvasは下書きまたはアイドルステータスにすることができます。

### コンテキスト変数は保持されますか？ {#are-context-variables-preserved}

はい。ソースCanvasの[コンテキスト]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)は常に送信先Canvasに渡されます。

### ユーザーは送信先Canvasの最初から入りますか？ {#do-users-enter-at-the-start-of-the-destination-canvas}

ユーザーは送信先Canvasの最初から入ります。現時点では、送信先Canvas内の特定のキャンバスステップにリンクすることはできません。

### 送信先へ送信ステップの進行動作はどのように機能しますか？ {#how-does-advancement-behavior-work-for-send-to-destination-steps}

送信先へ送信ステップに入ったユーザーは、ソースCanvasに追加のステップがある場合、ユーザージャーニーを続行します。ユーザーが送信先Canvasのエントリルールも満たしている場合、そのCanvasに入り、そのジャーニーを開始できます。
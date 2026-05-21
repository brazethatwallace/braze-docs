---
nav_title: 送信先へ送信
article_title: 送信先へ送信
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "この参照記事では、送信先へ送信コンポーネントと、キャンバスでの使用方法について説明します。"
tool: Canvas
---

# 送信先へ送信ステップ {#send-to-destination-step}

> 送信先へ送信ステップを使用すると、あるキャンバスから別のキャンバスにユーザーを送信できます。例えば、プロモーションオファーのメッセージングを共有する2つのキャンバスがある場合、送信先へ送信を使用してこれらのキャンバスを接続できます。

## 仕組み {#how-it-works}

![新しいキャンバスにユーザーを送信するための送信先へ送信ステップ。]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

送信先へ送信ステップを含む現在のキャンバスがソースです。ステップ内で、送信先のキャンバスを選択できます。ソースキャンバスからの受信ユーザーは、送信先キャンバスのエントリルールに従う必要があります。例えば、2つのキャンバスがあるとします。

- **ソース:** キャンバス 1、ユーザーをキャンバス 2に送信する送信先へ送信ステップを含む
- **送信先:** キャンバス 2、アイテムを注文したユーザーをエントリさせるエントリ条件を持つ

このステップにより、キャンバス 1のユーザーをキャンバス 2に送信できます。キャンバス 1のユーザーが送信先へ送信ステップに入ると、キャンバス 2のエントリルールによって評価され、キャンバスに入る資格があるかどうかが判断されます。この場合、アイテムを注文したユーザーはキャンバス 2に入ることができ、キャンバス 1のジャーニーも引き続き進みます。アイテムを注文していないユーザーは、キャンバス 1のジャーニーのみを続けます。

## 送信先へ送信ステップを作成する {#create-a-send-to-destination-step}

### ステップ 1: ステップを追加する {#step-1-add-a-step}

サイドバーから**Send to Destination**コンポーネントをドラッグ＆ドロップするか、ステップの下部にある <i class="fas fa-plus-circle"></i> プラスボタンを選択して**Send to Destination**を選択します。

### ステップ 2: 送信先を選択する {#step-2-choose-your-destination}

ドロップダウンを選択するか、**Destination**フィールドにキャンバス名を入力します。次に、**Done**を選択します。

![「Feature Adoption」という名前のキャンバスから「New キャンバス」にユーザーを送信するように設定された送信先へ送信ステップ。]({% image_buster /assets/img/send_to_destination2.png %})

### ステップ 3: 送信先をプレビューする {#step-3-preview-your-destination}

**Preview destination**を選択すると、送信先キャンバスのエントリ条件を満たすユーザーのジャーニーを確認できます。

このキャンバスステップを設定した後、[ユーザーパスをプレビュー]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths/)して、ユーザーが現在のキャンバスの次のステップに進むかどうか、また送信先キャンバスにも進むかどうかを確認できます。

## よくある質問 {#frequently-asked-questions}

### 送信先を下書きのキャンバスに設定できますか？ {#can-i-set-the-destination-to-a-draft-canvas}

はい。送信先のキャンバスは下書きまたはアイドルステータスにすることができます。

### コンテキスト変数は保持されますか？ {#are-context-variables-preserved}

はい。ソースキャンバスの[コンテキスト]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)は常に送信先キャンバスに渡されます。

### ユーザーは送信先キャンバスの最初から入りますか？ {#do-users-enter-at-the-start-of-the-destination-canvas}

ユーザーは送信先キャンバスの最初から入ります。現時点では、送信先キャンバス内の特定のキャンバスステップにリンクすることはできません。

### 送信先へ送信ステップの進行動作はどのように機能しますか？ {#how-does-advancement-behavior-work-for-send-to-destination-steps}

送信先へ送信ステップに入ったユーザーは、ソースキャンバスに追加のステップがある場合、ユーザージャーニーを続行します。ユーザーが送信先キャンバスのエントリルールも満たしている場合、そのキャンバスに入り、そのジャーニーを開始できます。
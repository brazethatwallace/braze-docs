---
nav_title: キャンバステンプレート
article_title: キャンバステンプレートの作成
page_order: 2
alias: "/canvas_templates/"
description: "再利用可能なキャンバステンプレートを作成・管理したり、一般的なユースケース向けのBraze組み込みテンプレートを活用して始めましょう。"
---

# キャンバステンプレートの作成 {#create-a-canvas-template}

> このリファレンス記事では、Canvasのテンプレートを作成・管理する方法について説明します。テンプレートを使用すると、一貫したフレームワークを作成してメッセージングを洗練させることができ、Canvasesごとの特定の目標に合わせて簡単にカスタマイズできます。

{% alert tip %}
[Brazeキャンバステンプレート](#available-braze-templates)を使用して、Canvas作成の時間を節約し、効率化しましょう！組み込みテンプレートのライブラリーを参照して、ユースケースに合ったものを見つけ、特定のニーズに合わせてカスタマイズしてください。
{% endalert %}

## 方法1: 既存のCanvasから作成する {#method-1-create-from-an-existing-canvas}

### ステップ1: 既存のCanvasを選択する {#step-1-select-your-existing-canvas}

Brazeダッシュボードで、**Messaging** > **Canvas**に移動し、テンプレートとして使用したい既存のCanvasを選択します。

### ステップ2: テンプレートを作成する {#step-2-create-your-template}

Canvasエディターで、Canvasがアクティブか下書きかに応じて、**Edit Canvas**または**Edit draft**を選択します。フッターの**Save as draft**ドロップダウンを展開し、**Save as template**を選択します。

![]({% image_buster /assets/img/save_canvas_as_template.png %})

### ステップ3: テンプレートを保存する {#step-3-save-your-template}

次に、テンプレートに名前を付け、関連するタグを追加します。その後、**Save**を選択します。これでテンプレートはCanvas作成に使用できる状態になり、基本設定とステップがすでに設定された状態で始めることができます。

## 方法2: キャンバステンプレートエディターから作成する {#method-2-create-via-canvas-template-editor}

### ステップ1: キャンバステンプレートエディターに移動する {#step-1-go-to-the-canvas-template-editor}

Brazeダッシュボードで、**Content** > **Canvas**に移動します。

### ステップ2: 新しいテンプレートを作成する {#step-2-create-a-new-template}

**Create template**を選択し、Canvasの詳細を設定します。まず、キャンバステンプレートに名前を付けることから始めましょう。

![「Annual sale キャンバステンプレート」という名前のキャンバステンプレートの例。説明には「年間スプリングプロモーションに使用」と記載されています。]({% image_buster /assets/img/canvas_template_example.png %})

### ステップ3: テンプレートをカスタマイズする {#step-3-customize-your-template}

次に、[Canvasを設定]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-2-build-your-canvas)してテンプレートをカスタマイズします。ユーザーがCanvasに入るタイミングの決定、このCanvasに入れるユーザーの指定、送信設定の調整、テンプレートのユーザージャーニーの構築を行うことができます。

### ステップ4: テンプレートを保存する {#step-4-save-your-template}

テンプレートのカスタマイズが完了したら、**Save template**ボタンを選択します。**Canvas template**ページで、<i class="fas fa-list"></i> **Template details**を選択すると、キャンバステンプレートの詳細を確認できます。

## キャンバステンプレートの使用 {#using-canvas-templates}

Canvasを作成する際にテンプレートを使用する方法は2つあります。

- **Messagingから**: **Messaging** > **Canvas**に移動します。**Create Canvas**ボタンを選択し、**Use a Canvas Template**を選択します。
- **Contentから**: **Content** > **Canvas**に移動し、**Canvas templates**で目的のテンプレートを見つけます。次に、<i class="fas fa-ellipsis-vertical"></i> メニューから**Apply template**を選択します。これにより、Canvasコンポーザーでテンプレートが適用された新しいCanvasが表示されます。

### 利用可能なBrazeテンプレート {#available-braze-templates}

利用可能なキャンバステンプレートの一覧については、[Brazeキャンバステンプレート]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/)を参照してください。eコマースキャンバステンプレートの使用方法については、[eコマース推奨イベントの使い方]({{site.baseurl}}/ecommerce_use_cases/)を参照してください。

## キャンバステンプレートの管理 {#managing-canvas-templates}

キャンバステンプレートは、実際のCanvasと同様に複製やアーカイブが可能です。キャンバステンプレートを編集するには、テンプレートを選択してから**<i class="fas fa-pencil-alt"></i>Edit**を選択します。

ワークスペースレベルでは、ユーザー権限を更新して、キャンバステンプレートの作成、編集、表示、アーカイブへのアクセスを許可または制限できます。

### チームとワークスペースの権限 {#permissions-for-teams-and-workspaces}

特定のユーザーのみが特定のキャンバステンプレートにアクセスして使用できるようにするには、テンプレートに[チームを追加]({{site.baseurl}}/user_guide/administer/global/user_management/teams/)し、チームレベルの「Access Campaigns, Canvases, Content Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Center」権限を割り当てます。

以下の権限をチームレベルで割り当て、ワークスペースレベルでは割り当てない場合、自分のチームに割り当てられた範囲でのみ以下の操作が可能です。

- キャンバステンプレートの作成と編集
- キャンバステンプレートの表示
- キャンバステンプレートのアーカイブ

権限がワークスペースレベルとチームレベルの両方で付与されている場合、ワークスペースレベルの権限が優先されます。

## よくある質問 {#frequently-asked-questions}

### キャンバステンプレートに不完全なステップを保存できますか？ {#can-i-save-an-incomplete-step-in-a-canvas-template}

はい、不完全なステップをキャンバステンプレートとして保存できます。ただし、テンプレートを使用する際、**Save template**ボタンにCanvasを起動するために必要な項目を示すエラーが表示されます。

### Canvasビルダーの設定をテンプレートとして保存できますか？それともステップのみ保存可能ですか？ {#can-i-save-my-canvas-builder-settings-as-a-template-or-can-i-only-save-steps}

はい、キャンバステンプレート内でCanvasビルダーの設定を保存できます。たとえば、Segmentsとフィルターの組み合わせを頻繁に使用する場合、これらの**ターゲットオーディエンス**設定をキャンバステンプレートの一部として保存できます。
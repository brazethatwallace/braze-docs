---
nav_title: ダッシュボード
article_title: Brazeダッシュボード
page_order: 1
page_type: reference
description: "Brazeダッシュボードは、カスタマーエンゲージメントの構築、管理、分析を行うための中心的なワークスペースです。メッセージングツール、オーディエンスインサイト、セグメンテーション、リアルタイムのパフォーマンスデータを一か所にまとめて提供します。"

---

# Brazeダッシュボード {#the-braze-dashboard}

> Brazeダッシュボードは、カスタマーエンゲージメントの構築、管理、分析を行うための中心的なワークスペースです。[dashboard.braze.com](https://dashboard.braze.com/) または [dashboard.braze.eu](https://dashboard.braze.eu/) からアクセスできます。

Brazeダッシュボードを使用して、キャンペーンの計画、メッセージの起動と管理、オーディエンスインサイトの探索、セグメンテーションの調整、リアルタイムのパフォーマンスおよびエンゲージメント指標の確認を、単一のインターフェイスから行うことができます。

## ダッシュボードの概要 {#dashboard-overview}

ログインすると、ダッシュボードにエンゲージメントツールとデータの一元的なビューが表示されます。

- **ホームページ:** [最近編集したコンテンツ](#pick-up-where-you-left-off)と主要なパフォーマンス指標を一目で確認できます
- **左側のナビゲーション:** ツールを機能別に整理します（メッセージング、オーディエンス、分析、設定）
- **グローバルヘッダー:** 検索、サポート、言語設定、通知、アカウントにすばやくアクセスできます

ダッシュボードの操作は[ワークスペース]({{site.baseurl}}/user_guide/get_started/workspaces/)ごとに整理されており、異なるブランド、地域、チームのコンテンツを管理するのに役立ちます。サイドナビゲーションからいつでも[ワークスペースを切り替える](#workspace-switcher)ことができます。

## ダッシュボードにアクセスする {#access-your-dashboard}

開始するには、[Brazeアカウントにサインイン]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account/)してください。ダッシュボード内のページへのアクセスや特定のアクションを実行する権限は、割り当てられた[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions)に基づいています。権限についてサポートが必要な場合は、Braze管理者にお問い合わせください。

## Brazeをナビゲートする {#navigate-braze}

Brazeのナビゲーションは、デバイスを問わず機能やコンテンツに効率的にアクセスできるように設計されています。Brazeダッシュボードには、グローバルヘッダーとサイドナビゲーションの2つのレベルのナビゲーションがあります。

グローバルヘッダーは、ほぼ常に画面上部に表示されます。以下を含む重要なツールや設定にすばやくアクセスできます。

- [検索](#search-your-dashboard)
- サポートおよびコミュニティリンク
- [ダッシュボードの言語]({{site.baseurl}}/user_guide/administer/personal/language_settings/)
- 通知
- アカウント設定
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/)

### サイドナビゲーションを使用する {#use-the-side-navigation}

左側の縦型メニューは、Brazeのツールを機能別に整理し、よく使う項目をすぐに利用できるようにします。メインメニュー項目を選択すると、そのオプションが縦型のスタックレイアウトで表示されます。

![Brazeダッシュボードのワークスペース切り替え]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### ワークスペース切り替え {#workspace-switcher}

サイドナビゲーションの上部にあるワークスペース切り替えを使用すると、Brazeインスタンス内の異なるワークスペース間を移動できます。アクティブなワークスペースがハイライト表示されます。

[ワークスペース]({{site.baseurl}}/user_guide/get_started/workspaces/)は、ブランド、地域、製品ライン、チームごとにコンテンツを整理するのに役立ちます。各ワークスペースには独自のデータ、キャンペーン、設定が含まれます。ワークスペースによってアクセス権が異なる場合があります。たとえば、あるワークスペースでは編集アクセス権があり、別のワークスペースでは閲覧のみのアクセス権がある場合があります。

ワークスペースを切り替えるには、サイドナビゲーションの上部にあるワークスペースドロップダウンを選択し、アクセスしたいワークスペースを選択します。また、よく使うワークスペースにすばやくアクセスするために、[お気に入りのワークスペースを追加](#favorite-workspaces)することもできます。

#### サイドナビゲーションを最小化する {#minimize-the-side-navigation}

キャンバスのデザインなどのタスク中に視覚的な煩雑さを減らすために、サイドナビゲーションパネルを最小化できます。**Minimize menu**を押して折りたたみます。最小化した状態でも、アイコンにカーソルを合わせるとメニュー項目名のツールチップが表示されます。これにより、ワークスペースをすっきり保ちながら、ツール間をすばやく移動できます。

![メニューの最小化と最大化のアイコン]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### レスポンシブナビゲーション {#responsive-navigation}

ナビゲーションは、さまざまな画面サイズにシームレスに適応します。小さな画面では、サイドナビゲーションが自動的に折りたたまれます。必要に応じて<i class="fa-solid fa-bars" aria-label="ナビゲーションメニューを開く"></i>を押してメニューを開きます。

![小さな画面では、サイドナビゲーションが自動的に折りたたまれます。メニューアイコンをタップするとナビゲーションオプションが開きます。]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## ダッシュボードを検索する {#search-your-dashboard}

ヘッダーにあるグローバル検索バーは、Brazeダッシュボード全体でコンテンツを見つける最も速い方法です。選択して検索インターフェイスを開き、必要なものに直接ジャンプします。

![検索語が入力されていない状態のグローバル検索。最近開いたページが表示されています。]({% image_buster /assets/img/navigation/search_recently_opened.png %})

最近開いたコンテンツが検索バーの下に表示されます。これには、最近操作したキャンペーン、キャンバス、テンプレート、ページが含まれ、作業に簡単に戻ることができます。

### 何を検索できますか？ {#what-can-you-search-for}

以下の項目やアクションを検索できます。

- キャンペーン名
- キャンバス名
- Content Blocks
- セグメント名
- メールテンプレート名
- Braze内のページ（同義語を含む）

{% alert tip %}
正確なテキストを検索するには、検索語を引用符で囲みます（""）。たとえば、["all users"] を検索すると、名前に「all users」という正確なフレーズを含むすべての項目が返されます。
{% endalert %}

### コンテンツタイプとステータスタグ {#content-type-and-status-tags}

各結果には、コンテンツタイプ（キャンペーン、キャンバス、セグメントなど）とステータス（アクティブ、アーカイブ、停止）を示すタグが付けられます。

### アクティブおよび下書きコンテンツでフィルタリングする {#filter-for-active-and-draft-content}

デフォルトでは、検索にはアクティブ、下書き、アーカイブされた項目が含まれます。**Show active and draft only**トグルを使用して、結果を絞り込みます。

![「Show active and draft only」トグル。]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### キーボードショートカット {#keyboard-shortcuts}

キーボードを使用して検索結果を移動できます。

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| アクション | キーボードショートカット |
| --------------------------- | ----------------------------------------------------------------------------- |
| 検索メニューを開く | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> </ul> {:/}  |
| 検索結果間を移動する | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| 検索結果を選択する | <kbd>Enter</kbd>    |
| 検索メニューを閉じる | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="キーボードショートカット" }

## 生産性機能 {#productivity-features}

Brazeダッシュボードには、より効率的に作業し、よく使うツールやコンテンツにすばやくアクセスするための機能がいくつか含まれています。

### BrazeAI Operator

BrazeAI Operator™は、ダッシュボードに組み込まれたAI搭載のアシスタントです。回答の取得、セットアップの手順確認、問題のトラブルシューティング、アイデアのブレインストーミングに使用できます。プロファイルの横にあるグローバルヘッダーの**BrazeAI Operator™**から開きます。詳細については、[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/)を参照してください。

### 前回の続きから再開する {#pick-up-where-you-left-off}

**Home**ページでは、最近編集または作成したキャンペーン、キャンバス、セグメントがダッシュボードに表示されます。これにより、検索せずに進行中の作業に簡単に戻ることができます。各項目には、コンテンツタイプとステータス（下書き、アクティブ、停止など）を示すタグが含まれます。

![「前回の続きから再開する」セクションに表示されたキャンバスの下書き、アクティブなセグメント、キャンペーンの下書き。]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

詳細については、[ホームダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboards/home/#pick-up-where-you-left-off)を参照してください。

### お気に入りのワークスペース {#favorite-workspaces}

複数のワークスペースで作業する場合、よく使うワークスペースをお気に入りとしてマークできます。お気に入りのワークスペースは、ワークスペース切り替えの上部に表示され、すばやくアクセスできます。

お気に入りのワークスペースを追加するには：

1. [プロファイル設定にアクセスします](#access-your-profile-settings)。
2. **Account Profile**セクションで、**Favorite workspaces**フィールドを見つけます。
3. お気に入りにしたいワークスペースを選択します。

### プロファイル設定にアクセスする {#access-your-profile-settings}

アカウント設定、通知設定、個人情報を管理するには：

1. グローバルヘッダーでプロファイルアイコンを選択します。
2. **Manage your account**を選択して、プロファイルページにアクセスします。

プロファイルページから、メール設定の更新、2要素認証の設定、APIキーの表示、その他のアカウント詳細の管理を行うことができます。

## ダッシュボードのアクセシビリティ {#accessibility-in-the-dashboard}

Brazeダッシュボードは、色のコントラストに関するWCAG AA基準を満たすブランドカラーを使用しています。これにより、すべてのユーザーにとってインクルーシブな体験をサポートし、アクセシビリティのベストプラクティスに沿っています。

## フィードバックの共有 {#sharing-feedback}

ご意見をお聞かせください。ナビゲーション、アクセシビリティ、ユーザビリティ、ビジュアルデザインなどに関するフィードバックを共有できます。グローバルヘッダーの**Support**メニューを開き、**Share feedback**を選択してください。すべてのフィードバックを確認し、Brazeの体験改善に役立てています。

## 関連リソース {#related-resources}

### 管理タスク {#administrative-tasks}

- [ワークスペースの作成と管理]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/)
- [Brazeユーザーの管理]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/)
- [ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)
- [チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams/)

### 主要なタスクと次のステップ {#key-tasks-and-next-steps}

- **キャンペーンを構築する**: [キャンペーンを作成する]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/)
- **ジャーニーを作成する**: [キャンバスを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)
- **オーディエンスを定義する**: [セグメントを作成する]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/)
- **パフォーマンスを確認する**: [分析の概要]({{site.baseurl}}/user_guide/analytics/dashboards/home/)
- **設定を構成する**: [アプリ設定]({{site.baseurl}}/user_guide/administer/global/workspace_settings/)
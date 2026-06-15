---
nav_title: Snapchat
article_title: キャンバスオーディエンスのSnapchatへの同期
description: "このリファレンス記事では、BrazeオーディエンスのSnapchatへの同期を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 6
alias: "/audience_sync_snapchat/"

tool:
  - キャンバス

---

# オーディエンスのSnapchatへの同期 {#audience-sync-to-snapchat}

BrazeオーディエンスのSnapchatへの同期を使用することで、ブランドはBraze統合からのユーザーデータをSnapchatの顧客リストに追加し、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいてBraze キャンバスでメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために通常使用する基準を、Snapchat顧客リスト内の該当ユーザーに対して広告をトリガーするためにも使用できるようになりました。

**オーディエンス同期の一般的なユースケースは次のとおりです。**

- 複数のチャネルを通じて価値の高いユーザーをターゲットにして、購入やエンゲージメントを促進する
- 他のマーケティングチャネルに対して反応が薄いユーザーをリターゲティングする
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する
- 新規ユーザーをより効率的に獲得するための類似オーディエンスを作成する

この機能により、ユーザーは特定のファーストパーティデータがSnapchatと共有されるかどうかをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro免責条項**<br>
BrazeオーディエンスのSnapchatへの同期はAudience Sync Pro統合です。この統合の詳細については、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

キャンバスでSnapchatオーディエンスステップを設定する前に、以下の項目が作成、完了、または承諾されていることを確認する必要があります。

| 要件 | 提供元 | 説明 |
| --- | --- | --- |
| Snapchatビジネスマネージャー | Snapchat | ブランドのSnapchatアセット（広告アカウント、ページ、アプリなど）を管理するための集中化されたツールです。 |
| Snapchat広告アカウント | Snapchat | ブランドのSnapchatビジネスマネージャーに紐づけられたアクティブなSnapchat広告アカウント。<br><br>Snapchatビジネスマネージャーの管理者が、Brazeで使用する予定のSnapchat広告アカウントに対する管理者権限を付与していることを確認してください。 |
| Snapchat利用規約とポリシー | [Snapchat](https://www.snap.com/en-US/policies) | Snapchat Audience Syncの使用に関連するSnapchatのすべての必須条件、ポリシー、ガイドライン、ドキュメントを遵守することに同意するものとします。これには、引用により組み込まれるすべての条件、ポリシー、ガイドライン、およびドキュメント（利用規約、ビジネス利用規約、開発者規約、オーディエンスマッチ、広告ポリシー、商用コンテンツポリシー、コミュニティガイドライン、サプライヤー責任などを含む）が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合 {#integration}

### ステップ1:Snapchatに接続する {#step-1-connect-to-snapchat}

{% alert important %}
BrazeアカウントにSnapchatを接続するには[「管理者」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)が必要です。
{% endalert %}

Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Snapchat**を選択します。Snapchat Audience Syncで、**Connect Snapchat**を選択します。

![BrazeのSnapchatテクノロジーページ。「概要」セクションと「Snapchat Audience Sync」セクション、および「Connect Snapchat」ボタンが表示されている。]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

次に、Snapchat OAuthページにリダイレクトされ、Audience Sync統合に関連する権限をBrazeに承認します。

確認を選択すると、Brazeに戻り、同期するSnapchat広告アカウントを選択します。

![Snapchatに接続できる利用可能な広告アカウントのリスト。]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

接続に成功すると、パートナーページに戻ります。このページでは、接続されているアカウントを表示したり、既存のアカウントを切断したりできます。

![広告アカウントが正常に接続されたことを示す更新後のSnapchatテクノロジーパートナーページ。]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Snapchat接続はBrazeワークスペースレベルで適用されます。Snapchatの管理者がSnapchat Business Managerまたは接続されたSnapchat広告アカウントへのアクセスからあなたを削除した場合、Brazeは無効なトークンを検出します。その結果、Snapchatを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2:Snapchatでオーディエンス同期ステップを追加する {#step-2-add-an-audience-sync-step-with-snapchat}

キャンバスにコンポーネントを追加し、**Audience Sync**を選択します。

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### ステップ3:同期のセットアップ {#step-3-sync-setup}

**Custom Audience**ボタンをクリックしてコンポーネントエディターを開きます。

希望するAudience Syncパートナーとして**Snapchat**を選択します。

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

次に、希望するSnapchat広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンスの名前を入力します。

{% tabs %}
{% tab 新規オーディエンスの作成 %}

**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択し、Snapchatと同期したいフィールドを選択します。次に、ステップエディターの下部にある**Create Audience**ボタンをクリックして、オーディエンスを保存します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここで、目的の広告アカウントを選択し、新しいオーディエンスが作成される。]({% image_buster /assets/img/audience_sync/snapchat3.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。ユーザーは、オーディエンスが下書きモードで作成されたため、後でキャンバスジャーニーでユーザーの削除のためにこのオーディエンスを参照できます。

![キャンバスコンポーネントで新しいオーディエンスが作成された後に表示されるアラート。]({% image_buster /assets/img/audience_sync/snapchat2.png %})

新しいオーディエンスを使用してキャンバスを起動すると、オーディエンス同期コンポーネントに入る時点で、Brazeはユーザーをほぼリアルタイムで同期します。

{% endtab %}
{% tab 既存のオーディエンスとの同期 %}
**既存のオーディエンスとの同期**<br>
Brazeは、これらのオーディエンスが最新であることを確認するために、既存のSnapchatオーディエンスにユーザーを追加する機能も提供しています。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンスの名前を入力し、**Add to the Audience**を選択します。Brazeは、オーディエンス同期コンポーネントに入ると、ほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここで、希望する広告アカウントと既存のオーディエンスが選択される。]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### ステップ4:キャンバスを起動する {#step-4-launch-canvas}

オーディエンス同期をSnapchatに設定したら、キャンバスを起動しましょう！新しいオーディエンスが作成され、オーディエンス同期ステップを通過するユーザーはSnapchatのこのオーディエンスに送られます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Snapchatでオーディエンスを表示するには、広告マネージャーアカウントにログインし、ナビゲーションのアセットセクションから**Audiences**を選択します。**Audiences**ページで、各オーディエンスが約1,000に達した後のサイズを確認できます。

![オーディエンスの名前、オーディエンスの種類、オーディエンスのサイズ、オーディエンスのリテンション（日単位）を含む、指定されたSnapchatオーディエンスのオーディエンス詳細。]({% image_buster /assets/img/snapchat/snapchat7.png %})

## ユーザーの同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期ステップに達すると、BrazeはSnapchatのAPIレート制限を尊重しながら、ほぼリアルタイムで同期を行います。Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理してからSnapchatに送信します。

SnapchatのAPIレート制限では、1秒あたり10クエリ、1リクエストあたり100,000ユーザーを超えてはなりません。顧客がこの制限に達した場合、Brazeは最大約13時間まで同期を再試行します。それでも同期できない場合、BrazeはこれらのユーザーをUsers Errored指標の下にリストアップします。

### 分析の理解 {#understanding-analytics}

次の表に、オーディエンス同期コンポーネントからの分析をよりよく理解するのに役立つ指標と説明を示します。

| 指標 | 説明 |
| --- | --- |
| 入力済み | Snapchatと同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進んだ | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数。キャンバスブランチの最後のステップである場合、すべてのユーザーは自動的に進みます。 |
| 同期済みユーザー | Snapchatに正常に同期されたユーザーの数。 |
| 未同期ユーザー | 一致するフィールドが不足しているため、同期されなかったユーザーの数。 |
| 保留中のユーザー | BrazeがSnapchatへの同期のために現在処理しているユーザーの数。 |
| エラーが発生したユーザー | APIエラーのため、約13時間のリトライ後にSnapchatに同期されなかったユーザーの数。エラーの潜在的な原因には、無効なSnapchatトークンや、Snapchatでオーディエンスが削除された場合が含まれます。 |
キャンバスを終了済み | キャンバスを終了したユーザーの数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
一括フラッシャーと13時間の再試行のため、同期済みユーザーとエラーが発生したユーザーの指標のレポートに遅延が発生することに注意してください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### Snapchatでサポート可能なオーディエンス数はいくつですか {#how-many-audiences-can-snapchat-support}

現時点では、Snapchatアカウントに含めることができるオーディエンスの数は1,000です。

この制限を超えると、Brazeは新しいオーディエンスを作成できないことを通知します。Snapchat広告アカウントで使用を終了したオーディエンスを削除する必要があります。

### ユーザーをSnapchatに渡した後、ユーザーがマッチしたかどうかを知るにはどうすればよいですか {#how-do-i-know-if-users-have-matched-after-passing-users-to-snapchat}

Snapchatは、データプライバシーポリシーに基づきこの情報を提供していません。

### 無効なトークンエラーが表示された場合、次に何をすればよいですか {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

SnapchatパートナーページでSnapchatアカウントを切断して再接続できます。同期する広告アカウントに対する適切な権限があることをSnapchat Business Manager管理者に確認してください。

### キャンバスを起動できないのはなぜですか {#why-is-my-canvas-not-allowed-to-launch}

SnapchatパートナーページでSnapchat広告アカウントがBrazeに正常に接続されていることを確認してください。広告アカウントを選択し、新しいオーディエンスの名前を入力し、一致させるフィールドを選択していることを確認してください。
---
nav_title: Snapchat
article_title: キャンバスオーディエンスのSnapchatへの同期
description: "このリファレンス記事では、BrazeオーディエンスのSnapchatへの同期を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 6
alias: "/audience_sync_snapchat/"

tool:
  - Canvas

---

# オーディエンスのSnapchatへの同期 {#audience-sync-to-snapchat}

BrazeオーディエンスのSnapchatへの同期を使用することで、ブランドはBraze統合からのユーザーデータをSnapchatの顧客リストに追加し、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいてBrazeキャンバスでメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために通常使用する基準を、Snapchat顧客リスト内の該当ユーザーに対して広告をトリガーするためにも使用できるようになりました。

**オーディエンス同期の一般的なユースケースは次のとおりです。**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

この機能により、ユーザーは特定のファーストパーティデータがSnapchatと共有されるかどうかをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Proに関する免責事項**<br>
BrazeオーディエンスのSnapchatへの同期はAudience Sync Pro統合です。この統合の詳細については、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

キャンバスでSnapchatオーディエンスステップを設定する前に、以下の項目が作成、完了、または承認されていることを確認する必要があります。

| 要件 | Origin | 説明 |
| --- | --- | --- |
| Snapchat Business Manager | Snapchat | ブランドのSnapchatアセット（広告アカウント、ページ、アプリなど）を管理するための一元的なツールです。 |
| Snapchat広告アカウント | Snapchat | ブランドのSnapchat Business Managerに紐づけられたアクティブなSnapchat広告アカウント。<br><br>Snapchat Business Managerの管理者が、Brazeで使用する予定のSnapchat広告アカウントに対する管理者権限を付与していることを確認してください。 |
| Snapchatの利用規約とポリシー | [Snapchat](https://www.snap.com/en-US/policies) | Snapchat Audience Syncの使用に関連するSnapchatの必須の利用規約、ポリシー、ガイドライン、およびドキュメント（参照により組み込まれるものを含む）に準拠することに同意してください。これには、利用規約、ビジネス利用規約、開発者規約、Audience Match、広告ポリシー、商用コンテンツポリシー、コミュニティガイドライン、およびサプライヤー責任が含まれる場合があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：Snapchatに接続する {#step-1-connect-to-snapchat}

{% alert important %}
SnapchatをBrazeアカウントに接続するには、[「管理者」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)が必要です。
{% endalert %}

Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Snapchat**を選択します。Snapchat Audience Syncの下で、**Connect Snapchat**を選択します。

![BrazeのSnapchatテクノロジーページ。概要セクションとSnapchat Audience Syncセクションが表示され、Connected Snapchatボタンがあります。]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

その後、SnapchatのOAuthページにリダイレクトされ、Audience Sync連携に関連する権限をBrazeに付与します。

確認を選択すると、Brazeに戻り、同期したいSnapchat広告アカウントを選択できます。

![Snapchatに接続できる利用可能な広告アカウントの一覧。]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

接続が完了すると、パートナーページに戻り、接続されているアカウントの確認や既存アカウントの切断ができます。

![更新されたSnapchatテクノロジーパートナーページ。広告アカウントが正常に接続されていることが表示されています。]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Snapchat接続はBrazeワークスペースレベルで適用されます。Snapchat管理者がSnapchat Business Managerからあなたを削除したり、接続されたSnapchat広告アカウントへのアクセスを取り消した場合、Brazeは無効なトークンを検出します。その結果、Snapchatを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2：SnapchatのAudience Syncステップを追加する {#step-2-add-an-audience-sync-step-with-snapchat}

キャンバスにコンポーネントを追加し、**Audience Sync**を選択します。

![Audience Syncコンポーネントオプションが表示されたキャンバスステップセレクター。]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![キャンバスパスに追加されたAudience Syncコンポーネントカード。]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### ステップ3：同期の設定 {#step-3-sync-setup}

**Custom Audience**ボタンをクリックして、コンポーネントエディターを開きます。

Audience Syncパートナーとして**Snapchat**を選択します。

![Snapchatが同期パートナーとして選択されたAudience Syncコンポーネントエディター。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

次に、目的のSnapchat広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンス名を入力します。

{% tabs %}
{% tab 新規オーディエンスを作成 %}

**新規オーディエンスを作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択して、Snapchatと同期するフィールドを選択します。次に、ステップエディターの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存します。

![カスタムオーディエンスキャンバスステップの展開ビュー。目的の広告アカウントが選択され、新しいオーディエンスが作成されています。]({% image_buster /assets/img/audience_sync/snapchat3.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。オーディエンスは下書きモードで作成されるため、キャンバスジャーニーの後のステップでユーザー削除のためにこのオーディエンスを参照できます。

![キャンバスコンポーネントで新しいオーディエンスが作成された後に表示されるアラート。]({% image_buster /assets/img/audience_sync/snapchat2.png %})

新しいオーディエンスでキャンバスを起動すると、ユーザーがAudience Syncコンポーネントに入るとほぼリアルタイムでBrazeがユーザーを同期します。

{% endtab %}
{% tab 既存のオーディエンスと同期 %}
**既存のオーディエンスと同期**<br>
Brazeでは、既存のSnapchatオーディエンスにユーザーを追加して、オーディエンスを最新の状態に保つこともできます。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**Add to the Audience**を選択します。Brazeは、ユーザーがAudience Syncコンポーネントに入るとほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンスキャンバスステップの展開ビュー。目的の広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### ステップ4：キャンバスを起動する {#step-4-launch-canvas}

Snapchatへの Audience Syncを設定したら、キャンバスを起動します。新しいオーディエンスが作成され、Audience Syncステップを通過するユーザーはSnapchat上のこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Snapchatでオーディエンスを確認するには、広告マネージャーアカウントにアクセスし、ナビゲーションのAssetsセクションから**Audiences**を選択します。**Audiences**ページで、各オーディエンスのサイズが約1,000に達した後に確認できます。

![特定のSnapchatオーディエンスのオーディエンス詳細。オーディエンス名、オーディエンスタイプ、オーディエンスサイズ、オーディエンスリテンション日数が表示されています。]({% image_buster /assets/img/snapchat/snapchat7.png %})

## ユーザー同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期ステップに到達すると、BrazeはSnapchatのAPIレート制限を遵守しながら、ほぼリアルタイムでユーザーを同期します。Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理し、Snapchatに送信します。

SnapchatのAPIレート制限では、1秒あたり10クエリ、1リクエストあたり100,000ユーザーまでに制限されています。顧客がこの制限に達した場合、Brazeは最大約13時間にわたって同期をリトライします。それでも同期できない場合、Brazeはそのユーザーをエラーユーザー指標に記録します。

### 分析について {#understanding-analytics}

以下の表には、オーディエンス同期コンポーネントの分析をより深く理解するための指標と説明が含まれています。

| 指標 | 説明 |
| --- | --- |
| エントリー済み | Snapchatに同期するためにこのコンポーネントに入ったユーザーの数です。 |
| 次のステップに進んだ | 次のコンポーネントがある場合、何人のユーザーが次のコンポーネントに進みましたか？キャンバスブランチの最後のステップである場合、すべてのユーザーが自動的に進みます。 |
| 同期済みユーザー | Snapchatへの同期に成功したユーザーの数です。 |
| 未同期ユーザー | マッチに必要なフィールドが不足しているため、同期されなかったユーザーの数です。 |
| 保留中のユーザー | 現在BrazeがSnapchatへの同期を処理中のユーザーの数です。 |
| エラーユーザー | 約13時間のリトライ後にAPIエラーによりSnapchatに同期されなかったユーザーの数です。エラーの原因としては、無効なSnapchatトークンや、Snapchat上でオーディエンスが削除された場合などが考えられます。 |
| キャンバス退出 | キャンバスを退出したユーザーの数です。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析について" }

{% alert important %}
同期済みユーザーとエラー指標のレポートには、それぞれ一括フラッシャーと13時間のリトライにより遅延が発生することにご注意ください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### Snapchatではいくつのオーディエンスをサポートできますか？ {#how-many-audiences-can-snapchat-support}

現時点では、Snapchatアカウント内で保持できるオーディエンスは1,000件までです。

この上限を超えた場合、Brazeは新しいオーディエンスを作成できないことを通知します。Snapchat広告アカウントで使用していないオーディエンスを削除する必要があります。

### ユーザーをSnapchatに渡した後、ユーザーがマッチしたかどうかはどうすればわかりますか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-snapchat}

Snapchatはデータプライバシーポリシーにより、この情報を提供していません。

### 無効なトークンエラーが表示された場合はどうすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Snapchatパートナーページで、Snapchatアカウントを切断してから再接続できます。同期したい広告アカウントに対する適切な権限があることを、Snapchat Business Managerの管理者に確認してください。

### キャンバスが起動できないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

SnapchatパートナーページでSnapchat広告アカウントがBrazeに正常に接続されていることを確認してください。広告アカウントを選択し、新しいオーディエンスの名前を入力し、マッチするフィールドを選択していることを確認してください。
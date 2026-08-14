---
nav_title: Criteo
article_title: キャンバスのオーディエンスをCriteoに同期する
description: "このリファレンス記事では、Braze Audience Sync to Criteoを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 1
alias: /audience_sync_criteo/

tool:
  - Canvas
---

# Audience Sync to Criteo

Braze Audience Sync to Criteoを使用すると、ブランドは独自のBraze統合からのユーザーデータをCriteoの顧客リストに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。通常はユーザーデータに基づいてBrazeキャンバスでメッセージをトリガーするための基準（プッシュ、メール、SMS、Webhookなど）を、Criteo顧客リスト内の該当ユーザーに対する広告のトリガーに使用できるようになりました。

**オーディエンス同期の一般的なユースケースには次のものがあります。**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

この機能により、ブランドはCriteoと共有される特定のファーストパーティデータを制御できるようになります。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro免責条項**<br>
Braze Audience Sync to CriteoはAudience Sync Pro統合です。この統合の詳細については、Brazeアカウントマネージャーにお問い合わせください。<br>
{% endalert %}

## 前提条件 {#prerequisites}

Criteoへのオーディエンス同期を設定する前に、以下の項目が作成済みまたは完了済みであることを確認する必要があります。

| 要件 | 提供元 | 説明 |
| --- | --- | --- |
| Criteo広告アカウント | [Criteo](https://marketing.criteo.com/) | ブランドに紐づけられたアクティブなCriteo広告アカウント。<br><br>Criteoの管理者から、オーディエンスにアクセスするための適切な権限が付与されていることを確認してください。 |
| [Criteo広告ガイドライン](https://www.criteo.com/advertising-guidelines/)<br>および<br>[Criteoブランドセーフティガイドライン](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | アクティブなCriteoの顧客として、Criteoキャンペーンを開始する前に、Criteoの広告ガイドラインおよびブランドセーフティガイドラインに準拠できることを確認する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：Criteoに接続する {#step-1-connect-to-criteo}

{% alert important %}
CriteoをBrazeアカウントに接続するには、[「管理者」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)が必要です。
{% endalert %}

Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Criteo**を選択します。Criteo Audience Exportの下で、**Connect Criteo**を選択します。

![概要セクションとConnect Criteoボタンを含むCriteoセクションが表示されたBrazeのCriteoテクノロジーページ。]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

Criteo oAuthページが表示され、オーディエンス同期連携に関連する権限をBrazeに付与することを承認します。

確認を選択すると、Brazeにリダイレクトされ、同期するCriteo広告アカウントを選択できます。

![Criteoに接続できる利用可能な広告アカウントのリスト。]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

接続が正常に完了すると、パートナーページに戻り、接続されているアカウントの確認や既存アカウントの切断ができます。

![広告アカウントが正常に接続されたことを示すCriteoテクノロジーパートナーページの更新版。]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Criteo接続はBrazeワークスペースレベルで適用されます。Criteo管理者がCriteo広告アカウントからあなたを削除した場合、Brazeは無効なトークンを検出します。その結果、Criteoを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2：キャンバスのエントリ条件を設定する {#step-2-configure-your-canvas-entry-criteria}

広告トラッキング用のオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したりすることや、[CCPA](https://oag.ca.gov/privacy/ccpa)に基づく「販売または共有の拒否」権利などのプライバシー法に準拠することが必要になる場合があります。マーケターは、キャンバスのエントリ条件内にユーザーの適格性に関する適切なフィルターを実装する必要があります。以下のオプションが役立ちます。

[Braze SDKを通じてiOS IDFAを収集]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)している場合、広告トラッキング有効フィルターを使用できます。値をtrueに設定すると、オプトインしたユーザーのみをオーディエンス同期の送信先に送信します。

![広告トラッキング有効がtrueに設定されたキャンバスエントリフィルター。]({% image_buster /assets/img/criteo/criteo11.png %})

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合は、キャンバスのエントリ条件にフィルターとして含める必要があります。

![オーディエンスの適格性のためにカスタムオプトイン属性を使用したキャンバスエントリフィルター。]({% image_buster /assets/img/criteo/criteo12.png %})

Brazeプラットフォーム内でこれらのデータ保護法に準拠する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance)を参照してください。

### ステップ3：Criteoを使用したオーディエンス同期ステップを追加する {#step-3-add-an-audience-sync-step-with-criteo}

キャンバスにコンポーネントを追加し、**Audience Sync**を選択します。

![キャンバスでCriteoオーディエンスコンポーネントを追加する前のステップのワークフロー。]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![キャンバスでCriteoオーディエンスコンポーネントを追加する前のステップのワークフロー。]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### ステップ4：同期の設定 {#step-4-sync-setup}

**Custom Audience**ボタンをクリックして、コンポーネントエディターを開きます。

オーディエンス同期パートナーとして**Criteo**を選択します。

![Criteoがパートナーとして選択されたオーディエンス同期ステップエディター。]({% image_buster /assets/img/criteo/criteo6.png %})

次に、目的のCriteo広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンス名を入力します。

{% tabs %}
{% tab 新規オーディエンスを作成 %}
**新規オーディエンスを作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択して、Criteoと同期するフィールドを選択します。次に、ステップエディターの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは、目的の広告アカウントが選択され、新しいオーディエンスが作成されています。]({% image_buster /assets/img/criteo/criteo3.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。オーディエンスは下書きモードで作成されるため、ユーザーはキャンバスジャーニーの後半でユーザー削除のためにこのオーディエンスを参照できます。

![キャンバスコンポーネントで新しいオーディエンスが作成された後に表示されるアラート。]({% image_buster /assets/img/criteo/criteo1.png %})

新しいオーディエンスを含むキャンバスを起動すると、Brazeはユーザーがオーディエンス同期コンポーネントに入るとほぼリアルタイムで同期します。
{% endtab %}
{% tab 既存のオーディエンスと同期 %}
**既存のオーディエンスと同期**<br>
Brazeでは、既存のCriteoオーディエンスにユーザーを追加して、オーディエンスを最新の状態に保つこともできます。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**Add to the Audience**を選択します。Brazeは、ユーザーがオーディエンス同期コンポーネントに入るとほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは、目的の広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### ステップ5：キャンバスを起動する {#step-5-launch-canvas}

Criteoへのオーディエンス同期を設定したら、キャンバスを起動します。新しいオーディエンスが作成され、オーディエンス同期ステップを通過するユーザーはCriteo上のこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Criteoでオーディエンスを確認するには、広告マネージャーアカウントに移動し、ナビゲーションの**Audience Library**から**セグメント**を選択します。**セグメント**ページでは、各オーディエンスのサイズが約1,000に達した後に確認できます。

![セグメント、ID、ソース、タイプ、サイズ、現在の使用状況、最終更新を表示するオーディエンスライブラリ。]({% image_buster /assets/img/criteo/criteo.png %})

## ユーザー同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期ステップに到達すると、BrazeはCriteoのAPIレート制限を遵守しながら、ほぼリアルタイムでユーザーを同期します。Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理し、Criteoに送信します。

CriteoのAPIレート制限では、1分あたり250リクエストまでしか許可されていません。顧客がこの制限に達した場合、Brazeは最大約13時間にわたって同期をリトライします。それでも同期ができない場合、Brazeはこれらのユーザーをユーザーエラー指標に記録します。

## 分析の理解 {#understanding-analytics}

以下の表には、Audience Syncコンポーネントの分析をより深く理解するための指標と説明が含まれています。

| 指標 | 説明 |
| --- | --- |
| エントリ済み | Criteoに同期するためにこのコンポーネントに入ったユーザー数。 |
| 次のステップに進んだ | 次のコンポーネントがある場合、そこに進んだユーザー数。キャンバスブランチの最後のステップである場合、すべてのユーザーが自動的に進みます。 |
| 同期済みユーザー | Criteoへの同期に成功したユーザー数。 |
| 未同期ユーザー | マッチに必要なフィールドが不足しているため、同期されなかったユーザー数。 |
| 保留中のユーザー | BrazeがCriteoへの同期を処理中のユーザー数。 |
| エラーが発生したユーザー | 約13時間のリトライ後にAPIエラーによりCriteoに同期されなかったユーザー数。エラーの原因としては、無効なCriteoトークンや、Criteo上でオーディエンスが削除された場合などが考えられます。 |
| キャンバスを退出 | キャンバスを退出したユーザー数。これは、キャンバスの最後のステップがAudience Syncコンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析の理解" }

{% alert important %}
同期済みユーザーとエラーが発生したユーザーの指標のレポートには、それぞれ一括フラッシャーと13時間のリトライにより遅延が生じることにご注意ください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### 無効なトークンエラーが表示された場合、次に何をすべきですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}
Criteoパートナーページで、Criteoアカウントを切断してから再接続するだけで対応できます。同期したい広告アカウントに対する適切な権限があることを、Criteo管理者に確認してください。

### キャンバスの起動が許可されないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

CriteoパートナーページでCriteo広告アカウントがBrazeに正常に接続されていることを確認してください。次に、広告アカウントを選択し、新しいオーディエンスの名前を入力し、マッチングするフィールドを選択していることを確認してください。

### ユーザーをCriteoに渡した後、ユーザーがマッチしたかどうかはどうすればわかりますか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-criteo}

Criteoは、独自のデータプライバシーポリシーにより、この情報を提供していません。

### Criteoはいくつのオーディエンスをサポートできますか？ {#how-many-audiences-can-criteo-support}

現時点では、Criteoアカウント内に保持できるオーディエンスは1,000件までです。この制限を超えた場合、Brazeは新しいオーディエンスを作成できないことを通知します。Criteo広告アカウントで使用していないオーディエンスを削除する必要があります。
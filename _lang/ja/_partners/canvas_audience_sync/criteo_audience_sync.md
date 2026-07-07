---
nav_title: Criteo
article_title: キャンバスのオーディエンスをCriteoに同期する
description: "このリファレンス記事では、Braze Audience Sync to Criteoを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 1
alias: /audience_sync_criteo/

tool:
  - キャンバス
---

# Audience Sync to Criteo

Braze Audience Sync to Criteoを使用すると、ブランドは独自のBraze統合からのユーザーデータをCriteoの顧客リストに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。通常はユーザーデータに基づいてBraze キャンバスでメッセージをトリガーするための基準（プッシュ、メール、SMS、Webhookなど）を、Criteo顧客リスト内の該当ユーザーに対する広告のトリガーに使用できるようになりました。

**オーディエンス同期の一般的なユースケースには次のものがあります。**

- 複数のチャネルを通じて価値の高いユーザーをターゲットにして、購入やエンゲージメントを促進する
- 他のマーケティングチャネルにあまり反応しないユーザーのリターゲティング
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスの作成
- Lookalikeオーディエンスを作成し、新規ユーザーをより効率的に獲得する

この機能により、ブランドはCriteoと共有される特定のファーストパーティデータを制御できるようになります。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro免責条項**<br>
Braze Audience Sync to CriteoはAudience Sync Pro統合です。この統合の詳細については、Brazeアカウントマネージャーにお問い合わせください。<br>
{% endalert %}

## 前提条件 {#prerequisites}

Audience Sync to Criteoを設定する前に、以下の項目が作成または完了していることを確認する必要があります。

| 必要条件 | 提供元 | 説明 |
| --- | --- | --- |
| Criteo広告アカウント | [Criteo](https://marketing.criteo.com/) | ブランドに関連付けられたアクティブなCriteo広告アカウント。<br><br>Criteo管理者から、オーディエンスにアクセスするための適切な権限が付与されていることを確認してください。 |
| [Criteo広告ガイドライン](https://www.criteo.com/advertising-guidelines/)<br>および<br>[Criteoブランドセーフティガイドライン](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Criteoのアクティブな顧客として、Criteo キャンペーンを開始する前に、Criteoの広告ガイドラインおよびブランドセーフティガイドラインを遵守できることを確認する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1:Criteoに接続する {#step-1-connect-to-criteo}

{% alert important %}
CriteoをBrazeアカウントに接続するには、[「Admin」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)が必要です。
{% endalert %}

Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、**Criteo**を選択します。Criteo Audience Exportで、**Connect Criteo**を選択します。

![Brazeの Criteoテクノロジーページ。概要セクション、Criteoセクション、および「Connected Criteo」ボタンが表示されています。]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

Criteo oAuthページが表示され、Audience Sync統合に関連する権限をBrazeに付与します。

確認を選択すると、Brazeにリダイレクトされ、同期するCriteo広告アカウントを選択できます。

![Criteoに接続できる広告アカウントのリスト。]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

接続に成功すると、パートナーページに戻り、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりできます。

![広告アカウントが正常に接続されたことを示す更新後のCriteoテクノロジーパートナーページ。]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Criteoとの接続はBrazeワークスペースレベルで適用されます。Criteo管理者がCriteo広告アカウントからユーザーを削除した場合、Brazeは無効なトークンを検出します。その結果、Criteoを使用しているアクティブなキャンバスにはエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2:キャンバスのエントリ基準を設定する {#step-2-configure-your-canvas-entry-criteria}

広告トラッキングのためにオーディエンスを作成する場合、ユーザーの設定に基づいて特定のユーザーを含めるか除外し、[CCPA](https://oag.ca.gov/privacy/ccpa)の「販売または共有を禁止する」権利などのプライバシー法に準拠することを希望する場合があります。マーケターは、キャンバスのエントリ基準の範囲内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかの選択肢を挙げます。

[Braze SDKでiOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)を収集した場合、「広告の追跡が有効」フィルターを使用できます。ユーザーがオプトインしたAudience Syncの宛先にのみユーザーを送信するには、値をtrueに選択します。

![]({% image_buster /assets/img/criteo/criteo11.png %})

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集する場合は、キャンバスのエントリ基準にこれらをフィルターとして含める必要があります。

![]({% image_buster /assets/img/criteo/criteo12.png %})

Brazeプラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance/)を参照してください。

### ステップ3:CriteoでAudience Syncステップを追加する {#step-3-add-an-audience-sync-step-with-criteo}

キャンバスにコンポーネントを追加し、**Audience Sync**を選択します。

![キャンバスにCriteoオーディエンスコンポーネントを追加する前のステップのワークフロー。]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![キャンバスにCriteoオーディエンスコンポーネントを追加する前のステップのワークフロー。]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### ステップ4:同期設定 {#step-4-sync-setup}

**Custom Audience**ボタンをクリックしてコンポーネントエディターを開きます。

目的のAudience Syncパートナーとして**Criteo**を選択します。

![]({% image_buster /assets/img/criteo/criteo6.png %})

次に、目的のCriteo広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンスの名前を入力します。

{% tabs %}
{% tab 新規オーディエンスの作成 %}
**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択して、Criteoと同期するフィールドを選択します。次に、ステップエディターの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは、目的の広告アカウントが選択され、新しいオーディエンスが作成されます。]({% image_buster /assets/img/criteo/criteo3.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。ユーザーは、後でキャンバスジャーニーでユーザーを削除するためにこのオーディエンスを参照できます。これは、オーディエンスが下書きモードで作成されたためです。

![新しいオーディエンスがキャンバスコンポーネントに作成された後に表示されるアラート。]({% image_buster /assets/img/criteo/criteo1.png %})

新しいオーディエンスを使用してキャンバスを起動すると、Audience Syncコンポーネントに入る時点で、Brazeはユーザーをほぼリアルタイムで同期します。
{% endtab %}
{% tab 既存のオーディエンスとの同期 %}
**既存のオーディエンスとの同期**<br>
Brazeは、これらのオーディエンスが最新であることを確認するために、既存のCriteoオーディエンスにユーザーを追加する機能も提供しています。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンスの名前を入力し、**Add to the Audience**を選択します。Brazeは、Audience Syncコンポーネントに入ると、ほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは、目的の広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### ステップ5:キャンバスを起動する {#step-5-launch-canvas}

Audience Sync to Criteoを設定したら、キャンバスを起動します。新しいオーディエンスが作成され、Audience Syncステップを経由したユーザーがCriteoのこのオーディエンスに送られます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Criteoでオーディエンスを表示するには、広告マネージャーアカウントにログインし、ナビゲーションの**Audience Library**からセグメントを選択します。**セグメント**ページから、各オーディエンスが約1,000に達した後のサイズを確認できます。

![セグメント、ID、ソース、タイプ、サイズ、現在使用中であるかどうか、および最終更新日時を示すオーディエンスライブラリ。]({% image_buster /assets/img/criteo/criteo.png %})

## ユーザーの同期とレート制限の考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがAudience Syncステップに到達すると、BrazeはCriteoのAPIレート制限を尊重しながら、ほぼリアルタイムでそれらを同期します。Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理してから、Criteoに送信します。

CriteoのAPIレート制限では、1分あたり250件を超えるリクエストは許可されません。顧客がこの制限に達すると、Brazeは最大約13時間まで同期を再試行します。それでも同期できない場合、Brazeはこれらのユーザーを「エラーが発生したユーザー」指標に一覧表示します。

## 分析の理解 {#understanding-analytics}

次の表に、Audience Syncコンポーネントからの分析をよりよく理解するのに役立つ指標と説明を示します。

| 指標 | 説明 |
| --- | --- |
| 入力 | Criteoと同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数。これがキャンバスブランチの最後のステップである場合、すべてのユーザーは自動的に進みます。 |
| ユーザーの同期 | Criteoに正常に同期されたユーザー数。 |
| 同期されていないユーザー | 一致するフィールドが不足しているため、同期されていないユーザーの数。 |
| 保留中のユーザー | BrazeがCriteoに同期するために現在処理しているユーザー数。 |
| エラーが発生したユーザー数 | 約13時間の再試行後、APIエラーによりCriteoに同期されなかったユーザー数。エラーの原因としては、Criteoトークンが無効である場合や、Criteoでオーディエンスが削除された場合などが考えられます。 |
| キャンバスを終了 | キャンバスを終了したユーザーの人数。これは、キャンバスの最後のステップがAudience Syncコンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析の理解" }

{% alert important %}
一括フラッシャーと13時間の再試行のために、同期されたユーザーとエラーが発生したユーザーの指標のレポートに遅延が発生することに注意してください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### 無効なトークンエラーが表示された場合、次に何をすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}
CriteoパートナーページでCriteoアカウントの接続を解除してから再接続できます。同期する広告アカウントに対する適切なアクセス許可があることをCriteo管理者に確認してください。

### キャンバスを起動できないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}
CriteoパートナーページでCriteo広告アカウントがBrazeに正常に接続されていることを確認してください。次に、広告アカウントを選択し、新しいオーディエンスの名前を入力し、一致させるフィールドを選択していることを確認します。

### Criteoにユーザーを渡した後、ユーザーが一致しているかどうかを知るにはどうすればよいですか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-criteo}
Criteoは、自社のデータプライバシーポリシーにより、この情報を提供していません。

### Criteoは何件のオーディエンスに対応できますか？ {#how-many-audiences-can-criteo-support}
現時点では、Criteoアカウントに含めることができるオーディエンスの数は1,000件です。この上限を超えた場合、Brazeから新しいオーディエンスを作成できないことが通知されます。Criteo広告アカウントで使用を終了したオーディエンスは削除する必要があります。
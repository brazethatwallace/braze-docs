---
nav_title: Justuno
article_title: Justuno
description: "JustunoとBrazeを統合して、両方のプラットフォームで顧客データを活用し、すべてのオーディエンスにパーソナライズされたエクスペリエンスを提供する方法について説明します。"

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [Justuno](https://www.justuno.com/)では、ダイナミックなセグメントにより、すべてのオーディエンスに対して完全に最適化されたビジター体験を作成することができ、サイトの速度に影響を及ぼしたり、開発作業を増やすことなく、最も高度なターゲティングを利用できます。作成されたプロファイル数、再訪者の影響率、セッションあたりのページ数などのカスタム分析を表示して、コンバージョン率を分析し、業界でのマーケティングの優位性を維持できます。Justunoを使用すると、訪問者あたりの収益を増やし、有意義なカスタマーエンゲージメントを確立し、ビジネスを成長させることができます。接続されたプラットフォームで、オーディエンスジャーニー全体をエンドツーエンドで最適化しましょう。

## ユースケース {#use-cases}

Brazeでは、あらゆるマーケターがあらゆるデータソースからあらゆる量のデータを収集し、アクションを実行できるため、1つのプラットフォームからさまざまなチャネルでリアルタイムにクリエイティブに顧客とエンゲージメントを進めることができます。

JustunoとBrazeを統合することで、両方の長所を生かすことができます。Brazeに保存された顧客データとJustunoに保存されたビジターデータや顧客データを組み合わせることで、すべてのオーディエンスに対してよりパーソナライズされたエクスペリエンスを提供できます。これにより、マーケティングキャンペーンやカスタマーエンゲージメントの効果を高めることができます。

## 前提条件 {#prerequisites}

| Braze REST APIキー | `users.track`および`custom_attributes.get`の権限があるBraze REST APIキー。<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | 利用するRESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)によって異なります。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## JustunoとBrazeの統合 {#integrating-justuno-with-braze}

### ステップ1:Brazeでカスタム属性を作成する {#step-1-create-custom-attributes-in-braze}

JustunoからBrazeにユーザー属性を同期するには、まだ作成していない場合はBrazeでそれらの属性を作成する必要があります。**データ設定** > **カスタム属性**に移動し、カスタム属性を作成してください。詳細なチュートリアルについては、[Brazeのカスタム属性の管理]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)を参照してください。

### ステップ2:BrazeアプリをJustunoに追加する {#step-2-add-the-braze-app-to-justuno}

#### ステップ2.1:アカウントに追加する {#step-21-add-it-to-your-account}

JustunoアカウントにBrazeアプリを追加するには、**Account Settings** > **Apps**に移動し、Brazeアプリを検索して選択します。

![Brazeアプリが検索結果のリストに表示されたJustunoの「Connect Apps」ページ。]({% image_buster /assets/img/justuno/search-for-braze.png %})

[すでに作成済みの](#prerequisites)APIキーとベースURLを入力し、**Connect**を選択します。

![Braze APIキーとベースURLを求めるBraze認証ポップアップウィンドウ。]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### ステップ2.2:ワークフローに追加する {#step-22-add-it-to-your-workflow}

Brazeアプリを[Justunoワークフロー](https://hub.justuno.com/knowledge/workflows-overview)に追加するには、**Sync to App**アクションをワークフローにドラッグ＆ドロップし、**Select App** > **Braze**の順に選択します。

![「Sync to App」アクションにある「Select App」オプション。]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### ステップ3:Braze購読グループを接続する {#step-3-connect-your-braze-subscription-groups}

Justunoから特定のBrazeメールまたはSMS購読グループにプロファイルデータを送信するには、Justunoワークフロー内のBrazeアプリにそのIDを追加する必要があります。

| IDタイプ                          | 必須？ | 説明                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| Braze SMS購読グループID  | はい       | このIDは、ユーザープロファイルからのSMS同意の収集に使用されます。JustunoにIDが入力されていない場合、JustunoがそのプロファイルをBrazeにプッシュしたときにプロファイルへの同意がないことになります。 |
| Brazeメール購読グループID | いいえ        | JustunoにこのIDが入力されていない場合、購読グループの関連付けがないユーザーとしてJustunoからBrazeにプロファイルデータが送信されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 3: Connect your Braze subscription groups" }

#### ステップ3.1:BrazeでIDを見つける {#step-31-locate-the-ids-in-braze}

BrazeダッシュボードでこれらのIDを見つけるには:

1. **オーディエンス** > **購読**に移動します。
2. 各購読グループについて、ID列にあるIDを書き留めます。

#### ステップ3.2:BrazeアプリにIDを追加する {#step-32-add-the-ids-to-the-braze-app}

Justunoワークフローで Brazeアプリを開き、各購読グループのIDを入力します。

![BrazeアプリがJustunoワークフローで開かれ、メールとSMS購読グループIDを追加するオプションが表示されている。]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### ステップ4:属性を設定する {#step-4-configure-your-attributes}

以下の属性は、JustunoからBrazeへ自動的に同期されます。

- メール
- 電話
- 名
- 姓
- 言語
- 性別
- 国

追加の属性を同期するには:

1. ワークフロー内のBrazeアプリで、**Sync Another Property**を選択します。
    ![BrazeアプリがJustunoワークフローで開かれ、「Sync Another Property」オプションが表示されている。]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. 同期するBrazeの属性を選択します。
3. Justunoのプロパティと対応するBrazeのプロパティをマッチングします（ソーシャルハンドル、誕生日、ショッピングの好み、調査の回答など）。これらのプロパティは、ゼロパーティデータまたはファーストパーティデータと見なされます。詳細については、[Justuno: Visitor data collection](https://www.justuno.com/guides/zero-first-party-data/)を参照してください。
4. ワークフロービルダーで、ワークフローの**Save**、**Preview**、または**Publish**を選択します。
    ![「Publish」メニューが開かれ、保存、プレビュー、バージョン履歴の表示のオプションが表示されている。]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## 知っておくべきこと {#things-to-know}

- アプリ設定で購読グループIDを手動で入力する必要があります。
- 次のBrazeデータタイプには**対応していません**: オブジェクト、オブジェクト配列。
- JustunoのSMS同意フィールドが使用されていない場合、SMS同意は暗黙的に提供されます。
- Justunoのデザインに同意フィールドが含まれている場合は、明示的なSMS同意が尊重されます。
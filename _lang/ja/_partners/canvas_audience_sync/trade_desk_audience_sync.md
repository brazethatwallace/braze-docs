---
nav_title: The Trade Desk
article_title: Canvas Audience Sync - The Trade Desk
description: "このリファレンス記事では、Braze Audience Syncを The Trade Desk と連携して、行動トリガー、セグメンテーションなどに基づいた広告配信を行う方法について説明します。"
alias: /trade_desk_audience_sync/
tool:
  - Canvas
page_order: 7
---

# The Trade Deskへの Audience Sync {#audience-sync-to-the-trade-desk}

> Braze Audience Sync to The Trade Deskを使用すると、Brazeのファーストパーティユーザーデータを The Trade Desk にダイナミックに直接同期し、広告リターゲティング、類似モデリング、抑制に活用できます。

**オーディエンス同期の一般的なユースケース:**

- The Trade Deskでパーソナライズ済みCampaignsを使用して既存ユーザーをリターゲティングする。
- 除外ターゲティングのためにファーストパーティデータを The Trade Deskに送信する。
- ユーザーを新規または既存のオーディエンスやCRMデータSegmentsに同期する。

## 前提条件 {#prerequisites}

Canvasで The Trade Deskとの Audience Sync ステップを設定する前に、以下の項目が作成、完了、または承認されていることを確認してください。

| 要件 | Origin | 説明 |
| --- | --- | --- |
| APIトークン | [The Trade Desk](https://partner.thetradedesk.com/v3/portal/api/doc/Authentication#ui-method-create) | The Trade Deskプラットフォームで作成された標準APIトークンです。The Trade Desk Audience Syncを使用するCanvasesへの影響を最小限に抑えるため、APIトークンの有効期間を最大1年に設定することをお勧めします。 |
| The Trade Deskの利用規約とポリシー | The Trade Desk | The Trade Deskへのデータ送信を有効にするには、UID2/CRM参加ポリシーに同意する必要があります。The Trade Deskの担当者に連絡して、The Trade Deskへのデータ配信を有効にするための適切な署名があることを確認してください。<br><br> {::nomarkdown}<ul><li>アカウントでCRMデータ管理アクセスが有効になっていることを確認してください。The Trade Deskの担当者がサポートします。広告主IDが必要です。</li><li>標準APIトークンを準備してください。このページの手順に従って生成できます。</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 統合 {#integration}

### ステップ 1: The Trade Deskアカウントを接続する {#step-1-connect-the-trade-desk-account}

開始するには、**パートナー連携** > **テクノロジーパートナー** > **The Trade Desk** に移動します。Trade Deskアカウントから以下の詳細を入力してください:

- **APIトークン**
- **広告主ID名**（このオプション名は、Audience Sync Canvasステップで参照する広告主アカウントを識別します）
- **広告主ID**

次に、**Connect** を選択します。

![The Trade Deskの未接続の Audience Sync の例。]({% image_buster /assets/img/audience_sync/trade_desk/connect_sync.png %}){: style="max-width:90%;"}

#### 複数の The Trade Deskアカウントを接続する（オプション） {#connect-multiple-the-trade-desk-accounts-optional}

最初の The Trade Deskアカウントを接続した後、The Trade Deskパートナーページで **Connect more advertisers** を選択し、各アカウントの**広告主ID名**と**広告主ID**を入力することで、追加の広告主アカウントを追加できます。

### ステップ 2: The Trade Deskとの Audience Sync ステップを追加する {#step-2-add-an-audience-sync-step-with-the-trade-desk}

Canvasにコンポーネントを追加し、**Audience Sync** を選択します。次に、Audience Syncパートナーとして **The Trade Desk** を選択します。

![Audience Syncステップで同期するパートナーを選択するオプション。]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step.png %}){: style="max-width:90%;"}

### ステップ 3: 同期を設定する {#step-3-set-up-your-sync}

次に、同期の詳細を設定します:

1. 広告アカウントを選択します。
2. 既存のオーディエンスを選択するか、新しいオーディエンスを作成します。

![オーディエンスフィールドに「valentines2025」という名前が含まれる Audience Syncの設定。]({% image_buster /assets/img/audience_sync/trade_desk/choose_audience.png %}){: style="max-width:90%;"}

{: start="3"}
3. **Add Users to Audience** または **Remove Users from Audience** のいずれかのアクションを選択します。

![オーディエンスにユーザーを追加する Audience Syncの設定。]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step2.png %}){: style="max-width:90%;"}

{: start="4"}
4. マッチングに使用するフィールドを選択します: **Email**、**Phone**、または **Mobile Advertiser ID**。

{% alert note %}
EUリージョンが設定された The Trade Deskのオーディエンスに同期する場合、電話番号は The Trade Deskでサポートされていません。EUリージョンでの電話番号サポートについては、The Trade Deskにお問い合わせください。
{% endalert %}

### ステップ 4: Canvasを起動する {#step-4-launch-your-canvas}

The Trade Deskへの Audience Syncを設定したら、Canvasを起動する準備が整いました。新しいオーディエンスが作成され、Audience Syncステップを通過するユーザーは The Trade Deskのこのオーディエンスに渡されます。Canvasに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

## よくある質問 {#frequently-asked-questions}

### The Trade Deskでオーディエンスサイズが反映されるまでどのくらいかかりますか？ {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-the-trade-desk}

最大24時間かかる場合があります。

### 広告アカウント内で The Trade Deskが反映するための最小オーディエンスサイズはありますか？ {#what-is-the-minimum-audience-size-for-the-trade-desk-to-populate-within-your-ad-account}

The Trade DeskのCRMオーディエンスには最小オーディエンスサイズはありません。

### The Trade Deskにユーザーを渡した後、ユーザーがマッチしたかどうかはどのように確認できますか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-the-trade-desk}

The Trade Deskでは、受信したIDがSegmentの横に表示されます。

- 受信済みIDは、過去30日間に受信したIDの数です。
- アクティブIDは、過去7日間に入札で確認されたIDの数です。

### The Trade Deskはいくつのオーディエンスをサポートできますか？ {#how-many-audiences-can-the-trade-desk-support}

The Trade Deskでサポートできるオーディエンス数に制限はありません。
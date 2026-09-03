---
nav_title: Currentsを設定する
article_title: Currentsの設定
page_order: 1
page_type: tutorial
description: "このハウツー記事では、Braze Currentsの連携と設定を行うプロセスを順に説明します。"
tool: Currents
search_rank: 8
---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Currentsの設定 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcurrents-the-basics-2-stylefloatrightwidth120pxborder0-classnoimgborderset-up-currents}

> このページでは、Braze Currentsの連携と設定を行う一般的なプロセスを概説します。

{% alert important %}
Currentsは特定のBrazeパッケージに含まれています。ご質問がある場合、またはアクセスを希望する場合は、Brazeの担当者にお問い合わせください。
{% endalert %}

## トラブルシューティング {#troubleshooting}

### 新しいCurrents連携を追加できない {#cannot-add-a-new-currents-integration}

新しい連携を追加する際に「You do not have any remaining Currents integrations」と表示される場合、または新しいCurrentsコネクターを追加するボタンがグレーアウトしている場合、一般的な原因は次のとおりです。

- このワークスペースに対してCurrentsのエンタイトルメントが購入されていない。
- Currentsのエンタイトルメントが、同じ会社内の別のワークスペースで利用可能になっている。

これを解決するには、会社内の他のワークスペースを確認してください。別のワークスペースで利用可能なCurrentsエンタイトルメントが表示される場合があります。エンタイトルメントのリクエストや設定の調整が必要な場合は、Brazeのアカウントマネージャーにお問い合わせください。

### 追加のイベントトラッキングを有効にできない {#cannot-enable-additional-event-tracking}

コネクターの作成や編集はできるものの、オプションのトラッキングスイッチを有効にできない場合、ワークスペースがそのイベントカテゴリーのエンタイトルメント上限に達している可能性があります。

- **Track Customer Behavior and User Events**には、利用可能な**Customer Behavior Events**エンタイトルメントが必要です。
- **Track user profiles and attributes**には、利用可能な**User Profiles and Attributes**エンタイトルメントが必要です。

追加のエンタイトルメントや設定の調整についてサポートが必要な場合は、Brazeのアカウントマネージャーにお問い合わせください。

## 要件 {#requirements}

Currentsをパートナーと連携して使用する場合、いずれのパートナーでも同じ基本パラメーターと接続方法が必要です。

各パートナーは、Brazeがデータファイルを書き込みおよび送信する権限を持つことを要求します。また、Brazeはそれらのファイルの書き込み先（具体的にはバケット名やキー）を確認します。

以下の要件は、ほとんどのパートナーとの連携に必要な基本的な最低要件です。一部のパートナーでは追加パラメーターが必要な場合があり、それらは各[パートナーのドキュメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)に、これらの基本要件に関連する注意事項とともに記載されています。

| 要件 | Origin | アクセス | 説明
|---|---|---|---|
| パートナーのアカウント | パートナーとアカウントを契約するか、Brazeアカウントマネージャーに提案を依頼してください。 | パートナーのサイトを確認するか、パートナーに連絡してサインアップしてください。 | 自社のアカウントを通じてデータにアクセスできない場合、Brazeはパートナーにデータを送信しません。
| パートナーAPIキーまたはトークン | 通常、パートナーのダッシュボードにあります。 | コピーして、指定のBrazeフィールドに貼り付けてください。 | Brazeでは、該当パートナーの連携ページに専用フィールドがあります。これはデータの送信先をマッピングするために必要です。**パートナーキーまたはトークンは常に最新の状態に保ってください。認証情報が無効になると、コネクターが無効化されイベントが欠落する可能性があります。**
| 認証コード/キー、シークレットキー、証明書ファイル | パートナーのアカウント担当者にお問い合わせください。パートナーのダッシュボードにある場合もあります。 | キーをコピーして、指定のBrazeフィールドに貼り付けてください。`.json`やその他の証明書ファイルを生成し、Braze内の適切な場所にアップロードしてください。 | Brazeでは、該当パートナーの連携ページに専用フィールドがあります。これにより、Brazeに認証情報が付与され、パートナーアカウントにファイルを書き込む権限が認可されます。**認証情報は常に最新の状態に保つことが重要です。認証情報が無効になると、コネクターが無効化されイベントが欠落する可能性があります。**
| バケット、フォルダーパス | 一部のパートナーはデータをバケットごとに整理・分類しています。これはパートナーのダッシュボードで確認できます。 | 必要な場合は、バケット名またはファイルパスを正確にBrazeの指定スペースにコピーしてください。 | これは一部のパートナーでのみ必要ですが、必要な場合は正確に設定することが重要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="要件" }

{% alert important %}
パートナーキー、パートナートークン、および認証情報は常に最新の状態に保つことが重要です。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を停止します。この状態が**5日間**以上続くと、コネクターのイベントは破棄され、データは永久に失われます。
{% endalert %}

## Currentsの設定 {#setting-up-currents}

### ステップ1：パートナーを選択する {#step-1-choose-your-partner}

Braze Currentsでは、フラットファイルを使用したデータストレージとの連携、または指定されたエンドポイントへのバッチ処理されたJSONペイロードを使用した行動分析・顧客データパートナーとの連携が可能です。

連携を開始する前に、お客様の目的に最適な連携方法を決定することをお勧めします。たとえば、すでにmParticleやセグメントを使用していて、そこにBrazeのデータをストリーミングしたい場合は、バッチ処理されたJSONペイロードを使用するのが最適です。データを独自に加工したい場合や、より複雑なデータ分析システムをお持ちの場合は、データストレージを使用するのが最適かもしれません（[Brazeもこの方法を使用しています]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)！）。

### ステップ2：Currentsを開く {#step-2-open-currents}

開始するには、**パートナー連携** > **Currents**に移動します。Currentsの連携管理ページに移動します。

![Brazeダッシュボードのcurrentsページ]({% image_buster /assets/img_archive/currents-main-page.png %})

### ステップ3：パートナーを追加する {#step-3-add-your-partner}

画面上部のドロップダウンを選択して、パートナー（「Currentsコネクター」とも呼ばれます）を追加します。

各パートナーには異なる設定ステップが必要です。各連携を有効にするには、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)のリストを参照し、それぞれのページの手順に従ってください。

{% multi_lang_include currents/contact_email_notifications.md %}

### ステップ4：イベントを設定する {#step-4-configure-your-events}

利用可能なオプションから、そのパートナーに送信するイベントを選択します。これらのイベントのリストは、[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)および[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)ライブラリで確認できます。

![エクスポートするパートナーイベントが選択されたCurrents設定ページ]({% image_buster /assets/img/current4.png %})

必要に応じて、[イベント配信のセマンティクス]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics)の記事で、イベントの詳細を確認できます。

### ステップ5：フィールド変換を設定する {#step-5-set-up-field-transformations}

Currentsのフィールド変換を使用して、文字列フィールドを削除またはハッシュ化できます。

- **削除：** 文字列フィールドを`[REDACTED]`に置き換えます。パートナーがフィールドの欠落や空のフィールドを含むイベントを拒否する場合に便利です。
- **ハッシュ化：** 文字列フィールドにSHA-256ハッシュアルゴリズムを適用します。

これらの変換のいずれかにフィールドを選択すると、そのフィールドが含まれるすべてのイベントにその変換が適用されます。たとえば、`email_address`をハッシュ化対象として選択すると、メール送信、メール開封、メールバウンス、および購読グループのステート変更イベントの`email_address`フィールドがハッシュ化されます。

![フィールド変換の追加]({% image_buster /assets/img/current3.png %})

### ステップ6：連携をテストする {#step-6-test-your-integration}

{% alert important %}
Currentsは、900&nbsp;KB を超える非常に大きなペイロードを持つイベントをドロップします。
{% endalert %}

テストの前に、[GitHubのCurrentsサンプルデータ](https://github.com/Appboy/currents-examples)を確認することを検討してください。テストの準備ができたら、以下のセクションでオプションを選択してください。

#### テストイベントの送信 {#sending-test-events}

連携をテストするには、**Send Test Events**を選択して、選択した各イベントタイプから1つのイベントをこのCurrentに送信できます。各イベントタイプの詳細情報については、[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)および[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)ライブラリを参照してください。

![Brazeダッシュボードの「Currentsテスト」ページ]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Currentsコネクターのテスト {#testing-currents-connectors}

テスト用Currentsコネクターは、テストやさまざまな送信先の試用に使用できる、既存のコネクターの無料バージョンです。テスト用Currentsには以下の特徴があります。

- ワークスペースごとに最大10個のテスト用Currentsコネクター。
- 固定の24時間期間あたり合計最大1,500イベント（UTC午前0時にリセットされます）。このイベント合計は、ダッシュボード上で1時間ごとに更新されます。

テスト用Currentsコネクターが送信制限に達すると、翌日（UTC午前0時）までコネクターはイベントを送信しません。

テスト用Currentsコネクターをアップグレードするには、ダッシュボードで連携を編集し、**Upgrade Test Integration**を選択してください。

## Currentsの更新 {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## IP許可リスト {#ip-allowlisting}

Brazeは以下のIPアドレスからCurrentsデータを送信します。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}
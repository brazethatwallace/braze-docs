---
nav_title: Currentsを設定する
article_title: Currentsの設定
page_order: 1
page_type: tutorial
description: "このハウツー記事では、Braze Currentsの連携と設定を行うプロセスを順に説明します。"
tool: Currents
search_rank: 8
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Currentsの設定 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcurrents-the-basics-2-stylefloatrightwidth120pxborder0-classnoimgborderset-up-currents}

> このページでは、Braze Currentsの連携と設定を行う一般的なプロセスを概説します。

{% alert important %}
Currentsは特定のBrazeパッケージに含まれています。ご質問がある場合、またはアクセスを希望する場合は、Brazeの担当者にお問い合わせください。
{% endalert %}

新しい連携を追加する際に「残りのCurrents連携がありません」と表示される場合、一般的な原因は次のとおりです。

- このワークスペースに対してCurrentsのエンタイトルメントが購入されていない。
- Currentsのエンタイトルメントが、お客様の会社の別のワークスペースで利用可能になっている。

エンタイトルメントのリクエストや設定の調整については、Brazeのアカウントマネージャーにお問い合わせください。

## 要件 {#requirements}

弊社のパートナーと連携してCurrentsを使用するには、同じ基本パラメーターと接続方法が必要です。

各パートナーは、Brazeがデータファイルを書き込んでパートナーに送信する権限を有することを要求し、Brazeはそれらのファイルを書き込む場所、具体的にはバケット名またはキーを尋ねます。

以下の要件は、ほとんどのパートナーと連携するための基本的な最小要件です。パートナーによっては追加のパラメーターが必要になります。それらのパラメーターは、これらの基本要件に関する注意事項とともに、それぞれの[パートナーのドキュメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)に記載されています。

| 要件 | Origin | アクセス | 説明
|---|---|---|---|
| パートナーのアカウント | そのパートナーとアカウントを設定するか、提案が必要な場合はBrazeのアカウントマネージャーに連絡します。 | そのパートナーのサイトを確認するか、そのパートナーに連絡して登録します。 | お客様の会社のアカウントを通じてそのデータにアクセスできない場合、Brazeはパートナーにデータを送信しません。
| パートナーAPIキーまたはトークン | 通常はパートナーのダッシュボードにあります。 | 指定されたBrazeのフィールドにコピーして貼り付けます。 | Brazeには、パートナーの連携ページに、このための指定フィールドがあります。データの送信先を特定するために、これが必要です。**パートナーキーやトークンは常に最新の状態に保ってください。無効な認証情報はコネクターを無効化し、イベントを消失させる可能性があります。**
| 認証コード/キー、秘密キー、認証ファイル | そのパートナーのアカウント担当者に連絡します。パートナーのダッシュボードに記載されている可能性もあります。 | キーをコピーして指定のBrazeフィールドに貼り付けます。`.json`または他の認証ファイルを生成して、Brazeの適切な場所にアップロードします。 | Brazeには、パートナーの連携ページに、このための指定フィールドがあります。これによりBrazeに認証情報が付与され、パートナーでのお客様のアカウントにBrazeがファイルを書き込むことができます。**認証の詳細を最新の状態に維持することが重要です。認証情報が無効の場合、コネクターが無効になり、イベントがドロップする可能性があります。**
| バケット、フォルダパス | 一部のパートナーは、バケットごとにデータを整理し、分類しています。これはパートナーのダッシュボードにあります。 | これが必要な場合は、バケット名またはファイルパスをBrazeの指定されたスペースに正確にコピーします。 | これはパートナーによっては必要なことですが、必要なときに正しく行うことが重要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="要件" }

{% alert important %}
パートナーキー、パートナートークン、および認証の詳細を最新の状態に保つことが重要です。コネクターの認証情報の有効期限が切れると、コネクターはイベントの送信を停止します。これが**5日**以上続くと、コネクターのイベントは破棄され、データは永久に失われます。
{% endalert %}

## Currentsの設定 {#setting-up-currents}

### ステップ1:パートナーの選択 {#step-1-choose-your-partner}

Braze Currentsを使用すると、フラットファイルを使用したデータストレージ経由での連携、またはバッチ化されたJSONペイロードを指定されたエンドポイントに送信して、行動分析や顧客データのパートナーとの連携ができます。

連携を開始する前に、目的に最適な連携を決定することをお勧めします。例えば、すでにmParticleとセグメントを利用していて、そこにBrazeデータをストリーミングしたい場合は、バッチ化されたJSONペイロードを使用するのが最適です。データを独自に操作したい場合、またはより複雑なデータ分析システムがある場合は、データストレージを使用するのが最適です（[Brazeではこの方法を採用]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)しています）。

### ステップ2:Currentsを開く {#step-2-open-currents}

始めるには、**パートナー連携** > **Currents**に移動します。Currentsの連携管理ページが表示されます。

![Brazeダッシュボードの Currentsページ]({% image_buster /assets/img_archive/currents-main-page.png %})

### ステップ3:パートナーを追加する {#step-3-add-your-partner}

画面上部のドロップダウンを選択し、パートナー（「Currentsコネクター」と呼ばれることもあります）を追加します。

パートナーごとに異なる設定ステップが必要です。各連携を有効にするには、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)のリストを参照し、それぞれのページの指示に従ってください。

### ステップ4:イベントを設定する {#step-4-configure-your-events}

利用可能なオプションから、パートナーに渡すイベントのチェックボックスをオンにします。これらのイベントのリストは、[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)ライブラリと[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)ライブラリにあります。

![エクスポート対象のパートナーイベントが選択されたCurrents設定ページ]({% image_buster /assets/img/current4.png %})

必要に応じて、イベントの詳細について[イベント配信のセマンティクス]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics)の記事を参照してください。

### ステップ5:フィールド変換の設定 {#step-5-set-up-field-transformations}

Currentsフィールド変換を使用して、文字列フィールドを削除またはハッシュできます。

- **削除:** 文字列フィールドを`[REDACTED]`に置き換えます。これは、パートナーが欠落フィールドまたは空のフィールドを持つイベントを拒否する場合に役立ちます。
- **ハッシュ:** SHA-256ハッシュアルゴリズムを文字列フィールドに適用します。

これらのいずれかの変換を行う対象のフィールドを選択すると、そのフィールドが含まれるすべてのイベントにその変換が適用されます。例えば、ハッシュ化の対象として`email_address`を選択すると、メール送信、メール開封、メールバウンス、サブスクリプショングループの状態変更イベントの`email_address`フィールドがハッシュ化されます。

![フィールド変換の追加]({% image_buster /assets/img/current3.png %})

### ステップ6:連携のテスト {#step-6-test-your-integration}

{% alert important %}
Currentsは、900&nbsp;KBを超える過度に大きなペイロードを持つイベントをドロップします。
{% endalert %}

テストする前に、[GitHubのサンプルCurrentsデータ](https://github.com/Appboy/currents-examples)をご確認ください。テストの準備ができたら、以下のオプションを選択します。

#### テストイベントの送信 {#sending-test-events}

連携をテストするには、**Send Test Events**を選択して、選択した各イベントタイプからこのCurrentに1つのイベントを送信します。各イベントタイプの詳細については、[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)ライブラリと[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)ライブラリを参照してください。

![Brazeダッシュボードの「Currentsテスト」ページ]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Currentsコネクターのテスト {#testing-currents-connectors}

Currentsのテストコネクターは、弊社の既存のコネクターの無料版であり、さまざまな送信先のテストと試行に使用できます。Currentsのテストには以下の特徴があります。

- ワークスペースあたり最大10個のテストCurrentsコネクター。
- 固定の24時間期間ごとに、合計最大1,500件のイベント。これはUTCの深夜0時にリセットされます。このイベントの合計はダッシュボードで1時間ごとに更新されます。

テストCurrentsコネクターが送信上限に達すると、そのコネクターは翌日の午前0時（UTC）までイベントを送信しません。

Currentsのテストコネクターをアップグレードするには、ダッシュボードで連携を編集し、**Upgrade Test Integration**を選択します。

## Currentsの更新 {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## IP許可リスト {#ip-allowlisting}

Brazeは、リストされたIPからCurrentsデータを送信します。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}
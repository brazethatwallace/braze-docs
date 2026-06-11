---
nav_title: Lexer
article_title: Lexer
description: "このリファレンス記事では、Braze と Lexer のパートナーシップについて説明します。Lexer はマーケターが顧客データを使用して、売上を伸ばすエクスペリエンスを生み出すことができる顧客データプラットフォームです。"
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer](https://lexer.io/) は小売業向けに構築された顧客データプラットフォームであり、堅牢なデータ強化機能と最も直感的なツールおよび専門家によるアドバイスを組み合わせて、ブランドが改善されたカスタマーエクスペリエンスによりインクリメンタルセールスを伸ばすことができるようにします。

_この統合は Lexer によって管理されています。_

## 統合について {#about-the-integration}

Braze と Lexer の統合により、この2つのプラットフォーム間でデータを同期できます。Lexer のデータを使用して有益な Braze Segmentを作成するか、既存のSegmentを Lexer にインポートしてインサイトを引き出します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| パートナーアカウント | このパートナーシップを活用するには、Lexer アカウントが必要です。 |
| Braze REST APIキー | すべての `user` 権限（`user.delete` を除く）と `segment.list` 権限を持つ Braze REST APIキー。Lexer でサポートされる Braze オブジェクトの増加に伴い、権限セットが変わる可能性があります。このため、この時点でより多くの権限を付与するか、これらの権限を今後更新する計画を立てることをお勧めします。<br><br> これは、Braze ダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [REST エンドポイントのURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントは、インスタンスの Braze URL に依存します。 |
| Amazon AWS S3 バケットと認証情報 | 統合を開始する前に、Lexer ハブに接続されている AWS S3 バケット（お客様が作成したバケットまたは Lexer がお客様のために作成して管理しているバケット）のアクセス認証情報が必要です。この要件に関するガイダンスについては、[Lexer](https://learn.lexer.io/docs/amazon-s3) を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Lexer で **Manage > Integration** に移動し、**Braze** タイルを選択し、**Integrate Braze** をクリックします。次の情報を入力します。
- **Braze REST エンドポイント**
- **Braze REST APIキー**
- **AWS 認証情報**
  - **AWS S3 バケット名**
  - **AWS S3 [バケットリージョン](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)**
  - **AWS S3 バケットのパス**：このパスは、[S3 バケットを Braze に接続する]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)ときに指定したパスと一致している必要があります。Braze に何も指定しなかった場合は空白にしてください。
  - **AWS S3 シークレットアクセスキー**：[アクセスキーの作成](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/)に関する情報は Amazon を参照してください。
- **Braze エクスポートセグメント ID**：Lexer にエクスポートしたいすべてのユーザーを含む、Braze で作成したSegmentの ID です。Lexer にエクスポートしたくないユーザーがいる場合は、Braze で作成したSegmentから除外できます。セグメント識別子を確認するには、Braze で目的のSegmentをクリックし、**セグメント API 識別子**を見つけます。

![]({% image_buster /assets/img/lexer/braze_integrate_screen.png %})

### AWS S3 オプションを選択する（Lexer マネージドまたはセルフマネージド） {#choosing-an-aws-s3-option-lexer-managed-or-self-managed}
Braze を Lexer ハブに接続する方法として、Lexer マネージドバケットを使用する方法が推奨されます。これにより、必要な設定作業が減ります。Lexer は、Braze の設定に必要な1回限りの詳細情報を提供します。

すでに S3 バケットを Braze に接続し、他の目的で使用している場合は、代わりに、前述の手順に従って、Lexer にこのセルフマネージドバケットへのアクセスを提供する必要があります。

この統合は、既存の API トークンとシークレットを Lexer に提供し、Lexer がお客様に代わってこれらのエクスポートを行うことで機能します。また、これらの認証情報と S3 設定を使用して Braze データが Lexer にインポートされ、両方のプラットフォームのデータが自動的に同期されます。

## Braze にSegmentを送信する {#sending-segments-to-braze}

### ステップ 1：アクティベーションを作成する {#step-1-create-activation}

Lexer Activate により Braze プロファイルが自動的に更新され、Segmentへの顧客の出入りに応じて属性が追加または削除されます。

1. Lexer の **Lexer Activations** で **ACTIVATE NEW AUDIENCE** をクリックします。
2. このCampaignに適切な Braze のアクティベーションを選択します。
3. Segmentを追加します。
4. オーディエンス名を更新します。これは Braze での属性値となります。
5. これが Braze で更新するカスタム属性です。更新については [Lexer サポート](support@lexer.io)に連絡してください。
6. 適切なリストアクションを確認します。ほとんどの場合、リストを維持します。
7. 規約を確認し、**SEND AUDIENCE** をクリックします。

![]({% image_buster /assets/img/lexer/lexer.png %})

### ステップ 2：アクティベーションを確認する {#step-2-verify-activation}

Activate でアクティベーションが送信されたことが確認されると、Braze でレコードの更新が開始されます。Lexer から確認メールが届くまで、Braze のプロファイルは完全には更新されません。

### ステップ 3：Braze Segmentを作成する {#step-3-create-your-braze-segment}

Braze では、Lexer のオーディエンス名が `lexer_audience` カスタム属性の値になっています。Braze では、属性あたりの値の数は100に制限されています。

Segmentを作成するには、**Segment > + Create Segment** に移動し、フィルターとして **Custom Attribute** を選択します。次に、属性として `lexer_audience` を選択し、目的の Lexer オーディエンス名を選択します。完了したら、オーディエンスを**保存**します。

この新しく作成したSegmentを、今後の Braze CampaignsやCanvasesに追加して、これらのエンドユーザーをターゲットにできます。
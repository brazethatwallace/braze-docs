---
nav_title: Sageflo
article_title: Sageflo Radiate
description: "この参考記事では、BrazeとSagefloのパートナーシップについて概説しています。Sagefloは分散型マーケティングツールで、BrazeとのAPI統合により、マーケティングで承認されたテンプレート、画像、オーディエンスセグメントを使用して、チームが独自のメールを簡単に送信できるようにします。"
alias: /partners/sageflo/
page_type: partner
search_tag: Partner

---

# Sageflo Radiate

> [Sageflo Radiate](https://sageflo.com/radiate)は分散型マーケティングツールであり、BrazeとのAPI統合により、ローカルチームがマーケティングで承認されたテンプレート、画像、およびオーディエンスセグメントを使用して独自のメールを簡単に送信できるようになります。

_この統合はSagefloによって管理されています。_

## 統合について {#about-the-integration}

オーディエンスのセグメンテーション、フリークエンシーガバナンス、ダイナミックなコンテンツなどのBrazeの高度な機能を活用し、ブランドを保護するガードレールを組み込みながら、ローカルチームにスマートなマーケティングに必要なツールを提供します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Sageflo Radiate アカウント | このパートナーシップを活用するには、Sageflo Radiateアカウントが必要です。 |
| Braze REST APIキー | 完全な`templates`および`campaigns`権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**Settings** > **API Keys**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。APIエンドポイントは、BrazeインスタンスのダッシュボードURLと一致します。<br><br> たとえば、ダッシュボードURLが`https://dashboard-03.braze.com`の場合、エンドポイントは`dashboard-03`になります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

Radiateは、Brazeを通じてローカルオーディエンスにメールを送信する権限を分散チームに与えることで、マーケティング活動の規模を拡大したいと考えているフランチャイズや小売業に最適です。

* 分散しているチームでも簡単にマーケティングメールやSMSを送信できるようにする
* 地域に密着した顧客とのつながりを構築する
* 組み込みのガードレールでブランドの一貫性を保つ
* 全国マーケティングチームの負担を軽減する

## 統合 {#integration}

Sagefloアカウントチームが統合の設定作業を主導します。Braze APIの認証情報を提供するよう求められ、Sagefloはマーケティングチームと協力して、特定のロケーションとBranchのオーディエンスセグメントを設定します。

接続が完了すると、Sagefloは次の作業を行います。

* Radiate環境とBrazeへの接続をセットアップする
* Brazeでロケーションベースのオーディエンスセグメントを設定する
* キャンペーン、ロケーション、ユーザーグループの設定を定義する
* Radiateのキャンペーンで使用できるようBrazeのテンプレートをマッピングする
* ユーザートレーニングのスケジュールと実施
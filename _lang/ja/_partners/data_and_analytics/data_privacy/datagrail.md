---
nav_title: DataGrail
article_title: DataGrail
description: "このリファレンス記事では、Brazeとプライバシー管理プラットフォームであるDataGrailのパートナーシップについて説明します。Braze内で収集・保存されている消費者データを検出し、DSRを迅速に処理できます。"
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> [DataGrail](https://www.datagrail.io/) は、消費者の信頼構築とリスクの高いビジネスの排除を支援するプライバシー管理プラットフォームです。継続的なシステム検出と自動化されたデータ主体要求 (DSR) の履行により、DataGrailはプライバシープログラムを推進し、GDPR、CCPA、CPRAなどの進化するプライバシー関連の法律や規制への準拠を支援します。

_この統合はDataGrailによって管理されています。_

## 統合について {#about-the-integration}

BrazeとDataGrailの統合により、Braze内に収集・保存された消費者データを検出し、DSR（アクセス、削除、販売禁止要求）を迅速に処理できます。自動化されたデータマッピングにより、消費者データが組織内のどこにあるかを正確に把握できるブループリントにBrazeが追加されるため、プライバシーフレームワークの維持や処理活動の記録 (RoPA) の作成にアンケートやスプレッドシートは不要になります。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| DataGrailアカウント | このパートナーシップを活用するには、DataGrailアカウントが必要です。<br>統合に関する問題や質問がある場合は、管理者にお問い合わせいただくか、support@datagrail.io までメールでお問い合わせください。 |
| Braze APIキー | `events.list`、`users.export.ids`、`users.delete`、`users.track`の権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Brazeインスタンス | Brazeインスタンスは、Brazeオンボーディングマネージャーから入手するか、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)で確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

DataGrailポータルにログインし、Brazeの統合ページで**Connect**を選択します。次にインスタンスとBraze APIキーを入力し、**Connect Braze**を選択します。

統合するBrazeアカウントが追加で存在する場合：
1. Brazeの統合ページで**Edit Connection**を選択します。
2. ドロップダウンから**+Add New Connection**を選択します。
3. **Connection Name**の下に、この別のアカウントを識別するための新しい名前を入力します（例：Braze Training Account）。
4. この新しいアカウント用に、別のBrazeインスタンスとAPIキーを入力します。
5. **Connect**を選択します。

統合に関する問題やご質問がある場合は、DataGrail（support@datagrail.io）までメールでお問い合わせください。
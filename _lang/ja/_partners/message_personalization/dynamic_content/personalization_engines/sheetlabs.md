---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "このリファレンス記事では、BrazeとSheetlabsのパートナーシップについて説明します。Sheetlabsは、スプレッドシートから取得したデータを使ってマーケティングキャンペーンをパーソナライズできるサービスです。"
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> [Sheetlabs](https://sheetlabs.com/)は、スプレッドシートを強力で十分にドキュメント化されたAPIに変換できるプラットフォームです。Google SheetsやExcelからデータをインポートしてAPIに変換し、そのAPIをBrazeなどの他のアプリケーションで使用できます。
_この統合はSheetlabsによって管理されています。_

## 統合について {#about-the-integration}

SheetlabsとBrazeの統合により、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)を使用して、BrazeマーケティングCampaignにSheetlabs APIを含めることができます。これは一般的に、Googleスプレッドシート（マーケティングチームが直接更新する）とBrazeテンプレートの橋渡しとして使用されます。これにより、翻訳やカスタム属性の大規模なセットなど、Brazeテンプレートでより多くのことを実現できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Sheetlabsアカウント | このパートナーシップを活用するには、[Sheetlabsアカウント](https://sheetlabs.com/)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

BrazeとSheetlabsの統合により、以下のユースケースを実現できます。

1. **マーケターアクセスとBraze Campaignアクセスの分離**: チームによっては、すべてのスタッフにBrazeのテンプレートやコンテンツを直接設定するアクセス権を与えたくない場合があります。代わりに、スタッフがスプレッドシートでマーケティングコンテンツを更新できるようにしたいと考えています。SheetlabsはスプレッドシートとBrazeの橋渡しを提供し、リアルタイムで更新できます。
2. **翻訳**: Brazeテンプレートはネイティブに翻訳をサポートしていません。複数の言語をサポートしたい場合は、複数のテンプレートを作成する必要があります。SheetlabsをBrazeと併用することで、1つのBrazeテンプレートを複数の言語に翻訳できます。
3. **カスタム属性の拡張**: Brazeには、設定可能なカスタム属性が一定数用意されています。SheetlabsをBrazeと併用することで、この初期割り当てを超えてカスタム属性を追加できます。

これらのユースケースの詳細については、[Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/)を参照してください。

## 統合 {#integration}

### ステップ 1: スプレッドシートをSheetlabsにインポートする {#step-1-import-your-spreadsheet-into-sheetlabs}

Sheetlabsで、Excelスプレッドシートをアップロードするか、Googleアカウントをリンクして Google Sheetをインポートします。

- Excelスプレッドシートをインポートするには、メニューバーの**Data Tables**をクリックし、次に**Import from CSV/Excel**をクリックします。
- Google Sheetsからインポートするには、メニューバーの**Data Tables**をクリックし、次に**Import from Google**をクリックします。その後、Googleログイン認証情報を入力してシートをインポートする必要があります。

また、Google Sheetを同期させておくこともできます。これにより、Google Sheetに変更があった場合、Sheetlabsが自動的に最新のデータを取得します。

スプレッドシートにBrazeユーザーIDを含めるか、後で検索に使用できる情報を含めるようにしてください。

### ステップ 2: SheetlabsでAPIを作成する {#step-2-create-an-api-in-sheetlabs}

次に、Sheetlabsで**APIs** > **Create API**に移動し、APIに名前を付けます。BrazeユーザーIDなど、スプレッドシートのルックアップフィールドを使ったクエリを許可することをお勧めします。

この時点で、以下のようなリンクでAPIにアクセスできるはずです。<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en)

### ステップ 3: BrazeコネクテッドコンテンツでAPIを使用する {#step-3-use-the-api-in-braze-connected-content}

APIにアクセスできるようになったので、コネクテッドコンテンツの呼び出しで使用できます。以下は、翻訳テンプレートの例です。

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
Sheetlabsとの統合に関する詳しい例やアドバイスについては、[Sheetlabsのドキュメント](https://app.sheetlabs.com/docs/producers/braze/)を参照してください。
{% endalert %}
---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "このリファレンス記事では、BrazeとPhraseのパートナーシップについて説明します。Phraseはクラウドベースのローカライゼーションソフトウェアです。この統合により、Brazeインターフェイスを離れることなく、メールテンプレートとContent Blocksを翻訳できます。"
page_type: partner
search_tag: Partner

---

# Phrase

> [Phrase](https://phrase.com/)はローカライゼーション管理のためのクラウドベースのソフトウェアです。Phraseは翻訳ワークフローの自動化を可能にし、アジャイルチームの継続的なローカライゼーションをサポートします。

*この統合はPhraseによって管理されています。*

## 統合について {#about-the-integration}

PhraseとBrazeの統合により、Brazeインターフェイスを離れることなく、メールテンプレートとContent Blocksを翻訳できます。Braze向けPhrase TMS統合により、シームレスなローカライゼーションでカスタマーエンゲージメントを高め、新しい市場への成長を促進できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| Phrase TMSアカウント | このパートナーシップを利用するには、Phrase TMS UltimateまたはEnterpriseアカウントが必要です。 |
| Braze REST APIキー | すべての権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**Settings** > **API Keys**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

## ステップ1:Phrase TMSの設定 {#step-1-phrase-tms-settings}

Phraseで、**Settings > Integrations > Connectors > New**の順に進みます。

1. 接続の名前を入力し、タイプを**Braze**に変更します。<br><br>
2. REST APIキーとBraze RESTエンドポイントを入力します。<br><br>
3. コネクターがリンクされたContent Blocksを含むメールテンプレートをインポートする方法を選択します。
- 選択したメールテンプレートのみ
- Content Blocksを含める<br><br>
4. コネクターがメールテンプレートの翻訳をエクスポートする方法を選択します。
- 新規アイテムを作成
- 元のアイテム
  - 元のアイテムを選択すると、同じテンプレート/ブロックに翻訳がエクスポートされます。言語セグメントは、指定された属性によって定義されます。<br><br>
    {% raw %}
    元のアイテムが選択されている場合は、言語属性を入力します。言語属性はif/elsif引数の言語を定義します。元のアイテムオプションを使用している場合は、以下のように構造化する必要があります。

    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
    danish content
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
    portuguese content
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
    swedish content
    {% else %}
    Original content
    {% endif %}
    ```
    または、assignキー/値マッピングを使用します。
    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
      {% assign abc_key1 = "danish_value1" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
      {% assign abc_key = "portuguese value" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
      {% assign abc_key = "swedish value" %}
    {% else %}
      {% assign abc_key = "Source language value" %}
    {% endif %}
    ```
    上記のLiquidに厳密に従う必要がありますが、言語属性と言語、キー、および値は調整可能です。<br><br>
    各言語コードは1回のみ使用できますが、複数の言語を1つのセグメントに使用できます。たとえば、次のようになります。
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. **Test connection**をクリックします。接続に成功するとチェックマークが表示されます。アイコンの上にマウスポインタを置くと、詳細が表示されます。<br><br>
7. 最後に、**Save**をクリックします。このコネクターは**Connectors**ページで使用可能になります。

## ステップ3:コンテンツをPhraseに送信してBrazeにエクスポートする {#step-3-send-content-to-phrase-and-export-back-to-braze}

1. まず[submitter portal](https://support.phrase.com/hc/en-us/articles/5709602111132)を設定して、送信者がオンラインリポジトリからファイルを直接リクエストに追加できるようにします。<br><br>
2. 指定されたワークフロー状態の変更が検出されたときにPhrase TMSが新しいプロジェクトを自動的に作成するようにするには、[Automated Project Creation (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356)を使用します。<br><br>
3. 選択されたコンテンツアイテムは、APCの初回実行時にインポートされます。

[Connector API](https://cloud.memsource.com/web/docs/api#)を使用すると、UIで手動で実行するステップを自動化できます。[Webhook](https://support.phrase.com/hc/en-us/articles/5709693398812)を使用して、Phrase TMSが特定のイベント（ジョブのステータス変更など）についてサードパーティのシステムに通知するようにできます。
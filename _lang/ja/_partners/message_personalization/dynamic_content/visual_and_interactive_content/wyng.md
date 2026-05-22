---
nav_title: Wyng
article_title: Wyng
description: "このリファレンス記事では、マイクロエクスペリエンス、顧客嗜好ポータル、APIプラットフォームを通じて顧客の嗜好や属性を収集、利用、統合するために使用されるゼロパーティデータプラットフォームであるBrazeとWyngのパートナーシップについて概説しています。"
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng](https://wyng.com/)は、インタラクティブなデジタルエクスペリエンス（クイズ、ユーザー設定センター、プロモーション）を構築するツールを提供し、重要な瞬間に消費者をエンゲージし、嗜好やその他のゼロパーティデータを収集し、リアルタイムでパーソナライズします。

_この統合はWyngによって管理されています。_

## 統合について {#about-the-integration}

BrazeとWyngの統合により、Wyngのエクスペリエンスから取得したゼロパーティデータを利用して、Braze キャンペーンとBraze キャンバスでインタラクションをパーソナライズできます。また、Wyngではユーザー設定センターにより、消費者がブランドと共有するデータや好み（好みのコミュニケーション方法など）をコントロールできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Wyngアカウント | このパートナーシップを活用するには、Wyngアカウントが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**Settings** > **API Keys**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1：Braze統合を接続する {#step-1-connect-the-braze-integration}

Wyngで、[**Integrations**](https://wyng.com/dashboard/integrations/)に移動し、**Add**タブを選択します。次に、**Braze**にマウスを合わせ、**Connect**をクリックして統合します。

![WyngプラットフォームのBrazeパートナータイル。]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### ステップ2：Brazeコネクターを設定する {#step-2-configure-the-braze-connector}

1. 表示される設定ウィンドウで、Braze REST APIキーを指定します。
![認証情報プロンプトの画面。]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. 次にドロップダウンを使用して、Brazeと共有するWyngキャンペーンを選択します。![Brazeと共有する既存のWyngキャンペーンを選択するように求めるBrazeコネクター。]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. 次に、サブスクリプション、属性オブジェクトとイベントオブジェクト、およびカスタムイベントを設定する必要があります。<br><br>
- **サブスクリプションの設定（必須）**<br>
ユーザーをサブスクリプショングループに登録するには、**Add Subscription**をクリックし、サブスクリプショングループの名前とIDを追加します。複数のグループ名とIDを追加するには、**Add Subscription**ボタンを再度クリックします。<br>![サブスクリプショングループの名前とIDの入力を促す画面。]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **ユーザートラックの設定**<br>
**Add custom property**をクリックして、`/users/track`エンドポイントに送信する属性とイベントオブジェクトのペアを追加します。これを使用して、統合のために送信される各データトランザクションのハードコーディングされた属性値を追加します。複数のプロパティを追加するには、**Add custom property**ボタンを再度クリックします。<br>![属性のカスタムプロパティの追加を促す画面。]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **カスタムイベントの送信**<br>
オプションで、**Sending custom event**を有効にすることができます。有効にした場合、イベント名と対応するアプリIDを含める必要があります。<br>![必要に応じてカスタムイベントの送信を促す画面。]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. 最後に、ユースケースに基づいてWyngのフィールドをBraze APIのフィールドにマッピングする必要があります。**Select a field**をクリックしてマッピングするフィールドを選択し、その後、統合を**Save**します。保存すると、これらのマッピングされたフィールドは**Integrations** > **Manage**の下で確認できます。
![特定のBrazeフィールドにマッピングできるさまざまなWyngフィールドの例。]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![使用可能なシンクフィールドの一覧。]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### ステップ3：統合をテストする {#step-3-test-your-integration}

Wyngで、Wyngキャンペーンのフォームを送信してテストします。メインの本番キャンペーンにレコードを追加したくない場合は、プレビューキャンペーンでフォームを送信することもできます。**Integration**ダッシュボードに、正常に完了したトランザクションが表示されます。

## この統合を使う {#using-this-integration}

データコネクターが配置されると、Wyngで作成されBrazeに追加されたフィールドを、他のデータフィールドと同様に使用して、キャンペーンのトリガー、オーディエンスのセグメンテーション、パーソナライズされたコンテンツのフィードを行うことができます。

用途は幅広いため、具体的なご質問がある場合には、[contact@wyng.com](mailto:contact@wyng.com)または担当のアカウントマネージャーにお問い合わせください。

## トラブルシューティング {#troubleshooting}

### 送信の失敗 {#failed-submission}

Brazeへのデータ送信時に送信が失敗した場合、**View Log**リンクをクリックして、失敗した送信と関連するエラーメッセージを確認します。

![アクションヘッダーの下にある「View Log」リンク。]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

ログページには、失敗した送信、再試行回数、送信されたデータ、エラー、および送信を再プッシュするためのリンクが表示されます。

![失敗した送信が表示される例。]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

**View Error**セクションには、エラーコードとエラーの原因に関する追加情報が表示されます。その後、Brazeでエラーコードを相互参照し、原因を特定できます。

![Wyngプラットフォームに表示されるエラーログの例。]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

その他のご質問がある場合は、Wyngサポート（[support@wyng.com](mailto:contact@wyng.com)）にお問い合わせください。
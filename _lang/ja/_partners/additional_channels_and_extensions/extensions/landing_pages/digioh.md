---
nav_title: Digioh
article_title: Digioh
description: "この参考記事では、BrazeとDigiohのパートナーシップについて概説しています。Digiohは、ポップアップ、フォーム、アンケート、コミュニケーションのユーザー設定センターを作成し、Brazeのキャンペーンを通じてエンゲージメントを促進する調査プラットフォームです。"
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/)は、リストの増加、ファーストパーティデータの取得、およびBrazeのキャンペーンでのそのデータの活用をサポートします。

_この統合はDigiohによって管理されています。_

## 統合について {#about-the-integration}

BrazeとDigiohの統合により、ドラッグ＆ドロップビルダーを使用して、顧客とつながるオンブランドのフォーム、ポップアップ、ユーザー設定センター、ランディングページ、アンケートを作成できます。Digiohは統合セットアップを支援し、最初のキャンペーンの構築、デザイン、起動をサポートします。

!["Digiohで柔軟性の高いメールとコミュニケーションのユーザー設定センターを作成する"]({% image_buster /assets/img/digioh/pref_pop_examples.png %}){: style="border:0"}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Digiohアカウント | このパートナーシップを活用するには、[Digiohアカウント](https://www.digioh.com/)が必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze API `/users/track/` エンドポイント | `/users/track/` の詳細が付加されたRESTエンドポイントURLです。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/api/basics/#endpoints)に応じて異なります。<br><br>たとえば、REST APIエンドポイントが `https://rest.iad-01.braze.com` の場合、`/users/track/` エンドポイントは `https://rest.iad-01.braze.com/users/track/` になります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Digiohを統合するには、まずBrazeコネクターを設定する必要があります。完了したら、ライトボックス（ウィジェット）に統合を適用する必要があります。[Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/)にアクセスして、統合の基礎についてお読みください。

### ステップ1:Digioh統合を作成する {#step-1-create-digioh-integration}

Digiohで**Integrations**タブをクリックし、次に**New Integration**ボタンをクリックします。**Integration**ドロップダウンから**Braze**を選択し、統合に名前を付けます。

!["ドロップダウンから正しい統合を選択する"]({% image_buster /assets/img/digioh/2.png %}){: style="max-width:50%;"}

次に、Braze REST APIキーとBraze API `/users/track/` エンドポイントを入力します。

最後に、マップフィールドセクションを使って、メールと名前以外のカスタムフィールドをマッピングします。次のコードスニペットは、ペイロードの例を示しています。完了したら、**Create Integration**を選択します。

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### ステップ2:Digiohライトボックスを作成する {#step-2-create-a-digioh-lightbox}

Digiohの[デザインエディター](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)を使用してライトボックス（ウィジェット）を作成します。<br>
デザインエディターの活用方法のギャラリーに興味がありますか？Digiohの[テーマギャラリー](https://www.digioh.com/theme-gallery)をご覧ください。

### ステップ3:統合を適用する {#step-3-apply-integration}

この統合をDigiohの[ライトボックス](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/)に適用するには、**Boxes**ページに移動し、**Integrations**カラムの**Add**または**Edit**リンクを選択します。これはエディターの**Integration**セクションからも追加できます。

!["統合をライトボックスに追加する"]({% image_buster /assets/img/digioh/3.png %}){: style="max-width:90%"}

ここで**Add Integration**を選択し、目的の統合を選択して**Save**をクリックします。Digiohは、キャプチャしたリードをリアルタイムでBrazeに渡します。
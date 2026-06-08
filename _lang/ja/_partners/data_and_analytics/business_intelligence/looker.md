---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "このリファレンス記事では、Brazeとビジネスインテリジェンスおよびビッグデータ分析プラットフォームであるLookerとのパートナーシップについて説明します。"
page_type: partner
search_tag: Partner

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomlooker-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderlooker}

> ビジネスインテリジェンスおよびビッグデータ分析プラットフォームである [Looker](https://looker.com/) を使用すると、リアルタイムのビジネス分析をシームレスに探索、分析、共有できます。

BrazeとLookerの統合により、会社ユーザーはREST APIを介してファーストパーティの[Looker Blocks](#looker-blocks)と[Looker Actions](#looker-actions)のユーザーフラグ機能を活用できます。フラグを設定したユーザーをセグメントに追加して、将来のBraze キャンペーンやキャンバスを[ターゲット](#segment-users)にすることができます。LookerをBrazeと併用するには、[Braze Currentsを使用してデータウェアハウス]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/)にBrazeデータを送信し、Braze Looker Blocksを使用してLookerでBrazeデータを素早くモデル化および視覚化することをお勧めします。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Lookerアカウント | このパートナーシップを活用するには、[Lookerアカウント](https://looker.com/)が必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents/)に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

#### 注意事項 {#considerations}

- このプロセスは、ピボットされていないデータに対してのみ機能します。
- APIは一度に最大100,000行を処理します。
- ユーザーの最終的なフラグの数は、重複や非ユーザーが原因で少なくなる可能性があります。

## 統合 {#integration}

### Looker Blocks {#looker-blocks}

Looker Blocksにより、Brazeのお客様は[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)で提供される詳細なデータのビューに素早くアクセスできるようになります。Brazeのブロックは、Currentsデータ用に事前に作成された視覚化とモデリング機能を提供するため、Brazeのお客様はリテンションなどの分析パターンを容易に実装し、メッセージの配信可能性を評価し、ユーザーの動作をより細かく確認することなどができます。

Looker Blocksを実装するには、GitHubコードのREADMEファイルの指示に従ってください。
- [メッセージエンゲージメント分析ブロック README](https://github.com/llooker/braze_message_engagement_block/blob/master/README.md)
- [ユーザー動作分析ブロック README](https://github.com/llooker/braze_retention_block/blob/master/README.md)

どちらの統合も、[初回のBraze統合]({{site.baseurl}}/user_guide/get_started/sdk_overview/)と、Looker互換の[データウェアハウス](https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)とのBraze統合が、必要なデータを取り込んで送信するように適切に設定されていることを前提としています。


{% alert important %}
Brazeは[Snowflake](https://www.snowflake.com/)をデータウェアハウスとして使用してLooker Blocksを構築しています。ブロックはできるだけ多くのデータウェアハウスで動作することを目指していますが、SQL関数の中には方言によって利用可能性、構文、動作が異なるものがあります。
{% endalert %}

{% alert warning %}
さまざまな命名規則に注意してください！カスタム名は、対応する名前をすべて変更しない限り、データの不整合を引き起こす可能性があります。ビュー名、テーブル名、モデル名をカスタマイズしている場合は、LookML内のそれぞれの名前を、選択した名前に変更してください。
{% endalert %}

#### 利用可能なブロック {#available-blocks}

| ブロック | 説明 |
|---|---|
| メッセージエンゲージメント分析ブロック | このブロックには、プッシュ、メール、アプリ内メッセージ、Webhook、コンバージョン、キャンバスエントリ、およびキャンペーンコントロールグループ登録イベントに関するデータが含まれます。<br><br>この[Lookerブロック](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)の詳細については、[GitHubのコード](https://github.com/llooker/braze_message_engagement_block)をご確認ください。 |
| ユーザー動作分析ブロック | このブロックには、カスタムイベント、購入、セッション、ロケーションイベント、アンインストールに関するデータが含まれます。<br><br>この[Lookerブロック](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)の詳細については、[GitHubのコード](https://github.com/llooker/braze_retention_block)をご確認ください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Available Blocks" }

### Looker Actions {#looker-actions}

Looker Actionsを使用すると、Looker LookからREST APIエンドポイントを介してBraze内のユーザーにフラグを設定できます。アクションを使用するには、ディメンションに `braze_id` というタグが付けられている必要があります。アクションは、フラグを設定した値をユーザーの `looker_export` カスタム属性に追加します。

{% alert important %}
フラグが設定されるのは既存のユーザーのみです。Brazeでデータにフラグを設定する場合、ピボットされたLookは使用できません。
{% endalert %}

#### ステップ1:Braze Lookerアクションを設定する {#step-1-set-up-a-braze-looker-action}

Braze REST APIキーとRESTエンドポイントを使用して、Braze Lookerアクションを設定します。

![Looker Brazeの設定ページ。Braze APIキーとBraze REST APIエンドポイントのフィールドがあります。]({% image_buster /assets/img/braze-looker-action.png %})

#### ステップ2:Looker Developをセットアップする {#step-2-set-up-looker-develop}

Looker Develop内で、適切なビューを選択します。ディメンションタグに `braze_id` を追加し、変更をコミットします。
この `braze_id` タグは、どのフィールドがユニークキーであるかを決定するために使用されます。

```lookml
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**必ず変更をコミットしてください。Lookerアクションは本番環境の設定でのみ機能します。**

#### ステップ3:タグにユーザー属性を設定する {#step-3-set-user-attributes-in-tags}

オプションで、`braze[]` タグを使用し、属性名を括弧で囲んで属性を設定することもできます。たとえば、カスタム属性 `user_segment` を送信する場合、タグは `braze[user_segment]` になります。

以下の制限に注意してください:
- 属性は、**Look内のフィールドとして含まれている**場合にのみ送信されます。
- サポートされているタイプは `Strings`、`Boolean`、`Numbers`、`Dates` です。
- 属性名は大文字と小文字を区別します。
- [標準ユーザープロファイル]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields)名と完全に一致する限り、標準属性も設定できます。
- 完全なタグは引用符で囲む必要があります。例: `tags: ["braze[first_name]"]`。他のタグを割り当てることもできますが、無視されます。
- 追加情報は [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze) で確認できます。

#### ステップ4:Lookerアクションを送信する {#step-4-send-the-looker-action}

1. `braze_id` ディメンションが選択されているLook内で、右上の設定の歯車（<i class="fas fa-cog"></i>）をクリックし、**Send...** を選択します。
2. カスタムBrazeアクションを選択します。
3. **Unique Key** で、Brazeアカウントのプライマリユーザーマッピングキー（`external_id` または `braze_id`）を入力します。
4. エクスポートに名前を付けます。指定されない場合は `LOOKER_EXPORT` が使用されます。
5. **Advanced Options** で、**Results in Table** または **All Results** を選択し、**Send** をクリックします。<br><br>![]({% image_buster /assets/img/send-looker-action.png %})<br><br>エクスポートが正しく送信された場合、`LOOKER_EXPORT` は、アクションに入力した値を含むカスタム属性としてユーザーのプロファイルに表示されます。<br><br>![]({% image_buster /assets/img/custom-attributes-looker.png %})

##### 送信APIの例 {#example-outgoing-api}

以下に、[`/users/track/` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)に送信される送信API呼び出しの例を示します。

###### ヘッダー {#header}
```
Authorization: Bearer [API_KEY]
```

###### 本文 {#body}
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Brazeでユーザーをセグメント化する {#segment-users}

Brazeでこれらのフラグ付きユーザーのセグメントを作成するには、**エンゲージメント**の下の**セグメント**に移動し、セグメントに名前を付け、フィルターとして **Looker_Export** を選択します。次に、「includes value」オプションを使用し、Lookerで割り当てたカスタム属性フラグを指定します。

![Brazeのセグメントビルダーで、フィルター「looker_export」が「includes_value」と「Looker」に設定されています。]({% image_buster /assets/img/braze_segments.png %})

保存すると、キャンバスやキャンペーン作成時のターゲットユーザーステップでこのセグメントを参照できます。

## トラブルシューティング {#troubleshooting}
Lookerアクションに問題がある場合は、テストユーザーを[内部グループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/)に追加し、以下を確認してください。

* APIキーに `users.track` 権限がある。
* 正しいRESTエンドポイントが入力されている（例: `https://rest.iad-01.braze.com`）。
* ディメンションビューで `braze_id` タグが設定されている。
* クエリにIdディメンションまたは属性が列として含まれている。
* Lookerの結果がピボットされていない。
* ユニークキーが正しく選択されている。通常は `external_id` です。
* ディメンションの `braze_id` はAPIの `braze_id` とは異なります。ディメンションの `braze_id` は、Braze APIの `id` フィールドであることを示すために使用されます。ほとんどの場合、送信時には `external_id` がプライマリキーとなります。
* `external_id` ユーザーがBrazeプラットフォームに存在する。
* `looker_export` フィールドが `Braze Platform > Settings > Manage Settings > Custom Attributes` の下で `Automatically Detect` として設定されている。
* 変更がプロダクションにコミットされている。Lookerアクションは本番環境の設定で機能します。
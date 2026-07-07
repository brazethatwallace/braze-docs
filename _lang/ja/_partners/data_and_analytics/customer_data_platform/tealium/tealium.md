---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "このリファレンス記事では、BrazeとTealiumのパートナーシップについて説明します。Tealiumは、モバイル、Web、および代替データをサードパーティのソースに接続できるユニバーサルデータハブです。"
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/)は、EventStream、AudienceStream、およびiQ Tag Managementで構成されるユニバーサルデータハブおよび顧客データプラットフォームであり、サードパーティのソースからモバイルデータ、Webデータ、および代替データを接続できます。TealiumをBrazeと接続することで、カスタムイベント、ユーザー属性、購入のデータフローが実現し、リアルタイムでデータに基づいたアクションを実行できるようになります。

![さまざまなTealium製品とBrazeプラットフォームがどのように連携してクロスチャネルキャンペーンをリアルタイムでアクティブにするかを示すTealiumの概要図。]({% image_buster /assets/img/tealium/tealium_overview.png %}){: style="border:0;"}

BrazeとTealiumの統合により、ユーザーを追跡し、さまざまなユーザー分析プロバイダーにデータをルーティングできます。Tealiumでは次の操作ができます。
- [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream)でTealiumオーディエンスをBrazeに同期し、Brazeキャンペーンやキャンバスのパーソナライズ、またはセグメントの作成に使用できるようにします。
- [プラットフォーム間でデータをインポートします](#choose-your-integration-type)。Brazeは、Android、iOS、およびWebアプリケーション向けの[サイドバイサイド](#side-by-side-sdk-integration)SDK統合と、イベントデータをレポートできる任意のプラットフォームで使用できる[サーバー間](#server-to-server-integration)統合の両方を提供します。<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStreamは、データの中心に位置するデータ収集およびAPIハブです。EventStreamは、セットアップとインストールから、受信ユーザーデータの識別、検証、および拡張まで、データサプライチェーン全体を処理します。EventStreamは、イベントフィードとコネクターを使用してリアルタイムアクションを実行します。以下は、[EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/)を構成する機能です。
- データソース（インストールおよびデータ収集）
- ライブイベント（リアルタイムデータ検査）
- イベント仕様と属性（データレイヤー要件と検証）
- イベントフィード（フィルタリングされたイベントタイプ）
- イベントコネクター（APIハブアクション）

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStreamは、オムニチャネルの顧客セグメンテーションおよびリアルタイムアクションエンジンです。AudienceStreamはEventStreamに流入するデータを取得し、ブランドとのカスタマーエンゲージメントの最も重要な属性を表す訪問者プロファイルを作成します。設定手順については、[AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream)の記事を参照してください。

{% endtab %}
{% tab iQ Tag Management %}
Tealium iQでは、Tealium iQ Tag Management UIでタグを使用してアプリでコードをトリガーできます。このタグにより、モバイルおよびWebプラットフォームからイベントデータが収集、制御、および配信されます。これにより、アプリにBraze固有のコードを追加することなく、ネイティブのBraze実装を設定できます。ユーザーは、iQ Tag ManagementまたはJSON設定ファイルを使用してモバイルリモートコマンドを統合できます（Tealium推奨のアプローチ）。Braze Web SDKを使用するユーザーは、Web iQタグを使用して統合を行う必要があります。

各メソッドの長所と短所について詳しくは、以下の[Tealium iQタグマネージャー](#mobile-remote-commands)セクションを参照してください。
{% endtab %}
{% endtabs %}

{% alert important %}
Tealiumは、バッチと非バッチの両方のコネクターアクションを提供します。非バッチコネクターは、リアルタイムリクエストがユースケースにとって重要であり、BrazeのAPIレート制限仕様に達する懸念がない場合に使用してください。ご質問がある場合は、Brazeサポートまたはカスタマーサクセスマネージャーにお問い合わせください。<br><br>

バッチコネクターの場合、リクエストは以下のいずれかのしきい値が満たされるまでキューに入れられます。<br><br>
- 最大リクエスト数：75
- 最も古いリクエストからの最大経過時間：10分
- リクエストの最大サイズ：1 MB

Tealiumは、デフォルトでは同意イベント（サブスクリプション設定）またはユーザー削除イベントをバッチ処理しません。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Tealiumアカウント | このパートナーシップを活用するには、サーバーおよび/またはクライアントサイドアクセスを持つ[Tealiumアカウント](https://my.tealiumiq.com/)が必要です。 |
| インストールされたソースとTealiumソースの[ライブラリ](https://docs.tealium.com/platforms/) | モバイルアプリ、Webサイト、バックエンドサーバーなど、Tealiumに送信されるデータの提供元。<br><br>適切なTealiumコネクターを設定できるようにするには、ライブラリをアプリ、サイト、サーバーにインストールしておく必要があります。 |
| Braze RESTおよびSDKエンドポイント | RESTまたはSDKエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/api/basics#endpoints)に応じて異なります。 |
| Brazeアプリ識別子キー（サイドバイサイドのみ） | アプリ識別子キー。<br><br>これは、**Brazeダッシュボード > 設定の管理 > APIキー**で確認できます。 |
| コードバージョン（サイドバイサイドのみ） | SDKバージョンに対応し、major.minor形式である必要があります（3.0.1ではなく3.2など）。コードバージョンは3.0以上である必要があります。 |
| REST APIキー（サーバー間のみ） | `users.track`および`users.delete`権限を持つBraze REST APIキー。<br><br>これは**Brazeダッシュボード > 開発者コンソール > REST APIキー > 新しいAPIキーを作成**で作成できます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合タイプを選択する {#choose-your-integration-type}

| 統合 | 詳細 |
| ----------- | ------- |
| [サイドバイサイド](#side-by-side-sdk-integration) | TealiumのSDKを使用して、イベントをBrazeのネイティブ呼び出しに変換します。これにより、サーバー間統合よりも高度な機能にアクセスでき、Brazeをより包括的に使用できるようになります。<br><br>Brazeのリモートコマンドを使用する場合は、TealiumがすべてのBrazeメソッド（Content Cardsなど）に対応しているわけではないことに注意してください。対応するリモートコマンドにマッピングされていないBrazeメソッドを使用するには、ネイティブBrazeコードをコードベースに追加してメソッドを呼び出す必要があります。|
| [サーバー間](#server-to-server-integration) | TealiumからBraze REST APIエンドポイントにデータを転送します。<br><br>アプリ内メッセージング、Content Cards、プッシュ通知などのBraze UI機能はサポートされていません。また、このメソッドでは利用できないデバイスレベルのフィールドなど、自動的にキャプチャされるデータも存在します。<br><br>これらの機能を使用する場合は、サイドバイサイド統合を検討してください。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="統合タイプを選択する" }

## サイドバイサイドSDK統合 {#side-by-side-sdk-integration}

### リモートコマンド {#remote-commands}

リモートコマンドは、Tealium iOSおよびAndroidライブラリの機能であり、Tealium SDKからBrazeサーバーを介してBrazeへの呼び出しを実行できるようにします。Brazeリモートコマンドモジュールは、必要なBrazeライブラリを自動的にインストールおよびビルドし、すべてのメッセージレンダリングと分析トラッキングを処理します。Brazeモバイルリモートコマンドを使用するには、アプリにTealiumライブラリがインストールされている必要があります。

Tealiumには、モバイルリモートコマンドを統合する2つの方法があります。統合タイプ間で機能が失われることはなく、基礎となるネイティブコードは同じです。

| モバイルリモートコマンド方式 | 長所 | 短所 |
| --- | --- | --- |
| **リモートコマンドタグ** | Tealium iQ UIを使用して、リモートコマンドに送信されるデータとマッピングを簡単に変更できます。<br><br>これにより、アプリがすでにアプリストアに公開された後でも、クライアントがアプリを更新する必要なく、追加のデータまたはイベントをサードパーティSDKに送信できます。 | アプリのタグマネジメントモジュールは、非表示のWebビューに依存してJavaScriptを処理します。 |
| **JSON設定ファイル**<br>([推奨](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | JSONメソッドを使用すると、アプリで非表示のWebビューを使用する必要がなくなり、メモリ使用量が大幅に削減されます。<br><br>JSONファイルは、顧客のアプリ内でリモートまたはローカルにホストできます。 | 現時点では、これを管理するUIがないため、少し手間がかかります。<br><br>注：Tealiumは、この問題を解決し、iQ Tag Managementバージョンと同じレベルの柔軟性をJSONリモートコマンドに取り入れるManagement UIの追加に取り組んでいます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="リモートコマンド" }

Brazeモバイルリモートコマンドのデータマッピングを使用して、デフォルトのユーザー属性とカスタム属性を設定し、購入とカスタムイベントを追跡します。対応するBrazeメソッドについては、次の表を参照してください。

| リモートコマンド | Brazeメソッド |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| emailnotification | setEmailNotificationSubscriptionType() |
| incrementcustomattribute | incrementCustomAttribute() |
| initialize | startWithApiKey() |
| logcustomevent | logCustomEvent() |
| logpurchase | logPurchase() |
| pushnotification | setPushNotificationSubscriptionType() |
| removecustomattribute | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| userattribute | ABKUser() |
| useridentifier | changeUser() |
{: .reset-td-br-1 .reset-td-br-2 aria-label="リモートコマンド" }

Brazeモバイルリモートコマンドの設定方法の詳細と、サポートされているメソッドの概要については、Tealium開発者ドキュメントを参照してください。
- [リモートコマンド](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [リモートコマンドタグ](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Brazeモバイルリモートコマンドは、すべてのBrazeメソッドとメッセージングチャネルをサポートしているわけではありません（Content Cardsなど）。対応するリモートコマンドにマッピングされていないBrazeメソッドを使用するには、ネイティブBrazeコードをコードベースに追加してメソッドを直接呼び出す必要があります。
{% endalert%}

### Braze Web SDKタグ {#braze-web-sdk-tag}

Braze Web SDKタグを使用して、WebサイトにBraze Web SDKをデプロイします。[Tealium iQ Tag Management](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)により、顧客は訪問者のアクティビティを追跡するためにTealiumダッシュボード内でタグとしてBrazeを追加できます。タグは一般的に、オンライン広告、メールマーケティング、およびサイトのパーソナライゼーションの効果を理解する目的でマーケターにより使用されます。

1. Tealiumで**iQ > Tags > + Add Tag > Braze Web SDK**に移動します。
2. Tag Configurationダイアログボックスで、APIキー（Brazeアプリ識別子キー）、ベースURL（Braze SDKエンドポイント）、および[Braze Web SDKコードバージョン](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)を入力します。また、ロギングを有効にして、デバッグ目的でWebコンソールに情報を記録することもできます。
3. [Load Rules](https://docs.tealium.com/iq-tag-management/load-rules/about/)ダイアログボックスで「Load on All Pages」を選択するか、**Create Rule**を選択して、サイトでこのタグのインスタンスをいつどこに読み込むかを決定します。
4. **[Data Mappings](https://docs.tealium.com/iq-tag-management/data-mappings/about/)**ダイアログボックスで、**Create Mappings**を選択してTealiumデータをBrazeにマッピングします。Braze Web SDKタグの宛先変数は、タグの**Data Mapping**タブに組み込まれています。[これらの表](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)に、使用可能な宛先カテゴリと、それぞれの宛先名の説明が示されています。
5. **Finish**を選択します。

### サイドバイサイド統合のリソース {#side-by-side-integrations-resources}

- iOSリモートコマンド：[Tealiumドキュメント](https://docs.tealium.com/platforms/remote-commands/integrations/braze/)、[Tealium GitHubリポジトリ](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Androidリモートコマンド：[Tealiumドキュメント](https://docs.tealium.com/platforms/remote-commands/integrations/braze/)、[Tealium GitHubリポジトリ](https://github.com/Tealium/tealium-android-braze-remote-command)
- Web SDKタグ：[Tealiumドキュメント](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## サーバー間統合 {#server-to-server-integration}

この統合により、TealiumからBraze REST APIにデータが転送されます。

サーバー間統合では、アプリ内メッセージング、Content Cards、プッシュ通知などのBraze UI機能はサポートされていません。また、このメソッドでは利用できないデバイスレベルのフィールドなど、自動的にキャプチャされるデータも存在します。

このデータとこれらの機能を使用する場合は、[サイドバイサイド]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium#side-by-side-sdk-integration)SDK統合を検討してください。

### ステップ1:ソースを設定する {#step-1-set-up-a-source}

Tealiumでは最初に、コネクターの取得元となる有効なデータソースを設定する必要があります。
1. Tealiumのサイドバーの**Server-Side**から**Sources > Data Sources > + Add Data Source**に移動します。
2. 使用可能なカテゴリ内で目的のプラットフォームを見つけ、ソースに名前を付けます。これは必須フィールドです。<br>![プラットフォーム選択とソース名フィールドを含むTealiumのデータソース追加ダイアログ。]({% image_buster /assets/img/tealium/data_source.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. **Event Specifications**オプションから、含める[イベント仕様](https://docs.tealium.com/server-side/event-specifications/about/)を選択します。イベント仕様は、インストールで追跡するイベント名と必須属性を特定するのに役立ちます。これらの仕様は受信イベントに適用されます。<br>![データソースのTealiumイベント仕様オプション。]({% image_buster /assets/img/tealium/event_specs.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>どのデータが最も価値があるか、どの仕様がユースケースに最も適しているか、時間をかけて検討してください。[カスタムイベント仕様](https://docs.tealium.com/iq-tag-management/events/about/)も利用可能です。<br>
4. 次のダイアログで**Get Code**ステップに進みます。ここで提供されるベースコードとイベント追跡コードは、インストールガイドとして機能します。これらの手順をチームと共有したい場合は、提供されたPDFをダウンロードしてください。完了したら**Save & Continue**を選択します。<br>
5. これで、保存したソースを表示し、イベント仕様を追加または削除できます。<br>![イベント仕様と接続の詳細を含む保存済みTealiumデータソース。]({% image_buster /assets/img/tealium/braze_connection.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>詳細なデータソースビューから、次のアクションを実行できます。
- データソースキーの表示とコピー
- インストール手順の表示
- **Get Code**ページに戻る
- イベント仕様の追加または削除
- イベント仕様に関連するライブイベントの表示
- その他<br>
6. 最後に、ページの上部にある**Save / Publish**を選択します。ソースを公開しないと、Brazeコネクターの設定時にソースを見つけることができません。

データソースの設定と編集の詳細な手順については、[データソース](https://docs.tealium.com/server-side/data-sources/about-data-sources/)を参照してください。

### ステップ2:イベントコネクターを作成する {#step-2-create-an-event-connector}

コネクターとは、Tealiumと他のベンダーの間でデータを伝送するために使用される統合です。これらのコネクターには、パートナーがサポートするAPIを表すアクションが含まれています。

1. Tealiumのサイドバーの**Server-Side**から**EventStream > Event Connectors**に移動します。
2. 青色の**+ Add Connector**ボタンを選択して、コネクターマーケットプレースを参照します。表示される新しいダイアログボックスで、スポットライト検索を使用して**Braze**コネクターを見つけます。
3. このコネクターを追加するには、**Braze**コネクタータイルを選択します。クリックすると、接続の概要と、必要な情報、サポートされるアクション、および設定手順の一覧が表示されます。この設定は、ソース、設定、アクションの3つのステップで構成されています。

#### ソース {#source}

ソースの設定が完了したら、**EventStream** > **Event Connectors** > **+ Add Connector** > **Braze**のBrazeコネクターページに戻ります。

作成したデータソースを選択し、**Event Feed**で**All Events**または特定のイベント仕様を選択します。変更された値のみをBrazeに送信する推奨パスです。**Continue**を選択します。

#### 設定 {#configuration}

次に、ページの下部で**Add Connector**を選択します。コネクターに名前を付け、BrazeのAPIエンドポイントとBraze REST APIキーを指定します。

![APIエンドポイントとREST APIキーフィールドを含むBrazeコネクター設定。]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%"}

以前にコネクターを作成したことがある場合は、利用可能なコネクターリストにある既存のコネクターを使用し、鉛筆アイコンでニーズに合わせて変更するか、ゴミ箱アイコンで削除することができます。

#### アクション {#action}

次に、コネクターアクションに名前を付け、設定するマッピングに従ってデータを送信するアクションタイプを選択します。ここでは、Brazeの属性、イベント、および購入をTealiumの属性、イベント、および購入名にマッピングします。

{% alert important %}
提供されるすべてのフィールドが必要なわけではありません。

![オプションフィールドが折りたたまれたTealiumコネクターアクション。]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab ユーザーの追跡 - バッチおよび非バッチ %}

このアクションを使用すると、ユーザー、イベント、購入属性をすべて1回のアクションで追跡できます。

| パラメータ | 説明 |
| ---------- | ----------- |
| ユーザーID | このフィールドを使用して、TealiumのユーザーIDフィールドをBrazeの対応するフィールドにマッピングします。1つ以上のユーザーID属性をマッピングします。複数のIDが指定されている場合、最初の非空白値が次の優先順位に基づいて選択されます：External ID、Braze ID、エイリアス名、エイリアスラベル。<br><br>- プッシュトークンをインポートする場合は、External IDとBraze IDを指定しないでください。<br>- ユーザーエイリアスを指定する場合、エイリアス名とエイリアスラベルの両方を設定する必要があります。<br><br>詳細については、Brazeの[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を参照してください。 |
| ユーザー属性 | 既存のBrazeのユーザープロファイルのフィールド名を使用して、Brazeダッシュボードのユーザープロファイル値を更新するか、独自のカスタム[ユーザー属性]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens)データをユーザープロファイルに追加します。<br><br>- デフォルトでは、新規ユーザーが存在しない場合は作成されます。<br>- **Update Existing Only**を`true`に設定すると、既存のユーザーのみが更新され、新しいユーザーは作成されません。<br>- Tealium属性が空の場合、その属性はNULLに変換され、Brazeユーザープロファイルから削除されます。ユーザー属性を削除する目的でBrazeにNULL値を送信すべきでない場合は、エンリッチメントを使用してください。 |
| ユーザー属性の変更 | このフィールドを使用して、特定のユーザー属性を増減します<br><br>- 整数属性は、正の整数または負の整数でインクリメントできます。<br>- 配列属性は、既存の配列に値を追加または削除することで変更できます。 |
| イベント | イベントは、タイムスタンプの時点で特定のユーザーによりカスタムイベントが1回発生したことを表します。このフィールドは、Brazeの[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object)の属性と同様にイベント属性を追跡、マッピングする場合に使用します。<br><br>- イベント属性`Name`は、マッピングされたすべてのイベントで必要です。<br>- イベント属性`Time`は、明示的にマッピングされていない限り、自動的に現時点の時刻に設定されます。<br>- デフォルトでは、新しいイベントは存在しない場合に作成されます。`Update Existing Only`を`true`に設定すると、既存のイベントのみが更新され、新規のイベントは作成されません。<br>- 配列型属性をマッピングして、複数のイベントを追加します。配列型の属性は等しい長さでなければなりません。<br>- 単一値属性を使用でき、各イベントに適用されます。 |
| イベントテンプレート | ボディデータで参照するイベントテンプレートを指定します。テンプレートを使用してデータを変換してから、Brazeに送信できます。詳細については、Tealiumの[テンプレートガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)を参照してください。 |
| イベントテンプレート変数 | イベントテンプレート変数をデータ入力として指定します。詳細については、Tealiumの[テンプレート変数ガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)を参照してください。 |
| 購入 | このフィールドは、Brazeの[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object)の属性と同様に購入属性を追跡、マッピングする場合に使用します。<br><br>- 購入属性`Product ID`、`Currency`、`Price`は、マッピングされたすべての購入に必要です。<br>- 購入属性`Time`は、明示的にマッピングされていない限り、自動的に現時点の時刻に設定されます。<br>- デフォルトでは、新規購入が存在しない場合は作成されます。`Update Existing Only`を`true`に設定すると、既存の購入のみが更新され、新規購入は作成されません。<br>- 配列型属性をマッピングして、複数の購入アイテムを追加します。配列型の属性は等しい長さでなければなりません。<br>- 単一値属性を使用でき、各アイテムに適用されます。|
| 購入テンプレート | テンプレートを使用して、Brazeに送信する前にデータを変換できます。<br>- ネストされたオブジェクトサポートが必要な場合は、購入テンプレートを定義します。<br>- 購入テンプレートを定義すると、アクションの購入セクションで設定された設定は無視されます。<br>- 詳細については、Tealiumの[テンプレートガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)を参照してください。|
| 購入テンプレート変数 | 商品テンプレート変数をデータ入力として指定します。詳細については、Tealiumの[テンプレート変数ガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アクション" }

![ユーザー属性、イベント、購入をマッピングするTealiumのユーザー追跡コネクターアクション。]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab ユーザーの削除 - 非バッチ %}

このアクションでは、Brazeダッシュボードからユーザーを削除できます。

| パラメータ | 説明 |
| ---------- | ----------- |
| ユーザーID | このフィールドを使用して、TealiumのユーザーIDフィールドをBrazeの対応するフィールドにマッピングします。<br><br>- 1つ以上のユーザーID属性をマッピングします。複数のIDが指定されている場合、最初の非空白値が次の優先順位に基づいて選択されます：External ID、Braze ID、エイリアス名、エイリアスラベル。<br>- ユーザーエイリアスを指定する場合、エイリアス名とエイリアスラベルの両方を設定する必要があります。<br><br>詳細については、Brazeの[`/users/delete`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アクション" }

![ユーザーIDマッピングを含むTealiumのユーザー削除コネクターアクション。]({% image_buster /assets/img/tealium/track_user_delete.png %})

選択したオプションを変更する場合は、**Back**を選択して編集するか、**Finish**を選択して完了します。

{% endtab %}
{% endtabs %}

**Continue**を選択します。

コネクターがTealiumホームページのコネクターリストに表示されます。<br>![Brazeを含む設定済みコネクターを一覧表示するTealiumホームページ。]({% image_buster /assets/img/tealium/summary_list.png %}){: style="max-width:80%;"}

完了したら、コネクターの**Save / Publish**を選択してください。設定したアクションは、トリガー接続が満たされたときに実行されます。

### ステップ3:Tealiumコネクターをテストする {#step-3-test-your-tealium-connector}

コネクターが稼動したら、正常に動作していることを確認するためにテストする必要があります。これを検証する最も簡単な方法は、Tealiumの**トレースツール**を使用することです。トレースの使用を開始するには、Tealium Toolsブラウザー拡張機能が追加されていることを確認してください。

1. 新しいトレースを開始するには、サイドバーの**Server-Side**のオプションから**Trace**を選択します。**Start**を選択し、トレースIDをキャプチャします。
2. ブラウザー拡張機能を開き、AudienceStream TraceにトレースIDを入力します。
3. リアルタイムログを調べます。
4. **Actions Triggered**エントリを選択して展開し、検証したいアクションを確認します。
5. 検証するアクションを探して、ログステータスを表示します。

Tealiumのトレースツールの詳しい実装手順については、Tealiumの[トレースドキュメント](https://docs.tealium.com/server-side/connectors/trace/about/)を参照してください。

## 統合デモ {#integration-demo}

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1mP84vVWifzNMN7eMYNORNy0y-WZurzBs/view?usp=sharing" title="Tealium統合デモ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## データポイントの潜在的な超過料金 {#potential-data-point-overages}

Tealiumを通じてBrazeを統合する際に、誤って不必要なデータポイントを記録してしまう可能性がある主な方法は3つあります。

### 重複データの送信 - Brazeの属性の差分のみを送信する {#sending-duplicate-data-only-send-braze-deltas-of-attributes}

Tealiumはユーザー属性のBraze差分を送信しません。たとえば、EventStreamアクションでユーザーの名、メール、および携帯電話番号を追跡している場合、このアクションがトリガーされると、Tealiumは3つの属性すべてをBrazeに送信します。Tealiumは、変更された内容や更新された内容を探してその情報のみを送信することはありません。

**解決策：**<br>バックエンドを確認して、属性が変更されているかどうかを評価し、変更されている場合は、Tealiumの関連メソッドを呼び出してユーザープロファイルを更新できます。**これは、Brazeを直接統合するユーザーが通常行う作業です。**<br>**または**<br>自分自身のユーザープロファイルをバックエンドに保存しておらず、属性が変更されたかどうかを判断できない場合は、AudienceStreamを使用して[エンリッチメントを作成](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/)し、値が変更されたときにのみユーザー属性を送信します。[エンリッチメントルール](https://docs.tealium.com/server-side-connectors/braze-connector/)に関するTealiumのドキュメントを参照してください。

### 無関係なデータの送信またはデータの不必要な上書き {#sending-irrelevant-data-or-needlessly-overwriting-data}

同じイベントフィードをターゲットとする複数のEventStreamがある場合、**そのコネクターに対して有効化されたすべてのアクション**は、単一のアクションがトリガーされるたびに自動的に発火します。その結果、Brazeでデータが上書きされ、不必要なデータポイントが記録される可能性もあります。

**解決策：**<br>それぞれのアクションを追跡するために、個別のイベント仕様またはフィードを設定します。<br>**または**<br>Tealiumダッシュボードのトグルを使用して、起動しないアクション（またはコネクター）を無効にします。

### Brazeの初期化が早すぎる {#initializing-braze-too-early}

Braze Web SDKタグを使用してTealiumと統合するユーザーの場合、MAUが大幅に増加する可能性があります。**Brazeがページ読み込み時に初期化されている場合、WebユーザーがWebサイトに初めてアクセスするたびに、Brazeによって匿名プロファイルが作成されます。**これにはボットトラフィックも含まれ、アクティブユーザー数が膨らむ可能性があります。MAU数を減らすために、「Signed In」や「Watched Video」などのアクションをユーザーが完了したときにのみユーザーの行動を追跡したい場合もあるでしょう。

**解決策：**<br>[読み込みルール](https://docs.tealium.com/iq-tag-management/load-rules/about/)を設定して、サイトでタグがいつどこに読み込まれるかを正確に決定します。ボットトラフィックのフィルタリングとSDKの条件付き初期化に関するより包括的なガイダンスについては、[ボットトラフィックのフィルタリング]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_bot-filtering)を参照してください。
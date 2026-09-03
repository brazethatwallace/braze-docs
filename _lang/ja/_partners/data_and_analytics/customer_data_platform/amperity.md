---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "このリファレンス記事では、BrazeとAmperityのパートナーシップについて概説しています。Amperityは包括的な企業向け顧客データプラットフォームであり、Amperityユーザーの同期、データの統合、AWS S3バケットを使用したBrazeへのデータ送信などを可能にします。"
page_type: partner
search_tag: Partner

---

# Amperity

> [Amperity](https://amperity.com/)は、包括的な企業向け顧客データプラットフォームであり、ブランドが顧客を理解し、戦略的な意思決定を行い、消費者により良いサービスを提供するために常に適切な行動を取れるよう支援します。Amperityは、データ管理の統合、分析、インサイト、およびアクティベーションにおけるインテリジェントな機能を提供します。

_この統合はAmperityによって管理されています。_

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

BrazeとAmperityの統合により、2つのプラットフォームにわたる顧客の統合ビューが提供されます。この統合により、以下のことが可能になります：
- **顧客プロファイルを同期する**：ユーザーデータとカスタム属性をAmperityからBrazeにマッピングします。
- **オーディエンスを作成して送信する**：アクティブな顧客とそれに関連付けられたカスタム属性のリストを返すセグメントを作成し、Brazeに送信します。
- **データの更新を管理する**：カスタム属性の更新をBrazeに送信する頻度を制御します。
- **データを統合する**：AmperityがサポートするさまざまなプラットフォームとBrazeでデータを統合します。
- **BrazeのデータをAmazon S3に同期する**：Braze Currentsを使用して、Brazeキャンペーンからのエンゲージメントデータを統合し、Apache AvroフォーマットでAmazon S3にデータを同期できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Amperityアカウント | このパートナーシップを活用するには、[Amperityアカウント](https://amperity.com/request-a-demo)が必要です。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。<br> これはBrazeダッシュボードの**開発者コンソール** > **REST APIキー** > **新しいAPIキーを作成**で作成できます。 |
| Brazeインスタンス | Brazeインスタンスは、Brazeオンボーディングマネージャーから入手するか、[API概要ページ]({{site.baseurl}}/api/basics#endpoints)で確認できます。 |
| Braze RESTエンドポイント | BrazeエンドポイントURL。エンドポイントはBrazeインスタンスに依存します。 |
| Currentsコネクター（オプション） | S3 Currentsコネクター。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## データマッピング {#data-mapping}

標準属性とカスタム属性の両方をAmperityからBrazeに送信できます。これにより、Amperityを通じてさまざまなソースのデータでBrazeの顧客プロファイルを強化できます。送信できる具体的な属性は、Amperityシステムのデータと、Brazeで設定した属性によって異なります。

これらの属性について以下で説明します。

### 標準属性 {#standard-attributes}

[プロファイル属性]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)は、顧客が誰であるかを示します。これらは多くの場合、次のような顧客の身元情報に関連付けられています：
- 名前
- 生年月日
- メールアドレス
- 電話番号

### カスタム属性 {#custom-attributes}

Brazeの[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)は、ブランドが決定するフィールドです。Brazeにすでに存在するカスタム属性をAmperityで管理したい場合は、Amperityから送信される出力を、Brazeワークスペースにすでにある名前に合わせてください。これには次のものが含まれます：
- 購入履歴
- ロイヤルティステータス
- 価値階層
- 最近のエンゲージメントデータ

AmperityからBrazeに送信されるカスタム属性の名前を確認してください。一致する名前がない場合、Amperityはカスタム属性を追加します。

カスタム属性は、Braze内で一致する`external_id`または`braze_id`を持つユーザーのみ更新されます。

### Amperityオーディエンス {#amperity-audiences}

AmperityからBrazeに同期されたオーディエンスは、カスタム属性としてユーザープロファイルに記録されます。これらは、Brazeでそれらのユーザーをターゲットにするために使用できます。

![カスタムデータカテゴリにカスタム属性が表示されたフィルターのドロップダウンリスト。]({% image_buster /assets/img/amperity/custom_attributes_filters.png %}){: style="max-width:60%;"}

![「l12m_frequency」や「l12m_monetary」などのカスタム属性のドロップダウンリスト。]({% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}){: style="max-width:40%;"}

### データタイプ {#data-types}

サポートされているデータタイプは以下の通りです：
- ブール値
- 日付
- 日時
- 小数
- フロート
- 整数
- 文字列
- 可変長文字列

使用されるデータタイプは属性の性質によって異なります。たとえば、メールアドレスは文字列で、顧客の年齢は整数です。

### 属性の重複 {#duplication-of-attributes}

デフォルトのユーザープロファイルフィールドと重複するカスタム属性の送信は避けてください。たとえば、誕生日はBraze標準属性項目と一致させるため、「dob」という名前のユーザープロファイルフィールドとしてBrazeに送信する必要があります。「birthday」、「Birthdate」、またはその他の文字列として送信された場合、カスタム属性が作成され、「dob」フィールドの値は更新されません。

### データポイント {#data-points}

Amperityは、Brazeとの同期間に行われた変更と送信全体のステータスを追跡します。Amperityは、前回の同期以降に変更されたリストメンバーシップとその他の選択された属性のみをBrazeに送信します。

## 統合 {#integration}

### ステップ1：Brazeの設定詳細を取得する {#step-1-capture-configuration-details-for-braze}

1. **ユーザーデータ**で、`users.track`権限を持つBrazeワークスペースのBraze REST APIキーを作成します。`users.track`エンドポイントは、Amperityオーディエンスをカスタム属性としてBrazeに同期します。
2. Brazeインスタンスの[REST APIエンドポイント]({{site.baseurl}}/api/basics#endpoints)を確認します。たとえば、BrazeのURLが`https://dashboard-03.braze.com`の場合、REST APIエンドポイントは`https://rest.iad-03.braze.com`で、インスタンスは「US-03」です。
3. AmperityからBrazeに送信できる[ユーザープロファイルフィールド]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)と[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)のリストを決定します。

### ステップ2：Brazeを送信先として設定する — DataGridオペレーター {#step-2-set-up-braze-as-a-destinationdatagrid-operator}

#### ステップ2a：顧客プロファイルテーブルを作成する {#step-2a-build-the-customer-profiles-table}

AmperityのCustomer 360データベース内に、「Braze Customer Attributes」という名前の新しいテーブルを作成します。このテーブルには、ブランドがAmperityで管理するすべてのBraze属性が含まれている必要があります。これには、Brazeが必要とするデフォルトのユーザープロファイルフィールドとカスタム属性の両方が含まれます。[Amperityドキュメント](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table)に示されているように、SQLを使用してこのテーブルの構造を定義します。

#### ステップ2b：テーブルに名前を付け、検証し、保存する {#step-2b-name-validate-and-save-the-table}

テーブル名を「Braze Customer Attributes」とし、保存します。テーブルが**セグメントエディター**およびキャンペーン内の**属性の編集**エディターにアクセス可能であることを確認します。

#### ステップ2c：Brazeを送信先として追加する {#step-2c-add-braze-as-a-destination}

Amperityプラットフォームで**Destinations**タブに移動します。新しい送信先を追加するオプションを探します。利用可能なオプションから**Braze**を選択します。

![名前が「Braze API」、説明が「Send audience attributes to Braze.」、プラグインが「Braze」である「New Destination」セクション。]({% image_buster /assets/img/amperity/destination_name.png %}){: style="max-width:60%;"}

#### ステップ2d：送信先の詳細を設定する {#step-2d-configure-destination-details}

[Amperityドキュメント](https://docs.amperity.com/datagrid/destination_braze.html#add-destination)に示されているように、**Braze settings**でBrazeの認証情報と送信先設定を指定します。前のステップで収集した設定詳細を入力し、Braze識別子を定義します。マッチングに使用できる識別子は以下の通りです：
- `braze_id`：自動的に割り当てられるBrazeの識別子で、Brazeで作成されたときに特定のユーザーに関連付けられ、変更できません。
- `external_id`：顧客が割り当てた識別子で、通常はUUIDです。

![Braze設定セクション。インスタンスは「US-03」、ユーザー識別子は「external_id」、セグメント名は空白、S3バケットは「amperity-training-abc123」、S3フォルダは「braze-attributes」。]({% image_buster /assets/img/amperity/braze_settings.png %}){: style="max-width:60%;"}

#### ステップ2e：データテンプレートを追加する {#step-2e-add-a-data-template}

**Destinations**タブでBraze送信先のメニューを開き、**Add data template**を選択します。テンプレートの名前と説明（たとえば「Braze」と「Send custom attributes to Braze」）を入力し、ビジネスユーザーのアクセスを確認し、すべての設定をチェックします。

必要な設定が送信先の一部として構成されていない場合は、データテンプレートの一部として構成します。データテンプレートを保存します。

![名前が「Braze Audience Attributes」で説明が「Send audience attributes to Braze.」である「Data Template Name」セクション。]({% image_buster /assets/img/amperity/data_template_name.png %}){: style="max-width:60%;"}

#### ステップ2f：設定を保存する {#step-2f-save-the-configuration}

必要な情報を入力したら、設定を保存します。Brazeが送信先として設定されたので、Amp360とAmpIQのユーザーはデータをBrazeに同期できます。

### ステップ3：データをBrazeに同期する {#step-3-sync-data-to-braze}

AmperityのテナントでBrazeが有効になっていることを確認します。有効になっていない場合は、DataGridオペレーターまたはAmperityの担当者に支援を依頼してください。

次に、該当するAmp360またはAmpIQの同期手順に従います。

#### 同期オプション1：Amp360経由でBrazeにクエリ結果を送信する {#syncing-option-1-send-query-results-to-braze-via-amp360}

Amp360のユーザーは、SQLを使って自由形式のクエリを作成し、その結果をBrazeに送信するスケジュールを設定できます。

##### ステップ1：Amperityでクエリを作成する {#step-1-create-a-query-in-amperity}

Amperityのクエリ機能に移動し、目的の顧客データセットを得るためのSQLクエリを構築します。結果には、Brazeに送信したい特定の属性が含まれている必要があります。購入履歴を持つユーザーのリストを返すAmperityクエリの例を参照してください。

##### ステップ2：Amperityに新しいオーケストレーションを追加する {#step-2-add-a-new-orchestration-in-amperity}

1. **Orchestration**セクションに移動し、新しいオーケストレーションを追加するオプションをクリックします。
2. オーケストレーションが何を行うべきかを指定します。これには通常、実行するSQLクエリと結果の送信先を指定することが含まれます。この場合、アクティブな顧客のリストを生成するために作成したSQLクエリを選択し、結果の送信先としてBrazeを指定します。
3. オーケストレーションをいつ、どのくらいの頻度で実行するかを定義します。たとえば、毎日特定の時間にオーケストレーションを実行できます。
4. オーケストレーションを好みに合わせて設定したら保存します。Amperityのオーケストレーションリストに追加されます。
5. オーケストレーションをテストして、期待通りに動作することを確認します。手動でオーケストレーションをトリガーし、Brazeで結果を確認することで検証できます。

##### ステップ3：オーケストレーションを実行する {#step-3-run-the-orchestration}

オーケストレーションを実行してクエリを実行し、結果をBrazeに送信します。これは手動で行うことも、オーケストレーション設定で設定したスケジュールで行うこともできます。

#### 同期オプション2：AmpIQ経由でBrazeにオーディエンスを送信する {#syncing-option-2-send-audiences-to-braze-via-ampiq}

AmpIQユーザーは、SQL以外のインターフェイスを使ってAmperityでセグメントを作成し、Brazeなどの下流の送信先に同期できます。ユーザーは送信先を選択し、各送信先に送信する属性のリストを設定できます。

##### ステップ1：Amperityでセグメントを作成する {#step-1-create-a-segment-in-amperity}

Amperityで顧客のリストを返すセグメントを作成します。このセグメントは、Brazeで更新するカスタム属性に関連付けられている必要があります。

{% alert note %}
Amperityのドキュメントで、Brazeに送信できるさまざまなセグメントタイプの例を確認してください。
{% endalert %}

##### ステップ2：Amperityでキャンペーンを構築する {#step-2-build-a-campaign-in-amperity}

1. **キャンペーン**セクションに移動し、新しいキャンペーンを作成するオプションをクリックします。
2. 特に複数のキャンペーンがある場合に後で識別しやすいよう、説明的でユニークな名前を付けます。
3. このキャンペーンでターゲットにする顧客のセグメントを選択します。これは先ほど作成したセグメントです。<br>![ターゲティングから除外するセグメントのドロップダウンフィールド。]({% image_buster /assets/img/amperity/select_segments.png %}){: style="max-width:50%;"}<br><br>
4. キャンペーンの一部として送信したいデータを選択します。これにはさまざまな顧客属性が含まれる可能性があります。![キャンペーン属性の編集モーダルでは、送信先と顧客属性を選択できます。]({% image_buster /assets/img/amperity/edit_campaign_attributes.png %}){: style="max-width:90%;"}<br><br>
5. キャンペーンデータの送信先として**Braze**を選択します。
6. いつ、どのくらいの頻度でキャンペーンを実行するかを選択します。これは1回限りのイベントでも、定期的なスケジュールでも構いません。
7. キャンペーンを保存してテストを実行し、期待通りに機能することを確認します。

##### ステップ3：キャンペーンを実行する {#step-3-run-the-campaign}

Brazeにセグメントを送信するためにキャンペーンを実行します。これは手動で行うことも、キャンペーン設定で設定したスケジュールに基づいて行うこともできます。


### AmperityとBraze Currentsを組み合わせて使用する {#using-amperity-with-braze-currents}
Braze CurrentsのデータをAmperityに送信するには：
1. Amazon S3バケットにデータを送信するために[Braze Currentをセットアップ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents)します。
2. [そのAmazon S3バケットからApache Avroファイルを読み込む](https://docs.amperity.com/datagrid/source_amazon_s3.html)ようにAmperityを設定します。
3. フィードを設定し、標準的なワークフローを使用してデータロードを自動化します。
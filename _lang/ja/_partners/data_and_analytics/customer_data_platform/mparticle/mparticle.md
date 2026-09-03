---
nav_title: mParticle by Rokt
article_title: mParticle by Rokt
alias: /partners/mparticle/
description: "このリファレンス記事では、BrazeとmParticleのパートナーシップについて説明します。mParticleは、マーケティングスタックのソース間で情報を収集してルーティングする顧客データプラットフォームです。"
page_type: partner
search_tag: Partner

---

# mParticle by Rokt

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> mParticleの顧客データプラットフォームは、データの有効活用を支援します。熟練したマーケターは、mParticleでグローススタック全体のデータのオーケストレーションを行い、カスタマージャーニーの重要なタイミングで適切なアクションを取ることができます。

BrazeとmParticleの統合により、2つのシステム間の情報の流れをシームレスにコントロールできます。
- Brazeのキャンペーンとキャンバスのセグメンテーションのために、mParticleのオーディエンスをBrazeに同期する。
- 2つのプラットフォーム間でデータを共有する。これはmParticleキット統合とサーバー間統合によって実現できます。
- [Currentsを介してBrazeユーザーインタラクションをmParticleに送信し]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents)、グローススタック全体でアクションに活用する。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| mParticleアカウント | このパートナーシップを利用するには、[mParticleアカウント](https://app.mparticle.com/login)が必要です。 |
| Brazeインスタンス | Brazeインスタンスは[API概要ページ]({{site.baseurl}}/api/basics#endpoints)で確認できます（例：`US-01`または`US-02`）。 |
| Brazeアプリ識別子キー | アプリ識別子キーです。<br><br>これはBrazeダッシュボードの**設定の管理** > **APIキー**で確認できます。 |
| ワークスペースREST APIキー | （サーバー間）Braze REST APIキーです。<br><br>これはBrazeダッシュボードの**開発者コンソール** > **API設定** > **APIキー**で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### オーディエンス {#audiences}

BrazeとmParticleのパートナーシップを使用して統合を設定し、mParticleオーディエンスをBrazeに直接インポートしてリターゲティングを行い、一方のシステムから他方へのデータの完全なループを作成します。

設定した統合はデータポイントを記録します。Brazeデータポイントの詳細についてご不明な点がある場合は、Brazeアカウントマネージャーにお問い合わせください。

#### オーディエンスの転送 {#forwarding-audiences}

mParticleは、「[セグメントとして送信](#send_settings)」設定によって制御される、コホートメンバーシップ属性を設定する3つの方法を提供しています。各オプションの処理については、以下のセクションを参照してください。

- [単一文字列属性](#string)
- [単一配列属性](#array)
- [セグメントごとに1つの属性](#per-segment)
- [単一配列属性と単一文字列属性の両方](#both-1)
- [単一配列属性とセグメントごとに1つの属性の両方](#both-2)
- [単一文字列属性とセグメントごとに1つの属性の両方](#both-3)
- [単一配列属性、単一文字列属性、セグメントごとに1つの属性](#multi)

##### 単一文字列属性 {#string}

mParticleは`SegmentMembership`と呼ばれる単一のカスタム属性を作成します。この属性の値は、ユーザーに一致するmParticleオーディエンスIDのカンマ区切り文字列です。これらのオーディエンスIDは、mParticleダッシュボードの**Audiences**で確認できます。

たとえば、mParticleオーディエンス「Ibiza dreamers」のオーディエンスIDが「11036」の場合、フィルター`SegmentMembership` — `matches regex` — `11036`を使用してこれらのユーザーをセグメント化できます。

これはmParticleのデフォルトオプションですが、ほとんどの企業ユーザーはBrazeでセグメントを作成する際のフィルタリング体験のために[単一配列属性](#array)を使用することを選択しています。

{% alert important %}
このソリューションは、オーディエンスが多数ある場合は推奨されません。カスタム属性は最大255文字であるため、この方法ではユーザープロファイルに数十または数百のオーディエンスを保存することはできません。ユーザーあたりのコホート数が多い場合は、「セグメントごとに1つの属性」の設定を強く推奨します。
{% endalert %}

![mParticleセグメントメンバーシップ]({% image_buster /assets/img_archive/mparticle1.png %})

##### 単一配列属性 {#array}

mParticleは各ユーザーに対して、Brazeで`SegmentMembershipArray`と呼ばれる単一のカスタム配列属性を作成します。この属性の値は、ユーザーに一致するmParticleオーディエンスIDの配列です。

たとえば、あるユーザーがオーディエンスIDが「13053」、「13052」、「13051」の3つのmParticleオーディエンスのメンバーである場合、フィルター`SegmentMembershipArray` — `includes value` — `13051`を使用してそれらのオーディエンスの1つに一致するユーザーをセグメント化できます。

{% alert note %}
Brazeの配列属性にはデフォルトの最大長が500あります。ユーザーが500を超えるオーディエンスのメンバーである場合、Brazeはメンバーシップ情報を切り捨てます。回避策については、Brazeアカウントマネージャーに連絡して最大配列長のしきい値を引き上げてください。
{% endalert %}

##### セグメントごとに1つの属性 {#per-segment}

mParticleは、ユーザーが所属する各オーディエンスに対してブール型のカスタム属性を作成します。たとえば、mParticleオーディエンスが「Possible Parisians」と呼ばれる場合、フィルター`In Possible Parisians` - `equals` - `true`を使用してこれらのユーザーをセグメント化できます。

![mParticleカスタム属性]({% image_buster /assets/img_archive/mparticle2.png %})

##### 単一配列属性と単一文字列属性の両方 {#both-1}

mParticleは、単一配列属性と単一文字列属性の両方で説明されている通りに属性を送信します。

##### 単一配列属性とセグメントごとに1つの属性の両方 {#both-2}

mParticleは、単一配列属性とセグメントごとに1つの属性の両方で説明されている通りに属性を送信します。

##### 単一文字列属性とセグメントごとに1つの属性の両方 {#both-3}

mParticleは、単一文字列属性とセグメントごとに1つの属性の両方で説明されている通りに属性を送信します。

##### 単一配列属性、単一文字列属性、セグメントごとに1つの属性 {#multi}

mParticleは、単一配列属性、単一文字列属性、セグメントごとに1つの属性で説明されている通りに属性を送信します。

#### ステップ1:mParticleでオーディエンスを作成する {#send_settings}

mParticleでオーディエンスを作成するには、以下を行います。

1. **Audiences** > **Single Workspace** > **+ New Audience**に移動します。
2. オーディエンスの出力としてBrazeを接続するには、以下のフィールドを入力する必要があります。

| フィールド名 | 説明 |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| APIキー | Brazeダッシュボードで、**設定** > **APIキー**に移動します。 |
| APIキーのオペレーティングシステム | BrazeのAPIキーに対応するオペレーティングシステムを選択します。この選択により、オーディエンス更新時に転送されるプッシュトークンの種類が制限されます。 |
| セグメントとして送信 | オーディエンスをBrazeに送信する方法です。詳細は[オーディエンスの転送](#forwarding-audiences)セクションを参照してください。 |
| ワークスペースREST APIキー | フル権限を持つBraze REST APIキーです。Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| 外部IDタイプ | BrazeにextreanlIDとして転送するmParticleユーザーIDタイプです。デフォルト値のCustomer IDのままにすることを推奨します。 |
| メールIDタイプ | Brazeにメールとして転送するmParticleユーザーIDタイプです。 |
| Brazeインスタンス | Brazeデータの転送先クラスターを指定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1：mParticleでオーディエンスを作成する" }

{:start="3"}
3. 最後にオーディエンスを**保存**します。

数分以内にオーディエンスがBrazeに同期され始めます。オーディエンスメンバーシップは、`external_ids`を持つユーザー（つまり匿名ユーザー以外）に対してのみ更新されます。Braze mParticleオーディエンスの作成に関する詳細は、mParticleのドキュメント[Configuration settings](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings)を参照してください。

#### ステップ2:Brazeでユーザーをセグメント化する {#step-2-segment-users-in-braze}

Brazeでこれらのユーザーのセグメントを作成するには、**エンゲージメント**の下にある**セグメント**に移動し、セグメントに名前を付けます。以下は、**セグメントとして送信**で選択したオプションに応じた2つのセグメントの例です。各オプションの詳細については、[オーディエンスの転送](#forwarding-audiences)を参照してください。

- **単一配列属性：** フィルターとして`SegmentMembershipArray`を選択します。次に、「includes value」オプションを使用して、目的のオーディエンスIDを入力します。![mParticleセグメントフィルター「SegmentMembershipArray」が「includes value」とオーディエンスIDに設定されている状態。]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **セグメントごとに1つの属性：** フィルターとしてカスタム属性を選択します。次に、「equals」オプションを使用して適切なロジックを選択します。![mParticleセグメントフィルター「in possible parisians」が「equals」と「true」に設定されている状態。]({% image_buster /assets/img_archive/mparticle3.png %})

保存後、キャンバスまたはキャンペーン作成時のターゲティングユーザーステップで、このセグメントを参照できます。

#### 接続の無効化と削除 {#deactivating-and-deleting-connections}

mParticleはBrazeでセグメントを直接管理しないため、対応するmParticleオーディエンス接続が削除または無効化された場合でも、セグメントは削除されません。この場合、mParticleはBrazeのオーディエンスユーザー属性を更新して各ユーザーからオーディエンスを削除することはありません。

削除前にBrazeユーザーからオーディエンスを削除するには、オーディエンスフィルターを調整してオーディエンスサイズを0にしてからオーディエンスを削除してください。オーディエンスの計算が完了して0ユーザーが返された後、オーディエンスを削除します。その後、Brazeでオーディエンスメンバーシップは、単一属性オプションの場合は`false`に更新され、配列形式の場合はオーディエンスIDが削除されます。

## データマッピング {#data-mapping}

モバイルアプリやWebアプリをmParticleを通じてBrazeに接続したい場合は、[組み込みキット統合](#embedded-kit-integration)を使用してデータをBrazeにマッピングできます。また、[サーバー間API統合](#server-api-integration)を使用して、サーバーサイドのデータをBrazeに転送することもできます。

どちらのアプローチを選択しても、Brazeをアウトプットとして設定する必要があります。

### Brazeのアウトプット設定を構成する {#configure-your-braze-output-settings}

mParticleで、**Setup** > **Outputs** > **Add Outputs**に移動し、**Braze**を選択してBrazeキット設定を開きます。完了したら**Save**をクリックします。

| 設定名 | 説明 |
| ------------ | ----------- |
| Brazeアプリ識別子キー | Brazeアプリ識別子キーは、Brazeダッシュボードの**設定** > **APIキー**から確認できます。APIキーはプラットフォーム（iOS、Android、Web）ごとに異なります。 |
| External identity type | Brazeにexternal IDとして転送するmParticleユーザーIDタイプです。デフォルト値のCustomer IDのままにすることをお勧めします。 |
| Email identity type | Brazeにメールとして転送するmParticleユーザーIDタイプです。デフォルト値のEmailのままにすることをお勧めします。 |
| Brazeインスタンス | Brazeデータが転送されるクラスターです。ダッシュボードと同じクラスターである必要があります。 |
| Enable event stream forwarding | （サーバー間）有効にすると、すべてのイベントがリアルタイムで転送されます。無効の場合、すべてのイベントは一括で転送されます。イベントストリーム転送を有効にする場合は、Brazeに渡すデータが[レート制限]({{site.baseurl}}/api/api_limits)を遵守していることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Brazeのアウトプット設定を構成する" }

![アプリ識別子、ID マッピング、インスタンスフィールドを含むmParticle Brazeアウトプット設定。]({% image_buster /assets/img_archive/configure_settings.png %})

### 組み込みキット統合 {#embedded-kit-integration}

組み込みキット統合を通じて、mParticleとBrazeのSDKがアプリケーションに組み込まれます。ただし、Brazeとの直接統合とは異なり、mParticleがBraze SDKメソッドの大部分の呼び出しを代行します。ユーザーデータを追跡するために使用するmParticleメソッドは、自動的にBraze SDKメソッドにマッピングされます。

これらのmParticle SDKの[Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy)、[iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy)、[Web](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze)向けのマッピングはオープンソースで、[mParticleのGitHubページ](https://github.com/mparticle-integrations)で確認できます。

組み込みキットSDK統合により、プッシュ、アプリ内メッセージ、および関連するすべてのメッセージ分析トラッキングなど、フル機能をご利用いただけます。

{% alert note %}
Content Cardsおよびカスタムアプリ内メッセージの統合には、Braze SDKメソッドを直接呼び出してください。
{% endalert %}

#### ステップ1: mParticle SDKを統合する {#step-1-integrate-the-mparticle-sdks}

プラットフォームの要件に基づいて、適切なmParticle SDKをアプリに統合します。

* [mParticle for Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle for iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle for Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### ステップ2: mParticleのBrazeイベントキット統合を完了する {#step-2-complete-mparticles-braze-event-kit-integration}

このmParticle統合では、Braze SDKをWebサイトやアプリに直接含める必要はありませんが、アプリからBrazeにデータを転送するには、以下のmParticle Appboy Kitをインストールする必要があります。

mParticleの[Brazeイベントキット統合ガイド](https://docs.mparticle.com/integrations/braze/event/#kit-integration)では、メッセージングのニーズ（プッシュ、位置情報の追跡など）に基づいたカスタムmParticleおよびBrazeの連携手順を説明しています。

#### ステップ3: Brazeアウトプットの接続設定 {#step-3-connections-settings-for-your-braze-output}

mParticleで、**Connections** > **Connect** > **[目的のプラットフォーム]** > **Connect Output**に移動して、Brazeをアウトプットとして追加します。次に、**Save**を選択します。

![Brazeアウトプット用のmParticleイベントキット接続設定。]({% image_buster /assets/img_archive/mParticle_event_config.png %})

すべての接続設定がすべてのプラットフォームおよび統合タイプに適用されるわけではありません。接続設定と適用されるプラットフォームの内訳については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#connection-settings)を参照してください。

### サーバーAPI統合 {#server-api-integration}

これは、mParticleのサーバーサイドSDK（Ruby、Pythonなど）を使用している場合にバックエンドデータをBrazeにルーティングするためのアドオンです。このサーバー間統合をBrazeで設定するには、[mParticleのドキュメント](https://docs.mparticle.com/guides/platform-guide/connections/)に従ってください。

{% alert important %}
サーバー間統合は、アプリ内メッセージ、Content Cards、プッシュ通知などのBraze UI機能をサポートしていません。また、このメソッドでは利用できないデバイスレベルのフィールドなど、自動的にキャプチャされるデータもあります。

これらの機能を使用したい場合は、サイドバイサイド統合を検討してください。

サーバーサイドのデータがBrazeに転送されるには、`external_id`が含まれている必要があります。匿名ユーザーは転送されません。
{% endalert %}

#### Brazeアウトプットの接続設定 {#connections-settings-for-your-braze-output}

mParticleで、**Connections > Connect > [目的のプラットフォーム] > Connect Output**に移動して、Brazeをアウトプットとして追加します。完了したら**Save**をクリックします。

![プラットフォーム上でBrazeをアウトプットとして追加するためのmParticle接続画面。]({% image_buster /assets/img_archive/mParticle_connections.png %})

すべての接続設定がすべてのプラットフォームおよび統合タイプに適用されるわけではありません。接続設定と適用されるプラットフォームの内訳については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#connection-settings)を参照してください。

「Enriched User Attributes」または「Enriched User Identities」を有効にする前に、[データポイントの超過](#potential-data-point-overages)を確認して、これらの設定がデータポイント使用量にどのように影響するかを把握することをお勧めします。

### データマッピングの詳細 {#data-mapping-details}

#### データ型 {#data-types}
すべてのデータ型が両方のプラットフォーム間でサポートされているわけではありません。
- [カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events)は、文字列、数値、ブール値、または日付オブジェクトをサポートします。配列やネストされたオブジェクトはサポートしていません。
- [カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)は、文字列、数値、ブール値、日付オブジェクト、および配列をサポートしますが、オブジェクトやネストされたオブジェクトはサポートしていません。

{% alert note %}
Brazeは`Time`型のカスタム属性で、0年より前または3000年より後のタイムスタンプをサポートしていません。mParticleから送信された場合、Brazeはこれらの値を取り込みますが、文字列として保存されます。
{% endalert %}

#### データマッピング

| mParticleデータ型 | Brazeデータ型 | 説明 |
| ------------------- | --------------- | ----------- |
| ユーザー属性（予約済み） | 標準属性項目 | 例えば、mParticleの`$FirstName`予約済みユーザー属性キーは、Brazeの`first_name`標準属性項目フィールドにマッピングされます。 |
| ユーザー属性（その他） | カスタム属性 | mParticleに渡されたユーザー属性のうち、予約済みユーザー属性キー以外のものは、Brazeでカスタム属性としてログに記録されます。<br><br>ユーザー属性は文字列、数値、ブール値、日付、配列をサポートしますが、オブジェクトやネストされたオブジェクトはサポートしていません。 |
| カスタムイベント | カスタムイベント | mParticleのカスタムイベントは、Brazeではカスタムイベントとして認識されます。イベント属性はカスタムイベントプロパティとして転送されます。<br><br>イベントプロパティとしてBrazeに渡されるイベント属性は、文字列、数値、ブール値、または日付オブジェクトをサポートしますが、配列やネストされたオブジェクトはサポートしていません。 |
| 購入コマースイベント | 購入イベント | 購入コマースイベントは、Brazeの購入イベントにマッピングされます。<br><br>bundle commerce event dataの設定値を切り替えて、注文レベルまたは製品レベルで購入を記録します。例えば、`false`の場合、2つの固有の製品、プロモーション、またはインプレッションを含む単一の受信イベントは、少なくとも2つの送信Brazeイベントになります。`true`に設定すると、ネストされた製品、プロモーション、またはインプレッション配列を含む単一の送信イベントになります。<br><br>ログに記録される追加のコマースフィールドの詳細については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#purchase-events)を参照してください。<br><br>「bundle commerce event data」を`false`に設定した場合、購入イベントプロパティとしてBrazeに渡される製品属性は、文字列、数値、ブール値、または日付オブジェクトをサポートしますが、配列やネストされたオブジェクトはサポートしていません。 |
| その他すべてのコマースイベント | カスタムイベント | その他すべてのコマースイベントは、カスタムイベントにマッピングされます。<br><br>bundle commerce event dataの設定値を切り替えて、注文レベルまたは製品レベルで購入を記録します。例えば、`false`の場合、2つの固有の製品、プロモーション、またはインプレッションを含む単一の受信イベントは、少なくとも2つの送信Brazeイベントになります。`true`に設定すると、ネストされた製品、プロモーション、またはインプレッション配列を含む単一の送信イベントになります。<br><br>特定のデフォルトコマース値に加えて、製品属性はBrazeイベントプロパティとしてログに記録されます。ログに記録される追加のコマースフィールドの詳細については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)を参照してください。<br><br>「bundle commerce event data」を`false`に設定した場合、イベントプロパティとしてBrazeに渡される製品属性は、文字列、数値、ブール値、または日付オブジェクトをサポートしますが、配列やネストされたオブジェクトはサポートしていません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="データマッピング" }

#### ユーザーIDマッピング {#user-identity-mapping}
各mParticleアウトプットに対して、Brazeに`external_id`として送信するexternal identity typeを選択できます。デフォルト値はcustomer IDですが、`MPID`などの別のIDを選択してBrazeの`external_id`として送信することもできます。customer ID以外の識別子を選択すると、Brazeでのデータ送信方法に影響する場合があることに注意してください。

例えば、MPIDをBrazeの`external_id`にマッピングすると、以下のような影響があります。
- MPIDが割り当てられるタイミングの性質上、すべてのユーザーにセッション開始時に`external_id`が割り当てられます。
- MPIDと`external_id`間のデータ型の違いにより、Currentsの設定に追加のマッピングが必要になる場合があります。

### 消去リクエストの転送（データ主体リクエスト） {#forwarding-erasure-requests-data-subject-requests}

データ主体リクエストのアウトプットをBrazeに設定することで、消去リクエストをBrazeに転送できます。消去リクエストをBrazeに転送するには、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/forwarding-dsr/)に従ってください。

## データポイントの超過の可能性 {#potential-data-point-overages}

### エンリッチされたユーザー属性 {#enriched-user-attributes}

#### ユーザー属性/IDのエンリッチの有効化（サーバー間連携のみ） {#enriched}

mParticleの接続設定で、Brazeは**Include Enriched User Attributes**をオフにすることを推奨しています。有効にすると、mParticleはログに記録された各イベントごとに、既存のプロファイルから利用可能なすべてのユーザー属性（標準属性、カスタム属性、計算属性など）をBrazeに転送します。これにより、mParticleが各呼び出しで同じ未変更の属性をBrazeに送信するため、データポイントの消費量が大きくなります。

例えば、ユーザーが最初のセッションで名、姓、電話番号を追加し、その後ニュースレターに登録して同じ情報とメールアドレスを追加し、ニュースレター登録イベントがトリガーされた場合：
- オンの場合（デフォルト）、5つのデータポイントが発生します。（登録イベント、メールアドレス、名、姓、電話番号）
- オフの場合、2つのデータポイントが発生します（登録イベントとメールアドレス）

{% alert note %}
この設定をオフにしても、変更されたデータのチェックは行われません。ただし、元のインバウンドバッチで受信されなかった、またはイベントの属性として明示的に設定されなかったユーザープロファイル上のすべてのユーザー属性を統合が送信することを防ぎます。Brazeに差分のみが渡されていることを引き続き確認することが重要です。
{% endalert %}

#### エンリッチされたユーザー属性をオフにする際の考慮事項 {#considerations-of-turning-off-enriched-user-attributes}

**Include Enriched User Attributes**をオフにする際に注意すべき考慮事項がいくつかあります：
1. サーバー間連携では、mParticleイベントAPIを使用してBrazeにイベントを送信します。各リクエストはイベントによってトリガーされます。メールアドレスの更新などユーザー属性が変更されたが、特定のイベント（例：プロファイル更新のカスタムイベント）に関連付けられていない場合、新しい値はユーザーがトリガーした次のイベントのペイロードの「エンリッチされた属性」としてのみBrazeなどの出力先に渡されます。**Include Enriched User Attributes**がオフの場合、特定のイベントに関連付けられていないこの新しい属性値はBrazeに渡されません。
  - これを解決するには、更新された特定のユーザー属性のみをBrazeに送信する別の「ユーザー属性更新」イベントを作成することを推奨します。このアプローチでは、「ユーザー属性更新」イベントに対して追加のデータポイントが記録されますが、この機能を有効にした状態で毎回すべてのユーザー属性を送信する場合と比べて、データポイント使用量ははるかに少なくなります。
2. 計算属性はエンリッチされたユーザー属性としてBrazeに渡されるため、「Enriched User Attributes」をオフにするとBrazeに渡されなくなります。「Enriched User Attributes」がオフの場合にBrazeに計算属性を転送するには、[計算属性フィード](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed)がすべての属性をプッシュせずに役立ちます。このフィードは、計算属性が変更されたときにBrazeへの更新をダウンストリームで実行します。

## トラブルシューティング {#troubleshooting}

### Brazeイベントキットを使用したiOSプッシュ通知のトラブルシューティング {#troubleshooting-ios-push-notifications-with-the-braze-event-kit}

iOS上でBrazeイベントキット（組み込みキット統合）を使用しているときにプッシュ通知が機能しない場合は、以下を確認してください。
1. **プッシュトークンの転送:** mParticleがプッシュトークンをBrazeに転送していることを確認します。mParticleダッシュボードで、Brazeキット接続のプッシュが有効になっていること、およびBrazeダッシュボードで正しいAppleプッシュ認証情報が設定されていることを確認してください。
2. **キットの初期化順序:** Brazeキットは、アプリがプッシュ権限を要求する前に初期化されている必要があります。キットがアクティブになる前にプッシュ権限が要求されると、プッシュトークンがBrazeに転送されない場合があります。mParticle SDKがアプリのライフサイクルの早い段階で開始されていることを確認してください。
3. **メソッドスウィズリング:** mParticle Appleキットは、メソッドスウィズリングを使用してプッシュトークンの転送とプッシュ通知イベントの処理を自動的に行います。スウィズリングを無効にしたか、別のSDKが干渉している場合、プッシュトークンがBrazeに届かないことがあります。mParticle設定でスウィズリングが有効になっていることを確認してください。
4. **手動トークン処理:** プッシュトークンを手動で管理している場合（例えば、`application:didRegisterForRemoteNotificationsWithDeviceToken:`を実装している場合）、プッシュ通知トークンプロパティに割り当てることでトークンをmParticleに渡していることを確認してください。例: `MParticle.sharedInstance().pushNotificationToken = deviceToken`。これにより、キットがBrazeにトークンを転送します。
5. **環境の不一致:** APNs認証情報の環境（開発 vs. 本番）がアプリのビルドと一致していることを確認してください。詳細については、[iOSプッシュのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)を参照してください。
6. **キットの初期化タイミング:** `didFinishLaunchingWithOptions`からBrazeインスタンスにアクセスする場合、プッシュが届いたときにmParticleキットの準備ができていない可能性があります。[`userNotificationCenter(_:didReceive:withCompletionHandler:)`]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)（または同等の通知応答デリゲート）でプッシュ処理を初期化し、ユーザーが通知を開いたときにBrazeキットがアクティブになるようにしてください。

### 不要なデータや重複データのBrazeへの送信 {#sending-unnecessary-or-duplicate-data-to-braze}
Brazeは、値が変更されていなくても、属性がBrazeに渡されるたびにデータポイントをカウントします。このため、Brazeでアクションに必要なデータのみを転送し、属性の差分のみを渡すようにすることを推奨しています。

### イベントがBrazeに表示されない {#events-are-not-appearing-in-braze}

mParticleのイベントや属性がBrazeに表示されない場合、問題はBrazeの障害ではなく、mParticleの接続やイベントマッピングの設定ミスであることがほとんどです。以下を確認してください。

- **接続出力:** 関連する接続の出力としてBrazeが有効になっていること、および正しいBrazeインスタンス、アプリ識別子、REST APIキーが設定されていることを確認してください。
- **ID マッピング:** サーバー間連携とオーディエンス同期には`external_id`が必要です。匿名ユーザーは転送されません。
- **イベントマッピング:** イベントがBraze出力にルーティングされていること、およびサポートされていないデータ型（ネストされたオブジェクト、イベントプロパティ内の配列）がドロップされていないことを確認してください。

設定が正しいにもかかわらずデータが届かない場合は、[mParticleサポート](https://support.mparticle.com/)に連絡して、mParticle側の配信ログを確認してもらってください。
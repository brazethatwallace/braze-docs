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
- BrazeのCampaignとCanvasのセグメンテーションのために、mParticleのオーディエンスをBrazeに同期する。
- 2つのプラットフォーム間でデータを共有する。これはmParticleキット統合とサーバー間統合によって実現できます。
- [Currentsを介してBrazeユーザーインタラクションをmParticleに送信し]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/)、グローススタック全体でアクションに活用する。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| mParticleアカウント | このパートナーシップを利用するには、[mParticleアカウント](https://app.mparticle.com/login)が必要です。 |
| Brazeインスタンス | Brazeインスタンスは[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)で確認できます（`US-01`、`US-02` など）。 |
| Brazeアプリ識別子キー | アプリ識別子キー。<br><br>これは、Brazeダッシュボードの**設定の管理** > **APIキー**で確認できます。 |
| ワークスペースREST APIキー | （サーバー間）Braze REST APIキー<br><br>これは、Brazeダッシュボードの**開発者コンソール** > **API設定** > **APIキー**で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### オーディエンス {#audiences}

BrazeとmParticleのパートナーシップを利用して統合を構成し、mParticleのオーディエンスを直接Brazeにインポートしてリターゲティングを行い、1つのシステムから別のシステムへのデータの完全なループを作成します。

設定した統合はすべてデータポイントを記録します。Brazeデータポイントの詳細についてご質問があれば、Brazeアカウントマネージャーがお答えします。

#### オーディエンスの転送 {#forwarding-audiences}

mParticleでは、コホートメンバーシップ属性を設定する3つの方法が提供されており、「[セグメントの送信方法](#send_settings)」設定で制御されます。各オプションの処理については、以下のセクションを参照してください。

- [単一文字列属性](#string)
- [単一配列属性](#array)
- [セグメントごとに1つの属性](#per-segment)
- [単一配列属性と単一文字列属性の両方](#both-1)
- [単一配列属性とセグメントごとに1つの属性の両方](#both-2)
- [単一文字列属性とセグメントごとに1つの属性の両方](#both-3)
- [単一配列属性、単一文字列属性、およびセグメントごとに1つの属性](#multi)

##### 単一文字列属性 {#string}

mParticleは`SegmentMembership`というカスタム属性を1つ作成します。この属性の値は、ユーザーに一致するmParticleオーディエンスIDのカンマ区切り文字列です。これらのオーディエンスIDは、mParticleダッシュボードの**Audiences**で確認できます。

たとえば、mParticleオーディエンス「Ibiza dreamers」のオーディエンスIDが「11036」の場合、フィルター`SegmentMembership` — `matches regex` — `11036`でこれらのユーザーをセグメントできます。

これはmParticleのデフォルトオプションですが、ほとんどの企業ユーザーは、Brazeでセグメントを作成する際のフィルタリング体験のために[単一配列属性](#array)を使用することを選択しています。

{% alert important %}
オーディエンスが少数の場合を除き、このソリューションは推奨されません。カスタム属性は最大255文字であるため、この方法ではユーザープロファイルに数十または数百のオーディエンスを保存することはできません。ユーザーあたりのコホート数が多い場合は、「セグメントごとに1つの属性」設定を強くお勧めします。
{% endalert %}

![mParticleセグメントメンバーシップ]({% image_buster /assets/img_archive/mparticle1.png %})

##### 単一配列属性 {#array}

mParticleは、各ユーザーに対して`SegmentMembershipArray`というカスタム配列属性をBrazeに1つ作成します。この属性の値は、ユーザーに一致するmParticleオーディエンスIDの配列です。

たとえば、ユーザーがオーディエンスID「13053」、「13052」、「13051」の3つのmParticleオーディエンスのメンバーである場合、フィルター`SegmentMembershipArray` — `includes value` — `13051`でこれらのオーディエンスのいずれかに一致するユーザーをセグメントできます。

{% alert note %}
Brazeの配列属性のデフォルトの最大長は500です。ユーザーが500を超えるオーディエンスのメンバーである場合、Brazeはメンバーシップ情報を切り捨てます。回避策については、Brazeアカウントマネージャーに連絡して最大配列長のしきい値を引き上げてください。
{% endalert %}

##### セグメントごとに1つの属性 {#per-segment}

mParticleは、ユーザーが所属する各オーディエンスに対してブール値のカスタム属性を作成します。たとえば、mParticleオーディエンスが「Possible Parisians」という名前の場合、フィルター`In Possible Parisians` - `equals` - `true`でこれらのユーザーをセグメントできます。

![mParticleカスタム属性]({% image_buster /assets/img_archive/mparticle2.png %})

##### 単一配列属性と単一文字列属性の両方 {#both-1}

mParticleは、単一配列属性と単一文字列属性の両方で説明されているとおりに属性を送信します。

##### 単一配列属性とセグメントごとに1つの属性の両方 {#both-2}

mParticleは、単一配列属性とセグメントごとに1つの属性の両方で説明されているとおりに属性を送信します。

##### 単一文字列属性とセグメントごとに1つの属性の両方 {#both-3}

mParticleは、単一文字列属性とセグメントごとに1つの属性の両方で説明されているとおりに属性を送信します。

##### 単一配列属性、単一文字列属性、およびセグメントごとに1つの属性 {#multi}

mParticleは、単一配列属性、単一文字列属性、およびセグメントごとに1つの属性で説明されているとおりに属性を送信します。

#### ステップ1:mParticleでオーディエンスを作成する {#send_settings}

mParticleでオーディエンスを作成するには:

1. **Audiences** > **Single Workspace** > **+ New Audience**に移動します。
2. Brazeをオーディエンスの出力として接続するには、以下のフィールドを入力する必要があります。

| フィールド名 | 説明 |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| APIキー | Brazeダッシュボードで**設定** > **APIキー**に移動します。 |
| APIキーのオペレーティングシステム | Braze APIキーが対応するオペレーティングシステムを選択します。この選択により、オーディエンス更新時に転送されるプッシュトークンの種類が制限されます。 |
| セグメントの送信方法 | オーディエンスをBrazeに送信する方法です。詳細については、[オーディエンスの転送](#forwarding-audiences)セクションを参照してください。 |
| ワークスペースREST APIキー | フル権限を持つBraze REST APIキー。これはBrazeダッシュボードの**設定** > **APIキー**で作成できます。 |
| 外部IDタイプ | Brazeにexternal IDとして転送するmParticleユーザーIDタイプ。デフォルト値のCustomer IDのままにすることをお勧めします。 |
| メールIDタイプ | Brazeにメールとして転送するmParticleユーザーIDタイプ。 |
| Brazeインスタンス | Brazeデータの転送先クラスターを指定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1:mParticleでオーディエンスを作成する" }

{:start="3"}
3. 最後にオーディエンスを**保存**します。

数分以内にオーディエンスがBrazeに同期され始めます。オーディエンスメンバーシップは、`external_ids`を持つユーザー（つまり、匿名ユーザーではないユーザー）に対してのみ更新されます。Braze mParticleオーディエンスの作成の詳細については、mParticleのドキュメント[設定](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings)を参照してください。

#### ステップ2:Brazeでユーザーをセグメントする {#step-2-segment-users-in-braze}

Brazeでこれらのユーザーのセグメントを作成するには、**Engagement**の下の**Segments**に移動し、セグメントに名前を付けます。以下は、**セグメントの送信方法**で選択したオプションに応じた2つのセグメントの例です。各オプションの詳細については、[オーディエンスの転送](#forwarding-audiences)を参照してください。

- **単一配列属性:** フィルターとして`SegmentMembershipArray`を選択します。次に、「includes value」オプションを使用して、目的のオーディエンスIDを入力します。![mParticleセグメントフィルター「SegmentMembershipArray」が「includes value」とオーディエンスIDに設定されている。]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **セグメントごとに1つの属性:** フィルターとしてカスタム属性を選択します。次に、「equals」オプションを使用して、適切なロジックを選択します。![mParticleセグメントフィルター「in possible parisians」が「equals」と「true」に設定されている。]({% image_buster /assets/img_archive/mparticle3.png %})

保存すると、ターゲットユーザーステップでCanvasまたはCampaign作成時にこのセグメントを参照できます。

#### 接続の無効化と削除 {#deactivating-and-deleting-connections}

mParticleはBrazeのセグメントを直接管理しないため、対応するmParticleオーディエンス接続が削除または無効化されてもセグメントは削除されません。この場合、mParticleはBrazeのオーディエンスユーザー属性を更新して各ユーザーからオーディエンスを削除しません。

削除前にBrazeユーザーからオーディエンスを削除するには、オーディエンスフィルターを調整してオーディエンスサイズを0にしてから、オーディエンスを削除します。オーディエンスの計算が完了して0ユーザーが返された後、オーディエンスを削除します。すると、Brazeのオーディエンスメンバーシップは、単一属性オプションの場合は`false`に更新され、配列形式の場合はオーディエンスIDが削除されます。

## データマッピング {#data-mapping}

mParticleを通じてモバイルアプリやWebアプリをBrazeに接続する場合は、[組み込みキット統合](#embedded-kit-integration)を使用してデータをBrazeにマッピングできます。また、[サーバー間API統合](#server-api-integration)を使用してサーバーサイドデータをBrazeに転送することもできます。

どちらのアプローチを選択する場合でも、Brazeを出力として設定する必要があります。

### Braze出力設定の構成 {#configure-your-braze-output-settings}

mParticleで**Setup > Outputs > Add Outputs**に移動し、**Braze**を選択してBrazeキット設定を開きます。完了したら**Save**を選択します。

| 設定名 | 説明 |
| ------------ | ----------- |
| Brazeアプリ識別子キー | Brazeアプリ識別子キーは、Brazeダッシュボードの**設定** > **APIキー**で確認できます。APIキーはプラットフォーム（iOS、Android、Web）ごとに異なることに注意してください。 |
| 外部IDタイプ | Brazeにexternal IDとして転送するmParticleユーザーIDタイプ。デフォルト値のCustomer IDのままにすることをお勧めします。 |
| メールIDタイプ | Brazeにメールとして転送するmParticleユーザーIDタイプ。デフォルト値のEmailのままにすることをお勧めします。 |
| Brazeインスタンス | Brazeデータの転送先クラスター。ダッシュボードと同じクラスターである必要があります。 |
| イベントストリーム転送の有効化 | （サーバー間）有効にすると、すべてのイベントがリアルタイムで転送されます。有効にしない場合、すべてのイベントは一括で転送されます。イベントストリーム転送を有効にする場合は、Brazeに渡すデータが[レート制限]({{site.baseurl}}/api/api_limits/)を遵守していることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze出力設定の構成" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### 組み込みキット統合 {#embedded-kit-integration}

組み込みキット統合により、mParticleとBraze SDKがアプリケーションに存在します。ただし、Brazeの直接統合とは異なり、mParticleがBraze SDKメソッドの大部分の呼び出しを代行します。ユーザーデータを追跡するために使用するmParticleメソッドは、自動的にBraze SDKメソッドにマッピングされます。

mParticle SDKの[Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy)、[iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy)、[Web](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze)のマッピングはオープンソースであり、[mParticleのGitHubページ](https://github.com/mparticle-integrations)で確認できます。

組み込みキットSDK統合により、プッシュ、アプリ内メッセージ、および関連するすべてのメッセージ分析トラッキングを含む、Brazeの全機能を活用できます。

{% alert note %}
Content Cardsおよびカスタムアプリ内メッセージ統合の場合は、Braze SDKメソッドを直接呼び出してください。
{% endalert %}

#### ステップ1:mParticle SDKを統合する {#step-1-integrate-the-mparticle-sdks}

プラットフォームのニーズに基づいて、適切なmParticle SDKをアプリに統合します。

* [mParticle for Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle for iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle for Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### ステップ2:mParticleのBrazeイベントキット統合を完了する {#step-2-complete-mparticles-braze-event-kit-integration}

このmParticle統合ではBraze SDKをWebサイトやアプリに直接含める必要はありませんが、アプリからBrazeにデータを転送するには、以下のmParticle Appboyキットをインストールする必要があります。

mParticleの[Brazeイベントキット統合ガイド](https://docs.mparticle.com/integrations/braze/event/#kit-integration)では、メッセージングのニーズ（プッシュ、位置情報の追跡など）に基づいたカスタムmParticleとBrazeの連携手順を説明しています。

#### ステップ3:Braze出力の接続設定 {#step-3-connections-settings-for-your-braze-output}

mParticleで**Connections** > **Connect** > **[目的のプラットフォーム]** > **Connect Output**に移動して、Brazeを出力として追加します。次に、**Save**を選択します。

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

すべての接続設定がすべてのプラットフォームと統合タイプに適用されるわけではありません。接続設定と適用されるプラットフォームの詳細については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#connection-settings)を参照してください。

### サーバーAPI統合 {#server-api-integration}

mParticleのサーバーサイドSDK（Ruby、Pythonなど）を使用している場合に、バックエンドデータをBrazeにルーティングするためのアドオンです。このサーバー間統合をBrazeで設定するには、[mParticleのドキュメント](https://docs.mparticle.com/guides/platform-guide/connections/)に従ってください。

{% alert important %}
サーバー間統合は、アプリ内メッセージ、Content Cards、プッシュ通知などのBraze UI機能をサポートしていません。また、デバイスレベルのフィールドなど、自動的にキャプチャされるデータもこの方法では利用できません。

これらの機能を使用する場合は、サイドバイサイド統合を検討してください。

サーバーサイドデータをBrazeに転送するには、`external_id`を含める必要があります。匿名ユーザーは転送されません。
{% endalert %}

#### Braze出力の接続設定 {#connections-settings-for-your-braze-output}

mParticleで**Connections > Connect > [目的のプラットフォーム] > Connect Output**に移動して、Brazeを出力として追加します。完了したら**Save**を選択します。

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

すべての接続設定がすべてのプラットフォームと統合タイプに適用されるわけではありません。接続設定と適用されるプラットフォームの詳細については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#connection-settings)を参照してください。

「Enriched User Attributes」または「Enriched User Identities」を有効にする前に、[データポイントの超過](#potential-data-point-overages)を確認して、これらの設定がデータポイント使用量にどのように影響するかを把握することをお勧めします。

### データマッピングの詳細 {#data-mapping-details}

#### データタイプ {#data-types}
両方のプラットフォーム間ですべてのデータタイプがサポートされているわけではありません。
- [カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)は、文字列、数値、ブール値、または日付オブジェクトをサポートしています。配列やネストされたオブジェクトはサポートしていません。
- [カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)は、文字列、数値、ブール値、日付オブジェクト、および配列をサポートしていますが、オブジェクトやネストされたオブジェクトはサポートしていません。

{% alert note %}
Brazeは、`Time`タイプのカスタム属性で西暦0年より前または西暦3000年より後のタイムスタンプをサポートしていません。BrazeはmParticleから送信されたこれらの値を取り込みますが、値は文字列として保存されます。
{% endalert %}

#### データマッピング

| mParticleデータタイプ | Brazeデータタイプ | 説明 |
| ------------------- | --------------- | ----------- |
| ユーザー属性（予約済み） | 標準属性 | たとえば、mParticleの`$FirstName`予約済みユーザー属性キーは、Brazeの`first_name`標準属性フィールドにマッピングされます。 |
| ユーザー属性（その他） | カスタム属性 | mParticleに渡されたユーザー属性のうち、予約済みユーザー属性キーに該当しないものは、Brazeにカスタム属性として記録されます。<br><br>ユーザー属性は、文字列、数値、ブール値、日付、および配列をサポートしていますが、オブジェクトやネストされたオブジェクトはサポートしていません。 |
| カスタムイベント | カスタムイベント | mParticleのカスタムイベントは、Brazeではカスタムイベントとして認識されます。イベント属性はカスタムイベントプロパティとして転送されます。<br><br>Brazeにイベントプロパティとして渡されるイベント属性は、文字列、数値、ブール値、または日付オブジェクトをサポートしていますが、配列やネストされたオブジェクトはサポートしていません。 |
| 購入コマースイベント | 購入イベント | 購入コマースイベントはBrazeの購入イベントにマッピングされます。<br><br>コマースイベントデータのバンドル設定値を切り替えて、注文レベルまたは製品レベルで購入を記録します。たとえば、`false`の場合、2つのユニークな製品、プロモーション、またはインプレッションを含む1つの受信イベントは、少なくとも2つの送信Brazeイベントになります。`true`に設定すると、ネストされた製品、プロモーション、またはインプレッション配列を含む1つの送信イベントになります。<br><br>記録される追加のコマースフィールドの詳細については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#purchase-events)を参照してください。<br><br>「bundle commerce event data」を`false`に設定した場合、Brazeに購入イベントプロパティとして渡される製品属性は、文字列、数値、ブール値、または日付オブジェクトをサポートしていますが、配列やネストされたオブジェクトはサポートしていません。|
| その他すべてのコマースイベント | カスタムイベント | その他すべてのコマースイベントはカスタムイベントにマッピングされます。<br><br>コマースイベントデータのバンドル設定値を切り替えて、注文レベルまたは製品レベルで購入を記録します。たとえば、`false`の場合、2つのユニークな製品、プロモーション、またはインプレッションを含む1つの受信イベントは、少なくとも2つの送信Brazeイベントになります。`true`に設定すると、ネストされた製品、プロモーション、またはインプレッション配列を含む1つの送信イベントになります。<br><br>特定のデフォルトコマース値に加えて、製品属性はBrazeイベントプロパティとして記録されます。記録される追加のコマースフィールドの詳細については、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)を参照してください。<br><br>「bundle commerce event data」を`false`に設定した場合、Brazeにイベントプロパティとして渡される製品属性は、文字列、数値、ブール値、または日付オブジェクトをサポートしていますが、配列やネストされたオブジェクトはサポートしていません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="データマッピング" }

#### ユーザーIDマッピング {#user-identity-mapping}
各mParticle出力について、Brazeに`external_id`として送信する外部IDタイプを選択できます。デフォルト値はCustomer IDですが、`MPID`などの別のIDをBrazeの`external_id`として送信するようにマッピングすることもできます。Customer ID以外の識別子を選択すると、Brazeでのデータ送信方法に影響する可能性があることに注意してください。

たとえば、MPIDをBrazeの`external_id`にマッピングすると、以下の影響があります。
- MPIDが割り当てられるタイミングの性質上、すべてのユーザーにセッション開始時に`external_id`が割り当てられます。
- MPIDと`external_id`のデータタイプの違いにより、Currentsの設定で追加のマッピングが必要になる場合があります。

### 消去リクエストの転送（データ主体リクエスト） {#forwarding-erasure-requests-data-subject-requests}

データ主体リクエスト出力をBrazeに設定して、消去リクエストをBrazeに転送します。消去リクエストをBrazeに転送するには、[mParticleのドキュメント](https://docs.mparticle.com/integrations/braze/forwarding-dsr/)に従ってください。

## データポイントの超過の可能性 {#potential-data-point-overages}

### エンリッチされたユーザー属性 {#enriched-user-attributes}

#### エンリッチされたユーザー属性/IDの有効化（サーバー間のみ） {#enriched}

mParticleの接続設定では、Brazeは**Include Enriched User Attributes**をオフにすることを推奨しています。有効にすると、mParticleは記録された各イベントに対して、既存のプロファイルから利用可能なすべてのユーザー属性（標準属性、カスタム属性、計算属性など）をBrazeに転送します。これにより、mParticleが各呼び出しで同じ変更されていない属性をBrazeに送信するため、データポイントの消費量が高くなります。

たとえば、ユーザーが最初のセッションで名、姓、電話番号を追加し、その後ニュースレターに登録して同じ情報とメールアドレスを追加し、ニュースレター登録イベントがトリガーされた場合:
- オンの場合（デフォルト）、5つのデータポイントが発生します。（登録イベント、メールアドレス、名、姓、電話番号）
- オフの場合、2つのデータポイントが発生します。（登録イベントとメールアドレス）

{% alert note %}
この設定をオフにしても、データの変更はチェックされません。ただし、元の受信バッチで受信されなかった、またはイベントの属性として明示的に設定されなかったユーザープロファイル上のすべてのユーザー属性の送信を防ぎます。差分のみがBrazeに渡されていることを確認することが引き続き重要です。
{% endalert %}

#### エンリッチされたユーザー属性をオフにする際の考慮事項 {#considerations-of-turning-off-enriched-user-attributes}

**Include Enriched User Attributes**をオフにする際に注意すべき考慮事項がいくつかあります。
1. サーバー間統合は、mParticleイベントAPIを使用してイベントをBrazeに送信します。各リクエストはイベントによってトリガーされます。メールアドレスの更新などのユーザー属性が変更されたが、特定のイベント（たとえば、プロファイル更新カスタムイベント）に関連付けられていない場合、新しい値は、ユーザーがトリガーした次のイベントのペイロードの「エンリッチされた属性」としてのみBrazeなどの出力に渡されます。**Include Enriched User Attributes**がオフの場合、特定のイベントに関連付けられていないこの新しい属性値はBrazeに渡されません。
  - これを解決するには、更新された特定のユーザー属性のみをBrazeに送信する別の「user attribute updated」イベントを作成することをお勧めします。このアプローチでは、「user attribute updated」イベントの追加データポイントが記録されますが、機能を有効にしてすべての呼び出しですべてのユーザー属性を送信するよりもデータポイント使用量ははるかに少なくなります。
2. 計算属性はエンリッチされたユーザー属性としてBrazeに渡されるため、「Enriched User Attributes」がオフの場合、これらはBrazeに渡されなくなります。「Enriched User Attributes」がオフの場合に計算属性をBrazeに転送するには、[計算属性フィード](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed)を使用すると、すべての属性をプッシュせずに済みます。このフィードは、計算属性が変更されたときにBrazeにダウンストリーム更新を送信します。

## トラブルシューティング {#troubleshooting}

### Brazeイベントキットを使用したiOSプッシュ通知のトラブルシューティング {#troubleshooting-ios-push-notifications-with-the-braze-event-kit}

iOSでBrazeイベントキット（組み込みキット統合）を使用しているときにプッシュ通知が機能しない場合は、以下を確認してください。
1. **プッシュトークンの転送:** mParticleがプッシュトークンをBrazeに転送していることを確認します。mParticleダッシュボードで、Brazeキット接続でプッシュが有効になっていること、および正しいAppleプッシュ認証情報がBrazeダッシュボードで設定されていることを確認してください。
2. **キットの初期化順序:** Brazeキットは、アプリがプッシュ権限をリクエストする前に初期化される必要があります。キットがアクティブになる前にプッシュ権限がリクエストされた場合、プッシュトークンがBrazeに転送されない可能性があります。mParticle SDKがアプリのライフサイクルの早い段階で開始されていることを確認してください。
3. **メソッドスウィズリング:** mParticle Appleキットは、メソッドスウィズリングを使用してプッシュトークンを自動的に転送し、プッシュ通知イベントを処理します。スウィズリングを無効にしている場合や、別のSDKが干渉している場合、プッシュトークンがBrazeに届かない可能性があります。mParticle設定でスウィズリングが有効になっていることを確認してください。
4. **手動トークン処理:** プッシュトークンを手動で管理している場合（たとえば、`application:didRegisterForRemoteNotificationsWithDeviceToken:`を実装している場合）、プッシュ通知トークンプロパティに割り当てることで、トークンをmParticleに渡していることを確認してください。例: `MParticle.sharedInstance().pushNotificationToken = deviceToken`。キットがそれをBrazeに転送します。
5. **環境の不一致:** APNs認証情報の環境（開発 vs. 本番）がアプリのビルドと一致していることを確認してください。詳細については、[iOSプッシュのトラブルシューティング]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)を参照してください。
6. **キットの初期化タイミング:** `didFinishLaunchingWithOptions`からBrazeインスタンスにアクセスしている場合、プッシュが届いたときにmParticleキットがまだ準備できていない可能性があります。[`userNotificationCenter(_:didReceive:withCompletionHandler:)`]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)（または同等の通知応答デリゲート）でプッシュ処理を初期化して、ユーザーが通知を開いたときにBrazeキットがアクティブになるようにしてください。

### 不要または重複したデータのBrazeへの送信 {#sending-unnecessary-or-duplicate-data-to-braze}
Brazeは、値が変更されていなくても、属性がBrazeに渡されるたびにデータポイントをカウントします。このため、Brazeでは、Braze内でアクションに必要なデータのみを転送し、属性の差分のみが渡されていることを確認することをお勧めします。
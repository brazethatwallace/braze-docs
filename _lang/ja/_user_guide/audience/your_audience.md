---
nav_title: オーディエンス
article_title: Brazeのオーディエンス
page_order: 0
page_type: reference
description: "Brazeがユーザーをどのように定義・管理し、ユーザーを識別し、ユーザーデータを活用してチャネル全体でセグメンテーション、パーソナライゼーション、メッセージングを実現するかについて説明します。"

---

# Brazeのオーディエンス {#your-braze-audience}

> Brazeがユーザーをどのように定義・管理し、ユーザーを識別し、ユーザーデータを活用してチャネル全体でセグメンテーション、パーソナライゼーション、メッセージングを実現するかについて説明します。

Brazeでは、ユーザー（およびそのユーザープロファイル）は、メッセージの送信や分析の対象となる個人を表します。

## ユーザープロファイル {#user-profiles}

[ユーザープロファイル]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)は、Brazeがその人物について把握しているすべての情報の唯一の信頼できるソースとして機能します。これには以下が含まれます。

- 識別子（ユーザーIDやexternal IDなど）
- デバイスとメッセージングチャネル
- 行動データとイベント
- 属性とプリファレンス
- メッセージエンゲージメント履歴

1つのユーザープロファイルは複数のデバイスやチャネルに関連付けることができるため、プラットフォーム全体にわたってユーザーを包括的に理解し、メッセージを送信できます。

## 匿名ユーザーと識別済みユーザー {#anonymous-users-and-identified-users}

Brazeのユーザーは、一般的に2つの状態のいずれかに分類されます。

### 匿名ユーザー {#anonymous-users}

[匿名ユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)とは、アプリやWebサイトとインタラクションしたものの、システムからの識別子（`external_id`など）がまだ割り当てられていないユーザーです。

- 匿名ユーザーは、Braze SDKの初期化時に自動的に作成されます
- イベント、属性、メッセージエンゲージメントを引き続き追跡できます
- チャネルやオプトインステータスに応じて、これらのユーザーにメッセージを送信できます

### 識別済みユーザー {#identified-users}

[識別済みユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#identified-user-profiles)とは、提供された`external_id`（顧客IDやアカウントIDなど）に関連付けられたユーザーです。

ユーザーを識別することで、以下が可能になります。

- デバイスやセッションをまたいだアクティビティの統合
- チャネル全体で一貫したメッセージの送信
- 長期的なユーザーデータを使用したセグメンテーションとパーソナライゼーション
- APIや統合を通じたプロファイルの管理

匿名ユーザーが後から識別されると、Brazeは[このマージ動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)に従って、対象となるデータを識別済みプロファイルにマージします。たとえば、プッシュトークンやメッセージング履歴は引き継がれ、匿名プロファイルの多くのフィールドは識別済みプロファイルにまだ設定されていない場合にのみマージされます。値が競合する場合は、識別済みプロファイルが保持されます。

## チャネルを通じたユーザーへのメッセージ送信 {#message-users-through-channels}

[チャネル]({{site.baseurl}}/user_guide/channels)とは、Brazeがユーザーにメッセージを配信するための特定の方法です。一般的なチャネルには以下があります。

- [プッシュ（Webまたはモバイル）]({{site.baseurl}}/user_guide/channels/push)
- [メール]({{site.baseurl}}/user_guide/channels/email)
- [SMS、MMS、RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
- [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp)
- [アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
- [バナー]({{site.baseurl}}/user_guide/channels/banners)
- [LINE]({{site.baseurl}}/user_guide/channels/line)
- [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)

1つのユーザープロファイルには、メールアドレスとモバイルデバイスの両方など、複数のチャネルを関連付けることができます。Brazeはこのモデルを使用して、ユーザーの統一されたビューを維持しながら、チャネル全体でメッセージングを調整します。

各チャネルには独自の配信ルール、オプトイン要件、メタデータがありますが、すべて同じユーザープロファイルに関連付けられています。

## ユーザーがBrazeに登録される方法 {#ways-users-enter-braze}

ユーザーは、サポートされている統合やチャネルを通じてブランドとインタラクションするたびにBrazeで作成されます。追加方法は、Brazeの実装方法によって異なります。

{% tabs %}
{% tab モバイルアプリ %}
- ユーザーが初めてアプリを開くと、Braze SDKがユーザープロファイルを作成します。
- デバイスとプッシュトークンは自動的に登録されます。
- イベントと属性はすぐに記録できます。
{% endtab %}

{% tab Web %}
- Web SDKの初期化時にユーザーが作成されます。
- Webプッシュサブスクリプションにより、ブラウザがメッセージングチャネルとして登録されます。
{% endtab %}

{% tab メールとSMS %}
- データのアップロード、APIの呼び出し、またはオプトインの収集時にユーザーを作成できます。
- メールアドレスと電話番号はチャネル識別子として保存されます。
- オプトインステータスはチャネルごと、地域ごとに追跡されます。
{% endtab %}

{% tab APIと統合 %}
- [REST API]({{site.baseurl}}/api/endpoints/user_data)や[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)を通じて、ユーザーを直接作成または更新できます。
- 外部ツール（CDP、CRM、データウェアハウスなど）は、ユーザーをBrazeに自動的に同期できます。
{% endtab %}
{% endtabs %}

## オーディエンスデータソース {#audience-data-sources}

Brazeのユーザーデータは、通常、複数のソースの組み合わせから取得されます。

{% tabs %}
{% tab 自動収集 %}
Braze SDKは、以下のようなコンテキストデータを自動的に収集します。

- デバイスタイプとOS
- 言語とタイムゾーン
- アプリバージョンとセッションアクティビティ
{% endtab %}

{% tab ユーザー行動 %}
ユーザーがアプリやメッセージとインタラクションすると、Brazeは以下を記録します。

- [カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)（購入や機能の使用など）
- メッセージの開封、クリック、コンバージョン
- セッションアクティビティとエンゲージメントの傾向
{% endtab %}

{% tab お客様のシステム %}
以下を使用して、独自のツールからBrazeにデータを送信できます。

- [REST API]({{site.baseurl}}/api/endpoints/user_data)
- [CSVアップロード]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- スケジュールされたデータ同期

これには通常、識別子、アカウントデータ、または履歴コンテキストが含まれます。
{% endtab %}
{% endtabs %}

### ユーザー提供の入力 {#user-provided-input}

ユーザーは以下を通じて直接データを提供する場合があります。

- [ユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)
- フォームやアンケート（SDKまたは統合）
- アプリ内エクスペリエンス

### 統合 {#integrations}

Brazeは、統合を通じて[Segment]({{site.baseurl}}/partners/segment)、データウェアハウス、分析テックパートナーなどのプラットフォームと連携し、ユーザーデータがユーザープロファイルに自動的に流れるようにします。

## ユーザーデータの管理 {#manage-user-data}

ユーザーデータの追加、更新、削除は、いくつかの方法で行えます。

- **ダッシュボードツール**：手動編集やCSVアップロード
- **API**：リアルタイムまたはプログラムによる更新
- **SDK**：アプリやサイトでの行動の直接キャプチャ
- **統合**：継続的な同期

データの削除は以下の方法で行えます。

- 属性値のクリア
- タグの削除
- サブスクリプションステータスの更新
- ログアウト時のユーザーリセット（匿名ユースケースの場合）

## オーディエンスデータ機能 {#audience-data-features}

ユーザーデータがBrazeに取り込まれると、ほぼすべてのエンゲージメント機能を支えます。ユーザーデータが完全で正確であるほど、以下の機能をより効果的に活用できます。

| 機能 | 説明 |
| ---- | ---- |
| [セグメンテーション]({{site.baseurl}}/user_guide/audience/segments) | 以下に基づいてオーディエンスを作成します。{::nomarkdown}<ul><li>属性とカスタムフィールド</li> <li>イベントと行動</li> <li>メッセージエンゲージメント</li> <li>デバイスとチャネルのプロパティ</li></ul>{:/} <br>SegmentsはCampaignsやCanvasesで再利用できます。 |
| [パーソナライゼーション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) | ユーザーデータを使用して、以下のようなコンテンツをカスタマイズします。{::nomarkdown}<ul><li>メッセージコピー内の名前やプリファレンス</li> <li>ダイナミックなおすすめ</li> <li>ロケーションや言語に固有のコンテンツ</li></ul>{:/} |
| オートメーションとオーケストレーション | 以下に基づいてメッセージやジャーニーをトリガーします。{::nomarkdown}<ul><li>ユーザーアクション</li> <li>属性の変更</li> <li>時間ベースの条件</li></ul>{:/} |
| クロスチャネルコーディネーション | 以下を尊重しながら、最も適切なチャネルでユーザーにリーチします。{::nomarkdown}<ul><li>オプトインステータス</li> <li>フリークエンシーキャップ</li> <li>チャネルプリファレンス</li></ul>{:/} |
| [分析とインサイト]({{site.baseurl}}/user_guide/analytics) | 以下を分析して、さまざまなオーディエンスの行動を理解します。{::nomarkdown}<ul><li>エンゲージメント率</li> <li>コンバージョンパス</li> <li>Segmentの経時的なパフォーマンス</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="オーディエンスデータ機能" }
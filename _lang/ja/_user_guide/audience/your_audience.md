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

[ユーザープロファイル]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)は、Brazeがその人物について把握しているすべての情報の唯一の信頼できる情報源として機能します。これには以下が含まれます。

- 識別子（ユーザーIDやexternal IDなど）
- デバイスとメッセージングチャネル
- 行動データとイベント
- 属性と設定
- メッセージエンゲージメント履歴

1つのユーザープロファイルは複数のデバイスやチャネルに関連付けることができるため、プラットフォーム全体を通じてユーザーを包括的に理解し、メッセージを送信できます。

## 匿名ユーザーと識別済みユーザー {#anonymous-users-and-identified-users}

Brazeのユーザーは、一般的に2つのステータスのいずれかに分類されます。

### 匿名ユーザー {#anonymous-users}

[匿名ユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)とは、アプリやWebサイトを操作したものの、まだシステムから識別子（`external_id`など）が割り当てられていないユーザーです。

- 匿名ユーザーは、Braze SDKの初期化時に自動的に作成されます
- イベント、属性、メッセージエンゲージメントを引き続き追跡できます
- チャネルやオプトインステータスに応じて、メッセージを受信できます

#### 匿名ユーザーと同意 {#anonymous-users-and-consent}

同意ポリシーに準拠するためにBraze SDKを同意ラッパーで囲む必要がある場合、ユーザーが同意を付与する前に匿名データを収集できます。SDKが初期化されると匿名ユーザープロファイルが作成され、同意要件を尊重しながら行動を追跡できます。

**匿名ユーザーへのメッセージ送信:**
匿名ユーザーは、Braze SDKが初期化されている限り、メッセージをトリガーおよび受信できます。これには以下が含まれます。

- [アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [プッシュ通知]({{site.baseurl}}/user_guide/channels/push)（プッシュトークンが登録されている場合）
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)

ただし、ユーザーが同意しなかった場合や同意を撤回した場合にSDKの初期化を無効化または阻止すると、SDKトリガーのチャネルはそのユーザーに対して機能しません。

**同意ステータスに基づくユーザーのターゲティング:**
同意ステータスに基づいてユーザーにメッセージを送信するには、ユーザープロファイルにカスタムユーザー属性（`has_marketing_consent`など）を設定します。その後、この属性に基づいてセグメントを作成し、ユーザーがBraze外で同意設定を変更した場合にもこの値を同期した状態に保つことができます。匿名ユーザーのターゲティングの詳細については、[ユースケース]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#use-cases)を参照してください。

### 識別済みユーザー {#identified-users}

[識別済みユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#identified-user-profiles)とは、お客様が提供する`external_id`（顧客IDやアカウントIDなど）に関連付けられたユーザーです。

ユーザーを識別することで、以下が可能になります。

- デバイスやセッション間のアクティビティの統合
- チャネル間で一貫したメッセージの送信
- 長期的なユーザーデータを使用したセグメンテーションとパーソナライゼーション
- APIやインテグレーションを通じたプロファイルの管理

匿名ユーザーが後に識別されると、Brazeは[このマージ動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)に従って、対象のデータを識別済みプロファイルにマージします。たとえば、プッシュトークンやメッセージング履歴は引き継がれ、匿名プロファイルの多くのフィールドは識別済みプロファイルにまだ設定されていない場合にのみマージされます。値が競合する場合は、識別済みプロファイルの値が保持されます。

## チャネルを通じてユーザーにメッセージを送信する {#message-users-through-channels}

[チャネル]({{site.baseurl}}/user_guide/channels)は、Brazeがユーザーにメッセージを届けるための特定の方法です。一般的なチャネルには次のものがあります。

- [プッシュ（Webまたはモバイル）]({{site.baseurl}}/user_guide/channels/push)
- [メール]({{site.baseurl}}/user_guide/channels/email)
- [SMS、MMS、RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
- [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp)
- [アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
- [バナー]({{site.baseurl}}/user_guide/channels/banners)
- [LINE]({{site.baseurl}}/user_guide/channels/line)
- [webhook]({{site.baseurl}}/user_guide/channels/webhooks)

1つのユーザープロファイルには、メールアドレスとモバイルデバイスの両方など、複数のチャネルを関連付けることができます。Brazeはこのモデルを使用して、ユーザーの統一されたビューを維持しながら、チャネル間のメッセージングを調整します。

各チャネルにはそれぞれ独自の配信ルール、オプトイン要件、メタデータがありますが、すべて同じユーザープロファイルに関連付けられています。

## ユーザーが Braze に入る方法 {#ways-users-enter-braze}

ユーザーは、サポートされている連携やチャネルを通じてブランドとやり取りするたびに Braze で作成されます。ユーザーの追加方法は、Braze の実装方法によって異なります。

{% tabs %}
{% tab モバイルアプリ %}
- ユーザーが初めてアプリを開くと、Braze SDKがユーザープロファイルを作成します。
- デバイスとプッシュトークンは自動的に登録されます。
- イベントと属性はすぐに記録できます。
{% endtab %}

{% tab Web %}
- Web SDKが初期化されるとユーザーが作成されます。
- Web プッシュの購読により、ブラウザーがメッセージングチャネルとして登録されます。
{% endtab %}

{% tab メールと SMS %}
- データのアップロード、API の呼び出し、またはオプトインの収集時にユーザーを作成できます。
- メールアドレスと電話番号はチャネル識別子として保存されます。
- オプトインステータスはチャネルごと、地域ごとに追跡されます。
{% endtab %}

{% tab API と連携 %}
- [REST API]({{site.baseurl}}/api/endpoints/user_data) または [CSV のインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)を通じて、ユーザーを直接作成または更新できます。
- 外部ツール（顧客データプラットフォーム、CRM、データウェアハウスなど）を使って、ユーザーを自動的に Braze に同期できます。
{% endtab %}
{% endtabs %}

## オーディエンスデータソース {#audience-data-sources}

Brazeのユーザーデータは通常、複数のソースの組み合わせから取得されます。

{% tabs %}
{% tab 自動収集 %}
Braze SDKは以下のようなコンテキストデータを自動的に収集します。

- デバイスタイプとOS
- 言語とタイムゾーン
- アプリのバージョンとセッションアクティビティ
{% endtab %}

{% tab ユーザー行動 %}
ユーザーがアプリやメッセージを操作すると、Brazeは以下を記録します。

- [カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)（例：購入や機能の利用）
- メッセージの開封、クリック、コンバージョン
- セッションアクティビティとエンゲージメントのトレンド
{% endtab %}

{% tab お客様のシステム %}
以下の方法を使用して、お客様のツールからBrazeにデータを送信できます。

- [REST API]({{site.baseurl}}/api/endpoints/user_data)
- [CSVアップロード]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- スケジュールされたデータ同期

これには、識別子、アカウントデータ、または履歴コンテキストが含まれることが多いです。
{% endtab %}
{% endtabs %}

### ユーザー提供の入力 {#user-provided-input}

ユーザーは以下を通じて直接データを提供することがあります。

- [ユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)
- フォームやアンケート（SDKまたはインテグレーション）
- アプリ内エクスペリエンス

### インテグレーション {#integrations}

Brazeは[セグメント]({{site.baseurl}}/partners/segment)、データウェアハウス、分析テックパートナーなどのプラットフォームとインテグレーションを通じて連携し、ユーザーデータがユーザープロファイルに自動的に流れるようにします。

## ユーザーデータの管理 {#manage-user-data}

ユーザーデータの追加、更新、削除は、いくつかの方法で行えます。

- **ダッシュボードツール**：手動編集やCSVアップロード
- **API**：リアルタイムまたはプログラムによる更新
- **SDK**：アプリやサイトでの行動を直接キャプチャ
- **インテグレーション**：継続的な同期

データの削除は以下の方法で行えます。

- 属性値のクリア
- タグの削除
- 購読ステータスの更新
- ログアウト時のユーザーリセット（匿名ユースケースの場合）

## オーディエンスデータの機能 {#audience-data-features}

ユーザーデータがBrazeに取り込まれると、ほぼすべてのエンゲージメント機能を活用できるようになります。ユーザーデータが完全で正確であるほど、以下の機能をより効果的に活用できます。

| 機能 | 説明 |
| ---- | ---- |
| [セグメンテーション]({{site.baseurl}}/user_guide/audience/segments) | 以下の条件に基づいてオーディエンスを作成します。{::nomarkdown}<ul><li>属性とカスタムフィールド</li> <li>イベントと行動</li> <li>メッセージエンゲージメント</li> <li>デバイスおよびチャネルのプロパティ</li></ul>{:/} <br>セグメントはキャンペーンやキャンバスで再利用できます。 |
| [パーソナライゼーション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) | ユーザーデータを使用して、以下のようなコンテンツをカスタマイズします。{::nomarkdown}<ul><li>メッセージ本文中の名前や設定</li> <li>ダイナミックなレコメンデーション</li> <li>場所や言語に応じたコンテンツ</li></ul>{:/} |
| オートメーションとオーケストレーション | 以下に基づいてメッセージやジャーニーをトリガーします。{::nomarkdown}<ul><li>ユーザーアクション</li> <li>属性の変更</li> <li>時間ベースの条件</li></ul>{:/} |
| クロスチャネルの連携 | 以下を考慮しながら、最適なチャネルでユーザーにリーチします。{::nomarkdown}<ul><li>オプトインステータス</li> <li>フリークエンシーキャップ</li> <li>チャネルの設定</li></ul>{:/} |
| [分析とインサイト]({{site.baseurl}}/user_guide/analytics) | 以下を分析して、さまざまなオーディエンスの行動を理解します。{::nomarkdown}<ul><li>エンゲージメント率</li> <li>コンバージョンパス</li> <li>セグメントパフォーマンスの時間推移</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="オーディエンスデータの機能" }
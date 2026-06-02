---
nav_title: mParticleとCurrents
article_title: mParticleとCurrents
alias: /partners/mparticle_for_currents/
description: "この参考記事では、Braze Currentsと、マーケティングスタック内のソース間で情報を収集しルーティングする顧客データプラットフォームであるmParticleとのパートナーシップについて概説しています。"
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticleとCurrents {#mparticle-for-currents}

> [mParticle](https://www.mparticle.com)は、複数のソースから情報を収集し、マーケティングスタックの他のさまざまな場所にルーティングする顧客データプラットフォームです。

BrazeとmParticleの統合により、2つのシステム間の情報の流れをシームレスに制御できます。[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)を使用すると、データをmParticleに接続し、グローススタック全体で実用的なデータにすることもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Currents | mParticleにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定する必要があります。 |
| mParticleアカウント | このパートナーシップを利用するには、[mParticleアカウント](https://app.mparticle.com/login)が必要です。 |
| mParticleのサーバー間キーとシークレット | これらを取得するには、mParticleダッシュボードに移動し、mParticleがiOS、Android、およびWebプラットフォームのBrazeインタラクションデータを受信できるようにする[必要なフィード](#step-1-create-feeds)を作成します。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## mParticle認証情報について {#about-mparticle-credentials}

mParticleには、アプリレベルとワークスペースレベルの認証情報があり、イベントの送信方法に影響を与えます。

- **アプリレベル：** mParticleは各アプリごとにイベントを分離するため、iOSアプリに与えるアプリレベルの認証情報は、iOS固有のイベントを送信するためにのみ使用できます。
- **ワークスペースレベル：** mParticleは、（アプリ固有**ではない**）すべてのイベントをグループ化します。つまり、アプリグループに与えるワークスペースレベルの認証情報は、アプリ固有ではないすべてのイベントの送信に使用されます。

これは、mParticleが個々のアプリに基づいて「フィード」を取り込んでいると考えることができます。例えば、iOS用、Android用、Web用のアプリを1つずつ用意すると、イベントがバラバラになります。つまり、各アプリに同じ認証情報を提供すると、1つのmParticleフィードが、重複することなく、すべてのアプリのすべてのデータを受信するために使用されます。

## 統合 {#integration}

### ステップ1:フィードを作成する {#step-1-create-feeds}

mParticle管理者アカウントから、**Setup > Inputs**に移動します。mParticleの**Directory**で**Braze**を見つけ、フィード統合を追加します。

Brazeフィード統合は、iOS、Android、Web、Unboundの4つの個別フィードをサポートしています。Unboundフィードは、プラットフォームに接続されていないメールなどのイベントに使用できます。メインプラットフォームフィードごとに入力を作成する必要があります。追加の入力は、**Setup > Inputs**の**Feed Configurations**タブから作成できます。

![]({% image_buster /assets/img/braze-feed-inputs.png %})

各フィードについて、**Act as Platform**でリストから一致するプラットフォームを選択します。**act-as**フィードを選択するオプションが表示されない場合、データはUnboundとして扱われますが、データウェアハウス出力に転送することは可能です。

![設定名の入力、フィードステータスの決定、およびプラットフォームの選択を求める最初の統合ダイアログボックス。]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![サーバー間キーとサーバー間シークレットを表示する2番目の統合ダイアログボックス。]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

各入力を作成すると、mParticleからキーとシークレットが提供されます。これらの認証情報をコピーし、各認証情報のペアがどのフィード用であるかを必ずメモしてください。

### ステップ2:Currentを作成する {#step-2-create-current}

Brazeで、**Currents > + Create Current > Create mParticle Export**に移動します。統合名、連絡先メールアドレス、および各プラットフォームのmParticle APIキーとmParticleシークレットキーを入力します。次に、追跡するイベントを選択します。利用可能なイベントのリストが提供されます。最後に、**Launch Current**をクリックします。

![BrazeのmParticle Currentsページ。ここでは、統合名、連絡先メールアドレス、APIキー、シークレットキーのフィールドがあります。]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
mParticle APIキーとmParticleシークレットキーを最新の状態に保つことが重要です。コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止します。この状態が**5日間**以上続くと、コネクタのイベントは破棄され、データは永久に失われます。
{% endalert %}

mParticleに送信されるすべてのイベントには、ユーザーの`external_user_id`が`customerid`として含まれます。現時点では、Brazeは`external_user_id`が設定されていないユーザーのイベントデータを送信しません。`external_user_id`をmParticleのデフォルトの`customerid`以外の別のIDにマッピングしたい場合は、Brazeのカスタマーサクセスマネージャーにお問い合わせください。

## サポートされているCurrentsイベント {#supported-currents-events}

Brazeは以下のイベントをmParticleにエクスポートすることをサポートしています：

- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

各イベントのペイロード構造については、[メッセージエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)および[顧客行動イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)の**mParticle**タブを選択してください。

mParticle統合の詳細については、[mParticleのドキュメント](http://docs.mparticle.com/integrations/braze/feed)をご覧ください。
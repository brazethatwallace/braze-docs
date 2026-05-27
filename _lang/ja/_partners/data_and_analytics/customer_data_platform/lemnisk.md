---
nav_title: Lemnisk
article_title: LemniskとBrazeの統合
description: "このリファレンス記事では、BrazeとAIを活用した顧客データプラットフォーム主導のマーケティングオートメーションプラットフォームであるLemniskとのパートナーシップについて詳しく説明しています。Lemniskでさまざまなソースから収集したユーザーデータをBrazeにストリーミングし、Brazeのツールを使用してさまざまなチャネルや送信先でアクティベーションできます。"
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/)は、AIを活用した顧客データプラットフォーム（CDP）およびマーケティングオートメーションソリューションであり、サイロ化した多様なソースから顧客データをリアルタイムで収集、統合、アクティベーションできます。堅牢なリアルタイム分析を提供し、顧客データのライフサイクルの各段階を追跡しながら、この統合データをさまざまなマーテクおよびビジネスプラットフォームにシームレスに配信します。

_この統合はLemniskによって管理されています。_

## 統合について {#about-the-integration}

LemniskとBrazeの統合により、ブランドや企業は、リアルタイムでプラットフォーム間のユーザーデータを統合するCDP主導のインテリジェンスレイヤーとして機能し、収集したユーザーの情報や行動をリアルタイムでBrazeに送信することで、Brazeの潜在能力を最大限に引き出すことができます。Lemniskは、行動シグナルと個人属性をブレンドすることで、エンリッチされた顧客プロファイルを直接Brazeに提供し、より深いコンテキストでメッセージングをパーソナライズできるようにします。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| Lemniskアカウント | このパートナーシップを利用するには、[Lemnisk](https://www.lemnisk.co/)のアカウントが必要です。 |
| LemniskのExternal API | Lemniskのカスタマーサクセスマネージャーに連絡して、アカウントの**External API**を有効にしてもらいます。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[アカウントのBraze URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/#api-and-sdk-endpoints)に依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Lemniskの統合 {#integrating-lemnisk}

### ステップ 1: Braze External APIを作成する {#create-a-braze-external-api}

Lemniskで、External APIチャネルに移動します。**Add New External API**を選択します。ここでは、[Track Users]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)エンドポイントをExternal APIとして設定します。

![LemniskでExternal API作成プロセスを開始する]({% image_buster /assets/img/lemnisk/open_external_api.png %})

**Basic Details**で、名前、説明、チャネル、チャネル識別子を入力します。

![Lemniskで新しいExternal APIの基本設定の詳細を入力する]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

**External API details**で、`users.track` エンドポイントの関連する詳細を入力します。{% raw %}`{{}}`{% endraw %}を使って複数のエンゲージメントレベルのフィールドを定義でき、キャンペーンごとに異なる値を設定できます。

![External APIエンドポイントとペイロードの詳細を記入する]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

Track Usersの設定を完了するには、**Save**を選択します。自動的に**Test API**ページにリダイレクトされます。

### ステップ 2: 設定をテストする {#step-2-test-the-configuration}

**Test API**ページで、JSONツリービューにAPIパラメータのテスト値を入力し、**Test Configuration**を選択します。

認証情報とAPI定義が正しければ、Brazeは成功レスポンスを返します。

![サンプルペイロードと成功レスポンスを使ってExternal API設定をテストする]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

次に、イベントがBrazeに正常に送信されていることを確認します。Brazeダッシュボードで、**オーディエンス** > **ユーザーを検索**に進み、External API設定から識別子の1つ（ユーザーのメールアドレスなど）を入力します。すべてが正しく機能していれば、テストAPIトリガーを受け取ったプロファイルがリストに表示されます。

![Brazeでユーザープロファイルとアクティビティ概要を表示する]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### ステップ 3: Brazeでユーザーイベントをトリガーする {#step-3-trigger-user-events-in-braze}

1. Lemniskで新しいセグメントを作成します。たとえば、ユーザーがリードフォームを送信するとすぐにBrazeに情報を送信するセグメントを作成できます。
2. 新しいセグメントで、**External API** > **Add Engagement**に進みます。
3. **Engagement Creation**で、基本的な詳細を入力し、[以前に作成した](#create-a-braze-external-api)設定を選択します。
4. **Configure Parameters**の下に、エンゲージメントレベルで公開することにしたBrazeパラメータの入力項目があります。以下の例では、_ユーザー名_、_製品ID_、_イベント時間_が表示されています。
    ![ユーザーデータをBrazeに送信するエンゲージメントを作成する]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. 選択したパラメータに関連するパーソナライゼーション変数を入力し、**Save**を選択します。
6. 完了したら、エンゲージメントを有効にします。
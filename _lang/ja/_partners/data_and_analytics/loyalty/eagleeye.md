---
nav_title: Eagle Eye
article_title: Eagle Eye
description: Braze と Eagle Eye を統合する方法について説明します。
alias: /partners/eagle_eye/
page_type: partner
search_tag: Partner
---

# Eagle Eye

> [Eagle Eye](https://eagleeye.com/) はSaaSとAIテクノロジーのリーディングカンパニーで、小売、旅行、ホスピタリティの各ブランドが、リアルタイム、オムニチャネル、パーソナライズされた消費者マーケティング活動を大規模に展開することで、エンド顧客のロイヤルティを獲得できるよう支援しています。

_この統合はEagle Eyeによって管理されています。_

## 概要 {#overview}

Eagle Eye Connectは、BrazeとAIR間の双方向統合で、ブランドがロイヤルティや販促データをBrazeで直接有効化できるようにします。クライアントは、AIR内でオーディエンスに参加した消費者に対して、AIRで報酬を発行できます。これにより、マーケターはポイント残高、プロモーション、報酬アクティビティなどのリアルタイムデータを使用して、カスタマーエンゲージメントをパーソナライズできます。

## ユースケース {#use-cases}

- ポイントのしきい値や獲得報酬などのロイヤルティイベントに基づいてBrazeのキャンペーンをトリガーします。
- Brazeのユーザープロファイルをリアルタイムのロイヤルティデータで充実させ、よりパーソナライズされたターゲティングを可能にします。
- 報酬の引き換えに関連するキャンペーンの効果を追跡およびレポートします。
- ユーザーがBrazeでキャンペーンに参加すると、AIRで報酬を発行します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|--------------------------|-------------|
| Eagle Eye AIR アカウント | このパートナーシップを利用するには、アクティブなEagle Eye AIRアカウントが必要です。開始するには、Eagle Eyeのパートナーシップチーム（[partnerships@eagleeye.com](mailto:partnerships@eagleeye.com)）にお問い合わせください。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [REST エンドポイント URL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントはインスタンスのBraze URLに応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## アウトバウンドとインバウンド {#outbound-vs-inbound}

以下の表は、BrazeとEagle Eye AIRの間でサポートされる2種類の統合の概要を示しています。Eagle Eye Connectは、AIRとBrazeのようなパートナーシステム間のデータ交換を可能にするミドルウェアです。詳しくは、[Eagle EyeのBrazeドキュメント](https://developer.eagleeye.com/docs/braze)を参照してください。

{% tabs local %}
{% tab アウトバウンド %}
<table aria-label="アウトバウンドとインバウンド">
  <caption>アウトバウンドとインバウンド</caption>
  <thead>
    <tr>
      <th>方向</th>
      <th>開始者</th>
      <th>データフロー</th>
      <th>目的</th>
      <th>例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eagle Eye → Braze</td>
      <td>Eagle Eye</td>
      <td>Braze APIへ</td>
      <td>
        ロイヤルティデータをカスタムイベント経由でカスタム属性としてBrazeユーザープロファイルに送信します。Brazeでは、取り込んだデータを次のように使用できます。
        <ul>
          <li>ユーザーのセグメント化、キャンペーンのトリガー</li>
          <li>メッセージのパーソナライズ</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>ロイヤルティポイントやティアステータスをBrazeに送信する（<code>ee_loyalty.points.current</code>、<code>ee_loyalty.tier.tierId</code>）</li>
          <li>ユーザーがクーポンを受け取ったり利用したりした際にユーザープロファイルを更新します。</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="アウトバウンドとインバウンド" }
{% endtab %}

{% tab インバウンド %}
<table aria-label="アウトバウンドとインバウンド">
  <caption>アウトバウンドとインバウンド</caption>
  <thead>
    <tr>
      <th>方向</th>
      <th>開始者</th>
      <th>データフロー</th>
      <th>目的</th>
      <th>例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Braze → Eagle Eye</td>
      <td>Braze</td>
      <td>Webhook経由でEagle Eye APIへ</td>
      <td>
        消費者が何らかのソースからBrazeのオーディエンスに入ると、BrazeはEE ConnectへのBraze Webhookをトリガーし、EEが報酬（クーポンまたはポイント）を発行できるようにします。<br><br>
        AIRでアクションが完了すると、BrazeはAIRからアウトバウンドイベントを受け取ります。
      </td>
      <td>
        <ul>
          <li>ロイヤルティプログラムに参加した消費者に報酬（クーポンまたはポイント）が発行されます。</li>
          <li>配送が遅延した消費者に報酬が発行されます。</li>
          <li>誕生日の報酬</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="アウトバウンドとインバウンド" }
{% endtab %}
{% endtabs %}

{% alert tip %}
カスタム属性やイベントとしてBrazeに送信できるカスタムデータの詳細については、[Eagle EyeのBrazeドキュメント](https://developer.eagleeye.com/docs/braze#data-model)を参照してください。
{% endalert %}

## 統合の概要 {#integration-overview}

現在、インバウンドおよびアウトバウンドのコネクターは、Eagle Eyeチームの直接サポートによるAPI経由でのみ設定できますが、AIRダッシュボード内のセルフサービスオプションが近日中に提供される予定です。

Eagle Eyeチームと協力する際には、以下を実行します。

### ステップ 1: 設定の詳細を提供する {#step-1-provide-configuration-details}

まず、Eagle Eyeチームに次の詳細情報を提供します。

| 提供する情報 | 説明 |
|------------------------|-------------|
| Braze API認証情報 | Braze RESTエンドポイント、アプリ識別子、APIキーをEagle Eyeの担当者と安全に共有します。 |
| 識別子マッチング | external IDやメールなど、AIRとBrazeで共通するプロファイル更新用の主要ユーザー識別子を決定し、共有します。 |
| 認証キー | インバウンドおよびアウトバウンドコネクターごとに秘密認証キーを決定して共有します。 |
| 通貨コード | 購入金額を表示するための3桁の通貨コードを共有します（例: USD）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 1: 設定の詳細を提供する" }

### ステップ 2: Eagle Eye Connectを設定する {#step-2-configure-eagle-eye-connect}

Eagle Eyeチームは、提供された詳細情報、固有のAIR API認証情報、およびコネクター用のアウトバウンドイベントを使用してEagle Eye Connectを設定します。

### ステップ 3: AIRでソーシャル行動アクションを設定する {#step-3-configure-social-behavioral-actions-in-air}

次に、ポイントまたはクーポンを発行するための一意のアクション参照を使用して、AIRで1つ以上のソーシャル行動アクションを設定します。

### ステップ 4: Brazeを設定する {#step-4-configure-braze}

Brazeで、以下を実行します。

- AIRで報酬を発行するためのキャンペーンをBrazeで設定する
- AIRイベントを受信したときの消費者へのコミュニケーションを設定する

### ステップ 5: 統合をテストする {#step-5-test-your-integration}

AIRでAPI呼び出しを行い、Brazeワークスペースへのイベントデータフローを確認します。AIRから受信したデータを検証し、属性が期待どおりに更新されていることを確認します。

また、ユーザーをオーディエンスに追加し、AIRで報酬が発行されることを確認します。

### ステップ 6: 本番環境にローンチする {#step-6-launch-to-production}

テストが成功した後は、統合を本番環境で稼働させ、Brazeにデータを継続的に送信できます。AIRとBrazeの本番環境でも同じ設定ステップが必要です。

Eagle Eyeカスタマーサクセスマネージャーに連絡してリソースの割り当てを依頼し、EE Connectの設定を行ってください。

## サポート {#support}

統合のサポートやトラブルシューティングについては、Eagle Eyeのサポートチーム（[support@eagleeye.com](mailto:support@eagleeye.com)）までお問い合わせください。
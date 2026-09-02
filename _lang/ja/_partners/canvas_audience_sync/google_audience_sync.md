---
nav_title: Google
article_title: キャンバスオーディエンスを Google に同期
alias: /google_audience_sync/
description: "このリファレンス記事では、Braze Audience Sync to Google を使用して、行動トリガー、セグメンテーションなどに基づいて広告を配信する方法について説明します。"
tool:
  - Canvas
page_order: 3

---

# オーディエンスを Google に同期する {#audience-sync-to-google}

{% alert important %}
Google は、2024年3月6日より施行されている[デジタル市場法（DMA）](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の改正に対応するため、[EU ユーザーの同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を改定しています。この新たな改正により、広告主は EEA、英国、スイスのエンドユーザーに対して特定の情報を開示し、必要な同意を得ることが求められます。詳細については、以下のドキュメントを確認してください。
{% endalert %}

Braze Audience Sync to Google 統合により、ブランドはクロスチャネルのカスタマージャーニーの範囲を Google 検索、Google ショッピング、Gmail、YouTube、および Google ディスプレイに拡大できます。ファーストパーティの顧客データを使用して、ダイナミックな行動トリガー、セグメンテーションなどに基づいて安全に広告を配信できます。Braze キャンバスの一部としてメッセージ（例えば、プッシュ、メール、SMS）をトリガーするために通常使用する任意の基準を使用して、Googleの[カスタマーマッチ](https://support.google.com/google-ads/answer/6379332?hl=en)を通じてそのユーザーに広告をトリガーすることができます。

{% alert note %}
Braze Audience Sync to Google 統合は、Google Ads マネージャー ではなく Google Ads でサポートされています。
{% endalert %}

Google Ads は、ターゲティングとレポート用に「lookalike audiences」とも呼ばれる類似オーディエンスを生成しなくなりました。詳細については、[Google 広告ドキュメント](https://support.google.com/google-ads/answer/12463119?)を参照してください。

## Google Data マネージャー API

{% alert important %}
Google Data マネージャー APIによるGoogle向けオーディエンス同期のサポートは、早期アクセス段階です。利用資格とロールアウトのタイミングについては、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

Googleは広告連携をData マネージャー APIに統合しています。早期アクセスでは、BrazeのGoogle向けオーディエンス同期がこのAPIを使用して、進行中のGoogle広告APIの変更に対応できます。

新規および再接続されたGoogleオーディエンス同期の接続では、Brazeが必要なData マネージャースコープを自動的にリクエストします。既存の接続は、再接続するまでレガシーパスを通じて同期を継続します。

アカウント接続、オーディエンスの設定、同期の動作については、引き続きこのガイドに従ってください。

**カスタムオーディエンスの同期に関する一般的なユースケース：**
{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

{% alert note %}
この機能により、ブランドはGoogleと共有するファーストパーティデータを具体的にコントロールできます。Brazeでは、ファーストパーティデータを共有できる連携と共有できない連携について、最大限の配慮を行っています。詳しくは[Brazeデータプライバシーポリシー](https://www.braze.com/privacy)をご覧ください。
{% endalert %}

## 前提条件 {#prerequisites}

キャンバスで Google オーディエンスステップを設定する前に、以下の項目が作成・完了していることを確認してください。

| 要件 | Origin | 説明 |
| ----------- | ------ | ----------- |
| Google 広告アカウント | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | ブランドのアクティブな Google 広告アカウント。<br><br>複数の管理アカウント間でオーディエンスを共有する場合は、[管理者アカウント](https://support.google.com/google-ads/answer/6139186)にオーディエンスをアップロードできます。 |
| Google 広告の利用規約と Google 広告ポリシー | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | Braze Audience Sync の使用にあたり、[Google の広告利用規約](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40)と [Google の広告ポリシー](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC)（該当する場合は [EU ユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を含む）に同意し、遵守する必要があります。<br><br>EEA、英国、スイスのエンドユーザーに対して Google 広告のサービスを使用するために適切な同意を収集していることを確認するため、Google の新しい EU ユーザー同意ポリシーについて法務チームにご相談ください。 |
| Google カスタマーマッチ | [Google](https://support.google.com/google-ads/answer/6299717) | カスタマーマッチはすべての広告主が利用できるわけではありません。<br><br>**カスタマーマッチを使用するには、アカウントが以下の条件を満たしている必要があります：**<br>• ポリシー遵守の良好な実績<br>• 良好な支払い履歴<br>• Google 広告での90日以上の利用実績<br>• 累計50,000米ドル以上の支出。USD以外の通貨で管理されているアカウントの場合、支出額はその通貨の月間平均コンバージョンレートを使用してUSDに換算されます。<br><br>アカウントがこれらの条件を満たしていない場合、現在カスタマーマッチを使用する資格がありません。<br><br>アカウントのカスタマーマッチの利用可否について詳しくは、Google 広告の担当者にお問い合わせください。 |
| Google 同意シグナル | [Google](https://support.google.com/google-ads/answer/14310715) | Google のカスタマーマッチサービスを使用して EEA のエンドユーザーに広告を配信する場合、Google の EU ユーザー同意ポリシーの一環として、以下のカスタム属性（ブール値）を Braze に渡す必要があります。詳細は[EEA、英国、スイスのエンドユーザーの同意の収集](#collecting-consent-for-eea-uk-and-switzerland-end-users)をご覧ください。 <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

### 必要な SDK バージョン {#required-sdk-versions}

Braze SDKを使用して同意シグナルを収集する場合は、以下の最小バージョンを満たしていることを確認してください。

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### EEA、英国、スイスのエンドユーザーの同意の収集 {#collecting-consent-for-eea-uk-and-switzerland-end-users}

Google の EU ユーザー同意ポリシーでは、広告主が EEA、英国、スイスのエンドユーザーに対して以下を開示し、同意を得ることが求められています。

* 法的に必要な場合における Cookie またはその他のローカルストレージの使用
* 広告のパーソナライゼーションのための個人データの収集、共有、使用

これは米国のエンドユーザーや、EEA、英国、スイス以外に所在するその他のエンドユーザーには影響しません。EEA、英国、スイスのエンドユーザーに対して Google 広告のサービスを使用するために適切な同意を収集していることを確認するため、Google の新しい EU ユーザー同意ポリシーについて法務チームにご相談ください。

2024年3月6日に発効したデジタル市場法（DMA）の要件に基づき、広告主は Google とデータを共有する際に EEA、英国、スイスのエンドユーザーの同意を渡す必要があります。この変更の一環として、Braze で以下のブール型カスタム属性として両方の同意シグナルを収集できます。

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze はこれらのカスタム属性のデータを [Google の適切な同意フィールド](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A)に同期します。

#### 同意の撤回の管理 {#managing-revoked-consent}

EEA のエンドユーザーがオーディエンスリストに追加された後、2つの同意（`$google_ad_user_data` または `$google_ad_personalization`）のいずれかを撤回した場合にオーディエンスリストを最新の状態に保つには、Audience Sync ステップを使用して既存のオーディエンスリストからユーザーを削除するキャンバスを設定する必要があります。

{% alert note %}
EEA のユーザーが以前に両方のシグナルに同意していた場合、そのデータはリストの有効期限が切れるか、Google Audience Sync を通じて同意ステータスが明示的に更新されるか、またはその両方が行われるまで、Google のカスタマーマッチに引き続き使用されます。
{% endalert %}

#### ヒント {#tips}

* 値は文字列型ではなく、ブール型として送信してください。
* 属性名にはドル記号（$）をプレフィックスとして付けてください。Braze は属性名の先頭にドル記号を使用して、特別な予約キーであることを示します。
* 属性名は小文字で入力してください。
* ユーザーを明示的に「未指定」に設定することはできませんが、`null` または `nil` の値、あるいは `true` でも `false` でもない値を送信した場合、Braze はそのユーザーを `UNSPECIFIED` として Google に渡します。
* いずれの同意属性も指定せずに追加または更新された新しいユーザーは、それらの同意属性が未指定としてマークされた状態で Google に同期されます。

必要な同意フィールドと付与ステータスなしに EEA ユーザーを同期しようとすると、Google はこれを拒否し、そのユーザーに広告を配信しません。さらに、明示的な同意なしに EEA ユーザーに広告が配信された場合、責任を問われ、財務的なリスクが生じる可能性があります。これを避けるため、`true` の Google 同意属性を持つ EEA、英国、スイスのユーザーのみを含むセグメントフィルターを使用してキャンペーンを送信することをお勧めします。カスタマーマッチアップロードパートナー向けの EU ユーザー同意ポリシーの詳細については、Google の [FAQ](https://support.google.com/google-ads/answer/14310715) をご覧ください。

### キャンバスの設定 {#setting-up-your-canvas}

Braze に同期した後、以下の同意属性がユーザープロファイルで利用可能になり、セグメンテーションに使用できます。

- `$google_ad_user_data`
- `$google_ad_personalization`

Google Audience Sync を使用してオーディエンスにユーザーを追加し、EEA、英国、スイスのエンドユーザーをターゲットにするキャンバスでは、両方の同意属性が `true` 以外の値である場合、これらのユーザーを除外する必要があります。同意値が `true` に設定されているユーザーをセグメント化することでこれを実現できます。これにより、Google がこれらのユーザーをオーディエンスから拒否することがわかっているため、同期されるユーザーのより正確な分析も確保されます。Google Audience Sync を使用してオーディエンスからユーザーを削除する場合、同意属性は必要ありません。

## 連携 {#integration}

### ステップ1：Google アカウントを接続する {#step-1-connect-google-account}

{% alert important %}
Google 広告をBrazeアカウントに接続するには、[「管理者」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)が必要です。
{% endalert %}

開始するには、**パートナー連携** > **テクノロジーパートナー** > **Google Ads** に移動し、**Connect Google Ads** を選択します。Google 広告アカウントに関連付けられたメールアドレスを選択し、BrazeにGoogle 広告アカウントへのアクセスを許可するよう求めるモーダルが表示されます。

Google 広告アカウントの接続に成功すると、Google 広告パートナーページに戻ります。次に、Brazeワークスペースでアクセスする広告アカウントを選択するよう求められます。

![Google 広告アカウントをBrazeに正常に接続するワークフローを示すGIF。]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### iOS IDFAまたはGoogle広告IDをエクスポートする {#export-ios-idfa-or-google-advertising-ids}

オーディエンス同期でiOS IDFAまたはGoogle広告IDをエクスポートする予定がある場合、Googleはリクエスト内にiOSアプリIDとAndroidアプリIDを必要とします。Google オーディエンス同期の下で、**Add Mobile Advertising IDs** を選択し、iOSアプリIDとAndroidアプリID（アプリパッケージ名）を入力して、それぞれ保存します。

<br><br>
![接続された広告アカウントを表示する更新されたGoogle 広告テクノロジーページ。アカウントの再同期やモバイル広告IDの追加が可能です。]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

1つのワークスペースに複数のアプリがある場合、セットアップ時にいずれかのアプリIDを入力できます。ユーザーのモバイル広告IDは複数のアプリ間で同じであるためです。これは、Android GAIDとiOS IDFAの両方がデバイス上のユニバーサル広告識別子であり、アプリ固有ではないためです。特定のアプリのユーザーのモバイル広告IDを同期するには、セグメントフィルター（「最後に使用した特定のアプリ」または「最新のアプリバージョン」）を使用してこれらのユーザーをターゲットにできます。

### ステップ2：キャンバスにGoogle オーディエンスステップを追加する {#step-2-add-a-google-audience-step-in-canvas}

キャンバスにコンポーネントを追加し、**Audience Sync** を選択します。

![エディターでキャンバスコンポーネントを選択するメニュー。]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![ユーザージャーニーに追加されたAudience Syncステップ。]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### ステップ3：同期の設定 {#step-3-sync-setup}

1. **Custom Audience** を選択してコンポーネントエディターを開きます。
2. Audience Syncパートナーとして **Google** を選択します。

![同期を開始するパートナーを選択するオプションがあるAudience Syncステップの設定。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3. 目的のGoogle広告アカウントを選択します。
4. **Choose a New or Existing Audience** ドロップダウンで、新規または既存のオーディエンスの名前を入力します。

{% tabs %}
{% tab 新しいオーディエンスを作成する %}

1. 新しいカスタムオーディエンスの名前を入力します。
2. **Add Users to Audience** を選択します。
3. オーディエンスに送信するファーストパーティユーザーフィールドデータを選択します。以下のいずれかを選択できます：

- **Customer Contact Info**：ユーザーのメールアドレスまたは電話番号、あるいはその両方（Brazeに存在する場合）が含まれます。Googleでは、個別の識別子ではなく、単一のフィールドとして同期する必要があります。識別子が1つしかない場合でも、この単一フィールドを使用できます。
- **Mobile Advertiser ID**：iOS IDFAまたはAndroid GAIDのいずれかを選択します。GoogleのCustomer Match要件により、同じ顧客リストに両方のモバイル広告IDを含めることはできません。

{% alert note %}
**「Missing Mobile Ad IDs? Let's fix that.」バナーについて：** iOS IDFAまたはAndroid GAIDをマッチングフィールドとしてオーディエンスに同期する場合、このメッセージがステップエディターに表示されることがあります。これは**情報メッセージであり、エラーではありません**。マッチングに使用するモバイル広告IDフィールドがオーディエンスデータに存在すること（例えば、キャンバスパス内のユーザーが対応する識別子を収集済みであること）を確認するよう促すものです。データを確認した後、このメッセージを閉じることができます。
{% endalert %}

{: start="4"}
4. 次に、ステップエディターの下部にある **Create Audience** ボタンを選択してオーディエンスを保存します。

![カスタムオーディエンスキャンバスコンポーネントの展開ビュー。目的の広告アカウントが選択され、新しいオーディエンスが作成され、「customer contact info」チェックボックスが選択されています。]({% image_buster /assets/img/audience_sync/g_sync.png %})

オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合、ステップエディターの上部にユーザーに通知されます。オーディエンスは下書きモードで作成されたため、キャンバスジャーニーの後半でユーザー削除のためにこのオーディエンスを参照できます。

![キャンバスコンポーネントで新しいオーディエンスが作成された後に表示されるアラート。]({% image_buster /assets/img/audience_sync/g_sync3.png %})

新しいオーディエンスを含むキャンバスを起動すると、Brazeはキャンバスの起動時に新しいカスタムオーディエンスを作成し、ユーザーがGoogle オーディエンスステップに入るとほぼリアルタイムで同期します。

{% alert important %}
GoogleのCustomer Match要件により、同じ顧客リストに顧客連絡先情報とモバイル広告IDを含めることはできません。Google Customer Matchはこの情報を使用して、Google検索、Googleディスプレイ、YouTube、Gmail内でターゲット可能なユーザーを判断します。GoogleのCustomer Match要件の詳細については、Googleの[ドキュメント](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507)を参照してください。
{% endalert %}
{% endtab %}
{% tab 既存のオーディエンスと同期する %}

Brazeでは、既存のGoogle顧客リストにユーザーを追加または削除して、これらのオーディエンスを最新の状態に保つこともできます。既存のオーディエンスと同期するには：

1. 同期する既存のカスタムオーディエンスを選択します。
2. **Add to the audience** または **Remove from the audience** のいずれかを選択します。
3. ユーザーがGoogle オーディエンスステップに入ると、Brazeはほぼリアルタイムでユーザーを追加または削除します。
4. Google オーディエンスステップの設定が完了したら、**Done** を選択します。Google オーディエンスステップに新しいオーディエンスの詳細が表示されます。

![カスタムオーディエンスキャンバスコンポーネントの展開ビュー。目的の広告アカウントと既存のオーディエンスが選択され、「Add user to Audience」ラジオボタンが選択されています。]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### ステップ4：キャンバスを起動する {#step-4-launch-canvas}

キャンバス内のユーザージャーニーの残りの部分を完成させてから起動します。新しいオーディエンスの作成を選択した場合、BrazeはGoogle内にオーディエンスを作成し、ユーザーがキャンバスのこのステップに到達するとユーザーを追加します。既存のオーディエンスへのユーザーの追加または削除を選択した場合、Brazeはユーザーがユーザージャーニーのこのステップに到達した時点でユーザーを追加または削除します。

その後、ユーザーはキャンバスの次のコンポーネントに進むか（次のコンポーネントがある場合）、ユーザージャーニーの最後のステップである場合はキャンバスを終了します。

## ユーザー同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期コンポーネントに到達すると、BrazeはGoogle 広告APIのレート制限を遵守しながら、ほぼリアルタイムでこれらのユーザーを同期します。具体的には、Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理し、Googleに送信しようとします。

顧客がGoogle 広告APIのレート制限に近づくと、Googleはリトライの推奨事項に関するフィードバックをBrazeに提供します。Brazeの顧客がレート制限に達した場合、Brazeのキャンバスは最大約13時間にわたって同期をリトライします。同期ができない場合、これらのユーザーはUsers Erroredメトリクスに表示されます。

## 分析の理解 {#understanding-analytics}

次の表には、Audience Sync ステップの分析をより深く理解するための指標と説明が含まれています。

| 指標 | 説明 |
| ------ | ----------- |
| *入場済み* | Google に同期するためにこのステップに入ったユーザーの数です。 |
| *次のステップに進んだ* | 次のコンポーネントがある場合、そこに進んだユーザーの数です。すべてのユーザーは自動的に進みます。これがキャンバスブランチの最後のステップである場合、この指標は 0 になります。 |
| *同期済みユーザー* | Google に正常に同期されたユーザーの数です。 |
| *未同期ユーザー* | マッチするフィールドが不足しているか、同意属性が `false` に設定されているために同期されなかったユーザーの数です。 |
| *エラーユーザー* | &#126;13 時間のリトライ後、エラーにより Google に同期されなかったユーザーの数です。Google 広告 API サービスの中断などの特定のエラーについては、キャンバスは最大 &#126;13 時間同期をリトライします。その時点でも同期ができない場合、*未同期ユーザー* に計上されます。 |
| *保留中のユーザー* | 現在 Braze が Google への同期を処理中のユーザーの数です。 |
| *キャンバスを退出* | キャンバスを退出したユーザーの数です。これは、キャンバスの最後のステップが Google ステップである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析の理解" }

## よくある質問 {#frequently-asked-questions}

### Google オーディエンスステップの設定で、マッチングに複数のフィールドを選択できないのはなぜですか？ {#why-can-i-not-select-multiple-fields-to-match-in-my-google-audience-step-configuration}

Google カスタマーマッチには、オーディエンスのフォーマット方法や含める顧客情報に関する厳格な要件があります。具体的には、モバイル広告主IDは顧客の連絡先情報（メールアドレスや電話番号など）とは別にアップロードする必要があります。詳細については、[Google のカスタマーマッチに関するドキュメント](https://support.google.com/google-ads/answer/7659867?hl=en#undefined)を参照してください。

### Google でオーディエンスが同期されるまでどのくらいかかりますか？ {#how-long-will-it-take-for-my-audiences-to-sync-in-google}

Google へのオーディエンスの同期には6〜12時間かかる場合があります。

### オーディエンスを同期しましたが、Google でオーディエンスサイズがゼロと表示されるのはなぜですか？ {#ive-synced-an-audience-so-why-is-the-audience-size-in-google-zero}

プライバシー保護の目的で、ユーザーリストのサイズはリストのメンバーが1,000人以上になるまでゼロと表示されます。その後、サイズは上位2桁に丸められて表示されます。

### Google でマッチしたオーディエンスサイズが、Brazeから同期したユーザー数より少ないのはなぜですか？ {#why-is-my-matched-audience-size-in-google-lower-than-the-number-of-users-synced-from-braze}

Brazeが一定数のユーザーを Google に同期しても、Google 広告で表示される実際のマッチしたオーディエンスサイズは大幅に少なくなる場合があります。これは、Google が提供されたユーザーデータ（メールアドレスや電話番号など）を、プラットフォーム上の実際の Google アカウントとマッチングする必要があるためです。

Brazeのユーザープロファイルに有効なマッチングフィールドが含まれていても、ユーザーが Google カスタムオーディエンスに表示されるのは、一致する情報を持つ Google アカウントがある場合のみです。

マッチ率を向上させるには：
- [データが正しくフォーマットされている](https://support.google.com/google-ads/answer/7659867)ことを確認してください。
- 可能な場合は複数の識別子を提供してください（例：メールアドレスと電話番号の両方）。
- Google がユーザーを処理してマッチングするまでに48〜72時間かかる場合がありますが、数日かかることもあります。

最終的なマッチしたオーディエンスサイズは、完全に Google のマッチングプロセスに依存します。データが Google のプラットフォームに渡された後のマッチング結果について、Brazeは把握できません。

### Google にオーディエンスを同期しましたが、広告が配信されません。 {#ive-synced-an-audience-into-google-but-my-ads-are-not-serving}

広告の配信を開始するには、オーディエンスに少なくとも5,000人のユーザーが含まれていることを確認してください。

### 「Mobile App IDs Deleted」エラーを解決するにはどうすればよいですか？ {#how-do-i-resolve-the-mobile-app-ids-deleted-error}

Google にオーディエンスを同期している場合、同期の一部としてモバイル識別子の同期を選択しているにもかかわらず、Google パートナーページからモバイルアプリIDを削除した場合にこのエラーが発生します。この問題を解決するには、iOS および Android の適切なモバイルアプリIDが Google パートナーページに追加されていることを確認してください。

### ダッシュボードではまだ接続済みと表示されているのに、Google 広告の無効な認証情報メールが届いたのはなぜですか？ {#why-did-i-get-a-google-ads-invalid-credentials-email-when-the-dashboard-still-shows-connected}

Brazeは、Google の API が認証エラーを返した場合にこのメールを自動的に送信します。これは、ダッシュボードで **Google 広告**がまだ接続済みと表示され、オーディエンスが同期されているように見える場合でも発生する可能性があります。例えば、接続された Google アカウントに Google がリクエストした特定のアクションに対する権限がない場合や、アカウントの Google 広告利用規約にまだ同意していない場合などです。

一部の認証エラーは自動的に解消されます。キャンバスの **Audience Sync** 分析（例：*Users Synced* や *Users Errored*）を確認して、ユーザーがまだ同期されているかどうかを確認してください。問題が続く場合は、**パートナー連携** > **テクノロジーパートナー** > **Google 広告**に移動し、**Google Audience Sync** を見つけて、**Change Account** を使用して、必要なアクセス権と設定が完了した Google 広告アカウントで再接続してください。
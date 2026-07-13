## Google Playプライバシーアンケート {#privacy-questionnaire}

2022年4月から、Android開発者はGoogle Playの[データ安全フォーム](https://support.google.com/googleplay/android-developer/answer/10787469)に記入し、プライバシーとセキュリティの慣行を開示する必要があります。このガイドでは、Brazeによるアプリデータの処理方法に関する情報をこの新しいフォームに記入する方法について説明します。

アプリ開発者は、どのデータをBrazeに送信するかを制御しています。Brazeが受け取ったデータは、指示に従って処理されます。これは、Googleが[サービスプロバイダー](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform)として分類したものです。

{% alert important %}
この記事では、Googleのセーフティセクションのアンケートについて、Braze SDKにより処理されるデータに関連する情報を提供します。この記事は法律上のアドバイスを提供するものではないため、Googleに情報を提出する前に法務チームに相談することをお勧めします。
{% endalert %}

### 質問 {#questions}

| 質問 | Braze SDKの回答 |
|---|---|
| お使いのアプリは、必要なユーザーデータの種類を収集または共有しますか？ | はい、Braze Android SDKはアプリ開発者によって設定されたデータを収集します。 |
| あなたのアプリが収集するすべてのユーザーデータは転送中に暗号化されていますか？ | はい。 |
| ユーザーがデータの削除を要求する方法を提供していますか？ | はい。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Questions" }

データおよび削除に対するユーザーリクエストの処理の詳細については、[Brazeデータリテンション情報]({{site.baseurl}}/api/data_retention/)を参照してください。

### データ収集 {#data-collection}

Brazeによって収集されるデータは、特定の統合と収集するユーザーデータによって決まります。デフォルトで収集されるデータの詳細、および特定の属性を無効にする方法については、[SDKデータ収集オプション]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration)を参照してください。

<table aria-label="Data collection" id="datatypes">
    <thead>
        <tr>
            <th width="25%">カテゴリー</th>
            <th width="25%">データタイプ</th>
            <th width="50%">Brazeの使用状況</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">ロケーション</td>
            <td>おおよその位置情報</td>
            <td rowspan="15">デフォルトでは収集されません。</td>
        </tr>
        <tr>
            <td>正確な位置情報</td>
        </tr>
        <tr>
            <td rowspan="9">個人情報</td>
            <td>名前</td>
        </tr>
        <tr>
            <td>メールアドレス</td>
        </tr>
        <tr>
            <td>ユーザー ID</td>
        </tr>
        <tr>
            <td>住所</td>
        </tr>
        <tr>
            <td>電話番号</td>
        </tr>
        <tr>
            <td>人種と民族</td>
        </tr>
        <tr>
            <td>政治的または宗教的信条</td>
        </tr>
        <tr>
            <td>性的指向</td>
        </tr>
        <tr>
            <td>その他の情報</td>
        </tr>
        <tr>
            <td rowspan="4">財務情報</td>
            <td>ユーザー決済情報</td>
        </tr>
        <tr>
            <td>購入履歴</td>
        </tr>
        <tr>
            <td>クレジットスコア</td>
        </tr>
        <tr>
            <td>その他の財務情報</td>
        </tr>
        <tr>
            <td rowspan="2">ヘルスとフィットネス</td>
            <td>ヘルス情報</td>
            <td rowspan="2">デフォルトでは収集されません。</td>
        </tr>
        <tr>
            <td>フィットネス情報</td>
        </tr>
        <tr>
            <td rowspan="3">メッセージ</td>
            <td>メール</td>
            <td rowspan="2">デフォルトでは収集されません。</td>
        </tr>
        <tr>
            <td>SMSまたはMMS</td>
        </tr>
        <tr>
            <td>その他のアプリ内メッセージ</td>
            <td>Brazeを通じてアプリ内メッセージやプッシュ通知を送信する場合、ユーザーがこれらのメッセージをいつ開封したか、またはいつ読んだかに関する情報を収集します。</td>
        </tr>
        <tr>
            <td rowspan="2">写真と動画</td>
            <td>写真</td>
            <td rowspan="8">収集されません。</td>
        </tr>
        <tr>
            <td>動画</td>
        </tr>
        <tr>
            <td rowspan="3">オーディオファイル</td>
            <td>音声やサウンドの録音</td>
        </tr>
        <tr>
            <td>音楽ファイル</td>
        </tr>
        <tr>
            <td>その他のオーディオファイル</td>
        </tr>
        <tr>
            <td>ファイルとドキュメント</td>
            <td>ファイルとドキュメント</td>
        </tr>
        <tr>
            <td>カレンダー</td>
            <td>カレンダーイベント</td>
        </tr>
        <tr>
            <td>連絡先</td>
            <td>連絡先</td>
        </tr>
        <tr>
            <td rowspan="5">アプリアクティビティ</td>
            <td>アプリのインタラクション</td>
            <td>Brazeは、デフォルトでセッションアクティビティデータを収集します。その他すべてのインタラクションとアクティビティは、アプリのカスタム統合によって決定されます。</td>
        </tr>
        <tr>
            <td>アプリ内検索履歴</td>
            <td>収集されません。</td>
        </tr>
        <tr>
            <td>インストール済みアプリ</td>
            <td>収集されません。</td>
        </tr>
        <tr>
            <td>その他のユーザー生成コンテンツ</td>
            <td rowspan="2">デフォルトでは収集されません。</td>
        </tr>
        <tr>
            <td>その他のアクション</td>
        </tr>
        <tr>
            <td>Webブラウジング</td>
            <td>Web閲覧履歴</td>
            <td>収集されません。</td>
        </tr>
        <tr>
            <td rowspan="3">アプリの情報とパフォーマンス</td>
            <td>クラッシュログ</td>
            <td>Brazeは、SDK内で発生したエラーのクラッシュログを収集します。これには、ユーザーの電話機モデルとOSレベル、およびBraze固有のユーザーIDが含まれます。</td>
        </tr>
        <tr>
            <td>診断</td>
            <td>収集されません。</td>
        </tr>
        <tr>
            <td>その他のアプリパフォーマンスデータ</td>
            <td>収集されません。</td>
        </tr>
        <tr>
            <td>デバイスまたはその他のID</td>
            <td>デバイスまたはその他のID</td>
            <td>Brazeは、ユーザーのデバイスを区別するためにデバイスIDを生成し、メッセージが意図した正しいデバイスに送信されるかどうかをチェックします。</td>
        </tr>
    </tbody>
</table>

Google Playのデータセーフティガイドラインの対象外となる可能性がある、Brazeが収集するその他のデバイスデータの詳細については、[Androidストレージの概要]({{site.baseurl}}/developer_guide/storage/?tab=android)および[SDKデータ収集オプション]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration)を参照してください。

## トラッキングを無効にする {#disabling-data-tracking}

Android SDKのデータトラッキングアクティビティを無効にするには、[`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html)メソッドを使用します。これにより、すべてのネットワーク接続がキャンセルされ、Braze SDKはBrazeサーバーにデータを渡さなくなります。

## 過去に保存したデータを消去する {#wiping-previously-stored-data}

[`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html)メソッドを使用すると、デバイスに保存されているクライアント側のデータをすべて消去できます。

## データトラッキングを再開する {#resuming-data-tracking}

データ収集を再開するには、[`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html)メソッドを使用します。これは、以前に消去したデータを復元するものではないことに留意してください。
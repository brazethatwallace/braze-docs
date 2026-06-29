---
nav_title: Brazeサポート
article_title: Brazeサポート
page_order: 4
description: "このページでは、Brazeサポートポータルにアクセスして、Braze製品のフィードバックを送信する方法をご案内します。このページはBrazeのお客様のみがアクセスできます。"
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Brazeサポート {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomthe-braze-support-portal-stylefloatrightwidth120pxborder0-classnoimgborderbraze-support}

> Brazeサポートポータルへのアクセス方法、サポートケースの送信と追跡方法、効率的なトラブルシューティングに必要な情報の提供方法について説明します。

## サポートポータルへのアクセス {#access-the-support-portal}

Brazeサポートチームに連絡するには、Brazeダッシュボードに移動し、**Support**を選択します。メニューには2つのオプションがあります。

- **Get help with Operator**を選択すると、BrazeAI Operator<sup>TM</sup>が開きます。会話の内容と現在の画面のコンテキストを使用して、その場で問題をトラブルシューティングできます。Operatorが問題を解決できない場合は、会話に基づいてサポートチケットの下書きを作成するよう依頼できます。詳細については、[BrazeAI Operatorでサポートチケットを提出する]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets)を参照してください。
- **Get help**を選択すると、Brazeサポートポータル（指定サポート連絡先の場合）または標準のサポートフォームに直接移動し、ケースの送信と追跡ができます。Brazeサポート連絡先かどうか不明な場合は、会社のBraze管理者、Brazeサクセスマネージャー、またはアカウントオーナーにお問い合わせください。

![「Get help with Operator」と「Get help」のオプションが表示された「Support」ドロップダウン。]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:50%;"}


## 指定サポート連絡先の追加 {#adding-designated-support-contacts}

指定サポート連絡先は、誰が送信したかに関係なく、会社のすべてのサポートケースにアクセスできます。**Edit user**ページから直接、ユーザーを指定サポート連絡先として設定できます。

1. **Settings** > **Company Users**に移動し、名前またはメールアドレスでユーザーを検索します。
2. ユーザー名を選択するか、ユーザー名の行にカーソルを合わせてメニューを表示します。
3. メニューで**Edit**を選択すると、**Edit user**ページにリダイレクトされます。
4. **Set this user as a Designated Support Contact for Braze Support Portal**のチェックボックスをオンにします。

### アクセスの取得 {#gaining-access}

ユーザーがサポート連絡先として指定されると、Brazeサポートポータルからそのユーザーにウェルカムメールが送信され、アクセスの設定手順が記載されています。

## 会社のケースを表示する {#view-cases-from-your-company}

指定サポート連絡先の場合、サポートポータルの**My Org's**フィルタービューを使用して、会社のユーザーが送信したすべてのケースを表示できます。すべての送信チャネル（BrazeAI Operator<sup>TM</sup>、Webフォーム、メール、またはポータル）からのケースがこれらのビューに含まれます。

## 開発者コンソールのスクリーンショットを提供する {#provide-developer-console-screenshots}

サポートとのやり取りの際に、追加情報を提供するために開発者コンソールにアクセスする必要がある場合があります。
- Chrome
  1. Webページを右クリックし、**Inspect**を選択します。
  2. 開いたウィンドウで**Console**タブを選択します。
  3. Consoleタブのスクリーンショットを撮ります。<br><br>
- Firefox
  1. Webページを右クリックし、**Inspect Element**を選択します。
  2. 開いたウィンドウで**Console**タブを選択します。
  3. Consoleタブのスクリーンショットを撮ります。<br><br>
- Safari
  1. 画面上部のメニューバーでSafariに移動し、**Preferences**を選択します。
  2. **Advanced**を選択し、**Show Develop menu in menu bar**の横にあるチェックボックスをオンにします。その後、ウィンドウを閉じることができます。
  3. Webページを右クリックし、**Inspect Element**を選択します。
  4. 開いたウィンドウで**Console**タブを選択します。
  5. Consoleタブのスクリーンショットを撮ります。

## サポートケース送信のベストプラクティス {#best-practices-for-submitting-a-support-case}

### できるだけ多くの情報を提供する {#provide-as-much-information-as-possible}

提供できるインサイトが多いほど、より効果的に対応できます。ワークスペース、CampaignやSegmentのURL、関連するexternal IDなどの具体的な情報を含めてください。これにより、問題をより効率的にトラブルシューティングできます。

### ユーザーのサンプルを提供する {#provide-a-sample-of-users}

影響を受けたSegment全体ではなく、ユーザーのサンプルを共有してください。少数のユーザーを提供することで、調査範囲を絞り込み、調査を迅速化できます。

### ネットワークログ（HARログ）を添付する {#attach-network-logs-har-logs}

サポートに連絡する場合、問題が発生している間に影響を受けたユーザーがブラウザからネットワークログ（HARログ）を収集しておくと役立ちます。これにより、Webページの個々のコンポーネントに対するブラウザとサーバー間のネットワークリクエスト、およびユーザーが開こうとしているBrazeダッシュボードが表示されます。

影響を受けたユーザーに以下の操作を行ってもらいます。

1. 開発者ツールを開きます。Chromeを使用している場合、キーボードショートカット`option` + `⌘` + `J`（macOSの場合）で開くことができます。WindowsまたはLinuxを使用している場合、ショートカット`shift` + `CTRL` + `J`で開くことができます。
2. **Network** > **Fetch/XHR**または**XHR**を選択します。
3. 要素の**Name**、**Status**、**Size**、**Time**が表示された画面録画またはスクリーンショットをキャプチャします。<br><br>![Chromeブラウザの「Fetch/XHR」タブ。]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

その後、ユーザーの録画またはスクリーンショットをサポートチケットに添付します。この情報はサポートの調査に役立ちます。

### 期待される動作と実際の動作を明確にする {#clarify-expected-versus-actual-behavior}

何を期待していたか、実際に何が起こったかをお知らせください。これにより、問題の原因を絞り込むことができます。

### 関連する画像を添付する {#attach-relevant-images}

問題を説明するスクリーンショットの添付を検討してください。これらの画像を提供することで、問題の理解が大幅に促進され、解決プロセスが迅速化されます。

### 影響度を評価する {#assess-the-impact}

適切な重大度レベルを選択して、問題に対処するための適切なリソースを割り当てられるようにしてください。

{% alert important %}
問題を「クリティカル」としてマークすると、本番インスタンスがダウンしており、Braze内のすべての作業が停止していることを意味します。
{% endalert %}

## ダッシュボードの読み込みに関するトラブルシューティング {#troubleshooting-dashboard-load-issues}

Brazeダッシュボードが正しく読み込まれない場合は、サポートに連絡する前に以下をお試しください。

1. 別のブラウザ、またはシークレットウィンドウやプライベートウィンドウでダッシュボードを開きます。
2. [ブラウザのキャッシュとCookieをクリアします]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#clearing-your-browser-cache-and-cookies)。
3. 広告ブロッカーとブラウザ拡張機能を無効にしてから、ダッシュボードを再読み込みします。
4. VPNを使用している場合は、切断してから再度お試しください。

ブラウザの開発者コンソールに`ERR_BLOCKED_BY_CLIENT`と表示される場合は、拡張機能または広告ブロッカーがダッシュボードのリソースをブロックしています。BrazeダッシュボードのURLに対してブロッカーを無効にし、ページを再読み込みしてください。

## アクセスのトラブルシューティング {#troubleshooting-access}

Brazeサポートポータルへのログイン時に`Check your entry`などのエラーが表示された場合は、ウェルカムメールのリンクに従ってポータルのパスワードを設定したことを確認してください。すでに設定済みの場合、または以前ポータルにログインできていた場合は、サポートチケットを作成してください。
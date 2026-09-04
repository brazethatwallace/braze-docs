---
nav_title: Brazeサポート
article_title: Brazeサポート
page_order: 4
description: "このページでは、Brazeサポートポータルにアクセスして、Braze製品のフィードバックを送信する方法をご案内します。このページはBrazeのお客様のみがアクセスできます。"
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Brazeサポート {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomthe-braze-support-portal-stylefloatrightwidth120pxborder0-classnoimgborderbraze-support}

> Brazeサポートポータルへのアクセス方法、サポートケースの送信と追跡方法、効率的なトラブルシューティングに必要な情報の提供方法について説明します。

## サポートポータルへのアクセス {#access-the-support-portal}

Brazeサポートチームに連絡するには、**サポート** > **Get help with Operator** を選択してBrazeAI Operator<sup>TM</sup>を開きます。

Operatorは、会話の内容と現在の画面のコンテキストを使用して問題のトラブルシューティングを行うことができます。Operatorで問題を解決できない場合は、会話に基づいてサポートチケットの下書きを作成するよう依頼し、Brazeサポートポータルでチケットを送信してください（指定されたサポート連絡先である場合）。また、Operator内で<i class="fa-regular fa-circle-question" aria-label="サポートに問い合わせる"></i> **Contact Support** を選択して、直接チケットを提出することもできます。ダッシュボードで **Get help with Operator** が利用できない場合は、**サポート** > **Get help** を選択してサポートポータルまたはサポートフォームを開いてください。

詳細については、[BrazeAI Operatorでサポートチケットを提出する]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets)を参照してください。自分がBrazeサポート連絡先かどうか不明な場合は、所属企業のBraze管理者、Brazeサクセスマネージャー、またはアカウントオーナーにお問い合わせください。

![「サポート」ドロップダウンに「Get help with Operator」が表示されている画面]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:50%;"}

## 指定サポート連絡先の追加 {#adding-designated-support-contacts}

指定サポート連絡先は、誰が送信したかに関係なく、会社のすべてのサポートケースにアクセスできます。**ユーザーを編集**ページから直接、ユーザーを指定サポート連絡先として設定できます。

1. **設定** > **会社のユーザー**に移動し、名前またはメールアドレスでユーザーを検索します。
2. ユーザー名を選択するか、ユーザー名の行にカーソルを合わせてメニューを表示します。
3. メニューで**編集**を選択すると、**ユーザーを編集**ページにリダイレクトされます。
4. **Set this user as a Designated Support Contact for Braze Support Portal**のチェックボックスをオンにします。

### アクセスの取得 {#gaining-access}

ユーザーがサポート連絡先として指定されると、Brazeサポートポータルからそのユーザーにウェルカムメールが送信され、アクセスの設定手順が案内されます。

## 自社のケースを表示する {#view-cases-from-your-company}

指定されたサポート連絡先の場合は、サポートポータルの **My Org's** フィルタービューを使用して、自社のユーザーが送信したすべてのケースを表示できます。すべての送信チャネル（BrazeAI Operator<sup>TM</sup>、Webフォーム、メール、またはポータル）からのケースがこれらのビューに含まれています。

## サポートケース送信のベストプラクティス {#best-practices-for-submitting-a-support-case}

### できるだけ多くの情報を提供する {#provide-as-much-information-as-possible}

提供できるインサイトが多いほど、対応がスムーズになります。ワークスペース、キャンペーンやセグメントのURL、関連するexternal IDなどの具体的な情報を含めてください。これにより、問題のトラブルシューティングをより効率的に行うことができます。

### ユーザーのサンプルを提供する {#provide-a-sample-of-users}

影響を受けたセグメント全体ではなく、ユーザーのサンプルを共有してください。少数のユーザーを提供していただくことで、調査範囲を絞り込み、調査を迅速に進めることができます。

### 期待される動作と実際の動作を明確にする {#clarify-expected-versus-actual-behavior}

期待していた動作と実際に起こった動作をお知らせください。これにより、問題の原因を絞り込むことができます。

### 関連する画像を添付する {#attach-relevant-images}

問題を説明するスクリーンショットの添付をご検討ください。これらの画像を提供していただくことで、問題の理解が大幅に促進され、解決プロセスが迅速化されます。

### 影響度を評価する {#assess-the-impact}

適切な重大度レベルを選択して、問題に対処するための適切なリソースを割り当てられるようにしてください。

{% alert important %}
問題を「Critical」としてマークすることは、本番環境がダウンしており、Braze内のすべての作業が停止していることを意味します。
{% endalert %}

## ダッシュボードの読み込みに関するトラブルシューティング {#troubleshooting-dashboard-load-issues}

Brazeダッシュボードが正しく読み込まれない場合は、サポートに連絡する前に以下をお試しください。

1. 別のブラウザ、またはシークレットウィンドウやプライベートウィンドウでダッシュボードを開きます。
2. [ブラウザのキャッシュとCookieをクリアします]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#clearing-your-browser-cache-and-cookies)。
3. 広告ブロッカーとブラウザ拡張機能を無効にしてから、ダッシュボードを再読み込みします。
4. VPNを使用している場合は、切断してから再度お試しください。

ブラウザの開発者コンソールに `ERR_BLOCKED_BY_CLIENT` と表示される場合は、拡張機能または広告ブロッカーがダッシュボードのリソースをブロックしています。BrazeダッシュボードのURLに対してブロッカーを無効にし、ページを再読み込みしてください。

## アクセスのトラブルシューティング {#troubleshooting-access}

Braze サポートポータルにログインする際に `Check your entry` などのエラーが表示された場合は、ウェルカムメールのリンクからポータルのパスワードを設定したことを確認してください。すでにパスワードを設定済みの場合、または以前ポータルにログインできていた場合は、サポートチケットを作成してください。
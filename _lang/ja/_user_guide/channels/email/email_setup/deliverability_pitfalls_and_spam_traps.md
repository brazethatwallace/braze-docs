---
nav_title: 配信の落とし穴とスパムの罠
article_title: 配信の落とし穴とスパムの罠
page_order: 7
page_type: reference
description: "この参考記事では、潜在的なメール配信の落とし穴、スパムの罠、そしてそれらを回避する方法について取り上げています。"
channel: email

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}配信の落とし穴とスパムの罠 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomemail-onboarding-for-pro-and-enterprise-achieving-high-deliverability-stylefloatrightwidth120pxborder0-classnoimgborderdeliverability-pitfalls-and-spam-traps}

> この記事では、一般的なメール配信の落とし穴、スパムの罠、そしてそれらを回避する方法について取り上げています。

以下のスパムトラップは、メール配信に影響を与える可能性があります。

| トラップタイプ | 説明 |
|---|---|
| プリスティントラップ | 一度も使用されたことのないメールアドレスとドメイン。 |
| リサイクルトラップ | 元々は実在のユーザーであったが、現在は休止状態のメールアドレス。 |
| タイポトラップ | よくあるタイプミスを含むメールアドレス。 |
| スパムの苦情 | メールが消費者によってスパムとしてマークされた場合。 |
| 高いバウンス率 | 受信者のアドレスが無効であるために、メールが常に配信できない場合。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="配信の落とし穴とスパムの罠" }

## スパムの罠を回避する方法 {#how-to-avoid-spam-traps}

このような罠は、確認オプトインプロセスを設定すれば回避できます。最初のオプトインメールを送信し、メッセージを希望するかどうかをサブスクライバーに確認することで、受信者があなたからの連絡を求めていること、そして実在する有効なアドレスに送信していることを確認できます。スパムの罠を回避するその他の方法を紹介します。

1. ダブルオプトインメールを送信します。これは、ユーザーがリンクをクリックしてサブスクリプションの選択を確認することを要求するメールです。
2. ベストプラクティスとして、[サンセットポリシー]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/)を導入します。
3. **メールリストは決して購入しないでください。**

{% alert tip %}
Brazeのカスタマーサクセスチームとデリバビリティチームは、お客様がベストプラクティスに従って世界中でデリバビリティを最大化できるようにサポートします。
{% endalert %}

## Microsoftの無料メールドメインブロックを解決する方法 {#how-to-resolve-a-free-email-domain-block-for-microsoft}

Microsoftは、無料メールドメイン（Hotmail、Live、MSN、Outlook）への配信に問題がある送信者のブロックを解除することはほとんどありません。代わりに、これらのドメインへの送信量を大幅に減らし、最近エンゲージメントのあった連絡先にのみ送信してください。エンゲージメントのある受信者のコアグループを特定できない場合は、これらのドメインへの送信を完全に停止してください。

無料メールドメインブロックメッセージの例は以下のとおりです。

`550 5.7.1 Unfortunately, messages from [xx.xx.xx.xx] weren't sent. Please contact your Internet service provider since part of their network is on our block list (S3150). You can also refer your provider to: http://mail.live.com/mail/troubleshooting.aspx#errors.`

[IPウォーミング]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/)と同様に、指標に細心の注意を払いながら、徐々に送信量を増やすことができます。多くの場合、配信の問題には特定して解決すべき根本原因があります。一般的には、適切な許可の欠如、継続的なリスト衛生管理の欠如、またはそれらの組み合わせが原因です。

## バウンスリストやスパムリストからメールアドレスを削除する {#remove-an-email-address-from-your-bounce-or-spam-list}

バウンスメールやBrazeスパムリストのメールは、以下のエンドポイントで削除できます。

- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)

## メール配信性を向上させる {#improve-email-deliverability}

詳細については、[メール配信性を向上させる]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/)を参照してください。
---
nav_title: 到達性の落とし穴とスパムトラップ
article_title: 到達性の落とし穴とスパムトラップ
page_order: 7
page_type: reference
description: "このリファレンス記事では、メールの到達性に関する潜在的な落とし穴、スパムトラップ、およびそれらを回避する方法について説明します。"
channel: email

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"}到達性の落とし穴とスパムトラップ

メールの到達性は、以下のスパムトラップのいずれかによって影響を受ける可能性があります。

| トラップの種類 | 説明 |
|---|---|
| Pristine Traps | 一度も使用されたことのないメールアドレスやドメインです。 |
| Recycled Traps | もともと実際のユーザーが使用していたが、現在は休止状態のメールアドレスです。 |
| Typo Traps | よくあるタイプミスを含むメールアドレスです。 |
| スパム苦情 | 顧客によってメールがスパムとしてマークされた場合です。 |
| 高バウンス率 | 受信者のアドレスが無効であるため、メールの配信が継続的に失敗する場合です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## スパムトラップを回避する方法

これらのトラップは、確認済みオプトインプロセスを設定することで回避できます。最初のオプトインメールを送信し、顧客にメッセージの受信を希望するかどうかを確認してもらうことで、受信者があなたからの連絡を望んでいること、そして実在する有効なアドレスに送信していることを確認できます。スパムトラップを回避するための追加の方法を以下に示します。

1. ダブルオプトインメールを送信します。これは、ユーザーがリンクをクリックしてサブスクリプションの選択を確認する必要があるメールです。
2. ベストプラクティスとして、[サンセットポリシー]({{site.baseurl}}/user_guide/channels/email/best_practices/sunset_policies/)を実装してください。
3. **メールリストを購入しないでください。**

{% alert tip %}
Brazeのカスタマーサクセスチームと到達性チームは、世界中で到達性を最大化するためのベストプラクティスに従えるようサポートします。
{% endalert %}

## バウンスリストまたはスパムリストからメールアドレスを削除する

バウンスしたメールやBrazeのスパムリストに登録されたメールは、以下のエンドポイントを使用して削除できます。
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

## メールの到達性を向上させる

メールの到達性を向上させるためのベストプラクティスについては、[メールの到達性を向上させる]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/)を参照してください。
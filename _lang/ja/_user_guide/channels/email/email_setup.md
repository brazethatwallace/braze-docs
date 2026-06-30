---
nav_title: "セットアップ"
article_title: メールセットアップ
layout: dev_guide
page_order: 0
guide_top_header: "メール設定"
guide_top_text: "Brazeはメールキャンペーンの送信開始をサポートします。以下のガイドに従うか、<a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>メールオンボーディング</a> Brazeラーニングコースをご覧ください。"
page_type: landing
description: "このランディングページには、IPやドメインの設定、IPウォーミング、メール検証など、メールキャンペーンを始めるためのリソースが含まれています。"
channel: email

guide_featured_title: "セクション記事"
guide_featured_list:
- name: "IPとドメインの設定"
  link: /docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains
  image: /assets/img/braze_icons/target-05.svg
- name: "IPウォーミング"
  link: /docs/user_guide/channels/email/email_setup/ip_warming
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "メール検証"
  link: /docs/user_guide/channels/email/email_setup/email_validation
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "メール認証"
  link: /docs/user_guide/channels/email/email_setup/authentication
  image: /assets/img/braze_icons/user-square.svg
- name: "メールリストのインポート"
  link: /docs/user_guide/channels/email/email_setup/import_your_email_list
  image: /assets/img/braze_icons/list.svg
- name: "SSLの概要"
  link: /docs/user_guide/channels/email/email_setup/ssl
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "同意とアドレスの収集"
  link: /docs/user_guide/channels/email/email_setup/consent_and_address_collection
  image: /assets/img/braze_icons/book-closed.svg
- name: "配信の落とし穴とスパムの罠"
  link: /docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps
  image: /assets/img/braze_icons/alert-triangle.svg
- name: "開封ピクセルとクリックトラッキング"
  link: /docs/user_guide/channels/email/email_setup/open_pixel_and_click_tracking
  image: /assets/img/braze_icons/cursor-click-02.svg
---

## 要件 {#requirements}

メールの送信を開始する前に、いくつか必要なものがあります。これらの要件について詳しくは、以下の表を参照してください。

| 要件 | 説明 | ソース |
|---|---|---|
| 専用IP（インターネットプロトコル）| 専用IPは、単一のホスティングアカウント専用に提供されるユニークなインターネットアドレスです。 | Brazeは、メール送信者のレピュテーションを確実にコントロールするための専用IPを提供します。Brazeのオンボーディングによって設定されます。|
| Whitelabel（独自ドメイン利用）ドメイン | これらはドメインとサブドメインで構成されています。Whitelabelを使用することで、DKIMおよびSPFのメール認証チェックを通過できます。 | Brazeオンボーディングチームがこれらのドメインを生成しますが、名前はお客様が選択する必要があります。 |
| サブドメイン | これは、メールアドレス内のドメイン（「@news.company.com」など）の下位区分です。サブドメインを持つことで、会社の公式メールの評判を損なう可能性のあるエラーを防ぐことができます。 | オンボーディングチームがサブドメインを生成しますが、サブドメインの名前はお客様が決定する必要があります。Brazeの外部で現在使用されているサブドメインは使用できません。 |
| IPプール | これらは、異なる種類のメール（「プロモーション」や「トランザクション」など）のレピュテーションを分離し、一方のレピュテーションが他方に影響を与えるのを防ぎ、より高い配信到達性をサポートするために使用されるオプションの設定です。 | オンボーディングチームがプールを設定します。その後、メールを作成する際に、**ターゲットオーディエンス**ステップでメールのIPプールを確認できます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="要件" }

## IPウォーミング {#ip-warming}

{% alert important %}
IPウォーミングはメール設定プロセスにおける**最も重要なステップ**です。最初のステップではありませんが（実際には最後のステップです）、ここでお知らせするのは、IPアドレスをウォームアップしなければ、送信するメールがスパムに振り分けられたり、その他の送信障害が発生したりする可能性があるためです。
{% endalert %}

[IPウォーミング]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)とは、最初のバッチで比較的少数のメールを送信し、その後のバッチで徐々に送信量を増やしていき、通常の1日の送信量に達するまで続けるプロセスです。これはメール設定プロセスの一番最後に行われます。

少量のメールから始めることで、メールプロバイダーとの信頼関係を構築し、関連性の高いユーザーにのみメールを送信していることを示します。最もエンゲージメントの高いユーザーに最初のバッチを送信することで、プロバイダーからの信頼をより早く獲得できます。

IPのウォームアップが完了したら、[メールの作成と送信を開始]({{site.baseurl}}/user_guide/channels/email/html_editor)できます！

## 法的に必要なトランザクションメール {#legally-required-transactional-emails}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

<br><br>
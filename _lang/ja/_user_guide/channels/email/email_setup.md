---
nav_title: "セットアップ"
article_title: メールセットアップ
layout: dev_guide
page_order: 0
guide_top_header: "メールセットアップ"
guide_top_text: "Brazeはメールキャンペーンの送信開始をサポートします。以下のガイドに従うか、<a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>メールオンボーディング</a>のBrazeラーニングコースをご覧ください。"
page_type: landing
description: "このランディングページには、IPやドメインの設定、IPウォーミング、メール検証など、メールキャンペーンの開始に関するリソースが含まれています。"
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
- name: "配信性の落とし穴とスパムトラップ"
  link: /docs/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps
  image: /assets/img/braze_icons/alert-triangle.svg
- name: "開封ピクセルとクリックトラッキング"
  link: /docs/user_guide/channels/email/email_setup/open_pixel_and_click_tracking
  image: /assets/img/braze_icons/cursor-click-02.svg
---

## 要件

メールの送信を開始する前に、いくつか準備が必要です。これらの要件の詳細については、以下の表を参照してください。

| 要件 | 説明 | ソース |
|---|---|---|
| 専用IP（インターネットプロトコル）| 専用IPは、単一のホスティングアカウントに排他的に提供されるユニークなインターネットアドレスです。 | Brazeはメール送信者レピュテーションの管理を確保するために専用IPを提供します。Brazeのオンボーディングチームがこれを設定します。|
| Whitelabel (独自ドメイン利用) ドメイン | これらはドメインとサブドメインで構成されます。Whitelabelを使用することで、DKIMおよびSPFのメール認証チェックに合格できます。 | Brazeのオンボーディングチームがこれらのドメインを生成しますが、名前はお客様が選択する必要があります。 |
| サブドメイン | これはメールアドレス内のドメインの下位区分（「@news.company.com」など）です。サブドメインを持つことで、会社の公式メールレピュテーションを損なう可能性のあるエラーを防ぐことができます。 | オンボーディングチームがこれを生成しますが、サブドメインの名前はお客様が決定する必要があります。Braze以外で現在使用されているサブドメインは使用できません。 |
| IPプール | これらは、異なる種類のメール（「プロモーション」や「トランザクション」など）のレピュテーションを分離し、一方のレピュテーションが他方に影響を与えるのを防ぎ、より高い配信性をサポートするために使用されるオプションの設定です。 | オンボーディングチームがプールを設定します。その後、メールを作成する際に、**ターゲットオーディエンス**ステップでメールのIPプールを確認できます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## IPウォーミング

{% alert important %}
IPウォーミングは、メールセットアッププロセスにおいて**最も重要なステップ**です。最初のステップではありませんが（実際には最後のステップです）、IPアドレスをウォーミングする必要があることをここでお知らせします。ウォーミングを行わないと、送信したメールがスパムに振り分けられたり、その他の送信障壁の対象になったりする可能性があります。
{% endalert %}

[IPウォーミング]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/)とは、最初のバッチで比較的少数のメールを送信し、その後、時間をかけて次のバッチで徐々に送信量を増やし、最終的に通常の1日あたりの送信量に達するまで続けるプロセスです。これはメールセットアッププロセスの最後に行います。

少量のメールから始めることで、メールプロバイダーとの信頼レベルを確立し、関連性のあるユーザーにのみメールを送信していることを示します。最初のバッチを最もエンゲージメントの高いユーザーに送信することで、プロバイダーからの信頼をより早く獲得できます。

IPのウォーミングが完了したら、[メールの作成と送信を開始]({{site.baseurl}}/user_guide/channels/email/html_editor/)できます！

## 法的に必要なトランザクションメール

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

<br><br>
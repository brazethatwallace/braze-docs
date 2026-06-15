---
nav_title: Campaignの自動保存
article_title: Campaignの自動保存
permalink: "/campaign_autosave/"
hidden: true
description: "このリファレンス記事では、Campaignの自動保存の仕組みについて説明します。"
page_type: reference
---

# Campaignの自動保存 {#autosaving-campaigns}

> BrazeでCampaignを作成する際、変更内容が自動的に保存されるようになりました。これにより、進捗が保持されていることを確信しながら、Campaignの詳細の微調整に集中できます。

{% alert important %}
自動保存は現在ベータ版であり、Campaignでのみ利用可能です。このベータへの参加にご興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% alert warning %}
メールやアプリ内メッセージなどのフルスクリーンエディターでメッセージを編集している場合、メッセージへの変更は自動保存されません。**Done**を選択してエディターを終了しCampaignに戻ると、次回の自動保存時にメッセージへの変更が保存されます。念のため、手動でメッセージを保存することもできます。
{% endalert %}

## 仕組み {#how-it-works}

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Campaignエディターで編集やタブの切り替えを行うと、Campaignは自動的かつ定期的に保存されます。

変更内容は、下書きおよびアクティブなCampaignの両方で下書きとして保存されます。停止中のCampaignの場合、変更内容は保存されますが、Campaignは停止状態のままになります。

あなたと別のユーザーが同じCampaignに変更を加えた場合、最初の変更セットが保存されます。2番目に変更を保存した場合は、ページを更新してCampaignの最新の更新内容を確認する必要があります。

[1]: {% image_buster /assets/unlisted_docs/img/campaign_autosave.png %}
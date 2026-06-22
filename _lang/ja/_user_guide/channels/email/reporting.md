---
nav_title: レポート
article_title: メールレポート
page_order: 21
description: "このリファレンス記事では、メールレポートのさまざまなコンポーネントと、ダッシュボードでの確認方法について説明します。"
tool:
  - Reports
channel:
  - email

---

# メールレポート {#email-reporting}

> この記事では、メールレポートのさまざまなコンポーネントと、ダッシュボードでの確認方法について説明します。

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## トラブルシューティング {#troubleshooting}

### バウンスしたメール {#bounced-emails}

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** 別のアドレスを試すか、別のチャネルで再エンゲージメントを行うか、自分のテストアドレスに限り抑制リストからアドレスを削除してください。実際のユーザーの抑制を解除すると、レピュテーションに悪影響を及ぼす可能性があるため避けてください。
- **Mailbox full / invalid account:** 多くの場合、リスト品質のシグナルです。最近開封またはクリックしたユーザー（例：過去30〜60日間）を優先し、非アクティブまたは無効なアドレスをクリーンアップしてください。

### 無効なドメイン {#invalid-domains}

`unable to get mx info` のようなエラーは、多くのターゲットが不正なドメイン（例：タイプミス）を使用していることを意味する場合が多いです。それらのプロファイルをセグメント化し、エクスポートして修正し、再インポートしてください。

### スロットリングされたIP {#throttled-ips}

メールボックスプロバイダーが送信量やレピュテーション、またはその両方を理由にIPからの配信を一時的に遅延またはブロックしている場合、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/)に `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` というメッセージが表示されることがあります。Brazeは遅延されたメッセージを再試行しますが、この原因による遅延が集中すると、ソフトバウンスの増加も同時に見られることがよくあります。

このパターンは通常、現在のレピュテーションに対してメールボックスプロバイダーが受け入れる速度よりも速く送信していることを意味します。エンゲージメントとリスト品質の改善に加えて、[配信速度レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting)を使用して、CampaignやCanvasでBrazeからメッセージが送信される速度にキャップを設定してください。これにより、配信到達性チームと長期的な修正に取り組む間、スロットリングを軽減できます。

特定のドメインに対してスロットリングが続く場合は、そのドメインへの送信量を減らし、Brazeの配信到達性サポートにガイダンスを依頼してください。
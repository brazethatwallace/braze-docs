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

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** 別のアドレスを試すか、別のチャネルで再エンゲージするか、自分のテストアドレスに限り抑制リストからアドレスを削除してください。実際のユーザーの抑制を解除すると、レピュテーションに悪影響を及ぼす可能性があるため避けてください。
- **Mailbox full / invalid account:** 多くの場合、リスト品質のシグナルです。最近開封またはクリックしたユーザー（例えば、過去30〜60日間）を優先し、非アクティブまたは無効なアドレスをクリーンアップしてください。

#### ソフトバウンスのリトライ動作 {#soft-bounce-retry-behavior}

一時的な問題（メールボックスの容量超過、サーバーの一時的な利用不可、その他の一時的な配信障害など）によりメールがソフトバウンスした場合、Brazeは最大72時間にわたって自動的に配信をリトライします。リトライ回数は受信者によって異なります。

リトライ期間後にメールが正常に配信されなかった場合、Brazeはそのキャンペーン送信に対して1つのソフトバウンスイベントを記録します。これらのソフトバウンスはキャンペーン分析には表示されませんが、以下のことが可能です。
- [メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)でバウンス理由を監視する
- [ソフトバウンスセグメントフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced)を使用して、今後の送信からこれらのユーザーを除外する

このリトライ期間があるため、ソフトバウンスしたメールが最終的に配信に失敗したキャンペーンでは、メール配信指標（配信数、バウンス数、スパム率）の合計が100%にならない場合があります。

ソフトバウンスの詳細については、[メール分析用語集]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce)を参照してください。

### 無効なドメイン {#invalid-domains}

`unable to get mx info`のようなエラーは、多くのターゲットが無効なドメイン（例えばタイプミス）を使用していることを意味する場合が多いです。それらのプロファイルをセグメント化し、エクスポートして修正し、再インポートしてください。

### スロットルされたIP {#throttled-ips}

メールボックスプロバイダーが送信量、レピュテーション、またはその両方の理由でIPからの配信を一時的に遅延またはブロックしている場合、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)に`Email was deferred due to the following reason(s): [IPs were throttled by recipient server]`というメッセージが表示されることがあります。Brazeは遅延されたメッセージをリトライします。これによる遅延が集中すると、ソフトバウンスの増加が併せて見られることがよくあります。

このパターンは通常、現在のレピュテーションに対してメールボックスプロバイダーが受け入れる速度よりも速く送信していることを意味します。エンゲージメントとリスト品質の改善に加えて、[配信速度レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)を使用して、キャンペーンまたはキャンバスでBrazeからメッセージが送信される速度を制限してください。これにより、配信チームと長期的な修正に取り組む間、スロットリングを軽減できます。

特定のドメインに対してスロットリングが続く場合は、そのドメインへの送信量を減らし、Brazeの配信サポートにガイダンスを求めてください。

### 不明なIPレピュテーションステータス {#unknown-ip-reputation-status}

メールパフォーマンスレポートでIPレピュテーションに「不明」の値が表示される場合、Google Postmaster Toolsの障害に関連している可能性があります。Google Postmaster ToolsはGmailの配信に関するレピュテーションデータを提供しており、一時的なサービス中断により、レピュテーション値が欠落したり不明になったりすることがあります。

不明なレピュテーションステータスが表示され、メールの配信性について質問がある場合は、[Brazeサポート]({{site.baseurl}}/support_contact)にお問い合わせください。
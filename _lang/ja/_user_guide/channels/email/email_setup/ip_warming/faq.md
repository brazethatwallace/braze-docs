---
nav_title: FAQ
article_title: 自動IPウォームアップ FAQ
channel: email
page_order: 3
description: "Brazeの自動IPウォームアップに関するよくある質問への回答です。"
---

# 自動IPウォームアップ FAQ {#automated-ip-warming-faq}

> [自動IPウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming)に関するよくある質問への回答です。IPウォームアップの概念や手動スケジュールについては、[IPウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)を参照してください。

## 自動IPウォームアップはいつ使用すべきですか？ {#when-should-i-use-automated-ip-warming}

以下のような場合に自動IPウォームアップを使用してください。

- 新しいIPアドレスを初めてウォームアップする場合
- 新しいサブドメインを持つ新しいビジネスユニットやブランドをウォームアップする場合
- 配信到達性を向上させるために既存のIPを再ウォームアップする場合
- 配信到達性を向上させるために特定のメールボックスプロバイダーに対して再ウォームアップする場合

設定手順と前提条件については、[自動IPウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming)を参照してください。

## 開始日はどのくらい前に設定する必要がありますか？ {#how-far-in-advance-must-the-start-date-be}

開始日は、ワークスペースのタイムゾーン（ワークスペースに上書き設定がない場合は会社のタイムゾーン）で翌日以降に設定する必要があります。

Brazeは、そのタイムゾーンの深夜0時に、当日と翌日のキャンペーンを作成します（送信の0〜1日前）。プランを開始すると、今後のキャンペーンも即座に作成されます。

## テンプレートはいくつ必要ですか？ {#how-many-templates-are-required}

Brazeは、計画された送信量と選択したセグメント内のメール送信可能なユーザー数（セグメント全体のサイズではありません）から最小数を計算します。配信性の問題が発生しても停止せずにシステムが調整できるよう、最小数よりも多くのテンプレートを用意してください。詳細については、[ステップ3：送信するメッセージを選択する]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send)を参照してください。

## 同じセグメントを複数のウォームアップ試行に使用できますか？ {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

1つのアクティブなプラン内では、Brazeは同じテンプレートに対する以前のIPウォームアップ送信をすでに受信したユーザーを自動的に除外します。プランを停止して同じセグメントを再利用する新しいプランを開始する場合は、以前のプランからキャンペーンを受信したユーザーを除外するフィルターを追加してください。

## スケジュールの途中からIPウォームアップを開始できますか？ {#can-i-start-ip-warming-mid-schedule}

自動IPウォームアップは、常にランプの開始からスケジュールを構築します。スケジュールの途中から開始するには、**現在の1日あたりの送信量**を現在のボリュームに合わせて0より大きい値に設定してください。現在のボリュームが0より大きい場合、Brazeは1日目にIPカウントのスケーリングを適用しません。

## 送信にはどのタイムゾーンが使用されますか？ {#what-time-zone-is-used-for-sending}

送信には、ワークスペースのタイムゾーンが設定されている場合はそれが使用され、設定されていない場合は会社のタイムゾーンが使用されます。キャンペーンは各ユーザーのローカルタイムゾーンでは作成されません。ローカルタイムゾーンで送信するには、プランによって作成されたキャンペーンを手動で更新してください。

## IP ウォームアッププランは同時にいくつ実行できますか？ {#how-many-ip-warming-plans-can-run-at-the-same-time}

複数のプランを同時に実行できます。詳細については、[複数のIP ウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming)を参照してください。

## 複数のIPを持つIPプールでは、ボリュームはどのようにスケールしますか？ {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

**現在の1日あたりの送信ボリューム**が0の場合、1日目はIPあたり50送信または合計500送信のいずれか低い方から開始します。その後、ボリュームはランプガードレールに従い、送信日ごとに約1.75倍ずつ増加します。例えば、10個のIPの場合：500 → 875 → 1,532 → 2,681となります。

カスタムの現在のボリュームを0より大きい値に設定した場合、1日目にはIPカウントのスケーリングは適用されません。マルチIPプランの詳細については、[1つのプールで複数のIPをウォームアップする]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool)を参照してください。

## 自動IPウォームアップはキャンペーンごとのレート制限をサポートしていますか？ {#does-automated-ip-warming-support-rate-limiting-per-campaign}

いいえ。各キャンペーンは、キャンペーンごとのレート制限なしに、設定された時間に送信されます。

## IP ウォームアップ中にBrazeがボリュームを保持するのはどのような場合ですか？ {#when-does-braze-hold-volume-during-ip-warming}

Brazeは、12〜20時間前に送信されたキャンペーンの配信到達性を評価します。配信率、開封率、バウンス率、またはスパム苦情率が[アクティブなIP ウォームアップ中]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming)のベンチマークを超えた場合、Brazeはボリュームを増加させる代わりに、次の送信日のボリュームを保持します。

## ボリュームが保留された場合はどうなりますか？ {#what-happens-when-volume-is-held}

ボリューム保留とは、これらのしきい値を超えた場合にBrazeが自動的に適用する調整です。次のスケジュールされた送信は、ボリュームを増加させずに同じボリュームを維持します。Brazeは今後のスケジュールエントリを再計画し、プランから既存の今後のキャンペーンをアーカイブし、更新されたスケジュールに対して新しいキャンペーンを即座に作成します。プランがターゲットボリュームに到達するまでに、より長い時間がかかる場合があります。

## IP ウォームアップトラッカーにキャンペーンの編集が反映されないのはなぜですか？ {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

自動 IP ウォームアップによって作成されたキャンペーンに加えた変更（スケジュール、セグメント、ボリュームなど）は、IP ウォームアップトラッカーには同期されません。関連する設定の注意事項については、[ステップ3：送信するメッセージを選択する]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send)を参照してください。

## IPウォームアッププランを停止できますか？ {#can-i-stop-an-ip-warming-plan}

はい。停止するとプランは永久に終了します。Brazeはリンクされたキャンペーンを無効にし、今後のキャンペーンも作成しません。停止したプランを再開することはできません。続行するには新しいプランを作成してください。停止後に再開するためのステップについては、[IPウォームアッププランを停止する]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan)を参照してください。

## IP ウォームアッププランはいつ完了としてマークされますか？ {#when-is-an-ip-warming-plan-marked-as-complete}

プランは、最後のスケジュールされた送信日が終了した後、有効なタイムゾーン（ワークスペースまたは会社）の深夜0時に完了としてマークされます。例えば、最後のキャンペーンが午後8時に送信される場合、プランはその4時間後の深夜0時に完了としてマークされます。

## どのようなデータをダウンロードできますか？ {#what-data-can-i-download}

CSVエクスポートには、キャンペーンごとの行と日次レベルの指標が含まれます：*送信数*、*配信数*、*バウンス数*、*スパムレポート数*、*合計開封数*、*ユニーク開封数*、*クリック数*、*購読解除数*。トラッカーテーブルは、同日の複数のキャンペーンを日次ビューに集約します。詳細については、[IPウォームアップが完了した場合]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes)を参照してください。
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

自動IPウォームアップは、以下のような場合に使用します。

- 新しいIPアドレスを初めてウォームアップする場合
- 新しいサブドメインを持つ新しいビジネスユニットやブランドをウォームアップする場合
- 配信性を向上させるために既存のIPを再ウォームアップする場合
- 特定のメールボックスプロバイダーに対する配信性を向上させるために再ウォームアップする場合

設定手順と前提条件については、[自動IPウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming)を参照してください。

## 開始日はどのくらい前に設定する必要がありますか？ {#how-far-in-advance-must-the-start-date-be}

開始日は、ワークスペースのタイムゾーン（ワークスペースにオーバーライドがない場合は会社のタイムゾーン）で翌日以降に設定する必要があります。

Brazeは、そのタイムゾーンの午前0時に、当日と翌日（送信の0〜1日前）のキャンペーンを作成します。プランを開始すると、今後のキャンペーンも即座に作成されます。

## テンプレートはいくつ必要ですか？ {#how-many-templates-are-required}

Brazeは、計画された送信量と選択したセグメント内のメール送信可能なユーザー数（セグメント全体のサイズではありません）から最小数を計算します。配信性の問題が発生しても停止せずにシステムが調整できるよう、最小数より多くのテンプレートを用意してください。詳細については、[ステップ3：送信するメッセージを選択する]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send)を参照してください。

## 複数のウォームアップ試行で同じセグメントを使用できますか？ {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

単一のアクティブなプラン内では、Brazeは同じテンプレートに対して以前のIPウォームアップ送信を受信済みのユーザーを自動的に除外します。プランを停止して同じセグメントを再利用する新しいプランを開始する場合は、前のプランのキャンペーンを受信したユーザーを除外するフィルターを追加してください。

## スケジュールの途中からIPウォームアップを開始できますか？ {#can-i-start-ip-warming-mid-schedule}

自動IPウォームアップは常にランプの最初からスケジュールを構築します。スケジュールの途中から開始するには、**現在の1日あたりの送信量**を0より大きい値に設定して、現在の送信量に合わせてください。現在の送信量が0より大きい場合、Brazeは1日目にIPカウントスケーリングを適用しません。

## 送信にはどのタイムゾーンが使用されますか？ {#what-time-zone-is-used-for-sending}

ワークスペースのタイムゾーンが設定されている場合はそれが使用され、設定されていない場合は会社のタイムゾーンが使用されます。キャンペーンは各ユーザーのローカルタイムゾーンでは作成されません。ローカルタイムゾーンで送信するには、プランによって作成されたキャンペーンを手動で更新してください。

## 同時にいくつのIPウォームアッププランを実行できますか？ {#how-many-ip-warming-plans-can-run-at-the-same-time}

ワークスペースが複数のプランをサポートしている場合、複数のプランを同時に実行できます。詳細については、[複数のIPウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming)を参照してください。

## 複数のIPを持つIPプールでは、送信量はどのようにスケーリングされますか？ {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

**現在の1日あたりの送信量**が0の場合、1日目はIPあたり50送信または合計500送信のいずれか少ない方から開始します。その後、ランプのガードレールに従い、送信日ごとに約1.75倍ずつ増加します。例えば、10個のIPの場合：500 → 875 → 1,532 → 2,681。

カスタムの現在の送信量を0より大きく設定した場合、1日目にはIPカウントスケーリングは適用されません。マルチIPプランの詳細については、[1つのプールで複数のIPをウォームアップする]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool)を参照してください。

## 自動IPウォームアップはキャンペーンごとのレート制限をサポートしていますか？ {#does-automated-ip-warming-support-rate-limiting-per-campaign}

いいえ。各キャンペーンは、キャンペーンごとのレート制限なしに設定された時間に送信されます。

## BrazeはIPウォームアップ中にいつ送信量を保持しますか？ {#when-does-braze-hold-volume-during-ip-warming}

Brazeは、12〜20時間前に送信されたキャンペーンの配信性を評価します。配信率、開封率、バウンス率、またはスパム苦情率が[アクティブなIPウォームアップ中]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming)のベンチマークを超えた場合、Brazeは次の送信日の送信量を増加させずに保持します。

## 送信量が保持されるとどうなりますか？ {#what-happens-when-volume-is-held}

送信量の保持は、これらのしきい値を超えた場合にBrazeが自動的に適用する調整です。次のスケジュールされた送信は、進行せずに同じ送信量を維持します。Brazeは将来のスケジュールエントリを再計画し、プランから既存の将来のキャンペーンをアーカイブし、更新されたスケジュールの新しいキャンペーンを即座に作成します。プランが目標送信量に到達するまでに時間がかかる場合があります。

## キャンペーンの編集がIPウォームアップトラッカーに反映されないのはなぜですか？ {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

自動IPウォームアップによって作成されたキャンペーンに加えた変更（スケジュール、セグメント、送信量など）は、IPウォームアップトラッカーには同期されません。関連する設定の注意事項については、[ステップ3：送信するメッセージを選択する]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send)を参照してください。

## IPウォームアッププランを停止できますか？ {#can-i-stop-an-ip-warming-plan}

はい。停止するとプランは永久に終了します。Brazeはリンクされたキャンペーンを無効にし、将来のキャンペーンは作成しません。停止したプランを再開することはできません。続行するには新しいプランを作成してください。停止後に再開する手順については、[IPウォームアッププランを停止する]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan)を参照してください。

## IPウォームアッププランはいつ完了としてマークされますか？ {#when-is-an-ip-warming-plan-marked-as-complete}

プランは、最後のスケジュールされた送信日が終了した後、有効なタイムゾーン（ワークスペースまたは会社）の午前0時に完了としてマークされます。例えば、最後のキャンペーンが午後8時に送信された場合、プランはその4時間後の午前0時に完了としてマークされます。

## どのようなデータをダウンロードできますか？ {#what-data-can-i-download}

CSVエクスポートには、日次レベルの指標を含むキャンペーンごとの行が含まれます：*送信数*、*配信数*、*バウンス数*、*スパムレポート数*、*合計開封数*、*ユニーク開封数*、*クリック数*、*購読解除数*。トラッカーテーブルは、同日の複数のキャンペーンを日次ビューに集約します。詳細については、[IPウォームアップが完了した場合]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes)を参照してください。
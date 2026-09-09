---
nav_title: FAQ
article_title: 自動IPウォームアップ FAQ
channel: email
page_order: 3
description: "Brazeの自動IPウォームアップに関するよくある質問への回答です。"
---

# 自動IPウォームアップ FAQ {#automated-ip-warming-faq}

> [自動IPウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming)に関するよくある質問への回答です。IPウォームアップの概念や手動スケジュールについては、[IPウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)を参照してください。

## 自動IP ウォームアップはいつ使用すべきですか？ {#when-should-i-use-automated-ip-warming}

自動IP ウォームアップは、以下のような場合に使用します。

- 新しいIPアドレスを初めてウォームアップする場合
- 新しいサブドメインで新しいビジネスユニットやブランドをウォームアップする場合
- 配信到達性を改善するために既存のIPを再ウォームアップする場合
- 特定のメールボックスプロバイダーに対する配信到達性を改善するために再ウォームアップする場合

設定手順と前提条件については、[自動IP ウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming)を参照してください。

## 開始日はどのくらい前に設定する必要がありますか？ {#how-far-in-advance-must-the-start-date-be}

開始日は、ワークスペースのタイムゾーン（ワークスペースに上書き設定がない場合は会社のタイムゾーン）で翌日以降である必要があります。

Brazeは、そのタイムゾーンの深夜0時に、当日と翌日のキャンペーンを作成します（送信の0〜1日前）。プランを開始すると、今後のキャンペーンも即座に作成されます。

## テンプレートはいくつ必要ですか？ {#how-many-templates-are-required}

Brazeは、計画された送信量と選択したセグメント内のメール送信可能なユーザー数（セグメント全体のサイズではありません）から最小値を計算します。配信到達性の問題が発生してもシステムが停止せずに調整できるよう、最小値よりも多くのテンプレートを用意してください。詳細については、[ステップ3: 送信するメッセージを選択する]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send)を参照してください。

## 同じセグメントを複数のウォームアップ試行に使用できますか？ {#can-i-use-the-same-segment-for-multiple-warmup-attempts}

1つのアクティブプラン内では、Brazeは同じテンプレートに対する以前のIPウォームアップ送信をすでに受信したユーザーを自動的に除外します。プランを停止し、同じセグメントを再利用する新しいプランを開始する場合は、以前のプランのキャンペーンを受信したユーザーを除外するフィルターを追加してください。

## 1人のユーザーが同じ日に複数のメールテンプレートを受信することはありますか？ {#can-a-user-receive-more-than-one-email-template-on-the-same-day}

はい。Brazeはプラン内で特定のテンプレートをすでに受信したユーザーを除外しますが、別のテンプレートを受信したユーザーは引き続き対象となります。1日のスケジュールに利用可能なオーディエンスが不足すると、プランはテンプレートを循環し、一部のユーザーがその日に2つ目のテンプレートを受信することがあります。

これは、選択したセグメント全体のメール送信可能なユーザーの合計数が**目標送信数**より少ない場合に発生し、プランの最終日またはその前後に最も多く起こります。例えば、メール送信可能なユーザーが400,000人で目標送信数が600,000の場合、最終日に約200,000人のユーザーが2つのテンプレートを受信します。これを避けるには、メール送信可能なユーザーの合計数を目標送信数以上に保ってください。詳細については、[オーディエンスサイズとユーザーあたりの複数送信]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#audience-size-and-multiple-sends-per-user)を参照してください。

## スケジュールの途中からIPウォームアップを開始できますか？ {#can-i-start-ip-warming-mid-schedule}

自動IPウォームアップは、常にランプの開始からスケジュールを構築します。スケジュールの途中から開始する場合に近い動作を実現するには、**現在の1日あたりの送信量**を現在のボリュームに合わせて0より大きい値に設定します。現在のボリュームが0より大きい場合、Brazeは1日目にIPカウントスケーリングを適用しません。

## 送信にはどのタイムゾーンが使用されますか？ {#what-time-zone-is-used-for-sending}

送信には、ワークスペースのタイムゾーンが設定されている場合はそれが使用されます。設定されていない場合は、会社のタイムゾーンが使用されます。キャンペーンは各ユーザーのローカルタイムゾーンでは作成されません。ローカルタイムゾーンで送信するには、プランによって作成されたキャンペーンを手動で更新してください。

## 同時に実行できるIPウォームアッププランはいくつですか？ {#how-many-ip-warming-plans-can-run-at-the-same-time}

複数のプランを同時に実行できます。詳細については、[複数のIPウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming)を参照してください。

## 複数のIPを持つIPプールでは、ボリュームはどのようにスケーリングされますか？ {#how-does-volume-scale-for-ip-pools-with-multiple-ips}

**現在の1日あたりの送信ボリューム**が0の場合、1日目はIPあたり50送信または合計500送信のいずれか低い方から開始されます。その後、ボリュームはランプガードレールに基づき、送信日ごとに約1.75倍ずつ増加します。例えば、10個のIPの場合：500 → 875 → 1,532 → 2,681となります。

カスタム現在ボリュームを0より大きい値に設定した場合、1日目にはIPカウントによるスケーリングは適用されません。複数IPプランの詳細については、[1つのプールで複数のIPをウォームアップする]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool)を参照してください。

## 自動IPウォームアップはキャンペーンごとのレート制限をサポートしていますか？ {#does-automated-ip-warming-support-rate-limiting-per-campaign}

いいえ。各キャンペーンは、キャンペーンごとのレート制限なしで、設定された時間に送信されます。

## BrazeはIPウォームアップ中、いつ送信量を保留しますか？ {#when-does-braze-hold-volume-during-ip-warming}

Brazeは、12〜20時間前に送信されたキャンペーンの配信到達性を評価します。配信率、開封率、バウンス率、またはスパム苦情率が[アクティブなIPウォームアップ中]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming)に記載されたベンチマークを超えた場合、Brazeは次の送信日の送信量を増加させず、保留します。

## ボリュームが保留された場合はどうなりますか？ {#what-happens-when-volume-is-held}

ボリューム保留とは、上記のしきい値を超えた場合にBrazeが自動的に適用する調整です。次のスケジュールされた送信は、ボリュームを増加させずに同じボリュームを維持します。Brazeは将来のスケジュールエントリを再計画し、プランから既存の将来のキャンペーンをアーカイブして、更新されたスケジュールに基づく新しいキャンペーンを即座に作成します。ターゲットボリュームに到達するまでに、プランの所要時間が長くなる場合があります。

## 自動 IP ウォームアップトラッカーにキャンペーンの編集が反映されないのはなぜですか？ {#why-dont-campaign-edits-appear-on-the-ip-warming-tracker}

自動 IP ウォームアップによって作成されたキャンペーン（スケジュール、セグメント、ボリュームなど）に加えた変更は、IP ウォームアップトラッカーに同期されません。関連する設定に関する注意事項については、[ステップ 3: 送信するメッセージを選択する]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send)を参照してください。

## IPウォームアッププランを停止できますか？ {#can-i-stop-an-ip-warming-plan}

はい。停止するとプランは永久に終了します。Brazeはリンクされたキャンペーンを無効にし、今後のキャンペーンを作成しません。停止したプランを再開することはできません。続行するには新しいプランを作成してください。停止後に再開する手順については、[IPウォームアッププランを停止する]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan)を参照してください。

## IP ウォームアップ計画が完了としてマークされるのはいつですか？ {#when-is-an-ip-warming-plan-marked-as-complete}

計画は、最終スケジュール送信日が終了した後、有効なタイムゾーン（ワークスペースまたは会社）の深夜0時に完了としてマークされます。例えば、最後のキャンペーンが午後8時に送信される場合、計画はその4時間後の深夜0時に完了としてマークされます。

## どのようなデータをダウンロードできますか？ {#what-data-can-i-download}

CSVエクスポートには、キャンペーンごとの行と日次レベルの指標（*送信数*、*配信数*、*バウンス数*、*スパムレポート数*、*総開封数*、*ユニーク開封数*、*クリック数*、*購読解除数*）が含まれます。トラッカーテーブルは、同日の複数のキャンペーンを日次ビューに集約します。詳細については、[IPウォームアップが完了した場合]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes)を参照してください。
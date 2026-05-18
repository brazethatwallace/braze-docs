{% if include.section == "UTM parameters" %}

リンクの短縮によりURLを自動的に追跡できますが、URLにUTMパラメータを追加して、Google Analyticsなどのサードパーティの分析ツールでキャンペーンのパフォーマンスを追跡することもできます。

URLにUTMパラメータを追加するには、次の手順を実行します。

1. ベースURLから始めます。これは、追跡するページのURLです（`https://www.example.com` など）。
2. ベースURLの後に疑問符（?）を追加します。
3. 各UTMパラメータをアンパサンド（&）で区切って追加します。

例: `https://www.example.com?utm_source=newsletter&utm_medium=sms`

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## よくある質問 {#frequently-asked-questions}

### テスト送信時に受け取るリンクは実際のURLですか？ {#are-the-links-i-receive-when-test-sending-real-urls}

キャンペーンがテスト送信前に下書きとして保存されている場合は、はい。それ以外の場合は、プレースホルダーリンクです。起動されたキャンペーンで送信される正確なURLは、テスト送信で送信されたURLとは異なる場合があることに注意してください。

### URLを短縮する前にUTMパラメータを追加できますか？ {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

はい。静的パラメータとダイナミックなパラメータの両方を追加できます。

### 短縮URLはどのくらいの期間有効ですか？ {#how-long-do-shortened-urls-remain-valid}

パーソナライズ済みURLは、URL登録時から2か月間有効です。[統合リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/?sdktab=unified)の場合は、静的またはパーソナライズ済みの区別がなく、すべてのリンクは9週間有効です。

### リンクを短縮するためにBraze SDKをインストールする必要がありますか？ {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-links}

いいえ。リンクの短縮は、SDKの統合なしで機能します。

{% endif %}

{% if include.section == "Custom Domains" %}

## カスタムドメイン {#custom-domains}

リンクの短縮では、独自のドメインを使用して短縮URLの外観をパーソナライズし、一貫したブランドイメージを表現することもできます。詳細については、[セルフサービスカスタムドメイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains/)を参照してください。

{% endif %}
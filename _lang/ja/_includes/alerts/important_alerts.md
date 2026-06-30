{% if include.alert == 'Web push private browsing' %}

{% alert important %}
プライベートブラウジングウィンドウはWeb プッシュをサポートしていません。
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
CampaignまたはCanvasにBCCアドレスを追加すると、請求対象となるメール数が倍増します。これは、Brazeがユーザー宛てに1通、BCCアドレス宛てに1通のメッセージを送信するためです。
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
通知表示優先度の設定は、Android O以降を実行するデバイスでは使用されなくなりました。これらのデバイスでは、[通知チャネルの設定](https://developer.android.com/training/notify-user/channels#importance)を通じて優先度を設定してください。
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
法的に要求されるトランザクションメールをSMSゲートウェイに送信しないでください。これらのメールは配信されない可能性が高いためです。
<br><br>
電話番号とプロバイダーのゲートウェイドメイン（MM3として知られている）を使用して送信したメールは、SMS（テキスト）メッセージとして受信される可能性がありますが、一部のメールプロバイダーはこの動作をサポートしていません。例えば、T-Mobileの電話番号（「9999999999@tmomail.net」など）にメールを送信した場合、SMSメッセージはT-Mobileネットワークでその電話番号を所有している人に送信されます。
<br><br>
これらのメールがSMSゲートウェイに配信されなくても、メール課金にはカウントされることにご注意ください。サポートされていないゲートウェイへのメール送信を避けるには、[サポートされていないゲートウェイのドメイン名のリスト](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads)を確認してください。
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
さらにセキュリティを高めるために、ユーザーのなりすましを防ぐ[SDK認証]({{site.baseurl}}/developer_guide/authentication)機能を追加することをお勧めします。
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
NaverのAndroidアプリやiOSアプリなど、Brazeのユーザー設定センターをサポートしていないブラウザがあります。一部のユーザーがこれらのブラウザを使用することが予想される場合は、メール設定を管理するための代替方法を提供することを検討してください。
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
レガシーの購入イベントはメンテナンスモードに移行します。既存のBrazeのお客様は、レガシーの購入イベントを引き続き使用できます。購入イベントは引き続き期待どおりに動作しますが、今後はeコマース推奨イベントを基盤として新しい機能が構築されます。Brazeは、サポート終了日が設定されるかなり前に事前通知を行います。新規のBrazeのお客様は、[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events)を使用してください。レガシーの購入イベントは利用できません。
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
レガシーの購入イベントは非推奨状態（メンテナンスモード）に移行します。購入イベントは引き続き期待どおりに動作しますが、[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events)が優先されるため、購入イベントの上にまったく新しい機能が構築されることはありません。この移行が行われると、Segmentフィルターは購入動作の下にデータが入力されなくなります。<br><br>現在購入イベントを使用している場合は、段階的廃止計画に関する事前通知を受け取ります。現時点では、正式な非推奨日まで購入イベントを引き続き使用できます。詳細については、[推奨イベントの概要]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events)を参照してください。
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
S3バケットに保存されたエクスポートファイルは、ダウンロードリンクの有効期限が切れた後（特に記載がない限り、エクスポートメール送信から4時間後）、自動的に削除されます。
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
Shopify連携は、Shopifyの顧客作成と顧客更新のwebhookをサポートしています。これらはデータ設定の構成設定にあります。Shopifyでユーザープロファイルが作成または更新されると、対応するBrazeのユーザープロファイルも作成または更新されます。<br><br>これらのアクションはBrazeでカスタムイベントをトリガーせず、[ShopifyのユーザーデータをBrazeと同期]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#how-the-integration-works)させるためだけに使用されます。同期されるデータには、[カスタム属性]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#supported-shopify-custom-attributes)、[標準属性項目]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#supported-shopify-standard-attributes)、および設定内で有効にされている場合は[サブスクリプショングループの状態]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins)が含まれます。
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Canvasのエントリプロパティは、Canvasコンテキスト変数の一部です。つまり、`canvas_entry_properties`は`context`として参照されます。各`context`変数には、名前、データタイプ、およびLiquidを含めることができる値が含まれます。現在、`canvas_entry_properties`は下位互換性があります。詳細については、[コンテキスト]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#how-it-works)と[Canvasコンテキストオブジェクト]({{site.baseurl}}/api/objects_filters/context_object)を参照してください。
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
このパートナーは、[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents)が有効になっている場合にのみ、**テクノロジーパートナー**ページに表示されます。利用開始に関するサポートが必要な場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**「Day of year」と「Time」のフィルタータイプの選択について**：日付を含むコンテキスト変数をフィルタリングする際は、その日付が毎年繰り返されるかどうかに基づいて、適切な比較タイプを選択してください。

- **毎年繰り返される日付（誕生日、記念日、クリスマスなどの祝日など）には「Day of year」を使用してください。**この比較タイプは、年の要素を無視し、その年の日数（1〜365/366）に基づいて計算します。
- **繰り返されない絶対日付（契約終了日、予約日、サブスクリプションの更新日など）には「Time」を使用してください。**この比較タイプは、年を含む完全なタイムスタンプに基づいて計算します。

絶対日付に「Day of year」を使用すると、計算が年の要素を無視するため、誤った結果や予期しない結果が生じることがあります。例えば、4月の将来の契約終了日が63日以内かどうかを判断する場合、「Day of year」を使用すると、日付番号（119対359）のみを比較し、実際には4月まで188日あることを考慮しないため、誤った一致が生じる可能性があります。

**一般的な指針**：その日付は毎年繰り返されますか？**はい** → 「Day of year」を使用してください。**いいえ** → 「Time」を使用してください。
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
詳細な権限設定は早期アクセス中です。会社の移行が計画された場合、Brazeの管理者はメールとダッシュボード上のバナーで[詳細な権限の移行]({{site.baseurl}}/granular_permissions_migration)に関する通知を受け取ります。
{% endalert %}

{% endif %}

{% if include.alert == 'WhatsApp audio and documents' %}

{% alert note %}
[Brazeメディアライブラリ]({{site.baseurl}}/media_library)は画像と動画のみをサポートしています。オーディオファイルと文書は、ホストされたURLを通じて参照する必要があります。
{% endalert %}

{% endif %}

{% if include.alert == 'Meta MP4 video issue' %}

{% alert important %}
Metaには、特定のエンコーディングやコンテナ設定が原因で、一部のMP4動画がAndroidデバイスで再生できなくなる既知の問題があります。恒久的な修正が利用可能になるまで、MP4ファイルを再フォーマットすることで、ほとんどの送信者の問題が解決します。すべての動画をAndroidデバイスでテストして、正しく配信されることを確認してください。<br><br>MP4ファイルを再フォーマットするには、[CloudConvert](https://cloudconvert.com/mp4-converter)などのWebツールを使用します。MP4ファイルをツールにアップロードし、再度MP4に変換してから、変換されたファイルをダウンロードしてください。
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify cart token alias' %}

{% alert important %}
この連携では、BrazeがWebhookを正しいユーザープロファイルに一致させるために、ユーザーエイリアスは以下の形式を使用する必要があります。<br><br>
- `alias_label`: `shopify_cart_${cartToken}`
- `alias_name`: `shopify_cart_token`
{% endalert %}

{% endif %}

{% if include.alert == 'network dependency' %}

{% alert important %}
Content Cards、アプリ内メッセージ、バナー、およびフィーチャーフラグは、Brazeサーバーとの同期にデバイスの接続性に依存しています。ネットワーク状況は変動する可能性があるため、コンテンツや更新がすぐに同期、表示、またはクリアされない場合があります（例えば、ユーザーがオフラインの場合）。重要な時間的制約のある更新には、これらのチャネルの使用を避けることをお勧めします。
{% endalert %}

{% endif %}

{% if include.alert == 'dynamic image URL' %}

{% alert important %}
[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)や[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)で画像を取得する場合は、画像URLが`https://`で始まることを確認してください。`http://`を使用すると、アプリがクラッシュします。
{% endalert %}

{% endif %}
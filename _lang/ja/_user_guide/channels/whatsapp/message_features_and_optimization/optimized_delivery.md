---
nav_title: 最適化配信
article_title: 最適化配信によるWhatsAppメッセージ
page_order: 1
description: "このリファレンス記事では、最適化配信によるWhatsAppメッセージの構築と作成に関するステップについて説明します。"
page_type: reference
tool:
  - キャンペーン
channel:
  - WhatsApp
---

# 最適化配信によるWhatsAppメッセージ {#whatsapp-messages-with-optimized-delivery}

> ダイナミックなエンゲージメントベースの配信により、WhatsAppで適切なユーザーにより多くリーチし、配信性とエンゲージメントを向上させましょう。

最適化配信によるWhatsAppメッセージは、Metaの[WhatsApp向けマーケティングメッセージAPI](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp)（WhatsApp向けMM API）を使用して送信されます。これにより、ダイナミックなエンゲージメントベースの配信が可能になります。つまり、高エンゲージメントのメッセージ（例えば、読まれてクリックされる可能性が高いメッセージ）は、エンゲージメントする可能性が高いユーザーにより多くリーチできます。WhatsAppは、メッセージが期待され、関連性があり、タイムリーであるため、読まれてクリックされる可能性が高い場合、そのメッセージを高エンゲージメントとみなします。

ブランドは、Cloud APIと比較して、WhatsApp向けMM APIで同等以上の配信性を期待できます。Metaによると、インドでは高エンゲージメントのマーケティングメッセージがCloud APIと比較して最大9%多く配信されました。なお、WhatsApp向けMM APIでも100%の配信性は保証されません。

## 地域別の利用可能性 {#regional-availability}

最適化配信の利用可能性と最適化機能は、ビジネス電話番号とユーザーの地域によって異なります。詳しくは、[機能の地理的な利用可能性](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features)を参照してください。

## 最適化配信の設定 {#setting-up-optimized-delivery}

1. Brazeで、**パートナー連携** > **テクノロジーパートナー** > **WhatsApp**に移動します。
2. **最適化配信で送信を最適化する**セクションで、**設定をアップグレード**を選択して[埋め込みサインアップワークフロー]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)をトリガーします。

![最適化配信で送信を最適化するオプションがあるWhatsAppメッセージ統合セクション。]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3. 最適化配信が有効になると、**WhatsAppビジネスアカウント管理**のアカウント詳細に最適化配信のステータスが表示されます。

![アクティブな番号ステータスを持つサブスクリプショングループが一覧表示されたWhatsAppビジネスアカウント管理セクション。]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

または、WhatsAppマネージャーで直接最適化配信を有効にしてから、Brazeで送信を開始することもできます。

### 設定のトラブルシューティング {#troubleshooting-your-setup}

- **一般的なエラー:** アップグレード中に問題が発生した場合、このエラーバナーが表示され、[サポートに連絡する]({{site.baseurl}}/braze_support)ことを推奨します。
- **不適格エラー:** Metaによって制限されている場合、次のエラーバナーが表示されます：「少なくとも1つのWhatsAppビジネスアカウントがMetaによって制限されています。アップグレードするには、アカウントが良好な状態である必要があります。」この問題が解決されるまで、このバナーは閉じることができません。

## キャンペーンおよびキャンバスでの最適化配信の使用 {#using-optimized-delivery-in-campaigns-and-canvases}

最適化配信は**マーケティングメッセージ**に使用してください。Brazeは**ユーティリティ、認証、サービス、および応答メッセージ**の最適化配信オプションを自動的に削除します。これらのメッセージは、デフォルト設定であるCloud APIを通じて引き続き送信されます。

### 配信方法の選択 {#selecting-the-delivery-method}

1. キャンペーンまたはキャンバスメッセージステップのBraze WhatsApp作成画面で、**設定**タブに移動します。
2. **配信方法**セクションで、WhatsAppビジネスアカウント（WABA）が有効になっている場合、**最適化配信（推奨）**のチェックボックスがデフォルトでオンになっています。特定のメッセージに最適化配信を使用しない場合は、チェックボックスをオフにしてください。
- 最適化配信を選択しても利用できない場合、メッセージは自動的にCloud API方式にフォールバックします。

![最適化配信を選択するチェックボックスがあるプレビュータブを持つメッセージ作成画面。]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### 他のBrazeチャネルでのユーザーのリターゲティング {#retargeting-users-on-other-braze-channels}

WhatsApp向けMM APIは100%の配信性を提供しないため、メッセージを受信しなかった可能性のあるユーザーを他のチャネルでリターゲティングする方法を理解することが重要です。

ユーザーをリターゲティングするには、特定のメッセージを受信しなかったユーザーのセグメントを構築することをお勧めします。これを行うには、エラーコード`131049`でフィルタリングします。このコードは、WhatsAppのユーザーごとのマーケティングテンプレート制限の適用により、マーケティングテンプレートメッセージが送信されなかったことを示します。これは、Braze CurrentsまたはSQLセグメントエクステンションを使用して行うことができます：

- **Braze Currents:** Braze Currentsを使用してメッセージ失敗イベントをエクスポートします。その後、このデータを使用してユーザープロファイルのカスタム属性（`whatsapp_failed_last_msg: true`など）を更新し、リターゲティングキャンペーンのフィルターとして使用できます。
- **SQLセグメントエクステンション:** この機能にアクセスできる場合、SQLを使用してメッセージ失敗ログをクエリし、それらのユーザーのセグメントを作成してから、別のチャネルでそのセグメントをターゲットにすることができます。
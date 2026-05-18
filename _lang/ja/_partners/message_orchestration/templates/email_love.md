---
nav_title: "Email Love"
article_title: "Email Love"
description: "Figmaから直接レスポンシブでアクセス可能なHTMLメールをデザインおよびエクスポートできるFigmaプラグインであるEmail LoveとBrazeを統合する方法について説明します。"
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Email Love

> [Email Love](https://emaillove.com/) は、Figmaから直接レスポンシブでアクセス可能なHTMLメールをデザインおよびエクスポートできるFigmaプラグインです。Email LoveのExport to Braze機能は、Braze APIを使用して、メールテンプレートをBrazeにシームレスにアップロードします。

## 前提条件 {#prerequisites}

| 必要条件            | 説明                                                      |
|------------------------|------------------------------------------------------------------|
| **Email Loveアカウント** | このパートナーシップを活用するには、Email Loveアカウントが必要です。 |
| **Braze REST APIキー** | `Templates` 権限がすべて有効化されているBraze REST APIキー。これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## BrazeでのEmail Loveの使用 {#using-email-love-with-braze}

### ステップ 1:プラグインを実行する {#step-1-run-the-plugin}

メールテンプレートをデザインするには、まずプラグインを読み込む必要があります。詳細な手順については、Email Loveの[メールのBrazeへのアップロード](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm)に関するドキュメントを参照してください。

### ステップ 2:最初のフレームを作成する {#step-2-create-your-first-frame}

プラグインで**[+ No Template Selected]**ボタンを選択し、メールデザイン用の新しいフレームを作成します。

### ステップ 3:Email Loveのビルド済みコンポーネントを使用してテンプレートをデザインする {#step-3-design-the-template-with-email-loves-pre-built-components}

作成したフレームを選択し、プラグインの**Assets**ライブラリーからコンポーネント（ヘッダー、コンテンツブロック、CTA、フッター）を追加して、メールの構造を組み立てます。

![Email Loveのビルド済みコンポーネント。]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### ステップ 4:コンポーネントをカスタマイズする {#step-4-customize-the-components}

Figmaのツールを使用してコンポーネントを変更し、テキスト、画像、色、レイアウトの要素を調整して、ブランドに合わせたテンプレートデザインに仕上げます。フッターコンポーネントを追加すると、エクスポート時にBrazeの配信停止リンクが自動的に含まれます。

![Figmaでコンポーネントをカスタマイズする。]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### ステップ 5:メールテンプレートをBrazeにエクスポートする {#step-5-export-your-email-template-to-braze}

1. 完了したら、エクスポートしたいフレームを選択します。エクスポートを実行するには、配信停止リンクを含むEmail Loveフッターを使用する必要があります。
2. プラグインで**Export**ボタンを選択し、ドロップダウンメニューから**Braze**を選択します。
3. Email Love Figmaプラグイン内の**Braze API Key**ボックスにAPIキーをコピーして貼り付けます。
4. **Set API Key**ボタンを選択します。
5. **Change Instance ID**を選択してから、BrazeインスタンスIDを選択します。

![Email LoveプラグインからBrazeにテンプレートをエクスポートする。]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### ステップ 6:Brazeでメールを編集する {#step-6-edit-your-email-in-braze}

Brazeで、**Templates** > **Edit Templates** > **Edit Message**に移動します。テンプレートエディター内で、メールのHTMLを編集するか、**Classic**タブの**Rich Text editor**を使用できます。

## サポートとトラブルシューティング {#support-and-troubleshooting}

詳細な手順については、Email Loveの[メールデザインのエクスポート](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm)に関するドキュメントを参照してください。その他のサポートについては、Email Loveサポートチームにお問い合わせください。
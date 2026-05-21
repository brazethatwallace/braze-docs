---
nav_title: Zeotap
description: "このリファレンス記事では、BrazeとZeotapのパートナーシップについて説明します。Zeotapは、アイデンティティ解決、インサイト、データ強化を提供する次世代顧客データプラットフォームです。"
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/) は、アイデンティティ解決、インサイト、データ強化を提供して、モバイルオーディエンスを発見、理解できるようにする次世代の顧客データプラットフォームです。

ZeotapとBrazeの統合により、Zeotapの顧客セグメントを同期してユーザーデータをBrazeのユーザーアカウントにマッピングすることで、キャンペーンの規模とリーチを拡大できます。そして、このデータに基づいて行動し、ユーザーにパーソナライズされたターゲット体験を提供できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| Zeotapアカウント | このパートナーシップを活用するには、[Zeotapアカウント](https://zeotap.com/)が必要です。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURLです。エンドポイントは[インスタンスのBraze URL]({% image_buster /assets/img/zeotap/zeotap1.png %})に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1: Zeotapの送信先を作成する {#step-1-create-a-zeotap-destination}

1. Zeotap Unityプラットフォームから**DESTINATIONS**アプリケーションに移動します。
2. **All Channels**で**Braze**を選択します。
3. 表示されるプロンプトで、送信先に名前を付け、Brazeアカウントに関連付けられたクライアント名とBraze REST APIキーを指定します。
4. 最後に、ドロップダウンからBraze RESTエンドポイントインスタンスを選択し、送信先を保存します。<br><br>![]({% image_buster /assets/img/zeotap/zeotap1.png %})

### ステップ2: Zeotap セグメントを作成して送信先にリンクする {#step-2-create-and-link-a-zeotap-segment-to-your-destination}

1. Zeotap Unityプラットフォームから**CONNECT**アプリケーションに移動します。
2. セグメントを作成し、ステップ1で作成したBrazeの送信先を選択します。
3. サポートされている出力識別子を選択します：MAID、SHA256にハッシュされたメールアドレス、またはBrazeで認識される1P顧客識別子（Brazeアカウントにカスタム識別子を使用する場合は、アカウントに対して有効にできるようにZeotapにお問い合わせください）。Brazeの統合に使用できる出力識別子は1つだけです。これらの識別子は、Braze SDKデータを収集するときに設定されたexternal IDと同じである必要があります。
4. セグメントを保存します。

![]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
表示される識別子はセグメントで使用でき、Brazeでサポートされています。
{% endalert %}

### ステップ3: Braze セグメントを作成する {#step-3-create-braze-segment}

Zeotapでセグメントの作成、プッシュ、処理に成功すると、BrazeダッシュボードにZeotapユーザーが表示されます。BrazeダッシュボードでユーザーIDからユーザーを検索できます。

![「カスタム属性」の下でセグメント1から4が「true」としてリストされているBrazeユーザープロファイル。]({% image_buster /assets/img/zeotap/zeotap4.png %})

ユーザーがZeotap セグメントの一部である場合、セグメント名はブール値`true`が設定されたカスタム属性としてユーザープロファイルに表示されます。Braze セグメントを作成する際に必要になるので、カスタム属性名をメモしておいてください。

次に、Braze内でこのセグメントを作成して定義する必要があります。
1. Brazeダッシュボードから**セグメント**を選択し、次に**Create セグメント**を選択します。
2. 次に、セグメントに名前を付け、Zeotapで作成したカスタム属性セグメントを選択します。
3. 変更を保存します。

![Brazeのセグメントビルダーでインポートされたセグメントがカスタム属性として設定されている画面。]({% image_buster /assets/img/zeotap/zeotap3.png %})

この新しく作成したセグメントを、今後のBrazeのキャンペーンやキャンバスに追加して、これらのエンドユーザーをターゲットにできます。
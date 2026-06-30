---
nav_title: 機能の認知と新しいアプリバージョン
article_title: 機能の認知と新しいアプリバージョン
page_order: 9
page_type: reference
description: "このリファレンス記事では、新機能やバージョンをリリースする際に、ユーザーに情報を提供し、期待感を高める方法について説明します。"
tool: Campaigns

---

# 機能の認知と新しいアプリバージョン {#feature-awareness-and-new-app-version}

> このリファレンス記事では、Brazeプラットフォームを使用して、アプリの新機能やバージョンについて顧客に最新情報を提供する方法について説明します。

アプリの継続的な更新と改善に取り組んでいる中で、ユーザーにこれらのエキサイティングな新機能や新しいアプリバージョンを体験してもらいたいと考えるのは当然のことです。まだ使用していない新機能についてユーザーに伝え、アプリを探索して最大限に活用するよう促す方法を学びましょう。

機能認知キャンペーンは、アプリの機能を改善し続ける中で、ユーザーがアプリに関心を持ち続けるよう促す優れた方法です。ユーザーに最新情報を提供し続けることは、ユーザーをアクティブに保ち、評価を向上させ、ユーザーエンゲージメントを確保するための優れた方法です。

## 最新のアプリバージョンによるフィルタリング {#filtering-by-most-recent-app-versions}

Braze SDKは、ユーザーの最新のアプリバージョンを自動的に追跡します。これらのバージョンは、フィルターやセグメントで使用して、どのユーザーにメッセージやキャンペーンを送信するかを決定できます。

![キャンペーン作成ワークフローのターゲットユーザーステップにあるターゲティングオプションパネル。追加のフィルターセクションには、「Android Stopwatch (Android) の最新アプリバージョン番号が 3.7.0 (134.0.0.0) 未満」というフィルターが含まれています。]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
現在のアプリバージョンが反映されるまでに時間がかかる場合があります。ユーザープロファイルのアプリバージョンは、SDKによって情報がキャプチャされたときに更新されますが、これはユーザーがアプリを開いたタイミングに依存します。ユーザーがアプリを開かない場合、現在のバージョンは更新されません。<br><br>また、これらのフィルターは遡及的には適用されません。現在および将来のバージョンに対して「より大きい」または「等しい」を使用することをお勧めしますが、過去のバージョンフィルターを使用すると予期しない動作が発生する可能性があります。
{% endalert %}

### アプリバージョン番号 {#app-version-number}

**アプリバージョン番号**フィルターを使用して、アプリのバージョンとビルド番号でユーザーをセグメント化します。

このフィルターは、アプリバージョンの範囲をターゲットにするための数値比較をサポートしています。たとえば、アプリバージョン「1.2.3」の「未満」、「超過」、「等しい」ユーザーをターゲットにできます。これは、アプリのアップグレードが必要な新機能を宣伝する際に役立ちます。

この新しいフィルターは、以前の各バージョンを明示的にリストするか、正規表現を使用する必要があったレガシーの「アプリバージョン名」フィルターを置き換えることができます。

**仕組み**

* アプリのアプリバージョンで送信される `major.minor.patch` バージョンの各部分は、整数として比較されます
* メジャー番号が等しい場合、マイナー番号が比較されます（以下同様）

**重要**

* Androidアプリには、人間が読める [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) と内部の [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) の両方があります。アプリバージョン番号フィルターは、アプリストアのリリースごとにインクリメントされることが保証されている `versionCode` を使用します。
* アプリの `versionName` と `versionCode` が同期していない場合、混乱が生じる可能性があります。特に、両方のフィールドがBrazeダッシュボードから確認できるためです。ベストプラクティスとして、アプリの `versionName` と `versionCode` が一緒にインクリメントされていることを確認してください。
* 人間が読める `versionName` フィールドでフィルタリングする必要がある場合（一般的ではありません）、アプリバージョン名フィルターを使用してください。

#### SDKの要件 {#sdk-requirements}

このフィルターの値は、Braze Android SDK v3.6.0以降およびiOS SDK v3.21.0以降から収集されます。このフィルターにはSDKの要件がありますが、この機能を使用して、アプリの低い（古い）バージョンを使用しているユーザーもターゲットにすることができます。

Androidの場合、このバージョン番号はアプリの [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) に基づいています。

iOSの場合、このバージョン番号はアプリの [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) に基づいています。

{% alert tip %}
このフィルターは、ユーザーがサポートされているBraze SDKバージョンにアプリをアップグレードした後に値が反映されます。それまでは、選択してもフィルターにバージョンは表示されません。
{% endalert %}

#### ユースケース {#use-case}

次のシナリオでは、アプリのバージョン `2.0.0` で、このフィルターをサポートするBraze SDKに最初にアップグレードしたと仮定します。

Brazeがアプリのバージョン2.0.0からデータを受信すると、以前または以降のバージョンのユーザーをターゲットにできます。

| フィルター  | ユーザーのアプリバージョン  | 結果 |
| :------------- | :----------- | :--------- |
| 2.0.0 未満 | 1.0.0 | Braze SDKが「アプリバージョン番号」フィルターをサポートしていなくても、ユーザーはセグメントに含まれます。 |
| 2.0.0 超過 | 2.5.1 | ユーザーおよび将来のすべてのインストールがセグメントに含まれます。 |
| 2.0.0 超過 | 1.9.9 | ユーザーはセグメントに含まれません。 |
| 2.0.0 以下 | 3.0.1 | ユーザーはセグメントに含まれません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユースケース" }

### アプリバージョン名 {#app-version-name}

「アプリバージョン名」フィルターを使用して、アプリのユーザー向け「ビルド名」でユーザーをセグメント化します。

このフィルターは、「一致する」、「一致しない」、および正規表現によるマッチングをサポートしています。たとえば、アプリがバージョン「1.2.3-test-build」ではないユーザーをターゲットにできます。

Androidの場合、このバージョン名はアプリの [Package Version Name](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) に基づいています。iOSの場合、このバージョン名はアプリの [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) に基づいています。

### 機能を使用していない場合 {#have-not-used-feature}

新しいアプリバージョンをリリースして新機能を導入した場合、ユーザーが新しいコンテンツに気づかないことがあります。機能認知キャンペーンを実施することは、新機能やまだ使用されていない機能についてユーザーに伝える優れた方法です。これを行うには、アプリ内で特定のアクションを完了したことがないユーザーに割り当てられる[カスタム属性]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#custom-data)を作成するか、特定のアクションを追跡する[カスタムイベント]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#custom-data)を使用する必要があります。この属性（またはイベント）を使用して、キャンペーンを送信するユーザーをセグメント化できます。

{% alert tip %}
オーディエンスの特定の部分をリターゲティングしたいですか？[リターゲティングキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns)をチェックして、ユーザーの過去のアクションを活用してキャンペーンをリターゲティングする方法を学びましょう。
{% endalert %}
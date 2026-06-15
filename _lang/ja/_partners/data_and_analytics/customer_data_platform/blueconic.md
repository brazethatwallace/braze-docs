---
nav_title: BlueConic
article_title: BlueConic
description: "このリファレンス記事では、Brazeと業界をリードするピュアプレイ顧客データプラットフォームであるBlueConicとのパートナーシップについて説明します。永続的な個々のプロファイル間でデータを統合し、Amazon Web Services S3サーバーを介してインポート目標のために2つのシステム間でデータを同期できます。"
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [BlueConic](https://www.blueconic.com/) は業界をリードするピュアプレイ顧客データプラットフォームであり、異種システムから企業のファーストパーティデータを解放し、顧客との関係を変革しビジネスの成長を促進するために必要なときに、いつでもどこからでもアクセスできるようにします。

_この統合はBlueconicによって管理されています。_

## 統合について {#about-the-integration}

BrazeとBlueConicの統合により、ユーザーは永続的な個々のプロファイル間でデータを統合し、Amazon Web ServicesのS3サーバーを経由してインポート目標のために2つのシステム間で同期できます。想定される目標には、成長に焦点を当てた取り組み、カスタマーライフサイクルのオーケストレーション、モデリングと分析、デジタル製品と体験、オーディエンスベースの収益化などが含まれます。この統合は、スケジュールされたバッチインポートとエクスポートの両方をサポートしています。

{% alert important %}
統合を使用する場合、BlueConicは同期ごとにデルタ（変化するデータ）を送信します。これには、前回の送信以降に変更されたプロファイルと、そのプロファイルのすべての属性が含まれます。データポイント使用量を適宜監視してください。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| BlueConicアカウント | このパートナーシップを活用するには、[BlueConicアカウント](https://www.blueconic.com/)が必要です。プラグインにアクセスするには、BlueConicアカウント内で[接続を表示および編集](https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles)するためのアクセス権が必要です。 |
| Braze REST APIキー | `users.track`、`users.export.segment`、`campaigns.list`、`campaigns.details`、`segments.lists`、`segments.details`の権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[BrazeインスタンスのURL](https://portal.aws.amazon.com/billing/signup#/start)によって異なります。 |
| S3認証 | データのエクスポートとインポートには、Amazon Web Services（S3）サーバーへのアクセスが必要です。 |
| アクセスキーID<br>シークレットアクセスキー | アクセスキーIDとシークレットアクセスキーを使用して、インポートとエクスポートのためにS3サーバーを認証できます。 |
| AWSバケット | プラグイン内でS3に接続する必要があります。認証後に、利用可能なバケットがドロップダウンメニューに表示されます。ここには、インポートまたはエクスポートされるファイルが保存されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1:Braze接続を作成する {#step-1-creating-a-braze-connection}

BlueConicのナビゲーションバーで**Connections**を選択し、次に**Add Connection**を選択します。表示されるプロンプトで**Braze**を検索し、**Braze connection**を選択します。

グレーの山形記号アイコンをクリックして、接続の使用可能なメタデータフィールドを展開または折りたたみます。これらのフィールドでは、この接続をお気に入りに追加したり、接続の名前を指定したり、ラベルを追加したり、説明を追加したり、接続が[実行されたか実行に失敗したか](https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ)に関するメール通知を受信するかどうかを選択したりできます。

設定を保存します。

### ステップ2:Braze接続を設定する {#step-2-configuring-a-braze-connection}

BlueConicとBraze間の接続を設定するには、接続を認証するためにBrazeのアカウント認証情報とAmazon Web Services（S3）のアカウント情報を追加する必要があります。

1. BlueConicの左パネルの**Setup**セクションで**Set up and run**を選択します。<br><br>
2. 開いたBraze認証ページで、Braze REST APIエンドポイントとBraze APIキーを入力します。<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. S3の設定と認証のセクションで、次の認証情報を入力します：Amazon Web Services（S3）のアクセスキーID、シークレットアクセスキー、S3バケット。これらは、BrazeとAmazon S3の統合を設定するときに構成した[のと同じ認証情報]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)である必要があります。設定を保存します。<br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### ステップ3:インポートゴールまたはエクスポートゴールを作成する（インポートマッピング） {#step-3-creating-import-or-export-goals-import-mapping}

認証が完了したら、少なくとも1つのインポートまたはエクスポートゴールを作成し、接続をオンにし、接続をスケジュールまたは実行する必要があります。

{% tabs %}
{% tab インポート %}

1. 左パネルで**Import data into BlueConic**を選択し、Brazeデータ設定ページを開きます。<br><br>
2. Brazeのデータの場所を選択します。ここで、Brazeのオーディエンスを選択することで、インポートするデータの場所をBlueConicに伝えることができます。<br>![「BlueConic Test Users」として設定されたBlueConic Brazeオーディエンス。]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. 次に、BrazeとBlueConicの間で識別子をマッピングします。<br>![Brazeのフィールド「External ID」がBlueConicの「Braze external ID」フィールドにマッピングされるように設定されている画面。]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> 2つのシステム間で顧客データをリンクさせるには、1つ以上の顧客識別子を入力します。<br>既存のBlueConicプロファイルに一致しないデータについて、BlueConicが新しいプロファイルを作成することを許可するには、**Allow creation...**チェックボックスを使用します。<br><br>
4. 次に、エクスポートするBlueConicのデータフィールドをBrazeのフィールドに合わせます。ドロップダウンフィールドを使用して、左側のBlueConicプロファイル識別子またはプロファイルプロパティのいずれかを選択し、対応するBrazeプロファイル識別子を選択します。次に、ドロップダウンメニューを使用して、インポートしたコンテンツを既存の値にどのように追加するかを指定します：追加、合計、プロファイルプロパティが空の場合のみ設定、またはクリアに設定（Brazeフィールドが空の場合）。<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>**Add Mapping**ボタンを使って、必要に応じてマッピング行を追加作成します。**Add remaining fields**オプションで複数のマッピング行を追加できます。BlueConicは残りのBrazeフィールドを検出し、BlueConicプロファイルプロパティと照合します。インポートのマージ戦略（set、add、sum、set if empty、clear）を設定し、BlueConicプロファイルプロパティの名前にカスタム接頭辞を指定できます。<br><br>
5. 最後に、**Run the connection**を選択して接続を開始します。接続のスケジューリングと実行については、[BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections)をご覧ください。
{% endtab %}
{% tab エクスポート %}

1. 左パネルで**Export data to Braze**を選択し、BlueConicからBrazeへのデータエクスポートを設定します。<br><br>
2. エクスポートするBlueConicセグメントを選択します。このセグメント内で、Brazeに一致する識別子を持つプロファイルのみがエクスポートされます。<br>![BlueConicの2万プロファイルのセグメント。]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. 次に、BlueConicプロファイルとBrazeフィールド間の識別子をリンクさせます。オプションで、一致するレコードがない場合にBlueConicが新しいレコードを作成するよう設定することもできます。<br>![Brazeのフィールド「External ID」がBlueConicの「Braze external ID」フィールドにマッピングされるように設定されている画面。]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. 次に、エクスポートするBlueConicのデータフィールドをBrazeのフィールドに合わせます。BlueConicアイコンのドロップダウンメニューを使用して、エクスポートする[情報](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals)のタイプを選択します。利用可能な情報には、プロファイルプロパティ、BlueConicプロファイル識別子、関連セグメント、閲覧されたすべてのインタラクション、権限レベル、静的テキスト値が含まれます。<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. 最後に、**Run the connection**をクリックして接続を開始します。接続のスケジューリングと実行については、[BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections)をご覧ください。
{% endtab %}
{% endtabs %}

## ステップ4:接続をオンに切り替える {#step-4-toggle-connection-on}

Braze接続のタイトルの横にあるトグルを使って、接続のオンとオフを切り替えます。スケジュールされた時間に実行するには、接続がオンになっている必要があります。
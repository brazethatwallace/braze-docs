---
nav_title: Redpoint
article_title: Redpoint
description: "Redpoint と Braze の統合により、ファーストパーティデータを使用して Braze ユーザープロファイルをオンボーディングおよび拡充できます。"
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint](https://www.redpointglobal.com) は、完全に統合されたキャンペーンオーケストレーションプラットフォームをマーケターに提供するテクノロジープラットフォームです。Redpointのセグメンテーション、スケジュール、およびオートメーション機能を活用して、CDP データが Braze にインポートされる方法とタイミングをコントロールできます。

_この統合は Redpoint によって管理されています。_

## 統合について {#about-the-integration}

Braze と Redpoint の統合により、Redpoint CDP データに基づいて Braze セグメントを作成できます。Redpoint には、データを Braze に渡すための2つのモードがあります。

1. **Braze Onboarding and Upsert** モード: Redpoint から Braze へユーザープロファイルを「Upsert」します。これは、データが変更されたときにユーザーレコードをオンボーディングまたは更新するために使用されます。
2. **Braze Append** モード: そのユーザーが Braze にすでに存在する場合に、ユーザープロファイルを更新します。

モードごとにエクスポートテンプレートとアウトバウンドチャネルを設定します。

{% alert note %}
「Upsert」は「update（更新）」と「insert（挿入）」を組み合わせた言葉です。データベーステーブルに新しいレコードが存在しない場合はそのレコードを挿入し、存在する場合はレコードを更新する場合に使用されます。基本的に、upsert は特定のレコードがデータベースに存在するかどうかを確認します。レコードが存在する場合は更新され、存在しない場合は新しいレコードが挿入されます。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Braze REST APIキー | `users.track` 権限を持つ Braze REST APIキー。<br><br>これは、Braze ダッシュボードの**「設定」**>**「APIキー」**から作成できます。 |
| Braze REST エンドポイント | [REST エンドポイント URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスの Braze URL に依存します。 |
| Redpoint Data Management アーティファクト | Braze 統合は、一連の Redpoint Data Management アーティファクトによりサポートされています。ご使用の Redpoint Data Management バージョンに対応したアーティファクトをリクエストするには、[Redpoint Support](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us) にお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Redpoint CDP カスタム属性 {#redpoint-cdp-custom-attributes}

以下の Redpoint カスタム属性を Braze ユーザープロファイルに追加できます。

| フィールド | 説明 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | Redpoint CDP プロファイル属性オブジェクト |
| `rpi_audience_outputs` | Redpoint Outbound Delivery Braze チャネルの実行でこのユーザーがターゲットとなるオーディエンス出力タグの配列 |
| `rpi_offers` | Redpoint Outbound Delivery Braze チャネルの実行でこのユーザーがターゲットとなるオファータグの配列 |
| `rpi_contact_ids` | Redpoint Outbound Delivery Braze チャネルの実行でこのユーザーがターゲットとなるオファー履歴連絡先 ID の配列 |
| `rpi_channel_exec_ids` | Redpoint Outbound Delivery Braze チャネルの実行でこのユーザーがターゲットとなるチャネル実行 ID の配列 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## 統合 {#integration}

### ステップ 1: テンプレートの設定 {#step-1-set-up-templates}

#### ステップ 1a: Braze Onboarding and Upsert テンプレートを作成する {#step-1a-create-the-braze-onboarding-and-upsert-template}

Redpoint Interaction (RPI) で、新しいエクスポートテンプレートを作成し、**Braze Onboarding and Upsert** という名前を付けます。このテンプレートでは、Redpoint CDP と Braze ユーザープロファイルの間のコアマッピングと、Braze でユーザープロファイルに追加するカスタム属性を定義します。

Redpoint CDP 属性を**属性**列にドラッグします。それぞれの**ヘッダー行値**を対応する Braze [ユーザー属性]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)に設定します。

以下のテーブルに、Redpoint CDP 属性と対応する Braze 属性を示します。

| Redpoint 属性 | ヘッダー行値 |
|--------------------|------------------|
| PID | `external_id` |
| First Name | `first_name` |
| Last Name | `last_name` |
| Primary Email | `email` |
| Primary Country | `country` |
| DOB | `dob` |
| Gender | `gender` |
| Primary City | `home_city` |
| Primary Phone | `phone` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Offer History** テーブルの **Output Name** 属性を追加します。最後に、Braze にマージする追加のカスタム Redpoint 属性を追加します。たとえば、以下は education、income、marital status が追加属性として含まれている Onboarding and Upsert テンプレートの例です。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### ステップ 1b: Braze Append テンプレートを作成する {#step-1b-create-the-braze-append-template}

追加専用操作のための2つ目のエクスポートテンプレートを **Braze Append** という名前で作成します。

このテンプレートには2つの属性のみを設定します。**PID** の場合は、**Header Row Value** を `external_id` に設定します。**Output Name** の場合は、**Header Row** を `output_name` に設定します。

![external_id および Output Name 属性を含むエクスポートテンプレートの例。]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### ステップ 1c: 日付形式の設定 {#step-1c-set-date-format}

両方のエクスポートテンプレートで、**Options** タブに移動し、**Date Format** を **Custom Format** の値に設定します。形式を **yyyy-MM-dd** に設定します。

![日付形式が yyyy-MM-dd に設定されている Options タブ。]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### ステップ 2: アウトバウンドチャネルを作成する {#step-2-create-outbound-channels}

RPI で2つの新しいチャネルを作成します。両方のチャネルを **Outbound Delivery** に設定します。1つのチャネルに **Braze Onboarding and Upsert** という名前を付け、もう1つのチャネルに **Braze Append** という名前を付けます。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
Braze への CDP レコードの最初のオンボーディング後に、Braze Onboarding and Upsert チャネルを使用する後続の Redpoint Interaction ワークフローが、最初のオンボーディング同期以降に変更されたレコードのみを選択するように設計されているかどうかを確認してください。
{% endalert %}

### ステップ 3: チャネルの設定 {#step-3-configure-the-channels}

#### ステップ 3a: テンプレートおよびエクスポートパス形式の設定 {#step-3a-set-template-and-export-path-format}

チャネルの **Configuration** 画面の **General** タブに移動します。エクスポートテンプレートをそれぞれのチャネルに設定します。

次に、Redpoint Interaction と Redpoint Data Management の両方がアクセスできる共有ネットワーク、ファイル転送プロトコル、または外部コンテンツプロバイダーのロケーションを指す**エクスポートパス形式**を両方のチャネルで定義します。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

両方のチャネルのエクスポートディレクトリ形式は同一であり、`\\[Channel]\\[Offer]\\[Workflow ID]` で終わる必要があります。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### ステップ 3b: 実行後の設定 {#step-3b-configure-post-execution}

チャネルの **Configuration** 画面の **Post Execution** タブに移動します。

**Post-execution** チェックボックスをオンにして、チャネル実行後にサービス URL を呼び出します。Redpoint Data Management Web サービスの URL を入力します。このエントリは、Onboarding チャネルと Append チャネルの両方で同一です。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### ステップ 4: Redpoint Data Management で Braze コンポーネントを設定する {#step-4-set-up-braze-components-in-redpoint-data-management}

Braze 統合をサポートするための Redpoint Data Management (RPDM) アーティファクトを含むアーカイブには、必要なコンポーネントの詳しい設定手順が記載された README が含まれています。統合を設定するときには以下の点に留意してください。

#### ステップ 4a: Braze REST エンドポイントとベース RPI 出力ディレクトリで RPI to Braze オートメーションを更新する {#step-4a-update-the-rpi-to-braze-automation-with-your-braze-rest-endpoint-and-base-rpi-output-directory}

Braze 関連のアーティファクトを Redpoint Data Management にインポートした後、**AUTO_Process_RPI_to_Braze** という名前のオートメーションを開き、以下の2つのオートメーション変数をご自身の環境の値で更新します。

* **BRAZE_API_URL**: Braze REST エンドポイント
* **BASE_OUTPUT_DIRECTORY**: Redpoint Interaction と Redpoint Data Management 間の共有出力ディレクトリ

![]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### ステップ 4b: RPI to Braze Append プロジェクトを更新する {#step-4b-update-the-rpi-to-braze-append-project}

**PROJ_RPI_to_Braze_Append** という名前の Redpoint Data Management プロジェクトには、Braze の `rpi_cdp_attributes` カスタム属性オブジェクトのための、アウトバウンド配信エクスポートファイルのスキーマとマッピングが含まれています。

ファイル入力スキーマとドキュメント挿入ツール **RPI to Braze Document Injector** を、エクスポートファイルテンプレートに定義されている追加のカスタム CDP 属性で更新します。次の例に、education、income、marital status の追加マッピングを示します。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## 統合の使用 {#using-the-integration}

Outbound Delivery Braze チャネルを Redpoint Interaction ワークフロー内で利用できるようになりました。RPI での選択ルールとオーディエンスの作成、および関連するワークフロースケジュールとトリガーの構築については、標準的な方法に従ってください。

RPI Audience 出力を Braze に同期するには、アウトバウンド配信オファーを作成し、**Braze Onboarding and Upsert** チャネルまたは **Braze Append** チャネルのいずれかに関連付けます。これは、Braze で新規レコードを作成またはマージすることが目的なのか、レコードが Braze にすでに存在する場合にのみキャンペーンデータを追加することが目的なのかによって異なります。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

ワークフローが RPI で正常に実行されると、RPI から取得したオーケストレーションおよび CDP データを使用して、Braze でセグメントを作成できるようになります。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

Redpoint 関連のプロパティは、ユーザープロファイルで確認できます。

![]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}
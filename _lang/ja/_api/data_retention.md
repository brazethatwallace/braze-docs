---
nav_title: データリテンション
article_title: データリテンション
alias: /data_retention/
description: "この参考記事では、Braze のデータリテンションに関する一般的な情報について説明します。"
page_type: reference
page_order: 2.5

---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Braze データリテンション情報 {#braze-data-retention-information}

*最終改訂日: 2024年4月1日*

> この記事では、Brazeのデータリテンションに関する一般的な情報について説明します。<br><br>Brazeに保存されたデータは、顧客のアカウントの存続期間中、セグメンテーション、パーソナライゼーション、およびターゲティングのために保持され、使用できます。これは、ユーザープロファイル属性、カスタム属性、カスタムイベント、および購入などのデータが、契約期間中、顧客によって削除されない限り、アクティブユーザーのために無期限に保存されることを意味します。<br><br>Brazeには、GDPRおよびその他のベストプラクティスに準拠するための適切なデータ衛生管理を自動的に実施するための機能、プロセス、およびAPIが備わっています。これらは以下に説明されています。

## Brazeのダッシュボードまたは API を使用した顧客によるデータリテンション {#data-retention-handled-by-customers-through-brazes-dashboard-or-api}

Brazeでは、顧客自身がワークスペースからユーザープロファイルと属性データのすべてを削除できます。

つまり、次のことが可能です。
- Brazeの[ユーザー削除APIエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)を使用してユーザープロファイルを削除する
- Brazeの[ユーザー追跡APIエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、ユーザープロファイルの属性を削除（null）または修正する

ユーザープロファイルから行動イベントを削除することはできません（カスタムイベント、セッション、キャンペーン、購入）。それらのイベントを削除するには、ユーザープロファイル全体を削除する必要があります。

プライバシーコンプライアンスのために、ユーザーの要求に応じて、ユーザーに関するすべての個人データを削除する必要がある場合があります。手順については、[データ保護技術支援]({{site.baseurl}}/help/dp-technical-assistance#the-right-to-erasure)ページをご覧ください。

{% alert note %}
ユーザーは複数のプロファイルを持つことができ、単一のユーザーに関連するすべてのデータを削除するには、複数のプロファイルを削除する必要がある場合があります。ユーザーに関するすべてのデータを完全に削除する方法については、データ保護技術支援ページの手順に従ってください。
{% endalert %}

## Brazeサービスの特定の機能のためにBrazeによって処理されるデータリテンション {#data-retention-handled-by-braze-for-specific-features-of-the-braze-services}

### Brazeデータベース：解約ユーザーの自動アーカイブ/削除 {#braze-database-automatic-archivingdeletion-of-churned-users}

Brazeは毎週、非アクティブユーザーと休眠ユーザーをBrazeサービスから削除するプロセスを実行します。一般的に、これらは到達不可能なユーザー（例えば、メールアドレスがない、電話番号がない、プッシュトークンがない、アプリを使用しない、またはWebサイトを訪問しない）であり、ユーザープロファイルにアクティビティが記録されておらず、Brazeを使用してメッセージを送信またはエンゲージメントを行っていないユーザーです。これはGDPRの原則とベストプラクティスに従うために行われます。このプロセスの詳細については、[ユーザーアーカイブの定義]({{site.baseurl}}/user_archival)ページをご覧ください。

{% alert note %}
顧客は、ユーザーが非アクティブまたは休止状態であるかどうかを完全にコントロールでき、定期的にデータポイントを記録することでユーザープロファイルのアーカイブを防ぐことができます。Braze キャンバスにはこれを自動的に行う機能が備わっており、一部またはすべての非アクティブユーザーまたは休眠ユーザーに対してこの機能を効果的にオフにすることができます。
{% endalert %}

### キャンペーンおよびキャンバスのインタラクションデータ {#campaign-and-canvas-interactions-data}

メッセージングインタラクションデータとは、ユーザーが受信したキャンペーンやキャンバスとどのようにやり取りしたかを示すデータです（例：ユーザーがキャンペーン Aを開封した、ユーザーがバリアントAを受信した、など）。このデータはリターゲティングに使用されます。メッセージングインタラクションデータの利用可能性については、[メッセージングインタラクションデータの利用可能性について]({{site.baseurl}}/messaging_interaction_data)で詳しくご覧いただけます。

## Brazeによって処理されるデータリテンション {#data-retention-handled-by-braze}

以下のリテンションポリシーは、BrazeのGDPRおよびプライバシー規制への準拠に関するものであり、当社の内部システムを通過する際の一時的なデータストレージに関するものです。これらのリテンションポリシーはBrazeサービスに影響を与えず、法務およびプライバシーチームのための情報提供を目的としています。

### Brazeサーバー：リカバリー目的の短期間のリテンション {#braze-servers-short-term-retention-for-recovery-purposes}

Brazeによって特定のサブプロセッサーに送信されたデータは、最大90日間Brazeの内部システムに存在する可能性があります。

### Brazeデータレイクデータリテンション {#braze-data-lake-data-retention}

Brazeダッシュボード内で顧客が利用できるデータは、ほとんどが集約されています。詳細なログは、Brazeによって作成された別のデータベース（「Data Lake」）に保存されます。Data Lakeのデータは、集計レポートやその他の高度な機能に使用されます。Brazeは、Data Lakeに保存されたイベントデータから2年後に個人を特定できる情報を削除します（詳細については、[Snowflakeデータリテンション]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention#snowflake-data-retention)に関するページを参照してください）。

当社のAPIを使用してユーザープロファイルを削除した場合、またはユーザープロファイルの属性を削除もしくは修正した場合、そのデータがBrazeのData Lakeから削除されるまで最大3週間かかる場合があります。Data Lake内のデータを削除しても、セグメンテーションまたはパーソナライゼーションには影響しませんが、データがすべてのBrazeシステムから確実に削除されます。

### Brazeバックアップサーバー {#braze-backup-servers}

本番インスタンスからデータが削除されると、そのデータはBrazeのバックアップサーバーに6か月間残り、その後内部プロセスに従って削除されます。
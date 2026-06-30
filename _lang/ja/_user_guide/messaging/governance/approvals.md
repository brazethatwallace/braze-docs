---
nav_title: 承認
article_title: 承認
page_order: 1
page_type: reference
description: "このリファレンス記事では、キャンペーンやキャンバスが持つさまざまなステータスとその意味について概要を説明します。"
tool:
    - キャンペーン
    - キャンバス
---

# キャンペーンとキャンバスの承認 {#approvals-for-campaigns-and-canvases}

> 承認を使用して、キャンペーンやキャンバスの起動前に最終チェックポイントを追加できます。このワークフローにより、メッセージのすべての必須セクションのコンテンツを確認し、承認できます。

## 仕組み {#how-it-works}

キャンペーンまたはキャンバスの詳細は、編集の最終ステップで確認できます。

キャンバスとキャンペーンの両方で、承認する前にすべての変更を保存する必要があります（自分自身の変更であっても同様です）。適切な権限を持つユーザーが、メッセージを起動する前にサマリーの各セクションを承認する必要があります。各セクションのデフォルトステータスは**Pending Approval**です。

{% tabs %}
{% tab campaign %}
キャンペーンを起動するには、以下のコンポーネントを承認する必要があります。

- **Messages:** キャンペーンのメッセージです。
- **Delivery:** 配信タイプであり、ユーザーがキャンペーンを受信するタイミングを決定します。
- **Target Audience:** キャンペーンを受信するユーザーを決定します。
- **Conversion Events:** エンゲージメントとレポート目的で追跡する指標です。
{% endtab %}

{% tab canvas %}
キャンバスを起動するには、以下の主要コンポーネントを承認する必要があります。

- **Conversion Events:** エンゲージメントとレポート目的で追跡する指標です。
- **Entry Schedule:** エントリスケジュールのタイプと、ユーザーがキャンバスに入るタイミングを含みます。
- **Target Audience:** このキャンバスに入るユーザーを決定します。
- **Send Settings:** キャンバス内のすべてのステップの送信オプションです。
- **Build キャンバス:** キャンバスのユーザージャーニーです。
{% endtab %}
{% endtabs %}

## 承認ワークフローの有効化 {#turning-on-the-approval-workflow}

デフォルトでは、キャンペーンとキャンバスの承認ワークフロー設定はオフになっています。この機能を有効にするには、**Settings** > **Approval Workflow**に移動し、該当するトグルを選択します。

- **Use approval workflow for all キャンペーン in [ワークスペース名]**
- **Use approval workflow for all キャンバス in [ワークスペース名]**

{% alert important %}
キャンペーンの承認は、[API キャンペーン]({{site.baseurl}}/api/api_campaigns)および[トランザクションメールキャンペーン]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)ではサポートされていません。
{% endalert %}

## ユーザー権限の設定 {#setting-user-permissions}

承認ワークフローを有効にした後、会社ユーザーがキャンペーンやキャンバスを承認または拒否できるようにユーザー権限を設定する必要があります。両方の権限は、ワークスペースまたは[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)に適用したり、[権限セット]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#permission-sets)に追加したりすることもできます。

{% tabs %}
{% tab campaign %}
[「Approve and Deny キャンペーン」権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#managing-limited-and-team-role-permissions)が必要です。この権限は、キャンペーンの承認ステータスを更新できるユーザーを制御します。この権限があると、以下のことが可能です。

- キャンペーンを自己承認する
- キャンペーンを承認して起動する
- キャンペーンを承認するが起動しない（「キャンペーン、キャンバスを送信」権限を持つ別のユーザーがキャンペーンを起動できます）
- キャンペーンを承認も起動もしない

**Summary**ステップで承認ステータスが設定された後、キャンペーンに対するその後の変更は、保存時にすべての承認ステータスをリセットします。これは、下書きのキャンペーンまたは起動後のキャンペーンのいずれかで行われた変更に適用されます。たとえば、ターゲットオーディエンスのみを変更した場合でも、**Summary**ステップはすべてのセクションの承認ステータスをデフォルトの状態である**Pending Approval**に戻します。

{% endtab %}

{% tab canvas %}
[「Approve and Deny キャンバス」権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#managing-limited-and-team-role-permissions)が必要です。この権限は、キャンバスの承認ステータスを更新できるユーザーを制御します。この権限があると、以下のことが可能です。

- キャンバスを自己承認する
- キャンバスを承認して起動する
- キャンバスを承認するが起動しない（「キャンペーン、キャンバスを送信」権限を持つ別のユーザーがキャンバスを起動できます）
- キャンバスを承認も起動もしない

**Summary**ステップで承認ステータスが設定された後、キャンバスに対するその後の変更は、保存時にすべての承認ステータスをリセットします。これは、下書きのキャンバスまたは起動後のキャンバスのいずれかで行われた変更に適用されます。たとえば、ターゲットオーディエンスのみを変更した場合でも、**Summary**ステップはすべてのセクションの承認ステータスをデフォルトの状態である**Pending Approval**に戻します。

{% alert note %}
**承認ステータスと保存**

- **Summary**ステップでセクションの**Approve**をクリックすると、その承認は即座に保存されます。
- **Save**ボタンは、キャンバスのコンテンツと設定の変更を保存するものであり、承認ステータスを保存するものではありません。

承認を失わないようにするには:

1. 必要なキャンバスの編集を行い、**Save**をクリックします。
2. キャンバスの保存が完了した後、**Summary**ステップで該当するセクションを承認します。
3. 承認後にキャンバスをさらに変更した場合のみ、再度**Save**をクリックします。キャンバスを変更して保存すると、すべての承認ステータスが**Pending Approval**にリセットされます。
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
ライブのキャンペーンを編集するには、「Approve and Deny キャンペーン」権限が必要です。キャンペーンの下書きバージョンはまだ利用できないため、ユーザーは自分の変更を承認する必要があります。キャンバスの場合はこの限りではなく、ユーザーが変更を加えて下書きとして保存し、別のユーザーがキャンバスを承認して起動できます。
{% endalert %}
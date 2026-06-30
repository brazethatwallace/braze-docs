---
nav_title: 承認
article_title: 承認
page_order: 1
page_type: reference
description: "このリファレンス記事では、CampaignやCanvasが持つさまざまなステータスとその意味について概要を説明します。"
tool:
    - Campaigns
    - Canvas
---

# CampaignとCanvasの承認 {#approvals-for-campaigns-and-canvases}

> 承認を使用して、CampaignやCanvasの起動前に最終チェックポイントを追加できます。このワークフローにより、メッセージのすべての必須セクションのコンテンツを確認し、承認できます。

## 仕組み {#how-it-works}

CampaignまたはCanvasの詳細は、編集の最終ステップで確認できます。

CanvasとCampaignの両方で、承認する前にすべての変更を保存する必要があります（自分自身の変更であっても同様です）。適切な権限を持つユーザーが、メッセージを起動する前にサマリーの各セクションを承認する必要があります。各セクションのデフォルトステータスは**Pending Approval**です。

{% tabs %}
{% tab campaign %}
Campaignを起動するには、以下のコンポーネントを承認する必要があります。

- **Messages:** Campaignのメッセージです。
- **Delivery:** 配信タイプであり、ユーザーがCampaignを受信するタイミングを決定します。
- **Target Audience:** Campaignを受信するユーザーを決定します。
- **Conversion Events:** エンゲージメントとレポート目的で追跡する指標です。
{% endtab %}

{% tab canvas %}
Canvasを起動するには、以下の主要コンポーネントを承認する必要があります。

- **Conversion Events:** エンゲージメントとレポート目的で追跡する指標です。
- **Entry Schedule:** エントリスケジュールのタイプと、ユーザーがCanvasに入るタイミングを含みます。
- **Target Audience:** このCanvasに入るユーザーを決定します。
- **Send Settings:** Canvas内のすべてのステップの送信オプションです。
- **Build Canvas:** Canvasのユーザージャーニーです。
{% endtab %}
{% endtabs %}

## 承認ワークフローの有効化 {#turning-on-the-approval-workflow}

デフォルトでは、CampaignとCanvasの承認ワークフロー設定はオフになっています。この機能を有効にするには、**Settings** > **Approval Workflow**に移動し、該当するトグルを選択します。

- **Use approval workflow for all Campaigns in [ワークスペース名]**
- **Use approval workflow for all Canvases in [ワークスペース名]**

{% alert important %}
Campaignの承認は、[API Campaigns]({{site.baseurl}}/api/api_campaigns)および[トランザクションメールCampaigns]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email)ではサポートされていません。
{% endalert %}

## ユーザー権限の設定 {#setting-user-permissions}

承認ワークフローを有効にした後、会社ユーザーがCampaignやCanvasを承認または拒否できるようにユーザー権限を設定する必要があります。両方の権限は、ワークスペースまたは[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)に適用したり、[権限セット]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#permission-sets)に追加したりすることもできます。

{% tabs %}
{% tab campaign %}
[「Approve and Deny Campaigns」権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#managing-limited-and-team-role-permissions)が必要です。この権限は、Campaignの承認ステータスを更新できるユーザーを制御します。この権限があると、以下のことが可能です。

- Campaignを自己承認する
- Campaignを承認して起動する
- Campaignを承認するが起動しない（「Send Campaigns, Canvases」権限を持つ別のユーザーがCampaignを起動できます）
- Campaignを承認も起動もしない

**Summary**ステップで承認ステータスが設定された後、Campaignに対するその後の変更は、保存時にすべての承認ステータスをリセットします。これは、下書きのCampaignまたは起動後のCampaignのいずれかで行われた変更に適用されます。たとえば、ターゲットオーディエンスのみを変更した場合でも、**Summary**ステップはすべてのセクションの承認ステータスをデフォルトの状態である**Pending Approval**に戻します。

{% endtab %}

{% tab canvas %}
[「Approve and Deny Canvases」権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#managing-limited-and-team-role-permissions)が必要です。この権限は、Canvasの承認ステータスを更新できるユーザーを制御します。この権限があると、以下のことが可能です。

- Canvasを自己承認する
- Canvasを承認して起動する
- Canvasを承認するが起動しない（「Send Campaigns, Canvases」権限を持つ別のユーザーがCanvasを起動できます）
- Canvasを承認も起動もしない

**Summary**ステップで承認ステータスが設定された後、Canvasに対するその後の変更は、保存時にすべての承認ステータスをリセットします。これは、下書きのCanvasまたは起動後のCanvasのいずれかで行われた変更に適用されます。たとえば、ターゲットオーディエンスのみを変更した場合でも、**Summary**ステップはすべてのセクションの承認ステータスをデフォルトの状態である**Pending Approval**に戻します。

{% alert note %}
**承認ステータスと保存**

- **Summary**ステップでセクションの**Approve**をクリックすると、その承認は即座に保存されます。
- **Save**ボタンは、Canvasのコンテンツと設定の変更を保存するものであり、承認ステータスを保存するものではありません。

承認を失わないようにするには:

1. 必要なCanvasの編集を行い、**Save**をクリックします。
2. Canvasの保存が完了した後、**Summary**ステップで該当するセクションを承認します。
3. 承認後にCanvasをさらに変更した場合のみ、再度**Save**をクリックします。Canvasを変更して保存すると、すべての承認ステータスが**Pending Approval**にリセットされます。
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
ライブのCampaignを編集するには、「Approve and Deny Campaigns」権限が必要です。Campaignの下書きバージョンはまだ利用できないため、ユーザーは自分の変更を承認する必要があります。Canvasの場合はこの限りではなく、ユーザーが変更を加えて下書きとして保存し、別のユーザーがCanvasを承認して起動できます。
{% endalert %}
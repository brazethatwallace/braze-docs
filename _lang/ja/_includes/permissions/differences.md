{% if include.content == "Differences" %}

[Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams)、[権限セット]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#creating-a-permission-set)、[ユーザーロール]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#creating-a-role)を使用して、Braze内での会社ユーザーのアクセスと責任を管理できます。各機能には、権限とアクセスコントロールの異なるコレクションが含まれています。

### 主な違い {#key-differences}

大まかに言えば、各機能にはそれぞれ異なるスコープがあります。
- 権限セットは、会社ユーザーがすべてのワークスペースで何ができるかをコントロールします。
- ロールは、会社ユーザーが特定のワークスペースで何ができるかをコントロールします。
- Teamsは、会社ユーザーがメッセージで到達できるオーディエンスをコントロールします。

| 機能 | できること | アクセス&nbsp;の&nbsp;範囲 |
| - | - | - |
| [権限セット]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#creating-a-permission-set) | 特定の分野やアクションに関連する権限（「開発者」や「マーケター」向けなど）をまとめ、異なるワークスペースで同じ権限を必要とする会社ユーザーに適用します。 | 全社 |
| [ロール]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#creating-a-role) | 個別のカスタム権限とワークスペースアクセスコントロールを組み合わせます（例：「マーケター - ファッションブランド」では、ユーザーはマーケターとしてのロールに関連する特定の権限を持ち、「ファッションブランド」ワークスペースに限定されます）。その後、会社ユーザーにロールを割り当て、関連する権限とワークスペースへのアクセスを直接付与します。<br><br>このレベルのアクセス権を持つユーザーは、通常、1つのダッシュボードに多数のブランドや地域別ワークスペースが存在する、より厳格にコントロールされた環境におけるマネージャーです。 | 特定のワークスペース |
| [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams#creating-teams) | 会社ユーザーのリソースへのアクセスを、オーディエンス（顧客基盤のロケーション、言語、カスタム属性など）に基づいて制限します。<br><br>このレベルのアクセス権を持つユーザーは、通常、担当するブランド内の特定の範囲に責任を持ちます。例えば、多言語ブランド向けに言語固有のコンテンツを作成するといった業務です。 | 特定のダッシュボード |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="主な違い" }

{% endif %}
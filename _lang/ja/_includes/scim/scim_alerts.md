{% comment %}
  SCIM integration alerts.
  Parameters:
  - alert (required): One of `one_integration`, `idp_integration`, or `custom_endpoint`
  - idp (required for `idp_integration`): IdP name, such as `Okta` or `Entra ID`
  - subject (optional for `custom_endpoint`): `endpoint` (default) or `endpoints`
{% endcomment %}

{% if include.alert == 'one_integration' %}

{% alert important %}
SCIM連携は1社につき1つのみ設定できます。IDプロバイダー（IdP）連携（OktaまたはEntra ID）を使用している場合、カスタムSCIM APIエンドポイントは使用できません。IdP連携ではユーザーアカウントの作成と削除が自動的に行われますが、権限やワークスペースの割り当ては管理されません。これらはBrazeダッシュボードで手動で設定する必要があります。
{% endalert %}

{% endif %}

{% if include.alert == 'idp_integration' %}

{% alert important %}
{{ include.idp }}連携では、ユーザーアカウントの作成と削除のみが行われます。権限の設定や特定のワークスペースへのユーザー割り当ては行われません。{{ include.idp }}を通じてユーザーがプロビジョニングされた後、Brazeダッシュボードでロールと権限を手動で更新する必要があります。また、{{ include.idp }}連携を使用している場合、カスタムSCIM APIエンドポイントは使用できません。SCIMブリッジは1社につき1つのみ設定できます。
{% endalert %}

{% endif %}

{% if include.alert == 'custom_endpoint' %}

{% alert important %}
{% if include.subject == 'endpoints' %}
これらのSCIM APIエンドポイントにはカスタムSCIM連携が必要です。IDプロバイダー（IdP）連携（OktaまたはEntra ID）を設定している場合、これらのエンドポイントは使用できません。SCIMブリッジは1社につき1つのみ設定できます。IdP連携ではユーザーアカウントの作成と削除が自動的に行われますが、権限やワークスペースの割り当ては管理されません。これらはBrazeダッシュボードで手動で設定する必要があります。
{% else %}
このエンドポイントにはカスタムSCIM連携が必要です。IDプロバイダー（IdP）連携（OktaまたはEntra ID）を設定している場合、このエンドポイントは使用できません。SCIMブリッジは1社につき1つのみ設定できます。
{% endif %}
{% endalert %}

{% endif %}
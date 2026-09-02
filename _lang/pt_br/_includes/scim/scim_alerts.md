{% comment %}
  SCIM integration alerts.
  Parameters:
  - alert (required): One of `one_integration`, `idp_integration`, or `custom_endpoint`
  - idp (required for `idp_integration`): IdP name, such as `Okta` or `Entra ID`
  - subject (optional for `custom_endpoint`): `endpoint` (default) or `endpoints`
{% endcomment %}

{% if include.alert == 'one_integration' %}

{% alert important %}
Você só pode configurar uma integração SCIM por empresa. Se você usa uma integração de provedor de identidade (IdP) (Okta ou Entra ID), não é possível usar os endpoints personalizados da API SCIM. As integrações de IdP criam e excluem contas de usuário automaticamente, mas não gerenciam permissões nem atribuições de espaço de trabalho. Você deve configurá-las manualmente no dashboard da Braze.
{% endalert %}

{% endif %}

{% if include.alert == 'idp_integration' %}

{% alert important %}
A integração com {{ include.idp }} apenas cria e exclui contas de usuário. Ela não define permissões nem atribui usuários a espaços de trabalho específicos. Depois que os usuários forem provisionados pelo {{ include.idp }}, você deve atualizar manualmente suas funções e permissões no dashboard da Braze. Além disso, não é possível usar os endpoints personalizados da API SCIM ao usar a integração com {{ include.idp }}; apenas uma ponte SCIM pode ser configurada por empresa.
{% endalert %}

{% endif %}

{% if include.alert == 'custom_endpoint' %}

{% alert important %}
{% if include.subject == 'endpoints' %}
Esses endpoints da API SCIM exigem a integração SCIM personalizada. Se você configurou uma integração de provedor de identidade (IdP) (Okta ou Entra ID), não é possível usar esses endpoints; apenas uma ponte SCIM pode ser configurada por empresa. As integrações de IdP criam e excluem contas de usuário automaticamente, mas não gerenciam permissões nem atribuições de espaço de trabalho. Você deve configurá-las manualmente no dashboard da Braze.
{% else %}
Esse endpoint exige a integração SCIM personalizada. Se você configurou uma integração de provedor de identidade (IdP) (Okta ou Entra ID), não é possível usar esse endpoint; apenas uma ponte SCIM pode ser configurada por empresa.
{% endif %}
{% endalert %}

{% endif %}
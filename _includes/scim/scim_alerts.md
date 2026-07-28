{% comment %}
  SCIM integration alerts.
  Parameters:
  - alert (required): One of `one_integration`, `idp_integration`, or `custom_endpoint`
  - idp (required for `idp_integration`): IdP name, such as `Okta` or `Entra ID`
  - subject (optional for `custom_endpoint`): `endpoint` (default) or `endpoints`
{% endcomment %}

{% if include.alert == 'one_integration' %}

{% alert important %}
You can only set up one SCIM integration per company. If you use an identity provider (IdP) integration (Okta or Entra ID), you can't use the custom SCIM API endpoints. The IdP integrations create and delete user accounts automatically but don't manage permissions or workspace assignments. You must set those manually in the Braze dashboard.
{% endalert %}

{% endif %}

{% if include.alert == 'idp_integration' %}

{% alert important %}
The {{ include.idp }} integration only creates and deletes user accounts. It doesn't set permissions or assign users to specific workspaces. After users are provisioned through {{ include.idp }}, you must manually update their roles and permissions in the Braze dashboard. Additionally, you can't use the custom SCIM API endpoints when using the {{ include.idp }} integration; only one SCIM bridge can be set up per company.
{% endalert %}

{% endif %}

{% if include.alert == 'custom_endpoint' %}

{% alert important %}
{% if include.subject == 'endpoints' %}
These SCIM API endpoints require the custom SCIM integration. If you set up an identity provider (IdP) integration (Okta or Entra ID), you can't use these endpoints; only one SCIM bridge can be set up per company. The IdP integrations create and delete user accounts automatically but don't manage permissions or workspace assignments. You must set those manually in the Braze dashboard.
{% else %}
This endpoint requires the custom SCIM integration. If you set up an identity provider (IdP) integration (Okta or Entra ID), you can't use this endpoint; only one SCIM bridge can be set up per company.
{% endif %}
{% endalert %}

{% endif %}

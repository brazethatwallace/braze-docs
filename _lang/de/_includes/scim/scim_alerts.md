{% comment %}
  SCIM integration alerts.
  Parameters:
  - alert (required): One of `one_integration`, `idp_integration`, or `custom_endpoint`
  - idp (required for `idp_integration`): IdP name, such as `Okta` or `Entra ID`
  - subject (optional for `custom_endpoint`): `endpoint` (default) or `endpoints`
{% endcomment %}

{% if include.alert == 'one_integration' %}

{% alert important %}
Sie können pro Unternehmen nur eine SCIM-Integration einrichten. Wenn Sie eine Identity-Provider-Integration (IdP) verwenden (Okta oder Entra ID), können Sie die angepassten SCIM-API-Endpunkte nicht nutzen. Die IdP-Integrationen erstellen und löschen Nutzer:innenkonten automatisch, verwalten jedoch keine Berechtigungen oder Workspace-Zuweisungen. Diese müssen Sie manuell im Braze-Dashboard festlegen.
{% endalert %}

{% endif %}

{% if include.alert == 'idp_integration' %}

{% alert important %}
Die {{ include.idp }}-Integration erstellt und löscht nur Nutzer:innenkonten. Sie legt keine Berechtigungen fest und weist Nutzer:innen keinen bestimmten Workspaces zu. Nachdem Nutzer:innen über {{ include.idp }} bereitgestellt wurden, müssen Sie deren Rollen und Berechtigungen manuell im Braze-Dashboard aktualisieren. Darüber hinaus können Sie die angepassten SCIM-API-Endpunkte nicht verwenden, wenn Sie die {{ include.idp }}-Integration nutzen. Pro Unternehmen kann nur eine SCIM-Bridge eingerichtet werden.
{% endalert %}

{% endif %}

{% if include.alert == 'custom_endpoint' %}

{% alert important %}
{% if include.subject == 'endpoints' %}
Diese SCIM-API-Endpunkte erfordern die angepasste SCIM-Integration. Wenn Sie eine Identity-Provider-Integration (IdP) eingerichtet haben (Okta oder Entra ID), können Sie diese Endpunkte nicht verwenden. Pro Unternehmen kann nur eine SCIM-Bridge eingerichtet werden. Die IdP-Integrationen erstellen und löschen Nutzer:innenkonten automatisch, verwalten jedoch keine Berechtigungen oder Workspace-Zuweisungen. Diese müssen Sie manuell im Braze-Dashboard festlegen.
{% else %}
Dieser Endpunkt erfordert die angepasste SCIM-Integration. Wenn Sie eine Identity-Provider-Integration (IdP) eingerichtet haben (Okta oder Entra ID), können Sie diesen Endpunkt nicht verwenden. Pro Unternehmen kann nur eine SCIM-Bridge eingerichtet werden.
{% endif %}
{% endalert %}

{% endif %}
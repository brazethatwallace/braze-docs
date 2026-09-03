{% comment %}
  SCIM integration alerts.
  Parameters:
  - alert (required): One of `one_integration`, `idp_integration`, or `custom_endpoint`
  - idp (required for `idp_integration`): IdP name, such as `Okta` or `Entra ID`
  - subject (optional for `custom_endpoint`): `endpoint` (default) or `endpoints`
{% endcomment %}

{% if include.alert == 'one_integration' %}

{% alert important %}
Solo puedes configurar una integración SCIM por empresa. Si usas una integración de proveedor de identidad (IdP) (Okta o Entra ID), no puedes usar los endpoints personalizados de la API de SCIM. Las integraciones de IdP crean y eliminan cuentas de usuario automáticamente, pero no gestionan permisos ni asignaciones de espacios de trabajo. Debes configurarlos manualmente en el panel de Braze.
{% endalert %}

{% endif %}

{% if include.alert == 'idp_integration' %}

{% alert important %}
La integración de {{ include.idp }} solo crea y elimina cuentas de usuario. No establece permisos ni asigna usuarios a espacios de trabajo específicos. Después de que los usuarios se aprovisionen a través de {{ include.idp }}, debes actualizar manualmente sus roles y permisos en el panel de Braze. Además, no puedes usar los endpoints personalizados de la API de SCIM cuando usas la integración de {{ include.idp }}; solo se puede configurar un puente SCIM por empresa.
{% endalert %}

{% endif %}

{% if include.alert == 'custom_endpoint' %}

{% alert important %}
{% if include.subject == 'endpoints' %}
Estos endpoints de la API de SCIM requieren la integración SCIM personalizada. Si configuraste una integración de proveedor de identidad (IdP) (Okta o Entra ID), no puedes usar estos endpoints; solo se puede configurar un puente SCIM por empresa. Las integraciones de IdP crean y eliminan cuentas de usuario automáticamente, pero no gestionan permisos ni asignaciones de espacios de trabajo. Debes configurarlos manualmente en el panel de Braze.
{% else %}
Este endpoint requiere la integración SCIM personalizada. Si configuraste una integración de proveedor de identidad (IdP) (Okta o Entra ID), no puedes usar este endpoint; solo se puede configurar un puente SCIM por empresa.
{% endif %}
{% endalert %}

{% endif %}
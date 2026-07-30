{% comment %}
  SCIM integration alerts.
  Parameters:
  - alert (required): One of `one_integration`, `idp_integration`, or `custom_endpoint`
  - idp (required for `idp_integration`): IdP name, such as `Okta` or `Entra ID`
  - subject (optional for `custom_endpoint`): `endpoint` (default) or `endpoints`
{% endcomment %}

{% if include.alert == 'one_integration' %}

{% alert important %}
회사당 하나의 SCIM 통합만 설정할 수 있습니다. ID 공급자(IdP) 통합(Okta 또는 Entra ID)을 사용하는 경우 커스텀 SCIM API 엔드포인트를 사용할 수 없습니다. IdP 통합은 사용자 계정을 자동으로 생성 및 삭제하지만 권한이나 워크스페이스 할당은 관리하지 않습니다. 이러한 설정은 Braze 대시보드에서 수동으로 지정해야 합니다.
{% endalert %}

{% endif %}

{% if include.alert == 'idp_integration' %}

{% alert important %}
{{ include.idp }} 통합은 사용자 계정의 생성 및 삭제만 수행합니다. 권한을 설정하거나 사용자를 특정 워크스페이스에 할당하지는 않습니다. {{ include.idp }}를 통해 사용자가 프로비저닝된 후에는 Braze 대시보드에서 역할과 권한을 수동으로 업데이트해야 합니다. 또한 {{ include.idp }} 통합을 사용하는 경우 커스텀 SCIM API 엔드포인트를 사용할 수 없습니다. 회사당 하나의 SCIM 브리지만 설정할 수 있습니다.
{% endalert %}

{% endif %}

{% if include.alert == 'custom_endpoint' %}

{% alert important %}
{% if include.subject == 'endpoints' %}
이 SCIM API 엔드포인트는 커스텀 SCIM 통합이 필요합니다. ID 공급자(IdP) 통합(Okta 또는 Entra ID)을 설정한 경우 이 엔드포인트를 사용할 수 없습니다. 회사당 하나의 SCIM 브리지만 설정할 수 있습니다. IdP 통합은 사용자 계정을 자동으로 생성 및 삭제하지만 권한이나 워크스페이스 할당은 관리하지 않습니다. 이러한 설정은 Braze 대시보드에서 수동으로 지정해야 합니다.
{% else %}
이 엔드포인트는 커스텀 SCIM 통합이 필요합니다. ID 공급자(IdP) 통합(Okta 또는 Entra ID)을 설정한 경우 이 엔드포인트를 사용할 수 없습니다. 회사당 하나의 SCIM 브리지만 설정할 수 있습니다.
{% endif %}
{% endalert %}

{% endif %}
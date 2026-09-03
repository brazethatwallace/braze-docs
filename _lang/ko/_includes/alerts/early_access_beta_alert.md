{% comment %}
  조기 액세스 또는 베타 알림입니다. 조기 액세스 또는 베타 단계의 기능/엔드포인트에 사용합니다.
  매개변수:
  - feature(필수): 기능 또는 주제, 예: "이 엔드포인트", "SCIM 프로비저닝", "Okta 통합"
  - type(선택 사항): "early_access"(기본값) 또는 "beta"
  - contact(선택 사항): 연락할 담당자, 예: "Braze 계정 매니저"(기본값) 또는 "고객 성공 매니저"
{% endcomment %}
{% assign contact_role = include.contact | default: "Braze account 매니저" %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }}은(는) 현재 베타 단계입니다. 베타 참여에 관심이 있으시면 {{ contact_role }}에게 문의하세요.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }}은(는) 현재 조기 액세스 단계입니다. 조기 액세스 참여에 관심이 있으시면 {{ contact_role }}에게 문의하세요.
{% endalert %}
{% endif %}
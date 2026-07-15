{% comment %}
  Alerta de acesso antecipado ou beta. Use para recursos/endpoints em acesso antecipado ou beta.
  Parâmetros:
  - feature (obrigatório): O recurso ou assunto, por exemplo, "This endpoint", "SCIM provisioning", "The Okta integration"
  - type (opcional): "early_access" (padrão) ou "beta"
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} está atualmente em beta. Fale com o gerente da sua conta da Braze se tiver interesse em participar da versão beta.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} está atualmente em acesso antecipado. Fale com o gerente da sua conta da Braze se tiver interesse em participar do acesso antecipado.
{% endalert %}
{% endif %}
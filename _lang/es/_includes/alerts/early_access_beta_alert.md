{% comment %}
  Alerta de acceso anticipado o beta. Úsalo para características/endpoints en acceso anticipado o beta.
  Parámetros:
  - feature (obligatorio): La característica o el tema, p. ej., «Este endpoint», «Aprovisionamiento de SCIM», «La integración de Okta»
  - type (opcional): "early_access" (predeterminado) o "beta"
  - contact (opcional): Con quién contactar, p. ej., "director de cuentas de Braze" (predeterminado) o "administrador de éxito de cliente"
{% endcomment %}
{% assign contact_role = include.contact | default: "Braze account manager" %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} se encuentra actualmente en fase beta. Ponte en contacto con tu {{ contact_role }} si te interesa participar en la beta.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} se encuentra actualmente en fase de acceso anticipado. Ponte en contacto con tu {{ contact_role }} si te interesa participar en el acceso anticipado.
{% endalert %}
{% endif %}
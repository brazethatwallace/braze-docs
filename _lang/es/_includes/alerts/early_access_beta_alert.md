{% comment %}
  Alerta de acceso anticipado o beta. Úsalo para características/puntos finales en acceso anticipado o beta.
  Parámetros:
  - feature (obligatoria): La característica o el tema, p. ej., «Este punto final», «Aprovisionamiento de SCIM», «La integración de Okta»
  - type (opcional): "early_access" (predeterminado) o "beta"
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} se encuentra actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en la beta.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} se encuentra actualmente en fase de acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en el acceso anticipado.
{% endalert %}
{% endif %}
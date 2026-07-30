{% comment %}
  Early access or beta alert. Use for features/endpoints in early access or beta.
  Parameters:
  - feature (required): The feature or subject, e.g. "This endpoint", "SCIM provisioning", "The Okta integration"
  - type (optional): "early_access" (default) or "beta"
  - contact (optional): Who to contact, e.g. "Braze account manager" (default) or "customer success manager"
{% endcomment %}
{% assign contact_role = include.contact | default: "Braze account manager" %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} is currently in beta. Contact your {{ contact_role }} if you're interested in participating in the beta.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} is currently in early access. Contact your {{ contact_role }} if you're interested in participating in the early access.
{% endalert %}
{% endif %}

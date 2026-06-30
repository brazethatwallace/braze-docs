{% comment %}
  Frühzeitiger Zugang oder Beta-Benachrichtigung. Verwenden Sie dies für Features/Endpunkte im Early Access oder in der Beta-Phase.
  Parameter:
  - feature (erforderlich): Das Feature oder Thema, z. B. „Dieser Endpunkt“, „SCIM-Bereitstellung“, „Die Okta-Integration“
  - type (optional): „early_access“ (Standard) oder „beta“
{% endcomment %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} befindet sich derzeit in der Beta-Phase. Kontaktieren Sie Ihre:n Braze Account Manager:in, wenn Sie an der Teilnahme an der Beta interessiert sind.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} befindet sich derzeit im Early Access. Kontaktieren Sie Ihre:n Braze Account Manager:in, wenn Sie an der Teilnahme am Early Access interessiert sind.
{% endalert %}
{% endif %}
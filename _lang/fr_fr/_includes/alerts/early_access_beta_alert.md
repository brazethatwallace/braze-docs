{% comment %}
  Alerte d'accès anticipé ou de version bêta. À utiliser pour les fonctionnalités/endpoints en accès anticipé ou en version bêta.
  Paramètres :
  - feature (requis) : La fonctionnalité ou le sujet, par ex. « Ce endpoint », « Le provisionnement SCIM », « L'intégration Okta »
  - type (facultatif) : "early_access" (par défaut) ou "beta"
  - contact (facultatif) : La personne à contacter, par ex. "Braze account gestionnaire" (par défaut) ou "CSM or gestionnaire de la satisfaction client or gestionnaire du succès des clients or gestionnaire de la satisfaction client or gestionnaire du succès des clients"
{% endcomment %}
{% assign contact_role = include.contact | default: "Braze account gestionnaire" %}
{% if include.type == "beta" %}
{% alert important %}
{{ include.feature }} est actuellement en version bêta. Contactez votre {{ contact_role }} si vous souhaitez participer à la bêta.
{% endalert %}
{% else %}
{% alert important %}
{{ include.feature }} est actuellement en accès anticipé. Contactez votre {{ contact_role }} si vous souhaitez participer à l'accès anticipé.
{% endalert %}
{% endif %}
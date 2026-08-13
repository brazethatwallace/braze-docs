{% comment %}
  SCIM integration alerts.
  Parameters:
  - alert (required): One of `one_integration`, `idp_integration`, or `custom_endpoint`
  - idp (required for `idp_integration`): IdP name, such as `Okta` or `Entra ID`
  - subject (optional for `custom_endpoint`): `endpoint` (default) or `endpoints`
{% endcomment %}

{% if include.alert == 'one_integration' %}

{% alert important %}
Vous ne pouvez configurer qu'une seule intégration SCIM par entreprise. Si vous utilisez une intégration de fournisseur d'identité (IdP) (Okta ou Entra ID), vous ne pouvez pas utiliser les endpoints personnalisés de l'API SCIM. Les intégrations IdP créent et suppriment automatiquement les comptes utilisateurs, mais ne gèrent pas les permissions ni les affectations aux espaces de travail. Vous devez les configurer manuellement dans le tableau de bord de Braze.
{% endalert %}

{% endif %}

{% if include.alert == 'idp_integration' %}

{% alert important %}
L'intégration {{ include.idp }} crée et supprime uniquement les comptes utilisateurs. Elle ne définit pas les permissions et n'affecte pas les utilisateurs à des espaces de travail spécifiques. Une fois les utilisateurs provisionnés via {{ include.idp }}, vous devez mettre à jour manuellement leurs rôles et permissions dans le tableau de bord de Braze. De plus, vous ne pouvez pas utiliser les endpoints personnalisés de l'API SCIM lorsque vous utilisez l'intégration {{ include.idp }} ; une seule passerelle SCIM peut être configurée par entreprise.
{% endalert %}

{% endif %}

{% if include.alert == 'custom_endpoint' %}

{% alert important %}
{% if include.subject == 'endpoints' %}
Ces endpoints de l'API SCIM nécessitent l'intégration SCIM personnalisée. Si vous avez configuré une intégration de fournisseur d'identité (IdP) (Okta ou Entra ID), vous ne pouvez pas utiliser ces endpoints ; une seule passerelle SCIM peut être configurée par entreprise. Les intégrations IdP créent et suppriment automatiquement les comptes utilisateurs, mais ne gèrent pas les permissions ni les affectations aux espaces de travail. Vous devez les configurer manuellement dans le tableau de bord de Braze.
{% else %}
Cet endpoint nécessite l'intégration SCIM personnalisée. Si vous avez configuré une intégration de fournisseur d'identité (IdP) (Okta ou Entra ID), vous ne pouvez pas utiliser cet endpoint ; une seule passerelle SCIM peut être configurée par entreprise.
{% endif %}
{% endalert %}

{% endif %}
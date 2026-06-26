---
article_title: Limites de débit de l'espace de travail
description: "Découvrez comment définir des limites de débit pour les espaces de travail, afin de contrôler la répartition de la limite de débit globale de l'API de votre société entre les différents espaces de travail, empêchant ainsi une seule intégration ou équipe d'envoyer trop de demandes à un endpoint spécifique."
permalink: /workspace_rate_limits/
---

# Limites de débit de l'espace de travail {#workspace-rate-limits}

> Découvrez comment définir des limites de débit pour les espaces de travail, afin de contrôler la répartition de la limite de débit globale de l'API de votre société entre les différents espaces de travail, empêchant ainsi une seule intégration ou équipe d'envoyer trop de demandes à un endpoint spécifique.

## Conditions préalables {#prerequisites}

Les limites de débit de l'espace de travail sont uniquement disponibles pour les contrats Braze sans points de donnée. De plus, vous aurez besoin des [autorisations d'administrateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) pour gérer les limites de débit.

## À propos des limites de débit de l'espace de travail {#about-workspace-rate-limits}

Par défaut, les limites de débit au niveau de la société sont partagées entre vos espaces de travail.

Avec les limites de débit de l'espace de travail, vous pouvez définir un nombre maximal de demandes API qu'un espace de travail peut envoyer à un endpoint d'ingestion spécifique, tel que `/users/track` ou les données SDK. Vous pouvez également appliquer des limites de débit à un groupe d'espaces de travail, ce qui signifie que la limite est partagée entre tous les espaces de travail de ce groupe.

Par exemple, si votre endpoint `/users/track` a une limite de débit au niveau de la société de 500 000 demandes par heure, vous pourriez définir les limites de débit d'espace de travail suivantes :

- Une limite de débit de 10 000 demandes par heure appliquée à l'_Espace de travail 1_
- Une limite de débit partagée de 200 000 demandes par heure appliquée à l'_Espace de travail 2_ et à l'_Espace de travail 3_
- Aucune limite de débit appliquée à l'_Espace de travail 4_, ce qui signifie que la limite de débit par défaut au niveau de la société est utilisée

## Gérer les limites de débit de l'espace de travail {#managing-workspace-rate-limits}

### Affecter une limite {#assigning-a-limit}

Pour affecter une nouvelle limite de débit à un ou plusieurs espaces de travail, accédez à **Paramètres** > **Paramètres d'administration** > **Limites de débit de l'espace de travail**, puis sélectionnez **Affecter des limites de débit**.

![La page « Limites de débit de l'espace de travail » dans le tableau de bord de Braze.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/settings.png %}){: style="max-width:85%;"}

Ensuite, choisissez un endpoint et un ou plusieurs espaces de travail, puis saisissez votre limite de débit. La limite peut être n'importe quel nombre entier supérieur à 1 000 et ne dépassant pas votre limite de débit au niveau de la société.

Lorsque vous avez terminé, sélectionnez **Mettre à jour la limite de débit**.

![La fenêtre contextuelle « Limite de débit » avec des options pour choisir un endpoint, des espaces de travail et une limite de débit.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/update_rate_limit.png %}){: style="max-width:45%;"}

{% alert note %}
Si vous choisissez plus d'un espace de travail, la limite de débit sera partagée entre ce groupe d'espaces de travail.
{% endalert %}

### Modifier une limite {#editing-a-limit}

Pour modifier une limite de débit d'espace de travail existante, accédez à **Paramètres** > **Paramètres d'administration** > **Limites de débit de l'espace de travail**, puis sélectionnez les <i class="fas fa-ellipsis-vertical" aria-label="Points de suspension verticaux"></i> points de suspension verticaux et choisissez **Modifier**. Votre nouvelle limite de débit peut prendre effet en quelques minutes.

### Réinitialiser une limite {#resetting-a-limit}

Pour réinitialiser une limite de débit existante afin qu'elle revienne à votre limite de débit au niveau de la société, accédez à **Paramètres** > **Paramètres d'administration** > **Limites de débit de l'espace de travail**, puis sélectionnez les <i class="fas fa-ellipsis-vertical" aria-label="Points de suspension verticaux"></i> points de suspension verticaux et choisissez **Réinitialiser**.

## Surveiller l'utilisation {#monitoring-usage}

### En-têtes de réponse {#response-headers}

Par défaut, toutes les réponses d'ingestion incluent les en-têtes suivants, qui reflètent votre limite de débit stable au niveau de la société.

Nous vous recommandons d'utiliser ces en-têtes dans votre logique d'intégration pour gérer efficacement les limites de débit. Par exemple, vous pouvez réduire le volume de demandes à mesure que vous approchez de ces limites et utiliser l'en-tête `Retry-After` pour déterminer quand réessayer.

| Nom de l'en-tête | Description |
| ----- | ----- |
| `X-RateLimit-Limit` | Le nombre maximal de demandes autorisées dans la fenêtre de limite de débit actuelle. |
| `X-RateLimit-Remaining` | Le nombre de demandes restantes dans la fenêtre actuelle. |
| `X-RateLimit-Reset` | Le moment où la fenêtre de limite de débit actuelle se réinitialise (secondes epoch UTC). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Codes d'erreur {#error-codes}

Si une limite de débit d'espace de travail est atteinte, votre demande renverra un code de réponse `429` et les en-têtes incluront une valeur `Retry-After`. Celle-ci représente le nombre de secondes avant la réinitialisation de la limite de débit.

La valeur `Retry-After` reflète le nombre de secondes avant le début de l'heure suivante, lorsque la limite de débit de l'espace de travail se réinitialise.

### Tableau de bord d'utilisation de l'API {#api-usage-dashboard}

Pour surveiller le volume de demandes, les codes de réponse et le comportement d'ingestion entre les espaces de travail, vous pouvez également utiliser le [tableau de bord d'utilisation de l'API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/).

Vous pouvez filtrer le tableau de bord pour afficher `429 Workspace Rate Limited` ou `429 Company Rate Limited`, afin d'identifier rapidement si une demande a été limitée par la limite de débit de la société ou de l'espace de travail.
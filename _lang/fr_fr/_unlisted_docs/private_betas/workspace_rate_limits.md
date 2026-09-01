---
article_title: Limites de débit de l'espace de travail
description: "Découvrez comment définir des limites de débit pour les espaces de travail, afin de contrôler la répartition de la limite de débit globale de l'API de votre société entre les différents espaces de travail, empêchant ainsi une seule intégration ou équipe d'envoyer trop de demandes à un endpoint spécifique."
permalink: /workspace_rate_limits/
---

# Limites de débit de l'espace de travail {#workspace-rate-limits}

> Découvrez comment définir des limites de débit pour les espaces de travail, afin de contrôler la répartition de la limite de débit globale de l'API de votre société entre les différents espaces de travail, empêchant ainsi une seule intégration ou équipe d'envoyer trop de demandes à un endpoint spécifique.

## Prérequis {#prerequisites}

Les limites de débit de l'espace de travail sont uniquement disponibles pour les contrats Braze sans points de données. De plus, vous aurez besoin des [permissions d'administrateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) pour gérer les limites de débit.

## À propos des limites de débit par espace de travail {#about-workspace-rate-limits}

Par défaut, les limites de débit au niveau de l'entreprise sont partagées entre vos espaces de travail.

Avec les limites de débit par espace de travail, vous pouvez définir un nombre maximum de requêtes API qu'un espace de travail peut effectuer vers un endpoint d'ingestion spécifique, tel que `/users/track` ou les données SDK. Vous pouvez également appliquer des limites de débit à un groupe d'espaces de travail, ce qui signifie que la limite est partagée entre tous les espaces de travail de ce groupe.

Par exemple, si votre endpoint `/users/track` a une limite de débit au niveau de l'entreprise de 500 000 requêtes par heure, vous pourriez définir les limites de débit suivantes par espace de travail :

- Une limite de débit de 10 000 requêtes par heure appliquée à l'_Espace de travail 1_
- Une limite de débit partagée de 200 000 requêtes par heure appliquée à l'_Espace de travail 2_ et à l'_Espace de travail 3_
- Aucune limite de débit appliquée à l'_Espace de travail 4_, ce qui signifie que la limite de débit par défaut au niveau de l'entreprise est utilisée

## Gérer les limites de débit des espaces de travail {#managing-workspace-rate-limits}

### Attribuer une limite {#assigning-a-limit}

Pour attribuer une nouvelle limite de débit à un ou plusieurs espaces de travail, accédez à **Paramètres** > **Paramètres d'administration** > **Limites de débit des espaces de travail**, puis sélectionnez **Attribuer des limites de débit**.

![La page « Limites de débit des espaces de travail » dans le tableau de bord de Braze.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/settings.png %}){: style="max-width:85%;"}

Ensuite, choisissez un endpoint et un ou plusieurs espaces de travail, puis saisissez votre limite de débit. La limite peut être n'importe quel nombre entier supérieur à 1 000 qui ne dépasse pas la limite de débit de votre entreprise.

Lorsque vous avez terminé, sélectionnez **Mettre à jour la limite de débit**.

![La fenêtre contextuelle « Limite de débit » avec des options pour choisir un endpoint, des espaces de travail et une limite de débit.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/update_rate_limit.png %}){: style="max-width:45%;"}

{% alert note %}
Si vous choisissez plusieurs espaces de travail, la limite de débit sera partagée entre ce groupe d'espaces de travail.
{% endalert %}

### Modifier une limite {#editing-a-limit}

Pour modifier une limite de débit d'espace de travail existante, accédez à **Paramètres** > **Paramètres d'administration** > **Limites de débit des espaces de travail**, puis sélectionnez les <i class="fas fa-ellipsis-vertical" aria-label="Ouvrir le menu d'options"></i> points de suspension verticaux et choisissez **Modifier**. Votre nouvelle limite de débit peut prendre effet en quelques minutes.

### Réinitialiser une limite {#resetting-a-limit}

Pour réinitialiser une limite de débit existante afin qu'elle revienne à la limite de débit de votre entreprise, accédez à **Paramètres** > **Paramètres d'administration** > **Limites de débit des espaces de travail**, puis sélectionnez les <i class="fas fa-ellipsis-vertical" aria-label="Ouvrir le menu d'options"></i> points de suspension verticaux et choisissez **Réinitialiser**.

## Surveillance de l'utilisation {#monitoring-usage}

### En-têtes de réponse {#response-headers}

Par défaut, toutes les réponses d'ingestion incluent les en-têtes suivants, qui reflètent votre limite de débit stable au niveau de l'entreprise.

Nous vous recommandons d'utiliser ces en-têtes dans votre logique d'intégration pour gérer efficacement les limites de débit. Par exemple, vous pouvez réduire le volume de requêtes à mesure que vous approchez ces limites et utiliser l'en-tête `Retry-After` pour déterminer quand relancer une requête.

| Nom de l'en-tête | Description |
| ----- | ----- |
| `X-RateLimit-Limit` | Le nombre maximum de requêtes autorisées dans la fenêtre de limitation de débit en cours. |
| `X-RateLimit-Remaining` | Le nombre de requêtes restantes dans la fenêtre en cours. |
| `X-RateLimit-Reset` | Le moment où la fenêtre de limitation de débit en cours est réinitialisée (secondes epoch UTC). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Codes d'erreur {#error-codes}

Si la limite de débit d'un espace de travail est atteinte, votre requête renverra un code de réponse `429` et les en-têtes incluront une valeur `Retry-After`. Celle-ci représente le nombre de secondes avant la réinitialisation de la limite de débit.

La valeur `Retry-After` reflète le nombre de secondes avant le début de l'heure suivante, lorsque la limite de débit de l'espace de travail est réinitialisée.

### Tableau de bord d'utilisation de l'API {#api-usage-dashboard}

Pour surveiller le volume de requêtes, les codes de réponse et le comportement d'ingestion à travers les espaces de travail, vous pouvez également utiliser le [tableau de bord d'utilisation de l'API]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage).

Vous pouvez filtrer le tableau de bord pour afficher `429 Workspace Rate Limited` ou `429 Company Rate Limited`, afin d'identifier rapidement si une requête a été limitée par la limite de débit de l'entreprise ou de l'espace de travail.
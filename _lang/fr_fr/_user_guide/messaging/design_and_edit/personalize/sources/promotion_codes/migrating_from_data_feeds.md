---
nav_title: Migrer depuis les flux de données
article_title: Migrer des flux de données vers les codes de promotion
page_order: 10
description: "Cet article de référence fournit des conseils pour migrer des flux de données vers les codes de promotion."
---

# Migrer des flux de données vers les codes de promotion {#migrate-from-data-feeds-to-promotion-codes}

> Cette page vous guide dans la migration des flux de données vers les codes de promotion. Il s'agit d'un processus simple qui consiste à créer manuellement des listes de codes de promotion à partir des informations de vos flux de données, puis à mettre à jour les références dans vos messages en conséquence.

{% alert note %}
Les flux de données sont en cours de dépréciation. Braze recommande aux clients qui utilisent les flux de données de passer aux listes de codes de promotion.
{% endalert %}

## Fonctionnalités {#features-and-functionality}

Il existe quelques différences entre les listes de codes de promotion et les flux de données.

| Fonctionnalité    | Codes de promotion | Flux de données  |
|-------------------|--------------------|-----------------|
| Descriptions      | Oui                | Non             |
| Dates d'expiration | Oui               | Non             |
| Méthode de création | Import d'un CSV  | Collage de texte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fonctionnalités" }

## Comment migrer {#how-to-migrate}

Pour remplacer un flux de données par une liste de codes de promotion, procédez comme suit :

1. Accédez à **Paramètres des données** et sélectionnez **Créer une liste de codes de promotion**.
2. [Configurez votre liste de codes de promotion]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/).
3. Accédez aux messages qui faisaient précédemment référence au flux de données et mettez-les à jour pour utiliser la liste de codes de promotion.
---
nav_title: Bonnes pratiques de remplissage rétrospectif
article_title: Bonnes pratiques de remplissage rétrospectif
page_order: 7
page_type: reference
description: "Découvrez comment remplir correctement les données historiques pour BrazeAI Decisioning Studio, y compris les exigences, les pièges courants et comment éviter les problèmes de qualité des données qui affectent les performances du modèle d'IA."
---

# Bonnes pratiques de remplissage rétrospectif {#backfill-best-practices}

> Pour diverses raisons, il peut être nécessaire de procéder à un remplissage rétrospectif des données, que ce soit en raison d'erreurs de données, de nouvelles informations (comme de nouvelles fonctionnalités) ou de la réconciliation de données entre deux systèmes. Lorsqu'un remplissage rétrospectif est effectué, suivez les principes de cet article pour maintenir la qualité des données et les performances du modèle.

## Quand le remplissage rétrospectif est nécessaire {#when-backfilling-is-needed}

Le remplissage rétrospectif est le processus de peuplement rétroactif d'un jeu de données avec des données historiques. Les scénarios courants incluent :

| Scénario | Description | Exemple |
|----------|-------------|---------|
| **Nouvelles fonctionnalités** | Vous avez identifié un nouvel indicateur important pour votre modèle, et vous disposez des journaux historiques bruts pour le calculer. | Vous ajoutez le « taux de clics » comme fonctionnalité et avez besoin de trois mois d'historique pour que le modèle dispose de suffisamment de données pour apprendre. |
| **Récupération de données** | Votre pipeline de données a échoué certains jours, créant des lacunes dans les données transmises à Decisioning Studio. | Une panne du pipeline mardi a laissé un vide. Après le déploiement du correctif, vous remplissez rétrospectivement ces enregistrements manquants depuis le système source. |
| **Changements de logique** | Vous avez mis à jour la formule de calcul d'une fonctionnalité ou modifié la définition d'un événement. | Vous avez redéfini « utilisateur actif » et devez réexporter les données historiques pour que le modèle s'entraîne sur la définition mise à jour. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="When backfilling is needed" }

## Exigences {#requirements}

Pour que Decisioning Studio fonctionne correctement, toutes les données entrantes doivent prendre en charge le remplissage rétrospectif pour les périodes historiques. La fenêtre de rétrospection spécifique requise (mesurée en mois) dépend des exigences d'entraînement du modèle d'IA. Consultez votre équipe AI Decisioning Services pour confirmer la valeur correcte pour votre cas d'utilisation.

Lors d'un remplissage rétrospectif historique, les normes suivantes sont obligatoires :

- **Cohérence du processus :** les instantanés historiques des fonctionnalités doivent être générés à l'aide d'un processus entièrement cohérent avec la création des instantanés en production. Si votre pipeline en production applique des transformations, des agrégations ou des filtres, ces mêmes étapes doivent être appliquées aux données remplies rétrospectivement.
- **Cohérence du schéma :** le schéma des données remplies rétrospectivement doit correspondre précisément au pipeline quotidien normal, y compris les mêmes champs, types de données et conventions de nommage des colonnes.

## Pièges courants {#common-pitfalls}

### Fuite de données (biais d'anticipation) {#data-leakage-look-ahead-bias}

La fuite de données est l'erreur de remplissage rétrospectif la plus critique. Elle se produit lorsque le processus de remplissage incorpore par inadvertance des informations qui n'auraient pas été disponibles au moment où l'enregistrement historique a été généré.

#### Pourquoi c'est important {#why-it-matters}

Si le modèle s'entraîne sur des données qui « connaissent l'avenir », il semblera bien fonctionner pendant l'entraînement mais produira de mauvais résultats en production, car les décisions en temps réel n'ont pas accès aux données futures.

Par exemple, considérez le calcul d'une fonctionnalité historique de « valeur vie client » en utilisant les dépenses totales d'un client à ce jour (c'est-à-dire jusqu'à aujourd'hui), puis l'utilisation de cette valeur pour prédire un comportement survenu il y a plusieurs mois. Au moment de cet événement historique, la valeur vie client complète n'était pas encore connue.

Ce problème peut être évité en reconstruisant toujours les fonctionnalités historiques en utilisant uniquement les informations qui auraient été disponibles à l'horodatage historique, et non les informations accumulées par la suite.

### Dérive du schéma et de la logique {#schema-and-logic-drift}

Les structures de données et les définitions métier évoluent au fil du temps. Les incohérences entre les données historiques et les données en production peuvent dégrader silencieusement la qualité du modèle.

- **Dérive du schéma :** si un champ (par exemple, `zip_code`) a été ajouté récemment à votre base de données, les enregistrements remplis rétrospectivement antérieurs à ce changement contiendront des valeurs nulles pour ce champ. Assurez-vous que votre pipeline gère correctement les champs manquants et que le modèle ne dépend pas excessivement de champs ayant une couverture historique limitée.
- **Dérive de la logique :** si la définition d'un indicateur a changé à un moment précis (par exemple, « utilisateur actif » a été redéfini en 2024), appliquer uniformément la nouvelle définition aux données plus anciennes (par exemple, les enregistrements de 2022) peut créer des pics ou des baisses artificiels qui ne se sont pas réellement produits. Dans la mesure du possible, appliquez la définition qui était en vigueur au moment de chaque enregistrement historique, ou documentez clairement le point de rupture afin que le modèle puisse en tenir compte.

### Enregistrements en double issus de tâches de remplissage échouées {#duplicate-records-from-failed-backfill-jobs}

Les tâches de remplissage rétrospectif qui échouent en cours d'exécution et sont relancées peuvent produire des enregistrements en double si le processus n'est pas conçu pour l'empêcher. Les enregistrements en double gonflent artificiellement les indicateurs et introduisent du bruit dans l'entraînement du modèle.

**La solution :** concevez tous les scripts de remplissage rétrospectif pour qu'ils soient idempotents : exécuter la même tâche deux fois doit produire le même résultat que l'exécuter une seule fois. Utilisez l'un des modèles suivants :

- **Upsert (mise à jour ou insertion) :** basé sur un identifiant de transaction unique ou un horodatage, de sorte que la réinsertion d'un enregistrement existant le met à jour plutôt que de créer un doublon.
- **Suppression puis insertion :** supprimez les enregistrements existants pour la plage temporelle cible avant l'insertion, afin que le jeu de données soit toujours remplacé proprement.
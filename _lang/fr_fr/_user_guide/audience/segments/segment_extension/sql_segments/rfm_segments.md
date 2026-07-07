---
nav_title: "Segments RFM"
article_title: Extensions de segments SQL RFM
page_order: 1
page_type: reference
alias: "/rfm_segments/"
description: "Cet article décrit comment créer des extensions de segments RFM, qui identifient vos meilleurs utilisateurs en mesurant leurs habitudes d'achat."
tool: Segments
---

# Segments SQL RFM {#rfm-sql-segments}

> Vous pouvez créer une extension de segment RFM (récence, fréquence, montant) pour cibler vos meilleurs utilisateurs en mesurant leurs habitudes d'achat.

L'analyse RFM est une technique marketing qui identifie vos meilleurs utilisateurs en attribuant à chacun un score de 0 à 3 pour chaque catégorie (récence, fréquence, montant), où 3 est le meilleur score et 0 le plus faible. Les valeurs de récence, de fréquence et de montant sont toutes basées sur les données d'une période spécifique de votre choix.

## Catégories RFM {#rfm-categories}

| Catégorie | Définition |
| --- | --- |
| Récence | Date du dernier achat d'un client. Un score plus élevé signifie des achats plus récents. |
| Fréquence | Fréquence à laquelle un client effectue des achats. Un score plus élevé signifie une fréquence plus importante. |
| Valeur monétaire | Montant total dépensé par un client. Un score plus élevé signifie des dépenses plus importantes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RFM categories" }

{% alert note %}
Les événements d'achat doivent être activés pour utiliser les segments SQL RFM, car la valeur monétaire de vos utilisateurs est déterminée par le chiffre d'affaires qu'ils ont généré via les événements d'achat Braze.
{% endalert %}

## Créer un segment RFM {#creating-an-rfm-segment}

1. Accédez à **Audience** > **Segment Extensions**.
2. Sélectionnez **New Extension**, puis sélectionnez **Recency, frequency, and monetary value (RFM) segment**.

![Fenêtre modale avec l'option de créer un segment de catalogue pour les événements, les achats ou les segments RFM.]({% image_buster /assets/img/segment/select_rfm_segment.png %}){: style="max-width:80%" }

{: start="3"}
3. Dans le panneau **Variables**, sélectionnez votre **Time Range** pour spécifier la période de données d'achat à analyser. Vous pouvez spécifier jusqu'aux 60 derniers jours. La période que vous sélectionnez correspond à la fenêtre temporelle à partir de laquelle les données de comportement des utilisateurs sont extraites, et dépend des objectifs de votre campagne.

| Champ de période | Description | Cas d'utilisation |
| --- | --- | --- |
| Relative | Spécifier l'activité au cours des X derniers jours | Analyser le comportement utilisateur le plus récent avec une fenêtre glissante. |
| Start date | Spécifier un point de départ fixe pour votre analyse | Analyser l'activité des utilisateurs à partir d'une date spécifique, par exemple après le lancement d'une campagne. |
| End date | Spécifier un point de fin fixe pour votre analyse | Analyser l'activité des utilisateurs jusqu'à une date spécifique, par exemple avant une mise à jour produit. |
| Date range | Spécifier à la fois une date de début et de fin pour une période personnalisée | Analyser le comportement des utilisateurs pendant une période définie, par exemple un événement promotionnel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Creating an RFM segment" }

{: start="4"}
4. Sélectionnez les [groupes RFM](#rfm-groups) générés à inclure dans votre segment. Si vous sélectionnez plusieurs groupes, votre segment inclut les utilisateurs qui font partie de l'un des groupes sélectionnés.

![Panneau Variables avec les groupes RFM « Champions » et « Loyal Users » sélectionnés.]({% image_buster /assets/img/segment/rfm_groups.png %})

{: start="5"}
5. Exécutez une prévisualisation, puis enregistrez votre segment.

{% alert note %}
Vous n'avez pas besoin de modifier le code SQL dans le modèle pour créer un segment RFM. Vous pouvez utiliser exclusivement le panneau **Variables** pour personnaliser votre segment.
{% endalert %}

### Groupes RFM {#rfm-groups}

Les segments RFM sont évalués dans un ordre spécifique. Les utilisateurs sont affectés au premier segment dont ils remplissent les critères, en partant du haut de la liste de priorité. Par exemple, un utilisateur qui remplit les conditions pour « Champions » et « Loyal Users » est affecté au segment « Champions » car il a une priorité plus élevée.

| Groupe RFM          | Description du segment                                                                 | Rang récence (R) | Rang fréquence (F) | Rang montant (M) |
|--------------------|-------------------------------------------------------------------------------------|------------------|--------------------|-------------------|
| Champions          | Le segment d'utilisateurs le plus précieux, avec les meilleurs scores dans toutes les catégories.                   | 3                | 2-3                | 2-3               |
| Loyal Users        | Utilisateurs avec une récence et une fréquence élevées. Peuvent avoir une valeur monétaire inférieure à celle des Champions. | 2-3              | 2-3                | 1-3               |
| Potential Loyalists| Utilisateurs ayant acheté récemment avec une fréquence et une valeur monétaire modérées.   | 3                | 1-3                | 1-3               |
| Promising          | Utilisateurs ayant effectué un premier achat récent de valeur élevée, mais n'ayant pas encore établi une fréquence d'achat élevée. | 3                | 0-3                | 1-3               |
| New Customer       | Utilisateurs ayant effectué leur tout premier achat très récemment.                             | 3                | 0-3                | 0-3               |
| Needing Attention  | Utilisateurs avec une récence supérieure à la moyenne, mais dont la fréquence d'achat ou la valeur monétaire sont inférieures à la moyenne. | 2-3              | 0-3                | 0-3               |
| Cannot lose them   | Utilisateurs autrefois à forte valeur avec de bons scores de fréquence et de montant, mais n'ayant pas acheté depuis longtemps. | 0-1              | 2-3                | 2-3               |
| At Risk            | Utilisateurs ayant historiquement des scores de fréquence et de montant modérés, mais n'ayant pas acheté depuis longtemps. | 0-1              | 1-3                | 1-3               |
| About to Sleep     | Utilisateurs ayant des scores faibles dans tous les indicateurs.                                       | 1                | 0-3                | 0-3               |
| Hibernating        | Utilisateurs avec une fréquence modérée mais inactifs depuis une période prolongée.    | 0                | 0-2                | 0-3               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="RFM groups" }
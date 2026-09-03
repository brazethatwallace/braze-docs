---
nav_title: Optimiser avec BrazeAI<sup>TM</sup>
article_title: Optimiser les tests A/B avec BrazeAI<sup>TM</sup>
page_order: 1.6
description: "Découvrez comment Optimiser avec BrazeAI<sup>TM</sup> sélectionne et distribue automatiquement les variantes les plus performantes dans les Campaigns à envoi unique et à envois multiples."
search_rank: 10
toc_headers: h2
---

# Optimiser les tests A/B avec BrazeAI<sup>TM</sup> {#optimizing-ab-tests-with-brazeai}

> Activez **Optimiser avec BrazeAI<sup>TM</sup>** pour optimiser automatiquement une Campaign comportant plusieurs variantes. La méthode d'optimisation dépend du fait que la Campaign est envoyée une seule fois ou plusieurs fois.

## Prérequis {#prerequisites}

Pour utiliser **Optimize with BrazeAI<sup>TM</sup>**, votre Campaign doit inclure au moins deux variantes de message.

Pour une Campaign à envois multiples, vous devez également :

- Définir au moins un événement de conversion.
- Configurer la fenêtre de rééligibilité à 24 heures ou plus.

## Activer l'optimisation {#turn-on-optimization}

Dans l'étape **Target Audiences**, accédez à **A/B Testing**, puis activez **Optimize with BrazeAI<sup>TM</sup>**.

## Campaigns à envoi unique {#single-send-campaigns}

Pour une campagne à envoi unique, Braze envoie une portion initiale de l'audience à chaque variante. Une fois la durée de l'expérience écoulée, BrazeAI<sup>TM</sup> sélectionne la variante la plus performante et l'envoie au reste de l'audience.

Braze applique les paramètres recommandés lorsque vous activez l'optimisation. Pour modifier ces paramètres, ouvrez **Contrôles avancés** :

- **Objectif d'optimisation :** Sélectionnez l'indicateur que BrazeAI<sup>TM</sup> utilise pour comparer les variantes. Les objectifs disponibles dépendent du canal.
- **Durée de l'expérience :** Sélectionnez 4 heures, 24 heures, 72 heures, ou saisissez une durée personnalisée.
- **Répartition des variantes :** Modifiez le pourcentage attribué à chaque variante ou groupe de contrôle.

La durée d'expérience par défaut est de 4 heures. Si vous optimisez pour un événement de conversion principal, la durée par défaut est de 24 heures.

### Objectifs d'optimisation par défaut par canal {#default-optimization-goals-by-channel}

| Canal | Objectif par défaut |
|---|---|
| Notifications push | *Opens* |
| E-mail | *Unique Clicks* |
| SMS, MMS, RCS et WhatsApp | *Clicks* |
| Autres canaux pris en charge | *Primary Conversion Event - A* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objectifs d'optimisation par défaut par canal" }

## Campaigns à envois multiples {#multi-send-campaigns}

Pour les Campaigns récurrentes, déclenchées par une action et déclenchées par l'API qui envoient plusieurs fois, BrazeAI<sup>TM</sup> optimise en continu la répartition de votre audience. Après la date limite de conversion initiale, Braze examine les performances toutes les 12 heures et envoie davantage d'utilisateurs vers les variantes les plus performantes.

La répartition initiale peut être uniforme pendant que BrazeAI<sup>TM</sup> collecte les données de performance. La répartition évolue à mesure que l'optimisation identifie des tendances de performance.

Ouvrez les **Advanced controls** pour ajouter ou supprimer un groupe de contrôle. Un groupe de contrôle fournit une référence pour mesurer les performances de la Campaign et ne reçoit pas de message.

## Rapports {#reporting}

Après la fin d'une expérience à envoi unique, ou lorsqu'une campagne à envois multiples a collecté suffisamment de données, la page **Campaign Analytics** affiche le gain produit par l'optimisation.

![Analyse de campagne montrant le gain obtenu grâce à Optimize with BrazeAI<sup>TM</sup>, avec des indicateurs de comparaison après la fenêtre d'expérimentation.]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %})

Pour en savoir plus, consultez [Analyse des tests A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).

## Questions fréquentes {#frequently-asked-questions}

### Pourquoi ne puis-je pas activer l'optimisation avec BrazeAI<sup>TM</sup> ? {#why-cant-i-turn-on-optimize-with-brazeai}

L'optimisation n'est pas disponible dans les cas suivants :

- La campagne comporte moins de deux variantes actives.
- Une campagne à envois multiples ne possède aucun événement de conversion.
- Une campagne à envois multiples a une fenêtre de rééligibilité inférieure à 24 heures.

### Pourquoi mes variantes ont-elles des volumes d'envoi similaires au début ? {#why-do-my-variants-have-similar-send-counts-at-first}

BrazeAI<sup>TM</sup> commence par une distribution initiale pour collecter des données de performance. La distribution est ajustée au fil du temps à mesure que les tendances de performance sont identifiées.

### Une campagne à envois multiples peut-elle cesser d'optimiser sans sélectionner une seule variante ? {#can-a-multi-send-campaign-stop-optimizing-without-selecting-one-variant}

Oui. L'optimisation s'arrête lorsque BrazeAI<sup>TM</sup> atteint un niveau de confiance de 95 % indiquant que poursuivre l'expérience n'améliorera pas le taux de conversion de plus de 1 % par rapport à son taux actuel.
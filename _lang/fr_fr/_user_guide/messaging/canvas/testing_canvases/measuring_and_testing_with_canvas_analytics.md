---
nav_title: Analytique Canvas
article_title: Analytique Canvas
page_order: 2
page_type: reference
description: "Cet article de référence décrit les différentes analyses et rapports que vous pouvez exploiter pour comprendre les performances de votre Canvas."
tool:
  - Canvas
  - Reports


---

# Analytique Canvas {#canvas-analytics}

> Vous devez savoir si ce que vous créez a un réel impact. Grâce à l'analytique Canvas, vous pouvez obtenir une vision complète pour comprendre comment les expériences que vous concevez contribuent à atteindre vos objectifs.

Une fois votre Canvas créé et mis en ligne, accédez à la page **Canvas** et sélectionnez votre Canvas pour ouvrir la page de détails. Vous pourrez alors mesurer et tester les performances de votre Canvas.

## Aperçu du Canvas {#canvas-overview}

Le haut de la page **Canvas Details** contient les statistiques principales du Canvas. Celles-ci incluent le nombre de messages envoyés dans le Canvas, le nombre total de fois où des utilisateurs sont entrés dans le Canvas, le nombre de conversions et votre taux global, le chiffre d'affaires généré par le Canvas, ainsi que l'audience totale estimée.

C'est l'endroit idéal pour obtenir un aperçu général et vérifier si votre Canvas atteint ses objectifs.

### Utilisateurs pouvant être atteints et statistiques exactes {#reachable-users-and-exact-statistics}

Lorsque l'option **[Calculer les statistiques exactes]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#single-user-segments)** est en cours d'exécution pour les audiences liées à votre Canvas, Braze peut brièvement afficher une estimation arrondie dans la zone **Utilisateurs pouvant être atteints**. Le total exact remplace l'estimation une fois le calcul terminé. Sélectionnez **Show Additional Stats** pour obtenir une répartition complète par canal. Le générateur de Canvas documente le même flux sous **Target Population** ; consultez [Calcul de la population cible]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#calculating-target-population).

![La page Canvas Details affichant les statistiques principales, notamment les messages envoyés, le taux de conversion, le nombre total d'entrées, le chiffre d'affaires total, le nombre total de sorties et l'audience estimée, avec des filtres par canal et par statistiques.]({% image_buster /assets/img_archive/Journey_5.png %})

{% alert tip %}
Si un segment que vous avez créé à partir de l'activité Canvas affiche moins d'utilisateurs pouvant être atteints que ce à quoi vous vous attendiez d'après l'analytique Canvas, il y a deux raisons courantes :

- **Échantillonnage d'estimation :** les statistiques du segment peuvent afficher une estimation basée sur un échantillon aléatoire avec un intervalle de confiance de 95 % de ±1 %, plutôt qu'un décompte exact.
- **Utilisateurs ne correspondant plus aux critères :** certains utilisateurs comptabilisés dans l'analytique Canvas peuvent ne plus remplir les conditions du segment, par exemple parce qu'ils se sont désabonnés ou que les données de leur profil ont changé depuis l'exécution du Canvas. Consultez les **performances historiques** du Canvas pour vérifier un volume élevé de désabonnements.
{% endalert %}

### Changes Since Last Viewed {#changes-since-last-viewed}

Le nombre de mises à jour apportées au Canvas par d'autres membres de votre équipe est suivi par l'indicateur *Changes Since Last Viewed* sur la page d'aperçu du Canvas. Sélectionnez **Changes Since Last Viewed** pour afficher un journal des modifications apportées au nom du Canvas, à la planification, aux étiquettes, aux messages, à l'audience, au statut d'approbation ou à la configuration d'accès de l'équipe. Pour chaque mise à jour, vous pouvez voir qui l'a effectuée et quand. Vous pouvez utiliser ce journal des modifications pour auditer les changements apportés à vos Canvas.

## Visualisation des performances {#performance-visualization}

En descendant sur la page **Canvas Details**, vous pouvez voir les performances de chaque composant, comme le nombre d'utilisateurs qui sont entrés, qui ont poursuivi vers l'étape suivante ou qui ont quitté le Canvas. Sélectionnez une étape ou un composant Canvas spécifique pour centrer le panneau sur cette partie du parcours et examiner ses indicateurs plus en détail.

{% alert note %}
Pour Canvas Flow, un utilisateur quitte le Canvas après être entré et avoir reçu le payload du message à la dernière étape de son parcours.
{% endalert %}

Les indicateurs incluent également les impressions, les destinataires uniques, le nombre de conversions et le chiffre d'affaires généré. Vous pouvez cliquer sur un composant pour affiner l'analyse de vos données et consulter les performances par canal.

![Deux exemples de détails de performance pour des composants Canvas. À gauche, les détails de performance d'un parcours utilisateur avec un composant Canvas. À droite, les détails de performance d'un composant Canvas développé et d'une étape imbriquée affichant le nombre d'impressions du message in-app.]({% image_buster /assets/img_archive/Journey_6.png %})

## Répartition des performances par variante {#performance-breakdown-by-variant}

En bas de la page **Canvas Details**, cliquez sur **Analyze Variants** pour ouvrir la fenêtre modale **Analyze Canvas**. Cette fenêtre modale contient trois onglets :

- Analyze Variants
- Canvas Funnel Report
- Canvas Retention Report

### Analyze Variants {#analyze-variants}

Dans l'onglet **Analyze Variants**, vous pouvez voir une répartition des performances par variante et par groupe de contrôle, si vous en avez plusieurs. Vous pouvez également copier l'identifiant API du Canvas, télécharger un fichier CSV des indicateurs et copier les cellules. L'onglet **Analyze Variants** contient un tableau qui vous présente une répartition de chaque variante à plusieurs niveaux.

Vous pouvez rapidement identifier les variantes les plus efficaces et déterminer les bonnes cadences, contenus, déclencheurs, timings, et bien plus encore.

![La fenêtre modale Analyze Canvas avec l'onglet Analyze Variants sélectionné, affichant un tableau comparatif pour Path 1 et Path 2 avec les entrées, les envois, le chiffre d'affaires, les taux de conversion, le pourcentage de variation et les indicateurs de confiance.]({% image_buster /assets/img_archive/analyze_variants.png %})

Les indicateurs de base incluent les éléments suivants :

- **Variant API Identifier :** l'identifiant API de votre variante, que vous pouvez utiliser dans vos appels API.
- **Total Entries :** le nombre total d'utilisateurs qui sont entrés dans la variante du Canvas.
- **Total Sends :** le nombre total de messages envoyés dans la variante du Canvas.
- **Total Steps :** le nombre total d'étapes dans la variante du Canvas.
- **Total Revenue :** le chiffre d'affaires total en dollars provenant des destinataires du Canvas dans la fenêtre de conversion principale définie. Le *chiffre d'affaires total* est la somme des achats attribués aux utilisateurs ayant reçu cette variante pendant cette fenêtre. Les achats sont toujours comptabilisés dans le *chiffre d'affaires total* même lorsque l'utilisateur n'effectue pas l'événement de conversion principal configuré, tant que l'achat respecte les règles d'attribution de la fenêtre.

{% alert note %}
Comme les conversions, le chiffre d'affaires est techniquement suivi au niveau du Canvas, mais il est attribué au composant le plus récent et à la variante la plus récente à partir desquels l'utilisateur a reçu un message (ou dans lesquels il est entré, s'il n'a pas encore reçu de message).<br><br>
Par exemple, si un utilisateur complète deux étapes puis effectue un achat, ce chiffre d'affaires est attribué au deuxième composant et à la variante dans laquelle il est entré. S'il entre dans le Canvas mais effectue un achat avant de recevoir le premier composant du Canvas, ce chiffre d'affaires est attribué à la variante dans laquelle il est entré, mais à aucun composant.
{% endalert %}

Au-delà de ces indicateurs, vous pouvez voir une répartition plus détaillée des [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), incluant les éléments suivants :

- Totaux de conversions et taux de conversion pour chaque événement de conversion
- Amélioration par rapport à la variante de contrôle
- Confiance statistique pour chaque événement de conversion

### Comment les conversions sont suivies {#how-conversions-are-tracked}

Un utilisateur ne peut convertir qu'une seule fois par événement de conversion et par entrée dans le Canvas. Les conversions sont attribuées au dernier message reçu par l'utilisateur pour cette entrée. Le résumé du Canvas reflète toutes les conversions effectuées par les utilisateurs dans ce parcours, qu'ils aient reçu un message ou non. Chaque étape suivante n'affichera que les conversions qui se sont produites lorsqu'elle était la dernière étape reçue par l'utilisateur.

Prenons l'exemple suivant : un Canvas comporte 10 notifications push et l'événement de conversion est « Ouvre l'application » (ou « Début de session »).
- L'utilisateur A ouvre l'application après être entré dans le Canvas mais avant de recevoir le premier message.
- L'utilisateur B ouvre l'application après chaque notification push.

Le résumé du Canvas affichera deux conversions, tandis que les étapes individuelles afficheront une conversion à la première étape et aucune pour toutes les étapes suivantes. Si les heures calmes sont actives au moment où l'événement de conversion se produit, les mêmes règles s'appliquent.

Imaginons maintenant un Canvas avec des heures calmes et les événements suivants :

1. L'utilisateur A entre dans un Canvas.
2. La première étape est une étape de délai pendant les heures calmes définies, le message est donc supprimé.
3. L'utilisateur A effectue l'événement de conversion.

L'utilisateur A sera comptabilisé comme converti dans la variante globale du Canvas, mais pas dans l'étape puisqu'il n'a pas reçu cette étape.

Pour notre dernier exemple, imaginons un Canvas avec la rééligibilité activée. Si un utilisateur rééligible effectue l'événement de conversion lors de la première entrée et de la deuxième entrée, deux conversions seront comptabilisées.

### Rapport d'entonnoir {#funnel-report}

Le rapport d'entonnoir offre un rapport visuel qui vous permet d'analyser les parcours de vos clients après avoir reçu un Canvas. Si votre Canvas utilise un groupe de contrôle ou plusieurs variantes, vous pourrez comprendre comment les différentes variantes ont impacté le tunnel de conversion à un niveau plus granulaire et optimiser en fonction de ces données. Pour plus d'informations sur les rapports d'entonnoir, consultez [Rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/).

### Rapport de rétention {#retention-report}

La rétention des utilisateurs est l'un des indicateurs les plus importants pour tout marketeur. Maintenir l'engagement des utilisateurs et les inciter à revenir est un signe de bonne santé de l'activité. Braze vous permet désormais de mesurer la rétention des utilisateurs directement sur la page **Canvas Analytics**. Pour plus d'informations sur la lecture et l'interprétation de votre rapport de rétention, consultez [Rapports de rétention]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/).
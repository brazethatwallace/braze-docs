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

Le haut de la page **Détails du Canvas** contient les statistiques principales du Canvas. Celles-ci incluent le nombre de messages envoyés dans le Canvas, le nombre total de fois où les clients sont entrés dans le Canvas, le nombre de conversions et votre taux global, le chiffre d'affaires généré par le Canvas, ainsi que l'audience totale estimée.

C'est un excellent endroit pour obtenir un aperçu de haut niveau et vérifier les performances de votre Canvas par rapport à votre objectif. Pour être notifié de manière proactive si les performances d'un Canvas sortent de la plage attendue, consultez les [alertes de seuil Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts).

### Utilisateurs joignables et statistiques exactes {#reachable-users-and-exact-statistics}

Lorsque l'option **[Calculer les statistiques exactes]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#single-user-segments)** est en cours d'exécution pour les audiences liées à votre Canvas, Braze peut brièvement afficher une estimation arrondie dans la zone **Utilisateurs joignables**. Le total exact remplace l'estimation une fois le calcul terminé. Sélectionnez **Afficher les statistiques supplémentaires** pour obtenir une ventilation complète par canal. Le générateur de Canvas documente le même flux sous **Population cible** ; consultez [Calcul de la population cible]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#calculating-target-population).

![La page Détails du Canvas affichant les statistiques principales, notamment les messages envoyés, le taux de conversion, le nombre total d'entrées, le chiffre d'affaires total, le nombre total de sorties et l'audience estimée, avec des filtres par canal et par statistiques.]({% image_buster /assets/img_archive/Journey_5.png %})

{% alert tip %}
Si un segment que vous avez créé à partir de l'activité du Canvas affiche moins d'utilisateurs joignables que prévu d'après l'analyse du Canvas, il y a deux raisons courantes :

- **Échantillonnage de l'estimation :** les statistiques du segment peuvent afficher une estimation basée sur un échantillon aléatoire avec un intervalle de confiance de 95 % de ±1 %, plutôt qu'un décompte exact.
- **Utilisateurs ne correspondant plus aux critères :** certains utilisateurs comptabilisés dans l'analyse du Canvas peuvent ne plus remplir les conditions du segment, par exemple parce qu'ils se sont désabonnés ou que les données de leur profil ont changé depuis l'exécution du Canvas. Vérifiez les **Performances historiques** du Canvas pour un volume élevé de désabonnements.
{% endalert %}

### Modifications depuis la dernière consultation {#changes-since-last-viewed}

Le nombre de mises à jour apportées au Canvas par d'autres membres de votre équipe est suivi par l'indicateur *Modifications depuis la dernière consultation* sur la page d'aperçu du Canvas. Sélectionnez **Modifications depuis la dernière consultation** pour afficher un journal des modifications apportées au nom du Canvas, à la planification, aux tags, au message, à l'audience, au statut d'approbation ou à la configuration d'accès de l'équipe. Pour chaque mise à jour, vous pouvez voir qui l'a effectuée et quand. Vous pouvez utiliser ce journal des modifications pour auditer les changements apportés à vos Canvas.

## Visualisation des performances {#performance-visualization}

En parcourant la page **Détails du Canvas**, vous pouvez consulter les performances de chaque composant, par exemple le nombre d'utilisateurs qui sont entrés, qui ont poursuivi vers l'étape suivante ou qui ont quitté le Canvas. Sélectionnez une étape ou un composant spécifique du Canvas pour concentrer le panneau sur cette partie du parcours et examiner ses indicateurs plus en détail.

{% alert note %}
Pour Canvas Flow, un utilisateur quittera le Canvas après être entré et avoir reçu le payload du message dans la dernière étape du parcours utilisateur.
{% endalert %}

Les indicateurs incluent également les impressions, les destinataires uniques, le nombre de conversions et le chiffre d'affaires généré. Vous pouvez cliquer sur un composant pour décomposer davantage vos données et consulter les performances par canal.

![Deux exemples de détails de performance pour des composants Canvas. À gauche, les détails de performance d'un parcours utilisateur avec un composant Canvas. À droite, les détails de performance d'un composant Canvas développé et d'une étape imbriquée affichant le nombre d'impressions du message in-app.]({% image_buster /assets/img_archive/Journey_6.png %})

## Répartition des performances par variante {#performance-breakdown-by-variant}

En bas de la page **Détails du Canvas**, cliquez sur **Analyser les variantes** pour ouvrir la fenêtre modale **Analyser le Canvas**. Cette fenêtre modale contient trois onglets :

- Analyser les variantes
- Rapport d'entonnoir du Canvas
- Rapport de rétention du Canvas

### Analyser les variantes {#analyze-variants}

Dans l'onglet **Analyser les variantes**, vous pouvez voir une répartition des performances par variante et par groupe de contrôle, si vous en avez plusieurs. Vous pouvez également copier l'identifiant API du Canvas, télécharger un fichier CSV des indicateurs et copier les cellules. L'onglet **Analyser les variantes** contient un tableau qui vous montre une répartition de chaque variante à plusieurs niveaux.

Vous pouvez rapidement identifier les variantes efficaces et déterminer les bonnes cadences, contenus, déclencheurs, timings, et plus encore.

![La fenêtre modale Analyser le Canvas avec l'onglet Analyser les variantes sélectionné, affichant un tableau comparatif pour le Chemin 1 et le Chemin 2 avec les entrées, envois, chiffre d'affaires, taux de conversion, pourcentage de variation et indicateurs de confiance.]({% image_buster /assets/img_archive/analyze_variants.png %})

Les indicateurs de base comprennent les éléments suivants :

- **Identifiant API de la variante :** L'identifiant API de votre variante, que vous pouvez utiliser dans vos appels API.
- **Total des entrées :** Le nombre total d'utilisateurs ayant accédé à la variante du Canvas.
- **Total des envois :** Le nombre total de messages envoyés dans la variante du Canvas.
- **Total des étapes :** Le nombre total d'étapes dans la variante du Canvas.
- **Chiffre d'affaires total :** Le chiffre d'affaires total en dollars provenant des destinataires du Canvas dans la fenêtre de conversion principale définie. Le *chiffre d'affaires total* est la somme des achats attribués aux utilisateurs ayant reçu cette variante pendant cette fenêtre. Les achats sont toujours comptabilisés dans le *chiffre d'affaires total* même lorsque l'utilisateur n'effectue pas l'événement de conversion principal configuré, tant que l'achat respecte les règles d'attribution de la fenêtre.

{% alert note %}
Comme les conversions, le chiffre d'affaires est techniquement suivi au niveau du Canvas, mais il est attribué au composant le plus récent et à la variante la plus récente à partir desquels l'utilisateur a reçu un message (ou dans lesquels il est entré, s'il n'a pas encore reçu de message).<br><br>
Par exemple, si un utilisateur complète deux étapes puis effectue un achat, ce chiffre d'affaires est attribué au deuxième composant et à la variante dans laquelle il est entré. S'il entre dans le Canvas mais effectue un achat avant de recevoir le premier composant du Canvas, ce chiffre d'affaires est attribué à la variante dans laquelle il est entré, mais pas à un composant.
{% endalert %}

Au-delà de cela, vous pouvez voir une répartition plus détaillée des [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), comprenant les éléments suivants :

- Totaux de conversions et taux de conversion pour chaque événement de conversion
- Amélioration par rapport à la variante de contrôle
- Confiance statistique pour chaque événement de conversion

### Comment les conversions sont suivies {#how-conversions-are-tracked}

Un utilisateur ne peut convertir qu'une seule fois par événement de conversion et par entrée dans le Canvas. Les conversions sont attribuées au message le plus récent reçu par l'utilisateur pour cette entrée. Le résumé du Canvas reflète toutes les conversions effectuées par les utilisateurs dans ce chemin, qu'ils aient reçu un message ou non. Chaque étape suivante n'affichera que les conversions survenues lorsque cette étape était la plus récente reçue par l'utilisateur.

Prenons l'exemple suivant : un Canvas comporte 10 notifications push et l'événement de conversion est « Ouvre l'application » (ou « Début de session »).
- L'utilisateur A ouvre l'application après être entré mais avant de recevoir le premier message.
- L'utilisateur B ouvre l'application après chaque notification push.

Le résumé du Canvas affichera deux conversions tandis que les étapes individuelles afficheront une conversion à la première étape et aucune pour toutes les étapes suivantes. Si les heures calmes sont actives lorsque l'événement de conversion se produit, les mêmes règles s'appliquent.

Maintenant, supposons que nous ayons un Canvas avec des heures calmes et que les événements suivants se produisent :

1. L'utilisateur A entre dans un Canvas.
2. La première étape est une étape de délai dans les heures calmes définies, donc le message est supprimé.
3. L'utilisateur A effectue l'événement de conversion.

L'utilisateur A sera comptabilisé comme converti dans la variante globale du Canvas, mais pas dans l'étape puisqu'il n'a pas reçu l'étape.

Pour notre dernier exemple, supposons que nous ayons un Canvas avec la rééligibilité activée. Si un utilisateur rééligible effectue l'événement de conversion lors de la première entrée et de la deuxième entrée, deux conversions seront comptabilisées.

### Rapport d'entonnoir {#funnel-report}

Le rapport d'entonnoir offre un rapport visuel qui vous permet d'analyser les parcours empruntés par vos clients après avoir reçu un Canvas. Si votre Canvas utilise un groupe de contrôle ou plusieurs variantes, vous pourrez comprendre comment les différentes variantes ont impacté l'entonnoir de conversion à un niveau plus granulaire et optimiser en fonction de ces données. Pour plus d'informations sur les rapports d'entonnoir, consultez [Rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports).

### Rapport de rétention {#retention-report}

La rétention des utilisateurs est l'un des indicateurs les plus importants pour tout marketeur. Garder les utilisateurs engagés qui reviennent régulièrement indique que l'activité est en bonne santé. Braze vous permet désormais de mesurer la rétention des utilisateurs directement sur la page **Analyse du Canvas**. Pour plus d'informations sur la lecture et l'interprétation de votre rapport de rétention, consultez [Rapports de rétention]({{site.baseurl}}/user_guide/analytics/reports/retention_reports).
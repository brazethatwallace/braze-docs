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

# Analytique Canvas

> Vous devez savoir si ce que vous créez a un réel impact. Grâce à l'analytique Canvas, vous pouvez obtenir une vision complète pour comprendre comment les expériences que vous concevez contribuent à atteindre vos objectifs.

Une fois votre Canvas créé et mis en ligne, accédez à la page **Canvas** et sélectionnez votre Canvas pour ouvrir la page de détails. Vous pourrez alors mesurer et tester les performances de votre Canvas.

## Aperçu du Canvas

Le haut de la page **Détails du Canvas** contient les statistiques principales du Canvas. Celles-ci incluent le nombre de messages envoyés dans le Canvas, le nombre total de fois où des utilisateurs sont entrés dans le Canvas, le nombre de conversions et votre taux global, le chiffre d'affaires généré par le Canvas, ainsi que l'audience totale estimée.

C'est l'endroit idéal pour obtenir un aperçu général et vérifier si votre Canvas atteint ses objectifs.

![]({% image_buster /assets/img_archive/Journey_5.png %})

### Modifications depuis la dernière consultation

Le nombre de mises à jour apportées au Canvas par d'autres membres de votre équipe est suivi par l'indicateur *Modifications depuis la dernière consultation* sur la page d'aperçu du Canvas. Sélectionnez **Modifications depuis la dernière consultation** pour afficher un journal des modifications apportées au nom du Canvas, à la planification, aux étiquettes, aux messages, à l'audience, au statut d'approbation ou à la configuration d'accès de l'équipe. Pour chaque mise à jour, vous pouvez voir qui l'a effectuée et quand. Vous pouvez utiliser ce journal des modifications pour auditer les changements apportés à vos Canvas.

## Visualisation des performances

En descendant sur la page **Détails du Canvas**, vous pouvez voir les performances de chaque composant, comme le nombre d'utilisateurs qui sont entrés, qui ont poursuivi vers l'étape suivante ou qui ont quitté le Canvas.

{% alert note %}
Pour Canvas Flow, un utilisateur quitte le Canvas après être entré et avoir reçu le PAYLOAD du message à la dernière étape de son parcours.
{% endalert %}

Les indicateurs incluent également les impressions, les destinataires uniques, le nombre de conversions et le chiffre d'affaires généré. Vous pouvez cliquer sur un composant pour affiner l'analyse de vos données et consulter les performances par canal.

![Deux exemples de détails de performance pour des composants Canvas. À gauche, les détails de performance d'un parcours utilisateur avec un composant Canvas. À droite, les détails de performance d'un composant Canvas développé et d'une étape imbriquée affichant le nombre d'impressions du message in-app.]({% image_buster /assets/img_archive/Journey_6.png %})

## Répartition des performances par variante

En bas de la page **Détails du Canvas**, cliquez sur **Analyser les variantes** pour ouvrir la fenêtre modale **Analyser le Canvas**. Cette fenêtre modale contient trois onglets :

- Analyser les variantes
- Rapport d'entonnoir du Canvas
- Rapport de rétention du Canvas

### Analyser les variantes

Dans l'onglet **Analyser les variantes**, vous pouvez voir une répartition des performances par variante et par groupe de contrôle, si vous en avez plusieurs. Vous pouvez également copier l'identifiant API du Canvas, télécharger un fichier CSV des indicateurs et copier les cellules. L'onglet **Analyser les variantes** contient un tableau qui vous présente une répartition de chaque variante à plusieurs niveaux.

Vous pouvez rapidement identifier les variantes les plus efficaces et déterminer les bonnes cadences, contenus, déclencheurs, timings, et bien plus encore.

![]({% image_buster /assets/img_archive/analyze_variants.png %})

Les indicateurs de base incluent les éléments suivants :

- **Identifiant API de la variante :** L'identifiant API de votre variante, que vous pouvez utiliser dans vos appels API.
- **Total des entrées :** Le nombre total d'utilisateurs qui sont entrés dans la variante du Canvas.
- **Total des envois :** Le nombre total de messages envoyés dans la variante du Canvas.
- **Total des étapes :** Le nombre total d'étapes dans la variante du Canvas.
- **Chiffre d'affaires total :** Le chiffre d'affaires total en dollars provenant des destinataires du Canvas dans la fenêtre de conversion principale définie.

{% alert note %}
Comme les conversions, le chiffre d'affaires est techniquement suivi au niveau du Canvas, mais il est attribué au composant le plus récent et à la variante la plus récente à partir desquels l'utilisateur a reçu un message (ou dans lesquels il est entré, s'il n'a pas encore reçu de message).<br><br>
Par exemple, si un utilisateur complète deux étapes puis effectue un achat, ce chiffre d'affaires est attribué au deuxième composant et à la variante dans laquelle il est entré. S'il entre dans le Canvas mais effectue un achat avant de recevoir le premier composant du Canvas, ce chiffre d'affaires est attribué à la variante dans laquelle il est entré, mais à aucun composant.
{% endalert %}

Au-delà de ces indicateurs, vous pouvez voir une répartition plus détaillée des [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/), incluant les éléments suivants :

- Totaux de conversions et taux de conversion pour chaque événement de conversion
- Amélioration par rapport à la variante de contrôle
- Confiance statistique pour chaque événement de conversion

### Comment les conversions sont suivies

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

### Rapport d'entonnoir

Le rapport d'entonnoir offre un rapport visuel qui vous permet d'analyser les parcours de vos clients après avoir reçu un Canvas. Si votre Canvas utilise un groupe de contrôle ou plusieurs variantes, vous pourrez comprendre comment les différentes variantes ont impacté le tunnel de conversion à un niveau plus granulaire et optimiser en fonction de ces données. Pour plus d'informations sur les rapports d'entonnoir, consultez [Rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/).

### Rapport de rétention

La rétention des utilisateurs est l'un des indicateurs les plus importants pour tout marketeur. Maintenir l'engagement des utilisateurs et les inciter à revenir est un signe de bonne santé de l'activité. Braze vous permet désormais de mesurer la rétention des utilisateurs directement sur la page **Analytique Canvas**. Pour plus d'informations sur la lecture et l'interprétation de votre rapport de rétention, consultez [Rapports de rétention]({{site.baseurl}}/user_guide/analytics/reports/retention_reports/).
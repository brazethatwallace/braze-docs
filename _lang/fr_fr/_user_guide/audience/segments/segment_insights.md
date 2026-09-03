---
nav_title: Statistiques des segments
article_title: Statistiques des segments
page_order: 6
page_type: tutorial
tool:
  - Segments
  - Reports
description: "Cet article pratique vous explique comment utiliser, interpréter et partager les statistiques des segments."
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Statistiques des segments {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsegmentation-course-stylefloatrightwidth120pxborder0-classnoimgbordersegment-insights}

> Découvrez comment utiliser, interpréter et partager les statistiques des segments.

Les statistiques des segments vous montrent les performances d'un segment par rapport à un autre sur un ensemble de KPI présélectionnés.

## Consultation des statistiques des segments {#viewing-segment-insights}

Accédez à la page **Statistiques des segments** de votre tableau de bord, sous **Analytics**, pour visualiser jusqu'à 10 segments différents comparés à une référence.

![Tableau de bord des statistiques des segments comparant trois segments, « UK Users », « FR Users » et « CA Users » à un segment de référence, « All Users ».]({% image_buster /assets/img_archive/segment_insights.png %})

{% alert note %}
Les statistiques de la page Statistiques des segments sont estimées par défaut. Pour calculer des valeurs exactes, ouvrez un segment et sélectionnez **Calculate Exact Statistics**. Les estimations peuvent être supérieures ou inférieures aux valeurs exactes, en particulier dans les espaces de travail volumineux ou pour les petits segments.
{% endalert %}

Le segment de référence peut être un segment spécifique que vous sélectionnez, ou un segment contenant l'ensemble de vos utilisateurs. Vous pouvez comparer les statistiques suivantes à l'aide des statistiques des segments :

| Mesure | Description | Formule |
| --------------------- | ------------- | ------------- |
| Sessions par jour | Nombre moyen de sessions par jour des utilisateurs du segment | (nombre total de sessions) / (nombre de jours depuis la première session) |
| Jours depuis la première session | Nombre moyen de jours entre la première session des utilisateurs du segment et maintenant | aujourd'hui – date de la première session |
| Jours depuis la dernière session | Nombre moyen de jours entre la dernière session des utilisateurs du segment et maintenant | aujourd'hui – date de la dernière session |
| Chiffre d'affaires à vie en dollars | Chiffre d'affaires moyen à vie en dollars pour les utilisateurs du segment | dépenses à vie de l'utilisateur |
| Jours depuis le premier achat | Nombre moyen de jours entre la première session et le premier achat des utilisateurs du segment | date du premier achat – date de la première session |
| Jours depuis le dernier achat | Nombre moyen de jours entre le dernier achat des utilisateurs du segment et maintenant | aujourd'hui – date du dernier achat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Consultation des statistiques des segments" }

Vous pouvez facilement partager des comparaisons spécifiques avec vos collègues en utilisant l'URL unique de la page, et vous pouvez également sélectionner l'icône en forme d'œil à côté de chaque segment pour afficher plus d'informations sur ce segment. Ces comparaisons seront réinitialisées lorsque vous changerez d'espace de travail.

![Détails du segment « Premium Users (iOS VideoApp) » avec un graphique affichant l'historique des membres et un tableau détaillant la taille estimée pour différents canaux de communication.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## Page Détails du Segment {#segment-details-page}

Les statistiques des segments ont également été intégrées directement dans la vue **Détails du Segment**. Lorsque vous consultez un Segment que vous avez précédemment configuré, vous pouvez retrouver les six mêmes statistiques présentées dans l'encadré gris dynamique Statistiques du Segment. Depuis cet encadré, vous pouvez rapidement lancer l'outil de statistiques des segments pour comparer ce Segment particulier avec n'importe quel autre que vous avez précédemment configuré, mais notez que cela écrasera tous les Segments que vous aviez précédemment sélectionnés dans l'outil de statistiques des segments.

{% alert note %}
Les [statistiques des segments](#viewing-segment-insights) et la page **Détails du Segment** calculent les estimations de taille séparément en utilisant des échantillons d'utilisateurs et des tailles d'échantillons différents. Il est donc normal que les chiffres ne correspondent pas exactement.
{% endalert %}

![Les statistiques des segments ont également été intégrées directement dans la vue Détails du Segment. Lorsque vous consultez un Segment que vous avez précédemment configuré, vous pouvez retrouver les six mêmes statistiques présentées dans l'encadré gris dynamique Statistiques du Segment. Depuis cet encadré, vous pouvez rapidement lancer l'outil de statistiques des segments pour comparer ce Segment particulier avec n'importe quel autre que vous avez précédemment configuré, mais notez que cela écrasera tous les Segments que vous aviez précédemment sélectionnés dans l'outil de statistiques des segments.]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## Cas d'usage {#insights-use-cases}

### Comparer les habitudes d'utilisation et d'achat selon les données démographiques {#comparing-demographic-usage-and-purchasing-patterns}

L'une des meilleures utilisations des statistiques des segments est de répondre aux questions sur l'impact des données démographiques des utilisateurs sur l'utilisation de l'application et l'efficacité des campagnes, par exemple :

- Certaines catégories démographiques d'utilisateurs obtiennent-elles des résultats significativement meilleurs ou moins bons que la moyenne ?
- Devrais-je repenser la localisation d'une campagne particulière ?
- Une campagne engage-t-elle une certaine catégorie démographique ?
- Quels objectifs devrais-je fixer pour une campagne ciblant une certaine catégorie démographique ?

Les statistiques des segments peuvent aider à révéler les différences entre les données démographiques des utilisateurs. L'exemple suivant montre une comparaison de la base d'utilisateurs d'une application par langue, illustrant comment les anglophones tendent à avoir une LTV et des niveaux d'activité plus élevés que les locuteurs d'autres langues.

![Détail des statistiques des segments pour les segments anglais, allemand, français et espagnol.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

Dans cet exemple, les germanophones se sont inscrits en moyenne il y a plus longtemps, ce qui pourrait expliquer pourquoi ils ne sont plus aussi actifs. Cela pourrait être dû à de nombreux facteurs. Par exemple, si l'application a d'abord été lancée en Europe mais est maintenant plus populaire aux États-Unis, où la plupart des gens parlent anglais ou espagnol. Pour des résultats plus robustes, lors de l'analyse des KPI selon les données démographiques, il est judicieux de tester les conclusions d'une étude générale des données démographiques (par exemple, si la langue impacte la LTV chez tous les utilisateurs) en examinant une population plus petite et plus homogène pour voir si les conclusions persistent.

Pour améliorer les conversions parmi les locuteurs de langues autres que l'anglais, une bonne première étape serait de [localiser les campagnes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) dans la langue de l'appareil de l'utilisateur et de s'assurer que le contenu de ces messages engage les utilisateurs en utilisant une [campagne multivariée]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) pour tester différentes versions du texte en langue étrangère.

### Comprendre les indicateurs d'un chiffre d'affaires plus élevé {#understanding-indicators-of-higher-revenue}

Convertir les utilisateurs en acheteurs peut être difficile, et essayer de pousser directement les nouveaux utilisateurs, les utilisateurs inactifs ou désengagés vers l'achat peut les amener à désinstaller votre application. Les statistiques des segments peuvent vous aider à découvrir les actions qui font progresser les utilisateurs dans l'entonnoir d'achat sans leur demander d'acheter immédiatement, par exemple s'abonner à votre newsletter, partager sur les réseaux sociaux ou s'inscrire aux messages promotionnels. Par exemple, vous pouvez visualiser l'impact sur les achats de différents comportements au sein d'une application d'e-commerce.

![Détail des statistiques des segments pour les utilisateurs ayant partagé sur les réseaux sociaux, s'étant inscrits aux promotions et s'étant inscrits à la newsletter.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

Dans ce cas, relativement peu d'utilisateurs sont actuellement inscrits aux messages promotionnels et ne sont pas aussi actifs, mais ces utilisateurs génèrent un chiffre d'affaires à vie plus élevé. Pour augmenter le chiffre d'affaires, il pourrait être judicieux d'inclure une invitation à s'inscrire aux messages promotionnels dans les campagnes d'onboarding. Pour réengager les utilisateurs inactifs, un bon plan serait d'envoyer une [campagne classique pour utilisateurs inactifs]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users) et de cibler les [utilisateurs ayant converti]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#converted-from-campaign) avec une campagne ultérieure pour s'inscrire aux messages promotionnels.
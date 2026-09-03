---
nav_title: Corrélation de conversion
article_title: Corrélation de conversion
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "Cet article de référence explique l'analyse de corrélation de conversion sur la page Analyse de campagne."
tool:
  - Reports

---

# Corrélation de conversion {#conversion-correlation}

> L'analyse de corrélation de conversion sur la page **Analyse de campagne** vous permet de comprendre quels attributs et comportements des utilisateurs favorisent ou nuisent aux résultats que vous avez définis pour vos campagnes.

## Aperçu {#overview}

Pour chaque campagne, Braze examine une liste d'attributs et de comportements utilisateur, puis détermine si ces éléments sont statistiquement associés de manière significative à une augmentation ou une diminution de chacun des [événements de conversion]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) que vous avez choisis pour la campagne. Nous calculons également dans quelle mesure les utilisateurs présentant un attribut ou un comportement donné ont plus ou moins de chances de convertir et, si le résultat est significatif, nous l'affichons du côté correspondant du tableau. Les utilisateurs présentant chaque attribut ou comportement d'intérêt sont comparés aux taux de l'ensemble de l'audience de la campagne. Les comportements et attributs qui ne présentent pas de corrélation significative avec la conversion ne sont pas affichés dans le tableau.

Pour lancer une analyse de corrélation de conversion, sélectionnez l'événement de conversion souhaité dans le menu déroulant.

![Panneau de corrélation de conversion montrant un exemple avec « Sélectionner un événement de conversion » défini sur « Événement de conversion principal - A » et le paramètre d'événement « A effectué un achat dans les 12 heures (tout produit) ».]({% image_buster /assets/img/convcorr.png %})

## Qu'est-ce qui est vérifié ? {#what-is-checked}

Nous vérifions les attributs suivants en les traitant comme des variables catégorielles. Autrement dit, un utilisateur possède ou ne possède pas chaque valeur possible de ces attributs, et nous testons si cela affecte le taux de conversion.

-  Pays
-  Langue
-  Genre

Nous vérifions également si les éléments suivants affectent le taux de conversion :

- L'exécution d'événements personnalisés
- Les campagnes et Canvas reçus au cours des 30 derniers jours (à l'exception de la campagne en cours d'évaluation)

Enfin, nous examinons plusieurs variables comportementales pouvant prendre différentes valeurs. Nous répartissons les éléments suivants en quatre compartiments ou quartiles, puis mesurons l'association entre l'appartenance à un quartile donné et l'augmentation ou la diminution de la conversion :

- Âge
- Total des dépenses en dollars
- Nombre de sessions

## Quand puis-je consulter cette analyse ? {#when-can-i-check-this-analysis}

Cette analyse devient disponible au moins 24 heures après le début de l'envoi d'une campagne et ne prend en compte que les envois effectués au cours des 30 derniers jours. Si aucun comportement ou attribut ne présente de corrélation significative avec l'un des événements de conversion de la campagne, le menu déroulant sera désactivé et un message vous en informera.

## Comment Braze vérifie la significativité {#how-braze-checks-for-significance}

Nous vérifions la significativité statistique à l'aide de l'[intervalle de confiance de Wilson](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Nous déterminons avec un niveau de confiance de 95 % le taux auquel l'ensemble de l'audience de la campagne a converti. C'est ce qu'on appelle le taux de base.

Ensuite, pour chacune des variables, nous calculons également le taux auquel les utilisateurs présentant cet attribut ou ce comportement particulier ont converti, avec un niveau de confiance de 95 %. En divisant ce taux par le taux de base, nous obtenons un ratio. Si ce ratio est nettement supérieur à 1, les utilisateurs présentant cet attribut ou ce comportement ont plus de chances de convertir. S'il est nettement inférieur, ils ont moins de chances de convertir. Nous affichons la valeur du ratio dans le tableau. Cette valeur n'est affichée que si elle s'écarte suffisamment de 1 pour être significative au niveau de confiance de 95 %.
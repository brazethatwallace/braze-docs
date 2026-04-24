---
nav_title: Conventions de nommage des événements
article_title: Conventions de nommage des événements
page_order: 4
page_type: reference
description: "Cet article de référence présente les conventions de nommage des événements et les bonnes pratiques à suivre."

---

# Conventions de nommage des événements

> Cette page présente les conventions de nommage des événements et les bonnes pratiques à suivre. En maintenant une cohérence dans la taxonomie de vos événements et attributs, vous garderez vos données propres et exploitables pour les utilisateurs actuels et futurs de la plateforme Braze. Cela permet d'éviter des problèmes ultérieurs, comme le déclenchement d'une campagne vers la mauvaise audience ou la génération de résultats erronés suite à l'utilisation du mauvais événement.

## Bonnes pratiques

- Adoptez une convention de nommage claire.
- Utilisez une casse et un formatage cohérents pour les noms d'événements.
- Évitez de donner des noms similaires à vos événements.
- Évitez les chaînes de caractères d'attributs d'événements trop longues, qui seront tronquées ou coupées dans le tableau de bord de Braze.

## Conventions de nommage

### Utiliser des groupes d'événements

Utilisez des groupes pour distinguer les différentes parties de votre produit lors du nommage des événements. En catégorisant votre produit en groupes, n'importe quel utilisateur peut comprendre clairement à quoi l'événement fait référence et ce qu'il représente.

### Structure de nommage des événements

La structure de nommage la plus courante est `group_noun_action`. Les événements doivent tous être en minuscules afin d'éviter les erreurs d'instrumentation liées à la casse et faciliter l'identification des propriétés.

### Propriétés

Étiquetez un seul événement, puis identifiez les différences à l'aide de propriétés. Cette approche est utile pour les événements qui sont fondamentalement identiques mais présentent des différences mineures, comme les canaux d'une campagne. Cela permet également de visualiser facilement le parcours des utilisateurs à travers les événements. Consultez l'[objet propriétés d'événement]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) pour un exemple et des informations complémentaires.

## Exemples

Imaginons que vous faites partie d'une entreprise de commerce en ligne et que vous souhaitez suivre le moment où les clients s'inscrivent sur votre application et celui où ils s'abonnent à votre newsletter. Voici des exemples de noms d'événements efficaces :

- `user_signup`
- `newsletter_subscribed`

Ces deux noms d'événements indiquent clairement ce qu'ils suivent. À mesure que vous créez de nouveaux événements personnalisés, veillez à ce que vos conventions de nommage restent compréhensibles. Par exemple, évitez d'utiliser des noms d'événements tels que `signup_event_1`, car cela manque de clarté et ne décrit pas ce que l'événement suit, contrairement à `user_signup`.
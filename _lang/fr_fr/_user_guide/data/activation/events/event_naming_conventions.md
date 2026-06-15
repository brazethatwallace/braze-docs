---
nav_title: Conventions de dénomination des événements
article_title: Conventions de nommage des événements
page_order: 4
page_type: reference
description: "Cet article de référence couvre les conventions et meilleures pratiques de nommage pour les événements."

---

# Conventions de dénomination des événements {#event-naming-conventions}

> Cette page traite des conventions de dénomination des événements et des meilleures pratiques. En maintenant la cohérence de votre taxonomie d'événements et d'attributs, vous garderez vos données propres et utilisables pour les utilisateurs nouveaux et existants de la plateforme Braze. Cela permet d'éviter des problèmes ultérieurs, comme le déclenchement d'une campagne auprès de la mauvaise audience ou la génération de mauvais résultats après avoir utilisé le mauvais événement.

## Bonnes pratiques {#best-practices}

- Adoptez une convention de nommage claire.
- Utilisez des majuscules et un formatage cohérents pour les noms d'événements.
- Évitez de donner des noms similaires à des événements.
- Évitez les longues chaînes de caractères pour les attributs d'événements, car elles seront tronquées ou coupées sur le tableau de bord de Braze.

## Conventions de nommage {#naming-conventions}

### Utilisez des groupes d'événements {#use-event-groups}

Utilisez des groupes pour nommer les événements et différencier les différentes parties de votre produit. En catégorisant votre produit en groupes, tout utilisateur peut clairement comprendre à quoi l'événement fait référence, et à quoi il sert.

### Structure de nommage des événements {#event-naming-structure}

La structure de nommage la plus courante est `group_noun_action`. Les événements doivent tous être en minuscules pour éviter les erreurs d'identification des propriétés et les erreurs d'instrumentation liées à la casse.

### Propriétés {#properties}

Étiquetez un seul événement, puis identifiez les différences à l'aide de propriétés. Cette approche est utile pour les événements qui sont fondamentalement identiques mais présentent des différences mineures, comme les canaux d'une campagne. Cela permet également de visualiser facilement le parcours des utilisateurs à travers les événements. Consultez l'[objet propriétés d'événement]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) pour un exemple et des informations complémentaires.

## Exemples {#examples}

Imaginons que vous faites partie d'une entreprise de commerce en ligne et que vous souhaitez suivre le moment où les clients s'inscrivent sur votre application et celui où ils s'abonnent à votre newsletter. Voici des exemples de noms d'événements efficaces :

- `user_signup`
- `newsletter_subscribed`

Ces deux noms d'événements indiquent clairement ce qu'ils suivent. À mesure que vous créez de nouveaux événements personnalisés, veillez à ce que vos conventions de nommage restent compréhensibles. Par exemple, évitez d'utiliser des noms d'événements tels que `signup_event_1`, car cela manque de clarté et ne décrit pas ce que l'événement suit, contrairement à `user_signup`.
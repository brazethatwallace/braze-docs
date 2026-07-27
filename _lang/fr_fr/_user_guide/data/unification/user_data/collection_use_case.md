---
nav_title: Cas d'usage de collecte de données
article_title: Cas d'usage de collecte de données
page_order: 3
page_type: reference
description: "Cet article de référence couvre un cas d'usage de collecte de données utilisateur sur la façon dont une application de covoiturage pourrait décider des données utilisateur à collecter."

---

# Cas d'usage de collecte de données {#collection-use-case}

> Cet article couvre un cas d'usage de collecte de données utilisateur sur la façon dont une application de covoiturage pourrait décider des données utilisateur à collecter.

Imaginons qu'une application de taxi ou de covoiturage, appelée StyleRyde, veuille décider des données utilisateur à collecter. Les questions et le processus de réflexion qui suivent constituent un excellent modèle à suivre pour leurs équipes de marketing et de développement. À la fin de cet exercice, les deux équipes devraient avoir une bonne compréhension des événements et attributs personnalisés qu'il est judicieux de collecter pour atteindre leur objectif.

## Question de cas 1 : Quel est l'objectif ? {#case-question-1-what-is-the-goal}

L'objectif de StyleRyde est simple : il s'agit de permettre aux utilisateurs de héler des courses de taxi par le biais de son application.

## Question de cas 2 : Quelles sont les étapes à suivre pour atteindre cet objectif après l'installation de l'application ? {#case-question-2-what-are-the-steps-to-reach-that-goal-after-app-installation}

1. StyleRyde demande aux utilisateurs de commencer le processus d'inscription et de remplir leurs informations personnelles.
2. StyleRyde a besoin que les utilisateurs complètent et vérifient le processus d'inscription en saisissant un code dans l'application qu'ils reçoivent par SMS.
3. StyleRyde demande aux utilisateurs de tenter de héler un taxi.
4. StyleRyde doit être disponible lorsque les utilisateurs hèlent un taxi.

Ces actions peuvent ensuite être étiquetées comme les événements personnalisés suivants :

- Inscription commencée
- Inscription terminée
- Appels de taxis réussis
- Appels de taxis échoués

Après avoir mis en œuvre les événements, StyleRyde peut mener des campagnes, notamment les suivantes :

1. Envoyer un message aux utilisateurs qui ont commencé l'inscription, mais qui ne l'ont pas terminée dans un certain délai.
2. Envoyer des messages de félicitations aux utilisateurs qui ont terminé l'inscription.
3. Envoyer des excuses et un crédit promotionnel aux utilisateurs qui ont eu des appels de taxis échoués, non suivis d'un appel de taxi réussi dans un certain laps de temps.
4. Envoyer des promotions aux utilisateurs les plus actifs ayant de nombreux appels de taxis réussis pour les remercier de leur fidélité.

## Question de cas 3 : Quelles autres informations sur les utilisateurs pourrions-nous collecter et utiliser pour enrichir nos messages ? {#case-question-3-what-other-user-information-could-we-collect-and-use-to-inform-our-messaging}

- Les utilisateurs disposent-ils d'un crédit promotionnel ?
- Quelle est la note moyenne que les utilisateurs attribuent à leurs chauffeurs ?
- Des codes de promotion uniques pour les utilisateurs ?

Ces caractéristiques peuvent ensuite être étiquetées comme les attributs personnalisés suivants :

- Solde de crédit promotionnel (type décimal)
- Note moyenne du chauffeur (type entier)
- Code de promotion unique (type chaîne de caractères)

Ces attributs vous permettent d'envoyer des campagnes aux utilisateurs, par exemple :

1. Rappeler aux utilisateurs qui n'ont pas utilisé l'application depuis sept jours et qui disposent d'un crédit promotionnel sur leur compte de revenir sur l'application et d'utiliser ce crédit.
2. Utiliser nos modèles de message et [les fonctionnalités de personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) pour intégrer l'attribut de code de promotion unique dans les messages destinés aux utilisateurs.

{% alert important %}
Braze bannira ou bloquera les utilisateurs (« utilisateurs fictifs ») ayant plus de 5 000 000 de sessions et n'ingérera plus leurs événements SDK, car ils sont généralement le résultat d'une mauvaise intégration. Si vous constatez que cela est arrivé à un utilisateur légitime, contactez votre gestionnaire de compte Braze.
{% endalert %}
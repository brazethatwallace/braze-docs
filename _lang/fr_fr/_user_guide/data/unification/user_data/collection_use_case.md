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

L'objectif de StyleRyde est simple : ils veulent que les utilisateurs commandent des courses de Taxi via leur application.

## Question de cas 2 : Quelles sont les étapes pour atteindre cet objectif après l'installation de l'application ? {#case-question-2-what-are-the-steps-to-reach-that-goal-after-app-installation}

1. StyleRyde a besoin que les utilisateurs commencent le processus d'inscription et remplissent leurs informations personnelles.
2. StyleRyde a besoin que les utilisateurs complètent et vérifient le processus d'inscription en saisissant dans l'application un code reçu par SMS.
3. StyleRyde a besoin que les utilisateurs tentent de héler un taxi.
4. StyleRyde doit être disponible lorsque les utilisateurs hèlent un taxi.

Ces actions pourraient ensuite être étiquetées comme les événements personnalisés suivants :

- Began Registration
- Completed Registration
- Successful Taxi Hails
- Unsuccessful Taxi Hails

Après avoir implémenté les événements, StyleRyde peut lancer des Campaigns incluant les suivantes :

1. Envoyer un message aux utilisateurs qui ont commencé l'inscription (Began Registration), mais qui n'ont pas complété l'inscription (Completed Registration) dans un certain délai.
2. Envoyer des messages de félicitations aux utilisateurs qui ont complété l'inscription (Completed Registration).
3. Envoyer des excuses et un crédit promotionnel aux utilisateurs qui ont eu des courses de taxi infructueuses (Unsuccessful Taxi Hails), non suivies d'une course de taxi réussie (Successful Taxi Hail) dans un certain délai.
4. Envoyer des promotions aux utilisateurs les plus actifs ayant de nombreuses courses de taxi réussies (Successful Taxi Hails) pour les remercier de leur fidélité.

## Question de cas 3 : Quelles autres informations utilisateur pourrions-nous collecter et utiliser pour orienter nos communications ? {#case-question-3-what-other-user-information-could-we-collect-and-use-to-inform-our-messaging}

- Les utilisateurs disposent-ils d'un crédit promotionnel ?
- Quelle est la note moyenne que les utilisateurs attribuent à leurs chauffeurs ?
- Les utilisateurs ont-ils des codes de promotion uniques ?

Ces caractéristiques pourraient ensuite être étiquetées comme les attributs personnalisés suivants :

- Solde de crédit promotionnel (type décimal)
- Note moyenne du chauffeur (type entier)
- Code de promotion unique (type chaîne de caractères)

Ces attributs vous permettent d'envoyer des Campaigns aux utilisateurs, par exemple :

1. Rappeler aux utilisateurs qui n'ont pas utilisé l'application depuis sept jours et qui disposent d'un crédit promotionnel sur leur compte de revenir sur l'application et d'utiliser ce crédit.
2. Utiliser nos modèles de messages et nos [fonctionnalités de personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) pour intégrer l'attribut de code de promotion unique dans les communications destinées aux utilisateurs.

{% alert important %}
Braze bloque les profils utilisateur (« utilisateurs fictifs ») ayant plus de 5 000 000 de sessions, plus de 20 000 noms d'événements personnalisés distincts ou plus de 20 000 noms de produits distincts dans les achats, car ils résultent généralement d'une mauvaise intégration. Une fois qu'un profil est bloqué, Braze cesse d'ingérer toutes les données entrantes pour ce profil, provenant aussi bien des SDK que de la REST API. Si vous constatez que cela est arrivé à un utilisateur légitime, contactez votre gestionnaire de compte Braze.
{% endalert %}
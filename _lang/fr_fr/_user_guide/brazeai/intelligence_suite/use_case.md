---
nav_title: "Cas d'utilisation"
article_title: "Cas d'utilisation : Intelligence Suite"
page_order: 10
search_rank: 12
description: "Vous découvrez l'Intelligence Suite de Braze ? Lisez ce cas d'utilisation pour comprendre comment le timing intelligent peut être exploité pour envoyer des promotions personnalisées dans un Canvas unifié."
tool:
  - Dashboard
---

# Cas d'utilisation : transformer le comportement passé dans l'application en offres personnalisées sur le bon canal {#use-case-turn-past-app-behavior-into-personalized-offers-on-the-right-channel}

> Cet exemple illustre comment une marque fictive utilise le timing intelligent pour exploiter les données d'engagement passées dans l'application et les messages afin d'envoyer des promotions personnalisées dans un Canvas unifié.

Supposons que Marvin soit responsable marketing chez SandwichEmperor, un restaurant de restauration rapide qui propose fréquemment des offres à durée limitée. L'équipe de Marvin est chargée de diffuser des messages promotionnels dans leur application pour promouvoir un nouveau produit à durée limitée : le Super Sub.

Jusqu'à présent, chaque message pour les produits à durée limitée était géré de manière isolée : différents tests de textes et angles étaient envoyés séparément. L'équipe a essayé différentes approches pour stimuler l'engagement sans vraiment comprendre quand les promotions à durée limitée sont les plus populaires auprès de leurs utilisateurs dans l'application.

Pour la nouvelle promotion du Super Sub, Marvin souhaite un Canvas coordonné unique qui continue d'apprendre au fil du temps, en s'appuyant sur les comportements que Braze capture déjà (sessions, ouvertures, clics) plutôt que de deviner les heures d'envoi ou de miser sur un seul message gagnant.

Grâce au timing intelligent, Marvin peut envoyer les étapes de message au moment où chaque personne est la plus susceptible de s'engager, en se basant sur une analyse statistique des interactions passées (par exemple, les habitudes de session et l'engagement par canal).

Ce tutoriel explique comment Marvin :

- Crée un Canvas avec des notifications push, des e-mails et des SMS dans des étapes de message
- Utilise le timing intelligent sur ces étapes pour que la distribution s'aligne sur les habitudes d'engagement déduites par utilisateur et par canal

## Étape 1 : définir l'indicateur de réussite et créer le Canvas {#step-1-define-the-success-metric-and-build-the-canvas}

Marvin définit ce que signifie la « réussite » pour le Super Sub (par exemple, les commandes ou un événement personnalisé qui se déclenche lorsqu'un utilisateur finalise un achat de Super Sub ou l'ajoute dans l'application).

Ensuite, Marvin crée un Canvas pour que les nouveaux utilisateurs y entrent selon un calendrier régulier pendant toute la durée de l'offre.

1. Dans le tableau de bord de Braze, Marvin accède à **Messaging** > **Canvas**.
2. Il crée un Canvas et le nomme « Limited item - Super Sub ».
3. Il ajoute ensuite un événement de conversion et une autre variante dans le Canvas.
4. Il complète les détails restants du Canvas et est maintenant prêt à cartographier le parcours utilisateur dans le générateur de Canvas.

## Étape 2 : configurer les paramètres de distribution {#step-2-set-up-delivery-settings}

Dans l'onglet **Delivery Settings** de l'étape de message, Marvin prévoit d'utiliser le timing intelligent pour analyser les interactions passées de ses utilisateurs avec l'application et chaque canal de communication, puis sélectionner automatiquement le meilleur moment pour promouvoir le Super Sub auprès de chaque utilisateur. Cela signifie que certains utilisateurs peuvent recevoir la promotion l'après-midi, tandis que d'autres la recevront le soir.

Il sélectionne **l'heure la plus populaire d'utilisation de l'application parmi tous les utilisateurs** pour ceux qui n'ont pas suffisamment d'interactions passées à analyser.

## Étape 3 : ajouter des délais et le timing intelligent aux étapes de message {#step-3-add-delays-and-intelligent-timing-to-message-steps}

Pour les étapes de message qui utilisent le timing intelligent, Marvin suit les recommandations de Canvas : il place une étape de délai d'au moins deux jours calendaires entre l'entrée (ou une étape précédente) et l'étape de message avec le timing intelligent. Il préfère les jours calendaires pour les délais lorsqu'il utilise le timing intelligent, afin que la distribution ait lieu le jour prévu à l'heure optimale de chaque utilisateur.

Dans chaque étape de message de notification push, d'e-mail et de SMS, il ouvre **Delivery Settings** et choisit **Using Intelligent Timing**. Il définit une heure de repli pour les utilisateurs qui n'ont pas suffisamment d'historique d'engagement pour déterminer une heure optimale. Il note que les étapes de message avec plusieurs canaux peuvent envoyer ou tenter d'envoyer à des heures différentes par canal, reflétant le fait que certains clients s'engagent davantage par e-mail le matin et par notification push le soir.

## Étape 4 : surveiller et optimiser {#step-4-monitor-and-optimize}

Marvin coordonne les ressources promotionnelles du Super Sub à travers les notifications push, les e-mails et les SMS dans les étapes de message (ainsi que dans toutes les étapes suivantes utilisées par ses variantes) et lance le Canvas.

Après le lancement, il surveille les analyses du Canvas et le nombre de conversions, et constate que le timing intelligent continue d'optimiser le moment où chaque canal est déclenché pour chaque utilisateur en fonction des habitudes d'engagement en cours. En conséquence, Marvin a permis à SandwichEmperor de relier les performances des offres à durée limitée au moment et au parcours qui fonctionnent, plutôt que de se fier uniquement au dernier message promotionnel ponctuel ayant obtenu les meilleurs résultats.
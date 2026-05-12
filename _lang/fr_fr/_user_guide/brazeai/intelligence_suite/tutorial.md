---
nav_title: "Tutoriel : Restaurant à service rapide"
article_title: Tutoriel sur l'Intelligence Suite
page_order: 10
search_rank: 12
description: "Vous découvrez l'intelligence suite de Braze ? Commencez par ce tutoriel."
tool:
  - Dashboard
---

# Tutoriel sur l'Intelligence Suite {#intelligence-suite-tutorial}

> Vous découvrez la Braze Intelligence Suite ? Commencez par ce tutoriel ! Pour plus d'informations générales, consultez [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/).

## Tutoriel : Restaurant à service rapide {#tutorial-quick-service-restaurant}

Imaginons que nous travaillons chez SandwichEmperor, un restaurant rapide qui propose un nouveau plat à durée limitée : le Royal Roast. Nous utiliserons deux fonctionnalités de l'Intelligence Suite pour envoyer des promotions personnalisées dans un Canvas.

### Étape 1 : Utilisez le timing intelligent pour déterminer quand envoyer les notifications {#step-1-use-intelligent-timing-for-when-to-send-notifications}

Nous utiliserons le timing intelligent pour analyser les interactions passées de nos utilisateurs avec notre application et chaque canal de communication, puis sélectionner automatiquement le meilleur moment pour promouvoir le Royal Roast auprès de chaque utilisateur. Certains utilisateurs pourraient recevoir la promotion dans l'après-midi, tandis que d'autres la recevraient en soirée.

Pour les utilisateurs qui n'ont pas suffisamment d'interactions passées à analyser, nous prévoyons un moment de repli : l'heure la plus populaire d'utilisation de l'application parmi l'ensemble des utilisateurs.

![Paramètres de réception du timing intelligent pour une étape Message.]({% image_buster /assets/img/intelligence_suite1.png %})

### Étape 2 : Utilisez la sélection intelligente pour choisir la promotion {#step-2-use-intelligent-selection-to-select-the-promotion}

Pour les messages promotionnels proprement dits, nous utiliserons la sélection intelligente afin de tester trois messages différents (notification push, e-mail et SMS) pour le Royal Roast. La sélection intelligente analysera les performances de tous nos messages promotionnels deux fois par jour, puis enverra progressivement davantage les messages les plus performants et moins les autres.

Une fois que la sélection intelligente aura recueilli suffisamment de données pour déterminer le message le plus performant, elle utilisera ce message dans 100 % des envois futurs.

![Section de test A/B d'un Canvas avec la sélection intelligente activée.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Étape 3 : Lancez le Canvas {#step-3-launch-the-canvas}

Grâce au timing intelligent et à la sélection intelligente, nous avons configuré nos promotions Royal Roast pour optimiser à la fois le moment d'envoi et le contenu des messages. Nous pouvons lancer notre Canvas et observer comment nos envois s'adaptent aux préférences des utilisateurs.
---
nav_title: Améliorer la faible latence
article_title: Améliorer la faible latence pour les Content Cards en tant que bannières
page_order: 10
description: "Cet article présente des stratégies pour garantir le respect des exigences de faible latence avec les Content Cards."
channel:
  - content cards
---

# Améliorer la latence pour les Content Cards en tant que bannières {#improve-latency-for-content-cards-as-banners}

> Si vous rencontrez des problèmes de latence avec votre implémentation de Content Cards pour des cas d'utilisation critiques, comme les bannières de page d'accueil, consultez cette page pour découvrir des stratégies et des conseils afin de résoudre ces problèmes et accélérer le rendu.

{% alert tip %}
Vous souhaitez afficher des bannières personnalisées et bien visibles sur votre application ou votre site web ? Essayez les [Bannières]({{site.baseurl}}/user_guide/channels/banners), conçues pour prendre en charge les cas d'utilisation de bannières à faible latence.
{% endalert %}

## Utilisez une entrée planifiée plutôt qu'une entrée basée sur une action {#use-scheduled-entry-instead-of-action-based-entry}

Les cartes basées sur une action, aussi bien dans les Campaigns que dans les Canvas, nécessitent un traitement en arrière-plan. Braze doit d'abord recevoir une notification de l'action déclencheur (comme un achat effectué ou le début d'une session) avant de créer une carte pour un utilisateur. Par conséquent, il y aura un délai avant que ces cartes ne soient disponibles.

Les cartes basées sur une action ajouteront de la complexité à votre application, car vous pourriez vous retrouver à interroger et actualiser en continu en attendant que la carte soit disponible. À la place, configurez votre carte avec une `Scheduled Entry`, qui agira comme une fenêtre de disponibilité permettant à la carte d'être toujours accessible à l'audience ciblée.

Si vous planifiez vos cartes à l'avance, elles seront prêtes et attendront que l'utilisateur ouvre votre application et demande les cartes.

## Utiliser la logique d'envoi « At First Impression » {#use-at-first-impression-send-logic}

Combinée aux envois planifiés, l'option `At First Impression` permet d'éviter la latence grâce à la rapidité avec laquelle une carte est créée et stockée dans Braze. L'option `At Campaign Launch` crée toutes les cartes pour l'ensemble des utilisateurs segmentés à l'avance, ce qui peut prendre du temps. L'option `At First Impression` génère une carte pour un utilisateur la première fois qu'elle est demandée, par exemple lorsqu'un utilisateur ouvre votre application pour la première fois.

Cela signifie qu'avec une entrée planifiée, les cartes sont disponibles immédiatement, dès que vous en avez besoin, que ce soit au démarrage de la session ou pour une fenêtre d'éligibilité basée sur le temps.

## N'oubliez pas que l'entrée dans le Canvas est un prérequis pour recevoir des cartes {#remember-that-canvas-entry-is-a-prerequisite-for-receiving-cards}

Lorsque vous utilisez Canvas, n'oubliez pas qu'un utilisateur doit d'abord entrer dans le Canvas en fonction de vos critères d'entrée configurés, *puis* doit passer par votre étape de message Content Cards. Ce n'est qu'à ce moment-là que la carte sera disponible pour votre application ou votre site web. N'oubliez pas qu'il existe une latence intégrée pour la création de la carte une fois que l'utilisateur a franchi l'étape, ce qui peut retarder le moment où la carte est disponible.

## Ne pas actualiser les cartes de manière excessive {#dont-refresh-cards-excessively}

Les Content Cards sont automatiquement actualisées par le SDK au début de chaque nouvelle session. Vous pouvez également demander manuellement une actualisation des Content Cards à tout moment pendant une session active. Sur les versions du SDK prises en charge, Braze envoie les ajouts et suppressions à l'appareil pendant la session grâce à la [distribution en temps réel]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#real-time-delivery), ce qui réduit la fréquence à laquelle vous devez actualiser manuellement.

Appeler la méthode `requestContentCardsRefresh` et actualiser trop fréquemment peut entraîner une limitation du débit. Si votre application est temporairement soumise à une limitation du débit, vous pourriez ne pas être en mesure d'actualiser les cartes au moment où vous en avez besoin ou à un moment critique de l'engagement de l'utilisateur avec votre application.

Pour éviter cela, n'appelez cette méthode d'actualisation qu'aux moments importants du cycle de vie de l'utilisateur, par exemple après un achat ou après une mise à niveau de son niveau d'abonnement.

## Éviter d'inclure du contenu connecté {#avoid-including-connected-content}

Le contenu connecté enrichit les Content Cards avec des données d'API internes ou tierces. Cependant, lorsqu'il est inclus dans un message Content Card, il bloque la disponibilité de la carte jusqu'à ce que la requête réseau du contenu connecté soit terminée. Dans certains cas, les SDK réessaieront quelques secondes plus tard afin de ne pas retarder la logique de rendu de votre application, qui peut attendre que le SDK termine sa tâche d'actualisation.

Si vous devez utiliser du contenu connecté, planifiez ces cartes à l'avance et utilisez l'option `At Campaign Launch` pour que les cartes soient pré-créées avant la prochaine session de l'utilisateur. Notez que ces cartes ne seront pas disponibles immédiatement, car Braze génère toutes les cartes pour tous les utilisateurs éligibles.
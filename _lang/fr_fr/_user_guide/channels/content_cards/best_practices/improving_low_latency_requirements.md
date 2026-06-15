---
nav_title: Améliorer la faible latence
article_title: Améliorer la faible latence pour les Cartes de contenu en tant que bannières
page_order: 10
description: "Cet article présente des stratégies pour garantir le respect des exigences de faible latence avec les Cartes de contenu."
channel:
  - content cards
---

# Améliorer la latence pour les Cartes de contenu en tant que bannières

> Si vous rencontrez des problèmes de latence avec votre implémentation de Cartes de contenu pour des cas d'utilisation critiques, comme les bannières de page d'accueil, consultez cette page pour découvrir des stratégies et des conseils afin de résoudre ces problèmes et accélérer le rendu.

{% alert tip %}
Vous souhaitez afficher des bannières personnalisées et bien visibles sur votre application ou votre site web ? Essayez les [Bannières]({{site.baseurl}}/user_guide/channels/banners/), conçues pour prendre en charge les cas d'utilisation de bannières à faible latence.
{% endalert %}

## Utiliser une entrée planifiée plutôt qu'une entrée basée sur une action

Les cartes basées sur une action, que ce soit dans les campagnes ou les Canvas, nécessitent un traitement en arrière-plan. Braze doit d'abord recevoir la notification de l'action déclencheuse (comme un achat effectué ou le début d'une session) avant de créer une carte pour un utilisateur. Il y aura donc un délai avant que ces cartes ne soient disponibles.

Les cartes basées sur une action ajoutent de la complexité à votre application, car vous pourriez vous retrouver à interroger et actualiser continuellement le système en attendant que la carte soit disponible. Configurez plutôt votre carte en `Scheduled Entry`, ce qui agira comme une fenêtre de disponibilité permettant à la carte d'être toujours accessible pour l'audience ciblée.

Si vous planifiez vos cartes à l'avance, elles seront prêtes et en attente que l'utilisateur ouvre votre application et demande les cartes.

## Utiliser la logique d'envoi « At First Impression »

Combinée aux envois planifiés, l'option `At First Impression` permet d'éviter la latence grâce à la rapidité avec laquelle une carte est créée et stockée dans Braze. L'option `At Campaign Launch` crée toutes les cartes pour tous les utilisateurs segmentés à l'avance, ce qui peut prendre du temps. L'option `At First Impression` génère une carte pour un utilisateur la première fois qu'elle est demandée, par exemple lorsqu'un utilisateur ouvre votre application pour la première fois.

Cela signifie qu'avec l'entrée planifiée, les cartes seront disponibles immédiatement, dès que vous en avez besoin, que ce soit au début de la session ou pour une fenêtre d'éligibilité basée sur le temps.

## N'oubliez pas que l'entrée dans le Canvas est un prérequis pour recevoir des cartes

Lorsque vous utilisez Canvas, n'oubliez pas qu'un utilisateur doit d'abord entrer dans le Canvas en fonction de vos critères d'entrée configurés, *puis* passer par votre étape de message Carte de contenu. Ce n'est qu'à ce moment-là que la carte sera disponible pour votre application ou votre site web. Gardez à l'esprit qu'il existe une latence inhérente à la création de la carte une fois que l'utilisateur passe par l'étape, ce qui peut retarder le moment où la carte devient disponible.

## N'actualisez pas les cartes de manière excessive

Les Cartes de contenu sont automatiquement actualisées par le SDK à chaque début de nouvelle session. Vous pouvez également demander manuellement une actualisation des Cartes de contenu à tout moment pendant une session active.

Appeler la méthode `requestContentCardsRefresh` trop fréquemment peut entraîner une limite de débit. Si votre application est temporairement soumise à une limite de débit, vous pourriez ne pas être en mesure d'actualiser les cartes au moment voulu ou à un moment critique de l'engagement de l'utilisateur avec votre application.

Pour éviter cela, n'appelez cette méthode d'actualisation qu'aux moments importants du cycle de vie de l'utilisateur, par exemple après un achat ou après la mise à niveau de son niveau d'abonnement.

## Éviter d'inclure du Contenu connecté

Le Contenu connecté enrichit les Cartes de contenu avec des données d'API internes ou tierces. Cependant, lorsqu'il est inclus dans un message de Carte de contenu, il bloque la disponibilité de la carte jusqu'à ce que la requête réseau du Contenu connecté soit terminée. Dans certains cas, les SDK réessaieront quelques secondes plus tard afin de ne pas retarder la logique de rendu de votre application, qui peut attendre que le SDK termine sa tâche d'actualisation.

Si vous devez utiliser du Contenu connecté, planifiez ces cartes à l'avance et utilisez l'option `At Campaign Launch` afin que les cartes soient pré-créées avant la prochaine session de l'utilisateur. Notez que ces cartes ne seront pas disponibles immédiatement, car Braze doit écrire toutes les cartes pour tous les utilisateurs éligibles.
---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes liés aux Canvas
page_order: 7
page_type: reference
description: "Cette page fournit des étapes de résolution des problèmes pour les Canvas."
tool: Canvas
---

# Résolution des problèmes liés aux Canvas {#troubleshoot-canvases}

> Cette page vous aide à résoudre les problèmes liés à vos Canvas.

## Erreur « Too many Canvas branches » {#too-many-canvas-branches-error}

Si vous voyez une erreur « Too many Canvas branches » lors du lancement d'un Canvas planifié, la combinaison de la ramification des étapes et de la taille de l'audience d'entrée peut créer des problèmes de performance du cluster Braze qui empêchent l'envoi des messages.

Braze affiche ce message lorsque vous lancez un Canvas avec une entrée planifiée, et non lorsque vous enregistrez un brouillon. Pour résoudre ce problème, essayez les solutions suivantes :

- Réduisez la ramification des étapes dans le Canvas.
- Réduisez la taille de l'audience d'entrée.
- Utilisez les [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) pour consolider la ramification au lieu de nombreux parcours parallèles.
- Si votre Canvas utilise l'éditeur d'origine, [clonez-le vers Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/) et reconstruisez-le avec les composants Canvas.

Si vous devez tout de même lancer le Canvas sans modifications et que vous ne pouvez pas passer à Canvas Flow, contactez l'[Assistance]({{site.baseurl}}/support_contact/).

## Pourquoi un utilisateur n'a-t-il pas reçu une étape de Canvas déclenchée ? {#why-did-a-user-not-receive-a-triggered-canvas-step}

Commencez par vérifier que l'événement personnalisé est bien transmis à Braze. Accédez à **Analytics** > **Rapport d'événements personnalisés**, puis sélectionnez l'événement personnalisé et la plage de dates concernés. Si l'événement ne s'affiche pas, vérifiez qu'il est correctement configuré et que l'utilisateur a bien effectué l'action attendue.

Si l'événement personnalisé s'affiche, poursuivez la résolution des problèmes en procédant comme suit :

- Consultez le téléchargement du profil de l'utilisateur pour confirmer qu'il a déclenché l'événement et à quel moment. Si l'événement a été déclenché, comparez l'horodatage du déclenchement avec le moment où le Canvas est passé en production. L'événement a peut-être été déclenché avant la mise en ligne du Canvas.
- Consultez les journaux des modifications du Canvas et des segments utilisés pour le ciblage afin de déterminer si l'utilisateur faisait partie du segment au moment où son événement personnalisé a été déclenché. S'il n'était pas dans le segment, il n'aurait pas reçu l'étape du Canvas.
- Vérifiez si l'utilisateur a été placé dans un groupe de contrôle via la segmentation, ce qui l'aurait empêché de recevoir l'étape du Canvas.
- S'il y a un délai planifié, vérifiez si l'événement personnalisé de l'utilisateur a été déclenché avant ce délai. Si l'événement a été déclenché avant le délai, l'utilisateur n'aurait pas reçu l'étape du Canvas.

{% alert note %}
Les messages in-app ne peuvent être déclenchés que par des événements envoyés via le SDK, et non via la REST API.
{% endalert %}

## Pourquoi mon Canvas ne s'envoie-t-il pas comme prévu ? {#why-isnt-my-canvas-sending-as-expected}

Les Canvas sont des outils robustes et complexes, et nous savons que vous consacrez du temps et du soin à leur création. Si vous constatez que votre Canvas ne s'envoie pas comme vous le souhaitez, nous vous recommandons de vérifier la planification de ce Canvas, l'audience d'entrée et les paramètres d'entrée, puis de revoir les étapes de [création d'un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).

### Planification {#schedule}

- Le Canvas est-il [correctement planifié]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types) ?
- Avez-vous sélectionné la bonne date et la bonne heure ?
- Pour la [livraison par événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types), les utilisateurs ont-ils effectué les actions spécifiées depuis le lancement du Canvas ?

### Paramètres d'entrée {#entry-settings}

Les [paramètres d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=basics#selecting-entry-controls) sont essentiels pour comprendre comment vos Canvas envoient des messages. Vérifiez si vous avez limité le nombre de personnes susceptibles d'entrer dans ce Canvas.

Les utilisateurs peuvent également quitter un Canvas s'ils ne sont plus éligibles à la réception de messages. Par exemple, si le Canvas ne contient que des notifications push et qu'un utilisateur se désabonne des notifications push après avoir reçu la première étape, cet utilisateur sortira du Canvas. Envisagez d'utiliser [différentes étapes de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/) pour ajouter des parcours utilisateur alternatifs.

### Segmentation de votre audience {#segmenting-your-audience}

Posez-vous les questions suivantes concernant votre audience cible :

- Avez-vous sélectionné le bon segment ?
- Comment le segment est-il configuré ?
- Avez-vous confirmé que le segment contient des utilisateurs ?
- Avez-vous ajouté des filtres supplémentaires qui limiteraient le nombre d'utilisateurs entrant dans le Canvas ?
- Les utilisateurs sont-ils éligibles pour recevoir la première étape de vos variantes ? Par exemple, si la première étape de votre Canvas est une notification push, mais que l'audience d'entrée est entièrement composée d'utilisateurs avec les notifications push désactivées, aucun utilisateur ne recevra de messages.

## Pourquoi les envois ou les distributions sont-ils inférieurs à la taille de mon audience cible ? {#why-are-sends-or-deliveries-lower-than-my-target-audience-size}

Le nombre de messages envoyés ou distribués diffère souvent de l'estimation de l'audience ou du nombre de destinataires. Les raisons courantes sont les suivantes :

- **Réévaluation de l'audience :** les utilisateurs peuvent sortir du segment entre le moment où ils entrent dans une étape et celui où le message est envoyé.
- **Éligibilité au canal :** il peut manquer aux utilisateurs une adresse e-mail, un jeton de notification push ou le statut d'abonnement requis pour ce canal à cette étape.
- **Groupes de contrôle :** un groupe de contrôle global ou de Canvas peut exclure des utilisateurs de l'envoi de messages.
- **Heures calmes, timing intelligent et limites de débit :** ces paramètres peuvent reporter ou supprimer des envois.
- **Étapes de messages in-app :** les messages in-app peuvent afficher zéro _Envoi_ alors que des impressions existent. C'est un comportement attendu, car la distribution in-app fonctionne différemment des notifications push ou des e-mails. Consultez [Pourquoi un Canvas peut-il afficher zéro envoi alors que des impressions sont enregistrées ?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged) dans la FAQ Canvas.

Pour les e-mails et les autres canaux, bon nombre des mêmes facteurs s'appliquent comme pour les campagnes. Pour une liste détaillée, consultez [Pourquoi les envois sont-ils inférieurs à la taille estimée de l'audience ?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#why-are-sends-lower-than-the-estimated-audience-size).

## Pourquoi aucun utilisateur n'est-il entré dans mon Canvas planifié quotidiennement le jour du changement d'heure ? {#why-did-no-users-enter-my-daily-scheduled-canvas-on-daylight-saving-time-day}

Lors des jours de transition vers l'heure d'été ou d'hiver, les Canvas planifiés quotidiennement peuvent s'exécuter jusqu'à une heure plus tôt ou plus tard que d'habitude. Si vos critères d'entrée reposent sur des attributs personnalisés ou des événements avec des horodatages situés dans l'heure précédant l'heure d'entrée planifiée, les utilisateurs peuvent ne pas encore être éligibles le jour du changement d'heure, car l'attribut ou l'événement n'a pas encore été enregistré.

Par exemple, supposons que les utilisateurs reçoivent généralement une mise à jour d'attribut personnalisé à 15 h 00 dans le fuseau horaire de votre Canvas et que votre Canvas s'exécute quotidiennement à 15 h 30 dans ce même fuseau horaire. Lors d'un passage à l'heure d'été (avance d'une heure), le Canvas peut évaluer les utilisateurs jusqu'à une heure plus tôt que d'habitude par rapport à cette mise à jour d'attribut, c'est-à-dire avant que l'attribut n'ait été enregistré. Si la rééligibilité est désactivée, les utilisateurs qui sont entrés les jours précédents ne peuvent pas entrer à nouveau, ce qui entraîne zéro entrée pour cette journée.

Pour éviter cela, assurez-vous que les mises à jour de vos attributs personnalisés ou événements se produisent plus d'une heure avant l'heure d'entrée planifiée du Canvas.

## Pourquoi mon audience ne s'est-elle pas répartie de manière égale entre le groupe de contrôle et le groupe de variantes ? {#why-didnt-my-audience-split-evenly-between-the-control-group-and-variant-group}

Lors de la création de votre Canvas, vous vous attendiez peut-être à ce que votre audience se répartisse de manière égale entre votre groupe de contrôle et votre groupe de variantes, comme dans le [cas d'utilisation](#use-case) suivant. Voyons pourquoi cela se produit et comment y remédier !

Le groupe dans lequel un utilisateur est placé dépend de ses paramètres. Il peut s'agir du groupe de contrôle ou du groupe de variantes. Un utilisateur entre dans un Canvas lorsqu'il remplit tous les critères définis dans l'[étape d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule). Lors de la configuration de votre Canvas, vous définissez le pourcentage d'utilisateurs qui entreront dans chaque variante et dans le groupe de contrôle.

Si votre groupe de contrôle est important par rapport à votre groupe de variantes (et que ce n'est pas votre intention), nous recommandons ce qui suit :
1. Définissez le filtre de votre audience d'entrée sur **is Foreground Push Enabled**.
2. Définissez le filtre de votre audience d'entrée pour le **statut d'abonnement push**, le **statut d'abonnement e-mail**, ou les deux, sur **Opted In** ou **Subscribed**.

Lors de la création d'un Canvas avec un groupe de contrôle, vérifiez que tous les utilisateurs de l'audience d'entrée sont en mesure de recevoir des messages au sein du Canvas (par exemple, si le Canvas contient des notifications push et des e-mails).

### Cas d'utilisation {#use-case}

Imaginons le scénario suivant :
- Un Canvas possède une seule variante et un groupe de contrôle.
- La première étape de la variante est une notification push.
- 90 % des utilisateurs ont été sélectionnés pour entrer dans la variante, et 10 % pour entrer dans le groupe de contrôle.

![Exemple de Canvas avec 90 % pour la variante et 10 % pour le groupe de contrôle.]({% image_buster /assets/img_archive/trouble15.png %})

Dans ce scénario, 90 % des utilisateurs qui entrent dans le Canvas entreront dans la variante.

Si nous examinons les utilisateurs actifs, nous pouvons constater que même si le segment contient 29,8 k utilisateurs, seuls 64 % d'entre eux ont les notifications push activées :

![Segment avec le filtre « Push Enabled » défini sur « true » et une estimation de 29,8 k utilisateurs.]({% image_buster /assets/img_archive/trouble16.png %})

Cela signifie que même si nous avons spécifié que 90 % des utilisateurs devaient entrer dans la variante, tous ces utilisateurs ne sont pas réellement en mesure de recevoir une notification push. Les utilisateurs qui ne peuvent pas recevoir de notification push entreront tout de même dans la variante.

## Pourquoi l'éditeur de Canvas se fige-t-il ou ne se charge-t-il pas ? {#why-is-the-canvas-editor-freezing-or-not-loading}

Si vous apportez des modifications à des Canvas volumineux ou complexes comportant de nombreuses branches ou variantes, de nombreuses étapes ou des flux très larges, l'éditeur peut ne pas se charger ou se figer. Dans ce cas, nous recommandons ce qui suit :

- Videz le cache et les cookies de votre navigateur, puis rechargez la page. Si vous utilisez des bloqueurs de publicités d'entreprise ou des extensions de navigateur, ceux-ci peuvent interférer avec la plateforme Braze.
- Utilisez les commandes de zoom du Canvas pour réduire la vue à 25 % ou 10 %. Cela réduit la quantité d'interface que le navigateur doit afficher en une seule fois.
- Essayez un autre navigateur web.
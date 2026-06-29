---
nav_title: FAQ
article_title: FAQ sur les messages in-app
page_order: 30
description: "Cet article fournit des réponses aux questions fréquemment posées sur les messages in-app."
tool: in-app messages

---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article fournit des réponses à certaines questions fréquemment posées sur les messages in-app.

## Qu'est-ce qu'un message dans le navigateur et en quoi diffère-t-il d'un message in-app ? {#what-is-an-in-browser-message-and-how-does-it-differ-from-an-in-app-message}

Les messages dans le navigateur sont des messages in-app envoyés aux navigateurs web. Pour créer un message dans le navigateur, assurez-vous de sélectionner **Web Browser** dans le champ **Send To** lors de la création de votre campagne ou Canvas de messages in-app.

## Un message in-app s'affiche-t-il si un appareil est hors ligne ? {#does-an-in-app-message-display-if-a-device-is-offline}

Cela dépend. Étant donné que les messages in-app sont distribués au démarrage de la session, l'appareil est en mesure de télécharger le payload avant de passer hors ligne, et le message in-app peut toujours s'afficher hors ligne. Si le payload n'est pas téléchargé, le message in-app ne s'affiche pas.

## Si un utilisateur a déjà un payload de message in-app sur son appareil et que l'expiration du message est modifiée, l'expiration est-elle mise à jour sur son appareil ? {#if-a-user-already-has-an-in-app-message-payload-on-their-device-and-the-message-expiration-is-changed-does-the-expiration-update-on-their-device}

Lorsqu'un utilisateur démarre une session, Braze vérifie si des modifications ont été apportées aux messages in-app auxquels il est éligible et les met à jour en conséquence. Ainsi, si l'expiration a changé et qu'il enregistre une session, le message in-app est envoyé à l'appareil avec les informations mises à jour.

## Comment configurer les heures calmes pour une campagne de messages in-app ? {#how-do-i-set-up-quiet-hours-for-an-in-app-message-campaign}

La fonctionnalité des heures calmes n'est pas disponible pour les campagnes de messages in-app. Cette fonctionnalité est utilisée pour empêcher l'envoi de messages à vos utilisateurs pendant des heures spécifiques. Pour les campagnes de messages in-app, vos utilisateurs ne reçoivent des messages in-app que s'ils sont actifs dans l'application.

Comme solution de contournement pour envoyer des messages in-app à un moment précis, utilisez l'exemple de code Liquid suivant. Cela permet d'annuler le message si le message in-app est affiché après 19 h 59 ou avant 8 h dans le fuseau horaire spécifié.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

## Les utilisateurs peuvent-ils recevoir à nouveau un message in-app après l'avoir fermé ? {#can-users-receive-an-in-app-message-again-after-they-dismiss-it}

### Campaigns

Pour les campagnes de messages in-app, vous pouvez permettre aux utilisateurs de redevenir éligibles à la réception de la campagne en activant la rééligibilité dans les **Contrôles de l'envoi** (**Allow users to become re-eligible to receive campaign**). La rapidité avec laquelle ils peuvent le recevoir à nouveau dépend de la fenêtre de rééligibilité que vous définissez et de la manière dont Braze a enregistré l'envoi précédent. Consultez [Rééligibilité pour les campagnes et Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) pour le comportement des campagnes, y compris la relation entre la rééligibilité et la réception du message.

Si la rééligibilité est désactivée, les utilisateurs ne recevront généralement plus cette même campagne après l'avoir reçue, sur la seule base des critères de qualification.

### Canvas {#canvases}

Pour les messages in-app envoyés depuis un Canvas, la possibilité pour un utilisateur de revoir le message dépend des contrôles d'entrée du Canvas (comme le fait d'autoriser les utilisateurs à réintégrer le Canvas) et de la configuration de votre étape, et pas uniquement des contrôles de distribution de la campagne.

## Quand l'éligibilité à un message in-app est-elle calculée ? {#when-is-eligibility-for-an-in-app-message-calculated}

L'éligibilité à un message in-app est calculée au moment de la distribution. Si un message in-app est planifié pour être envoyé à 7 h, l'éligibilité est vérifiée pour ce message in-app à 7 h.

Une fois le message in-app affiché, l'éligibilité dépend du moment où le message in-app est téléchargé et déclenché.

## Pourquoi ma campagne de messages in-app archivée continue-t-elle à générer des impressions de messages in-app ? {#why-is-my-archived-in-app-message-campaign-still-delivering-in-app-message-impressions}

Cela peut se produire pour les utilisateurs qui remplissaient les critères du segment lorsque la campagne de messages in-app était active.

Pour éviter cela, lors de la configuration de votre campagne, sélectionnez **Re-evaluate campaign eligibility before displaying**.

## Plusieurs messages in-app peuvent-ils s'afficher au cours de la même session ? {#can-multiple-in-app-messages-display-in-the-same-session}

Oui, mais un seul message in-app peut s'afficher par occurrence d'un [événement déclencheur]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create#choose-a-trigger). Si plusieurs campagnes de messages in-app partagent le même déclencheur (par exemple, le démarrage de session), seul le message ayant la priorité la plus élevée s'affiche à chaque occurrence de ce déclencheur. Pour les déclencheurs de démarrage de session, cela signifie qu'un seul message peut s'afficher par session, et la prochaine occasion d'afficher un autre message éligible est la session suivante.

Lorsque plusieurs messages partagent le même niveau de priorité, le message créé le plus récemment s'affiche en premier. Pour les déclencheurs de démarrage de session, le message suivant le plus récent s'affiche lors d'une session ultérieure ; pour les autres types de déclencheurs, le message suivant le plus récent s'affiche la prochaine fois que cet événement déclencheur se produit, ce qui peut être au cours de la même session ou d'une session ultérieure.

Pour contrôler l'ordre d'affichage au sein d'un niveau de priorité, accédez aux paramètres de distribution de l'une des campagnes et sélectionnez **Définir la priorité exacte**, puis glissez-déposez les campagnes dans l'ordre souhaité. Pour plus de détails, consultez [Choisir une priorité]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create#choose-a-priority).

## Comment Braze calcule-t-il l'expiration d'un message in-app définie sur « après 1 jour(s) » ? {#how-does-braze-calculate-an-in-app-message-expiration-set-to-after-1-days}

Braze calcule un délai d'expiration d'un jour comme 24 heures après que les utilisateurs sont devenus éligibles à la réception d'un message.

## Que sont les messages in-app modélisés ? {#what-are-templated-in-app-messages}

Les messages in-app sont distribués en tant que messages in-app modélisés lorsque **Re-evaluate campaign eligibility before displaying** est sélectionné ou si l'une des étiquettes Liquid suivantes existe dans le message :

- `canvas_entry_properties`
- `connected_content`
- Variables SMS telles que {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Cela signifie que lors du démarrage de la session, l'appareil reçoit le déclencheur de ce message in-app au lieu du message complet. Lorsque l'utilisateur déclenche le message in-app, son appareil effectue une requête réseau pour récupérer le message réel.

{% alert note %}
Le message n'est pas distribué si l'appareil n'a pas accès à Internet. Le message peut ne pas être distribué si la logique Liquid prend trop de temps à se résoudre.
{% endalert %}

## Comment fonctionne le comportement d'annulation pour les messages in-app ? {#how-does-abort-behavior-work-for-in-app-messages}

Chez Braze, une annulation se produit lorsqu'un utilisateur effectue une action qui le rend éligible à la réception d'un message, mais qu'il ne reçoit pas le message parce que sa logique Liquid le marque comme inéligible. Par exemple :

1. Sam effectue une action qui devrait déclencher une campagne par e-mail.
2. Le corps de l'e-mail contient une logique Liquid qui stipule que si un score d'attribut personnalisé est inférieur à 50, ne pas envoyer cet e-mail.
3. Le score d'attribut personnalisé de Sam est de 20.
4. Braze reconnaît que Sam ne devrait pas recevoir cet e-mail, et l'e-mail est annulé.
5. Un événement d'annulation est enregistré.

Cependant, étant donné que les messages in-app sont un canal de type « pull », les annulations fonctionnent un peu différemment pour eux.

### Comportement d'annulation standard des messages in-app {#standard-in-app-message-abort-behavior}

Les messages in-app sont récupérés par l'appareil au démarrage de la session et mis en cache sur l'appareil, de sorte que, quelle que soit la qualité de la connexion Internet, le message peut être distribué instantanément à l'utilisateur. Par exemple, si un utilisateur reçoit cinq messages in-app au cours de sa session, il les reçoit tous les cinq au démarrage de la session. Les messages sont mis en cache localement et apparaissent lorsque leurs événements déclencheurs définis se produisent (démarrage de session, clic sur un bouton qui enregistre un événement personnalisé, ou autre).

En d'autres termes, la logique qui détermine si un message in-app doit être annulé se produit **avant** que le déclencheur ne se soit produit. Pour illustrer cela, supposons que Sam de l'exemple de l'e-mail est abonné aux notifications push.

1. Sam démarre une session en lançant une application propulsée par Braze sur son téléphone.
2. En fonction des critères d'audience des campagnes actives dans l'espace de travail, Sam pourrait être éligible à cinq campagnes différentes. Les cinq sont récupérées sur son téléphone et mises en cache.
3. Sam **n'a pas** effectué d'actions qui déclencheraient ces messages, mais il pourrait recevoir ces messages au cours de la session.
4. La logique Liquid de deux des messages in-app contient des règles qui excluent Sam de la réception du message (comme son attribut personnalisé de score n'étant pas assez élevé).
5. Sam ne reçoit pas les deux messages in-app qui l'excluent, mais il reçoit les trois autres messages.
6. Aucun événement d'annulation n'est enregistré.

Braze n'enregistre aucun événement d'annulation dans le cas de Sam car cela ne correspond pas à la définition d'une annulation ; Sam **n'a pas** effectué d'actions qui déclencheraient les messages. Pour les messages in-app, les utilisateurs n'effectuent jamais réellement le déclencheur avant que Braze ne détermine qu'ils ne devraient pas voir le message.

### Comportement d'annulation des messages in-app modélisés {#templated-in-app-message-abort-behavior}

Les [messages in-app modélisés](#what-are-templated-in-app-messages) forcent le SDK à réévaluer si un message doit s'afficher lorsque l'événement déclencheur se produit. Cela entraîne un comportement d'annulation différent. Pour illustrer, considérez cet exemple :

1. Sam démarre une session Braze en lançant une application propulsée par Braze sur son téléphone.
2. Les critères d'audience des campagnes actives indiquent que Sam pourrait être éligible à un message in-app modélisé, de sorte que les informations de déclenchement sont envoyées à son appareil sans le payload du message.
3. Sam sélectionne un bouton qui enregistre un événement personnalisé, déclenchant le message in-app modélisé.
4. L'appareil de Sam effectue une requête réseau pour récupérer le message in-app.
5. La logique Liquid du message conduit à une annulation, donc Braze enregistre cela comme une annulation ; Sam a effectué l'action de déclenchement avant cette évaluation.

### Comparaison du comportement d'annulation des messages in-app {#comparing-in-app-message-abort-behavior}

Ce tableau compare les flux de messages in-app que Sam a expérimentés :

| Message in-app | Comportement d'annulation |
| --- | --- |
| Standard | Un événement d'annulation n'a pas été enregistré car Sam n'a effectué aucune action qui déclencherait un message.<br><br>Les messages in-app standard n'enregistrent pas d'annulations car la définition d'une annulation est « n'a pas vu le message malgré l'exécution de l'action de déclenchement ». Étant donné que les messages in-app sont distribués à l'appareil avant que les actions de déclenchement ne se produisent, il n'est pas logique de considérer les messages in-app omis en raison de la logique Liquid. |
| Modélisé | Un événement d'annulation a été enregistré car Sam a effectué l'action de déclenchement pour déclencher le message in-app modélisé, mais a reçu une annulation lors du templating Liquid.<br><br>Les messages in-app modélisés enregistrent les annulations car l'évaluation Liquid se produit après que l'action de déclenchement a été effectuée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparaison du comportement d'annulation des messages in-app" }

### Quand le contenu connecté s'exécute-t-il pour les messages in-app ? {#when-does-connected-content-run-for-in-app-messages}

Pour les [messages in-app modélisés](#what-are-templated-in-app-messages), le contenu connecté et les autres étiquettes Liquid sont résolus lorsque l'événement déclencheur se produit et que l'appareil demande le payload du message, et non lorsque l'utilisateur clique sur un bouton à l'intérieur du message. Chaque récupération modélisée peut inclure des appels de contenu connecté pour cet affichage.

Si votre HTML fait référence à des données REST renvoyées par le contenu connecté, ces données sont disponibles pour la session au cours de laquelle le message a été modélisé. Plusieurs boutons peuvent faire référence à la même réponse de contenu connecté sans déclencher d'appels supplémentaires au clic.

### Pourquoi y a-t-il un délai avant l'affichage de mon message in-app ? {#why-is-there-a-delay-before-my-in-app-message-displays}

Les messages in-app standard s'affichent dès que le payload mis en cache est prêt après l'événement déclencheur. Sur Android et iOS, les images volumineuses ou d'autres ressources hébergées sur un réseau de diffusion de contenu référencées dans le message peuvent ajouter un court délai pendant le téléchargement de ces ressources avant l'apparition du message in-app.

Les [messages in-app modélisés](#what-are-templated-in-app-messages) et les campagnes avec l'option **Re-evaluate campaign eligibility before displaying** sélectionnée nécessitent une requête réseau supplémentaire après le déclencheur avant l'affichage du message. Cela peut ajouter un court délai (généralement inférieur à 100 ms sur une connexion stable). Pour plus d'informations, consultez [Choisir les utilisateurs à cibler]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create#choose-users-to-target).

### Pourquoi mon message in-app est-il différent de l'aperçu du tableau de bord ? {#why-does-my-in-app-message-look-different-from-the-dashboard-preview}

Les messages in-app distribués peuvent différer de l'aperçu du tableau de bord lorsque :

- Votre intégration applique un style personnalisé ou remplace l'interface utilisateur par défaut des messages in-app sur certaines plateformes
- L'aperçu utilise un profil d'utilisateur test avec des attributs différents de ceux du destinataire
- Le contenu modélisé se résout différemment au moment de l'envoi par rapport au mode aperçu

Utilisez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) avec un utilisateur test dont le profil correspond à votre audience cible lors de la validation de l'apparence.

### Pourquoi un message in-app multipage utilise-t-il le même arrière-plan sur chaque page ? {#why-does-a-multi-page-in-app-message-use-the-same-background-on-every-page}

Lorsque l'option **Image d'arrière-plan** est activée sur une page d'un message in-app multipage, cet arrière-plan s'applique à toutes les pages du message. Pour utiliser des arrière-plans différents par page, utilisez un bloc HTML personnalisé avec du JavaScript pour changer les images entre les pages.

### Comment tester les messages in-app web ? {#how-do-i-test-web-in-app-messages}

Les envois de test de messages in-app web nécessitent que les notifications push soient activées sur l'appareil de test, car le flux de test envoie une notification push qui ouvre l'application ou le site où le message in-app s'affiche. Le même chemin de test basé sur les notifications push s'applique sur toute plateforme où les notifications push ne sont pas configurées avec Braze, bien que l'absence de notifications push soit le plus souvent rencontrée sur le web car de nombreuses intégrations mobiles ont déjà les notifications push activées. Utilisez plutôt une campagne en production vers un segment de test interne. Pour les étapes, consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message).

## Pourquoi le bouton de fermeture est-il masqué sur les messages in-app HTML plein écran sur Android ? {#why-is-the-close-button-hidden-on-full-screen-html-in-app-messages-on-android}

Sur les appareils avec des écrans bord à bord (y compris Android 15+), les messages in-app HTML plein écran peuvent s'afficher derrière la barre d'état du système et masquer un contrôle de fermeture en haut de la mise en page.

Le SDK Android de Braze version 37.0.0 et ultérieure applique par défaut les marges intérieures de fenêtre aux messages in-app HTML afin que les contrôles restent dans la zone sûre. Si les utilisateurs constatent toujours un chevauchement, mettez à jour vers la dernière version du SDK Android de Braze.

Sur les versions antérieures du SDK, les développeurs pouvaient activer `BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled(true)` avant que ce comportement ne devienne le comportement par défaut.

## Que faut-il savoir lors de la personnalisation des messages in-app par glisser-déposer ? {#what-should-i-know-when-customizing-drag-and-drop-in-app-messages}

L'[éditeur par glisser-déposer]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) prend en charge les types d'affichage fenêtre modale et plein écran. Vous construisez le contenu à l'intérieur de ces conteneurs avec des blocs éditeur.

Gardez à l'esprit :

- **Liens et liens profonds :** Chaque action au clic dispose d'un seul champ URL par défaut. Utilisez Liquid dans l'URL pour varier les liens en fonction de l'appareil, du type d'application ou des attributs utilisateur. Sur le **conteneur de message**, vous pouvez également activer le comportement au clic spécifique à la plateforme pour définir des liens différents par plateforme.
- **Opacité et arrière-plans :** L'opacité du conteneur de message affecte l'ensemble de l'arrière-plan du message. Les blocs individuels peuvent définir leurs propres couleurs d'arrière-plan. Pour un contrôle plus fin, ajoutez du CSS personnalisé dans un bloc de code personnalisé.
- **Largeur du message :** La largeur maximale du **conteneur de message** ne peut pas être définie en dessous de 325 px dans l'éditeur, ce qui garantit la lisibilité du contenu sur les écrans plus petits. Utilisez du CSS personnalisé si vous avez besoin d'une mise en page plus étroite.
- **Arrière-plans spécifiques à la plateforme :** Un même message utilise la même image et les mêmes couleurs d'arrière-plan sur le web et le mobile. Vous ne pouvez pas définir des arrière-plans différents par plateforme dans l'éditeur.
- **Messages multipages :** Les images d'arrière-plan et les actions au clic au niveau du message s'appliquent à toutes les pages d'un message multipage. Pour utiliser des images différentes sur chaque page, ajoutez des boutons qui renvoient vers la page suivante.
- **Styles au niveau du message :** Les styles au niveau du message s'appliquent à l'ensemble du message.
- **Images d'arrière-plan :** Les images d'arrière-plan s'étirent pour s'adapter à la fenêtre modale.

Pour plus de considérations sur l'éditeur, consultez le [Guide de préparation des messages in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices/prep_guide#drag-and-drop-editor-considerations).

## Que signifie « Event was published, but no subscribers were found » dans les journaux du SDK Android ? {#what-does-event-was-published-but-no-subscribers-were-found-mean-in-android-sdk-logs}

Cette ligne de journal n'est généralement pas une erreur. Elle apparaît souvent lorsque Braze publie un événement interne (tel que `NoMatchingTriggerEvent`) et qu'aucun écouteur de message in-app ou de Content Cards n'est abonné à ce moment-là.

Si vous voyez ce journal alors que vous vous attendez à ce qu'un événement personnalisé déclenche un message in-app, vérifiez que l'événement est bien enregistré, que l'utilisateur fait partie de l'audience de la campagne ou du Canvas, et que les Content Cards sont synchronisées lorsque le message en dépend.
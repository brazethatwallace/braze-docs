---
nav_title: Bonnes pratiques
article_title: Bonnes pratiques pour Canvas
page_order: 1
description: "Cet article présente quelques bonnes pratiques pour créer et personnaliser des parcours utilisateurs avec Canvas et Canvas Flow."
tool: Canvas

---

# Bonnes pratiques pour Canvas {#canvas-best-practices}

> Cet article présente quelques bonnes pratiques pour créer et personnaliser des parcours utilisateurs avec Canvas et Canvas Flow.

## Identifiez votre objectif {#identify-your-purpose}

Plongez dans le quoi, le qui et le pourquoi !
- Qu'essayez-vous d'aider vos utilisateurs à accomplir ?
- Quels sont les utilisateurs que vous cherchez à atteindre ?
- Pourquoi créez-vous ce Canvas ?

## Combinez les possibilités {#mix-and-match}

Explorez de nouvelles combinaisons de parcours utilisateurs grâce aux [composants Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/).
- Segmentez vos utilisateurs avec l'[arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) et créez différents workflows.
- Espacez vos parcours utilisateurs avec une étape de [délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/).
- Ajoutez des [messages autonomes]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) où vous le souhaitez dans votre flux Canvas.

{% alert note %}
Les étapes du Canvas ne peuvent faire avancer les utilisateurs que dans le flux. Vous ne pouvez pas configurer un Canvas pour relier une étape à une étape précédente, car cela ferait reculer les utilisateurs. Cette validation garantit que les utilisateurs progressent dans une seule direction à travers votre Canvas.
{% endalert %}

## Créez des messages plus riches {#create-richer-messages}

Captivez vos utilisateurs avec des messages plus riches.

- Créez des [messages in-app]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) pour les Canvas d'onboarding afin de tirer le meilleur parti de votre première impression.
- Intégrez des [Content Cards]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) dans un parcours Canvas pour des offres promotionnelles et des notifications push.

## Testez vos parcours utilisateurs {#test-your-user-journeys}

Mesurez l'impact de vos messages Canvas en intégrant des groupes de contrôle. Vous pourrez ainsi mieux comprendre comment votre Canvas a été reçu !

- Nommez chaque étape de votre Canvas pour identifier votre parcours utilisateur.
- Utilisez le composant [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) dans votre parcours utilisateur pour assigner aléatoirement des utilisateurs aux différents chemins que vous créez.
- Diversifiez vos parcours utilisateurs avec des étapes de délai et de message pour découvrir quel chemin est le plus efficace.
- Consultez les [analyses Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pour voir les performances de chaque composant de votre parcours utilisateur.
- [Modifiez votre Canvas]({{site.baseurl}}/post-launch_edits/) après le lancement initial.

## Planifier vos Canvas {#scheduling-your-canvases}

{% alert note %}
Canvas vous empêchera d'utiliser un envoi planifié avec une heure déjà passée. Cependant, il est possible de lancer un Canvas pendant la même minute exacte où la campagne est planifiée (ou dans les secondes qui précèdent). Le Canvas risque alors de manquer l'heure d'entrée planifiée, empêchant les utilisateurs d'y entrer. Nous recommandons d'envoyer les Canvas immédiatement si des campagnes sont modifiées dans les minutes précédant l'heure d'envoi planifiée.
{% endalert %}

{% alert important %}
Si vous modifiez l'audience, la planification ou les paramètres de réception peu avant une entrée planifiée ou une fenêtre d'envoi, certains utilisateurs peuvent déjà être en attente sur une étape ou avoir été évalués avec les paramètres précédents, de sorte que tout le monde n'est pas garanti de prendre en compte la modification. Pour comprendre comment les modifications de planification, les modifications d'audience, l'option **Évaluer au moment de la mise en file d'attente** et le timing de réception des étapes de message interagissent, consultez [Modifier votre Canvas après le lancement]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/). En cas de doute, arrêtez le Canvas, dupliquez-le et relancez-le pour une réévaluation propre.
{% endalert %}

Pour les étapes du Canvas, tenez compte des détails suivants lors de la planification de votre Canvas :

- Les modifications de planification ne s'appliquent qu'aux utilisateurs qui ne sont pas déjà en attente de recevoir l'étape.
- Les modifications d'audience s'appliquent par défaut à tous les utilisateurs, sauf si vous planifiez les modifications pour qu'elles ne s'appliquent qu'aux utilisateurs qui ne sont pas en attente de recevoir l'étape.
- La modification d'un Canvas planifié pour être envoyé dès son déploiement, suivie de la sélection de **Mettre à jour**, entraîne essentiellement son envoi.

### Modifications après le lancement {#post-launch-edits}

Si vous arrêtez un Canvas actif alors qu'un brouillon non enregistré existe, l'arrêt peut supprimer ce brouillon. Enregistrez, lancez ou supprimez le brouillon avant d'arrêter le Canvas si vous souhaitez conserver les modifications en cours.

#### Moment de l'évaluation de l'audience {#audience-evaluation-timing}

Braze évalue les audiences à différents moments dans le générateur Canvas et dans les étapes individuelles. Pour plus de détails sur la configuration, consultez :

- [Définir votre audience cible d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-13-set-your-target-entry-audience) et [Déterminer la planification d'entrée de votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-12-determine-your-canvas-entry-schedule) lors de la création d'un Canvas
- [Comment l'audience cible et les critères d'entrée fonctionnent ensemble]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/#how-target-audience-and-entry-criteria-work-together)
- [Modifier les paramètres de réception]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) pour les étapes de message
- [Comment les utilisateurs sont évalués]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/#how-users-are-evaluated) pour les étapes de parcours d'audience

Si vous modifiez un Canvas actif peu avant une fenêtre d'entrée ou d'envoi planifiée, les utilisateurs déjà en file d'attente pour une étape **Message** peuvent ne pas prendre en compte vos modifications. Pour en savoir plus, consultez [Modifier les Canvas après le lancement]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/).